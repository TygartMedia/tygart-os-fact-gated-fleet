#!/usr/bin/env python3
"""Router design trio (hackathon, Meta Model API credits).

Runs the ROUTER design question (BRIEF.md) through the Trio on
muse-spark-1.3 STANDARD:
  scout       — chat, reasoning_effort low,    cap 8000  (map the space)
  designer    — chat, reasoning_effort medium, cap 24000 (concrete draft)
  adjudicator — Responses background, max,     cap 60000 (attack + rule)

Usage: run_router_trio.py <scout|designer|adjudicator>
Each leg reads its inputs from disk (BRIEF.md + prior legs' raw outputs),
saves its raw output, and appends a receipt row to runs.jsonl.
Retry doctrine: one re-run on 503 / empty / truncated; never on timeout.
Prices (Spark standard, from TRIO-COSTING): in $1.25/1M, cached $0.15/1M,
out $4.25/1M. If usage comes back null, cost is recorded as UNVERIFIED.
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, "/opt/muse/skills/custom-connector-setup/bin")
from dynamic_credentials import add_surrogate_to_request, read_json_response  # noqa: E402

BASE = "https://api.meta.ai/v1"
PROVIDER = "custom.meta-model-api"
HOSTS = ["api.meta.ai"]
HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = "muse-spark-1.3"
PRICE = {"in": 1.25 / 1e6, "cached": 0.15 / 1e6, "out": 4.25 / 1e6}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args):
        raise RuntimeError("redirect refused, verify the endpoint")


def raw(method, path, body=None, timeout=300):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(BASE + path, data=data, method=method)
    if data is not None:
        req.add_header("Content-Type", "application/json")
    add_surrogate_to_request(req, PROVIDER, allowed_hosts=HOSTS)
    with urllib.request.build_opener(NoRedirect()).open(req, timeout=timeout) as resp:
        return resp.status, read_json_response(resp)


def cost_of(u_in, u_cached, u_out):
    if u_in is None or u_out is None:
        return None
    return round((u_in - u_cached) * PRICE["in"] + u_cached * PRICE["cached"]
                 + u_out * PRICE["out"], 5)


def is_timeout(ex):
    s = repr(ex).lower()
    return "timeout" in s or "timed out" in s


def chat_once(prompt, effort, cap):
    t0 = time.time()
    e = {"route_api": "chat", "effort": effort, "cap": cap, "model": MODEL}
    try:
        status, payload = raw("POST", "/chat/completions", {
            "model": MODEL, "messages": [{"role": "user", "content": prompt}],
            "reasoning_effort": effort, "max_completion_tokens": cap})
        e["status"] = status
        u = payload.get("usage")
        if u:
            det = u.get("prompt_tokens_details") or {}
            cdet = u.get("completion_tokens_details") or {}
            e["input_tokens"] = u.get("prompt_tokens", 0)
            e["cached_tokens"] = det.get("cached_tokens", 0)
            e["output_tokens"] = u.get("completion_tokens", 0)
            e["reasoning_tokens"] = cdet.get("reasoning_tokens")
            e["cost"] = cost_of(e["input_tokens"], e["cached_tokens"], e["output_tokens"])
        else:
            e["usage"] = None
            e["cost"] = None
        e["finish"] = (payload.get("choices") or [{}])[0].get("finish_reason")
        e["output"] = ((payload.get("choices") or [{}])[0].get("message") or {}).get("content") or ""
    except urllib.error.HTTPError as ex:
        e["status"] = ex.code
        try:
            e["error_body"] = ex.read().decode("utf-8", "replace")[:300]
        except Exception:
            e["error_body"] = ""
        e["output"] = ""
    except Exception as ex:
        e["status"] = "EXC"
        e["error_body"] = repr(ex)[:300]
        e["timeout"] = is_timeout(ex)
        e["output"] = ""
    e["wall_s"] = round(time.time() - t0, 2)
    return e


def bg_once(prompt, cap=60000):
    t0 = time.time()
    e = {"route_api": "responses_background", "effort": "max", "cap": cap, "model": MODEL}
    try:
        status, payload = raw("POST", "/responses", {
            "model": MODEL, "input": prompt,
            "reasoning": {"effort": "max"}, "max_output_tokens": cap,
            "background": True})
        e["status"] = status
        rid = payload.get("id")
        e["response_id"] = rid
        final = None
        for _ in range(60):
            time.sleep(8)
            s2, p2 = raw("GET", f"/responses/{rid}")
            if p2.get("status") in ("completed", "failed", "incomplete", "cancelled"):
                final = p2
                break
        if final is None:
            e["final_status"] = "poll_timeout"
            e["timeout"] = True
            e["output"] = ""
        else:
            e["final_status"] = final.get("status")
            u = final.get("usage")
            if u:
                det = u.get("input_tokens_details") or {}
                odet = u.get("output_tokens_details") or {}
                e["input_tokens"] = u.get("input_tokens", 0)
                e["cached_tokens"] = det.get("cached_tokens", 0)
                e["output_tokens"] = u.get("output_tokens", 0)
                e["reasoning_tokens"] = odet.get("reasoning_tokens")
                rt = e["reasoning_tokens"]
                e["near_cap"] = bool(rt and rt > 0.7 * cap)
                e["cost"] = cost_of(e["input_tokens"], e["cached_tokens"], e["output_tokens"])
            else:
                e["usage"] = None
                e["cost"] = None
            texts = []
            for item in final.get("output") or []:
                if item.get("type") == "message":
                    for part in item.get("content") or []:
                        if part.get("type") == "output_text":
                            texts.append(part.get("text", ""))
            e["output"] = "\n".join(texts)
            if final.get("status") == "incomplete":
                e["incomplete_details"] = final.get("incomplete_details")
    except urllib.error.HTTPError as ex:
        e["status"] = ex.code
        try:
            e["error_body"] = ex.read().decode("utf-8", "replace")[:300]
        except Exception:
            e["error_body"] = ""
        e["output"] = ""
    except Exception as ex:
        e["status"] = "EXC"
        e["error_body"] = repr(ex)[:300]
        e["timeout"] = is_timeout(ex)
        e["output"] = ""
    e["wall_s"] = round(time.time() - t0, 2)
    return e


def classify(att):
    if att.get("timeout") or att.get("final_status") == "poll_timeout":
        return False, "timeout"
    if att.get("status") == 503:
        return False, "http_503"
    if att.get("status") != 200:
        return False, "http_other"
    if att.get("route_api") == "responses_background" and att.get("final_status") not in ("completed", "incomplete"):
        return False, "bg_failed"
    out = att.get("output") or ""
    if not out.strip():
        return False, "empty"
    if att.get("finish") == "length":
        return False, "truncated"
    if att.get("route_api") == "responses_background" and att.get("final_status") == "incomplete":
        return False, "truncated"
    return True, None


def run_leg(leg, prompt, call_fn, out_name):
    attempts = []
    final, ok = None, False
    for n in (1, 2):
        att = call_fn(prompt)
        att["attempt"] = n
        ok, fail_class = classify(att)
        att["fail_class"] = fail_class
        attempts.append(att)
        with open(os.path.join(HERE, f"{leg}-attempt{n}.md"), "w") as f:
            f.write(f"# {leg} attempt {n}\nstatus {att.get('status')} "
                    f"final={att.get('final_status')} finish={att.get('finish')} "
                    f"fail={fail_class} | wall {att.get('wall_s')}s | "
                    f"cost {'UNVERIFIED' if att.get('cost') is None else '$' + str(att.get('cost'))}\n\n"
                    f"{att.get('output', '')}\n")
        print(f"{leg} attempt {n}: status={att.get('status')} fail={fail_class} "
              f"wall={att.get('wall_s')}s cost={att.get('cost')} "
              f"in={att.get('input_tokens')} out={att.get('output_tokens')} "
              f"reasoning={att.get('reasoning_tokens')} chars={len(att.get('output') or '')}",
              flush=True)
        final = att
        if ok:
            break
        if fail_class in ("timeout", "http_other", "bg_failed"):
            break
    row = {"leg": leg, "model": MODEL, "route_api": final.get("route_api"),
           "effort": final.get("effort"), "cap": final.get("cap"), "ok": ok,
           "attempts": len(attempts), "status": final.get("status"),
           "final_status": final.get("final_status"), "finish": final.get("finish"),
           "fail_class": final.get("fail_class"), "wall_s": final.get("wall_s"),
           "total_wall_s": round(sum(a.get("wall_s", 0) for a in attempts), 2),
           "input_tokens": final.get("input_tokens"),
           "cached_tokens": final.get("cached_tokens"),
           "output_tokens": final.get("output_tokens"),
           "reasoning_tokens": final.get("reasoning_tokens"),
           "near_cap": final.get("near_cap"), "cost": final.get("cost"),
           "total_cost": (None if any(a.get("cost") is None for a in attempts)
                          else round(sum(a.get("cost") or 0 for a in attempts), 5)),
           "output_chars": len(final.get("output") or "")}
    with open(os.path.join(HERE, out_name), "w") as f:
        f.write(final.get("output") or "")
    with open(os.path.join(HERE, "runs.jsonl"), "a") as f:
        f.write(json.dumps(row) + "\n")
    print(f"{leg}: ok={ok} -> {out_name} ({row['output_chars']} chars), "
          f"total_cost={row['total_cost']}")
    return row


SCOUT_PROMPT = """You are the SCOUT in a three-seat design process (Scout maps, Designer drafts, Adjudicator rules). Your job is NOT to write the design. Your job is to MAP the design space for the question in the brief below, so the Designer cannot miss a load-bearing decision.

Output a tight map with these sections:
1. TIP ANATOMY — every candidate field a "tip" (destination profile) might need, each marked CORE / MAYBE / SUSPECT with a one-line reason. A field is CORE only if it changes a routing or shaping decision. Be exhaustive here; striking is the next seats' job.
2. DECISION POINTS — every judgment the router must make from intake to confirmed delivery, in pipeline order. For each: what signals feed it, whether it looks deterministic or model-judgment, and what goes wrong if it's decided badly.
3. FAILURE MODES — every way this router can hurt someone: emitting an ungrounded field, misrouting to the wrong stakeholder, leaking what a destination must never see, silently dropping an item, claiming a delivery that never landed, a learned tip drifting wrong. For each: the concrete scenario (use the brief's worked example), and what would catch it.
4. OPEN QUESTIONS the Designer must take a position on — the genuine forks (e.g. one tip per destination vs per destination-per-job-type; who wins a conflict), stated as forks with the tension named, not answered.

Rules: ground everything in the brief. Do not invent product facts beyond it. No design draft, no schema code — map only.

=== BRIEF ===
{brief}
"""

DESIGNER_PROMPT = """You are the DESIGNER in a three-seat design process. The Scout has mapped the space; you now draft the concrete design. Answer all five questions in the brief, taking a position on every fork the Scout raised.

Required output structure:
1. TIP SCHEMA — the destination profile as an explicit field list (field name, type, what it controls, where its value comes from). Only fields that change a routing or shaping decision survive; if you drop a Scout CORE/MAYBE field, say so in one line.
2. ROUTING DECISION PROCEDURE — numbered steps from "checked item arrives" to "emission list decided". Mark each step DETERMINISTIC or MODEL (with effort tier where a model is used, inside the measured budget: routing decision ≈ $0.025/item at medium). Cover: multi-tip fan-out, no-tip, and how the item's job/source/content signals are used.
3. TIP-LEARNING PROCEDURE — numbered steps for a brand-new destination, building on the existing pattern (per-target translator learns the template + confirmation read-back + exceptions place). Name the evidence sources, the number of examples before trust levels change, the trust levels themselves, and exactly where the operator taps.
4. EXCEPTIONS + CONFLICTS — what lands in the exceptions place and in what record shape; conflict classes (two tips claim an item; stale vs current profile for one destination; a tip's NEVER list vs another tip's required field) and the resolution rule for each, plus what is logged.
5. EMISSION + READ-BACK PROTOCOL — per destination class (API-readable system / upload-only portal / email-or-file drop): how emission happens, how read-back verifies it, what the operator sees, and the failure ladder when read-back mismatches.
6. WORKED TRACE — run the brief's worked example (14 photos, contract PDF, moisture CSV, 2 homeowner emails, scope spreadsheet → 5 destinations) through your design end to end, naming the decision at each step.

Grounding discipline (from the brief) binds you: every emitted field traces to the checked item or the destination's verified template; certainty is never upgraded. Be concrete — vague principles will be struck by the Adjudicator.

=== BRIEF ===
{brief}

=== SCOUT MAP ===
{scout}
"""

ADJUDICATOR_PROMPT = """You are the ADJUDICATOR in a three-seat design process, at maximum effort. The Designer has drafted a router design (below). Your job is to attack it the way the production Adjudicator attacks a fix: find every place where this design would

- emit a field the source item does not support (ungrounded emission),
- misroute an item to the wrong stakeholder or shape,
- leak content into a destination that must never see it,
- silently drop an item, a field, or a failure,
- claim a format, schema, or delivery it never verified,
- upgrade certainty in transit,
- or quietly require effort the one-person operator does not have.

Rule on the draft section by section. Output exactly this structure:

## FINAL DESIGN DECISIONS
The surviving design, restated tight and complete enough to build from: tip schema (final field list), routing decision procedure, tip-learning procedure, exceptions + conflict rules, emission + read-back protocol. Keep what survived verbatim where it was right; rewrite what survived only in amended form, and mark amendments inline as [AMENDED].

## STRUCK LIST
Every element you struck, one per line, in this format:
STRUCK: <the element> — <the concrete failure it would cause, in the worked example's terms>.
If part of an element survives, write it as AMENDED in the decisions above and note the strike of the original form here.

## RESIDUAL RISKS
What still can go wrong under the final design, stated honestly — the risks no rule in the design removes.

Be specific. A strike needs a failure scenario, not a taste objection. The grounding standard from the brief — nothing emitted that is not in the item or the destination's verified template; the production strike on "and any crime / funds-transfer extension" is your model ruling.

=== BRIEF ===
{brief}

=== DESIGNER DRAFT ===
{designer}
"""


def main():
    leg = sys.argv[1]
    with open(os.path.join(HERE, "BRIEF.md")) as f:
        brief = f.read()
    if leg == "scout":
        run_leg("scout", SCOUT_PROMPT.format(brief=brief),
                lambda p: chat_once(p, "low", 8000), "scout-raw.md")
    elif leg == "designer":
        with open(os.path.join(HERE, "scout-raw.md")) as f:
            scout = f.read()
        run_leg("designer", DESIGNER_PROMPT.format(brief=brief, scout=scout),
                lambda p: chat_once(p, "medium", 24000), "designer-raw.md")
    elif leg == "adjudicator":
        with open(os.path.join(HERE, "designer-raw.md")) as f:
            designer = f.read()
        run_leg("adjudicator", ADJUDICATOR_PROMPT.format(brief=brief, designer=designer),
                lambda p: bg_once(p, 60000), "adjudicator-raw.md")
    else:
        print(f"unknown leg: {leg}")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

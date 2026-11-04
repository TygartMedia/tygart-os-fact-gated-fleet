#!/usr/bin/env python3
"""Contribution sweep runner — contributor tier, house fanout pattern.

Usage: sweep.py <jobs.jsonl> <results.json> [cap_usd]
Jobs JSONL: {"leg","id","prompt","max_tokens"?}
Spend cap: cumulative metered cost is checked before each submission;
once the cap is hit, remaining jobs are recorded as SKIPPED_CAP.
One retry per call. Checkpoint written every 20 completions.
Contributor prices: in $0.10/1M, out $0.20/1M.
"""
import json
import os
import sys
import threading
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, "/opt/muse/skills/custom-connector-setup/bin")
from dynamic_credentials import add_surrogate_to_request, read_json_response  # noqa: E402

BASE = "https://api.meta.ai/v1"
PROVIDER = "custom.meta-model-api"
HOSTS = ["api.meta.ai"]
MODEL = "muse-spark-1.3-contributor"
PRICE = {"in": 0.10 / 1e6, "out": 0.20 / 1e6}
CAP = float(sys.argv[3]) if len(sys.argv) > 3 else 9.00

lock = threading.Lock()
state = {"spent": 0.0, "done": 0}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args):
        raise RuntimeError("redirect refused")


def raw(body, timeout=240):
    req = urllib.request.Request(BASE + "/chat/completions",
                                 data=json.dumps(body).encode(), method="POST")
    req.add_header("Content-Type", "application/json")
    add_surrogate_to_request(req, PROVIDER, allowed_hosts=HOSTS)
    with urllib.request.build_opener(NoRedirect()).open(req, timeout=timeout) as resp:
        return read_json_response(resp)


def run_job(job):
    with lock:
        if state["spent"] >= CAP:
            return {**job, "status": "SKIPPED_CAP", "response": None,
                    "input_tokens": None, "output_tokens": None, "cost": 0.0,
                    "seconds": 0.0, "attempts": 0}
    t0 = time.time()
    last_err = None
    budget = job.get("max_tokens", 3000)
    for attempt in (1, 2):
        try:
            payload = raw({"model": MODEL,
                           "messages": [{"role": "user", "content": job["prompt"]}],
                           "max_completion_tokens": budget})
            content = payload["choices"][0]["message"]["content"]
            if not content or not content.strip():
                # Contributor reasoning can consume the whole token budget and
                # emit no visible content (content=null). Retry with 2x budget.
                raise ValueError("empty content (reasoning consumed budget)")
            u = payload.get("usage") or {}
            it, ot = u.get("prompt_tokens", 0), u.get("completion_tokens", 0)
            cost = it * PRICE["in"] + ot * PRICE["out"]
            with lock:
                state["spent"] += cost
                state["done"] += 1
            return {**job, "status": "OK", "response": content,
                    "input_tokens": it, "output_tokens": ot,
                    "cost": round(cost, 6), "seconds": round(time.time() - t0, 2),
                    "attempts": attempt}
        except Exception as e:  # noqa: BLE001
            last_err = repr(e)
            budget = min(budget * 2, 16000)
            time.sleep(2)
    with lock:
        state["done"] += 1
    return {**job, "status": "ERROR", "response": f"ERROR: {last_err}",
            "input_tokens": None, "output_tokens": None, "cost": None,
            "seconds": round(time.time() - t0, 2), "attempts": 2}


def main():
    jobs = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]
    out_path = sys.argv[2]
    t0 = time.time()
    results = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        for i, r in enumerate(ex.map(run_job, jobs)):
            results.append(r)
            if i % 20 == 19:
                with open(out_path + ".partial", "w") as f:
                    json.dump(results, f, indent=1)
    wall = round(time.time() - t0, 2)
    ok = [r for r in results if r["status"] == "OK"]
    total = round(sum(r["cost"] or 0 for r in results), 5)
    summary = {"jobs": len(jobs), "ok": len(ok),
               "errors": sum(1 for r in results if r["status"] == "ERROR"),
               "skipped_cap": sum(1 for r in results if r["status"] == "SKIPPED_CAP"),
               "wall_seconds": wall, "total_cost": total,
               "input_tokens": sum(r["input_tokens"] or 0 for r in results),
               "output_tokens": sum(r["output_tokens"] or 0 for r in results)}
    with open(out_path, "w") as f:
        json.dump({"summary": summary, "results": results}, f, indent=1)
    print(json.dumps(summary))


if __name__ == "__main__":
    main()

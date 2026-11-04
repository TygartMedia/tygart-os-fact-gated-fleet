#!/usr/bin/env python3
"""Verify extractor quotes verbatim against each recording's source files.

Normalization: lowercase, collapse every non-alphanumeric run to one space.
A quote is VERIFIED iff its full normalized form appears in the normalized
text of the named source file. Also records a PREFIX check (first 12 words)
to distinguish near-misses from inventions.
Outputs work/quotes-verified.json: per rec, findings with verify status.
"""
import json
import re

VT = "/home/hatch/workspace/out/model-bakeoff/video-test"
WORK = "/home/hatch/workspace/out/meta-hackathon-2026/corpus-pickout/work"
FILES = ["SESSION-REPORT.md", "USER-READ.md", "AGENT-READ.md", "TRANSCRIPT.md"]


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def parse_json_lenient(resp):
    if not resp:
        return None
    try:
        return json.loads(resp)
    except Exception:
        pass
    m = re.search(r"\{.*\}", resp, re.S)
    if m:
        try:
            return json.loads(m.group(0))
        except Exception:
            return None
    return None


def main():
    data = json.load(open(f"{WORK}/results-recs.json"))
    out = {}
    stats = {"recs": 0, "parse_ok": 0, "parse_fail": [],
             "findings": 0, "verified": 0, "prefix_only": 0, "not_found": 0,
             "absent": 0}
    for r in data["results"]:
        rec = r["id"]
        stats["recs"] += 1
        obj = parse_json_lenient(r.get("response") or "")
        if obj is None:
            stats["parse_fail"].append(rec)
            out[rec] = {"parse": "FAIL", "raw_status": r["status"]}
            continue
        stats["parse_ok"] += 1
        src = {}
        for fn in FILES:
            try:
                src[fn] = norm(open(f"{VT}/{rec}/{fn}").read())
            except FileNotFoundError:
                src[fn] = ""
        findings = []
        for f in obj.get("findings") or []:
            q = f.get("quote", "")
            nq = norm(q)
            target = src.get(f.get("source_file", ""), "")
            if nq and nq in target:
                status = "VERIFIED"
                stats["verified"] += 1
            elif nq and " ".join(nq.split()[:12]) in target:
                status = "PREFIX-ONLY"
                stats["prefix_only"] += 1
            else:
                status = "NOT-FOUND"
                stats["not_found"] += 1
            stats["findings"] += 1
            findings.append({**f, "verify": status})
        if obj.get("findings_absent"):
            stats["absent"] += 1
        out[rec] = {"parse": "OK", "one_line": obj.get("one_line", ""),
                    "findings": findings,
                    "findings_absent": bool(obj.get("findings_absent")),
                    "read_aloud": obj.get("read_aloud") or {}}
    json.dump({"stats": stats, "recs": out}, open(f"{WORK}/quotes-verified.json", "w"), indent=1)
    print(json.dumps(stats, indent=1))


if __name__ == "__main__":
    main()

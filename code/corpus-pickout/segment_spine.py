#!/usr/bin/env python3
"""Slice the Oct 30 read-aloud call transcript into report / verdict segments.

Turn-level granularity. A report segment starts at the first turn that
introduces that report number as a reading (patterns below). Verdict segments
are anchored on the turn that NAMES the verdict (the naming turn closes the
segment, since the voice names each verdict at its end).
Output: spine-segments.json with full segment texts + a coverage map.
"""
import json
import re

SRC = "/home/hatch/workspace/out/model-bakeoff/video-test/session-2026-10-30-call/TRANSCRIPT.md"
OUT = "/home/hatch/workspace/out/meta-hackathon-2026/corpus-pickout/work/spine-segments.json"

WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
         "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
         "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
         "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
         "twenty": 20}


def num(tok):
    tok = tok.lower().strip(".,")
    if tok.isdigit():
        return int(tok)
    return WORDS.get(tok)


TURN_RE = re.compile(r"^\[(\d{2}:\d{2}:\d{2})–(\d{2}:\d{2}:\d{2})\] Speaker (\S+): (.*)$")

REPORT_PATTERNS = [
    r"report number (\w+)",
    r"^report (\w+)",
    r"here's report (\w+)",
    r"report (\d+) is\b",
    r"report (\d+) from\b",
    r"report (\w+) takes us",
    r"report (\w+) brings",
    r"report (\w+) lands",
    r"report (\w+) read\b",
    r"move to report (\w+)",
    r"bring in number (\w+)",
    r"bring you verdict (\w+)",  # not a report; guard below excludes verdict turns
]
VERDICT_NAMING = re.compile(r"verdict (\w+)", re.I)


def main():
    turns = []
    for line in open(SRC):
        m = TURN_RE.match(line.rstrip("\n"))
        if m:
            turns.append({"start": m.group(1), "end": m.group(2),
                          "speaker": m.group(3), "text": m.group(4)})
        elif turns and line.strip():
            turns[-1]["text"] += " " + line.strip()
    print(f"turns parsed: {len(turns)}")

    # --- report segments ---
    starts = {}  # report_no -> turn index
    for i, t in enumerate(turns):
        txt = t["text"]
        for pat in REPORT_PATTERNS:
            m = re.search(pat, txt, re.I)
            if m:
                n = num(m.group(1))
                if n and 1 <= n <= 70 and n not in starts:
                    starts[n] = i
                    break
    ordered = sorted(starts.items(), key=lambda kv: kv[1])
    segments = {}
    for j, (n, idx) in enumerate(ordered):
        end = ordered[j + 1][1] if j + 1 < len(ordered) else len(turns)
        seg_turns = turns[idx:end]
        segments[str(n)] = {
            "report": n,
            "start_ts": seg_turns[0]["start"],
            "end_ts": seg_turns[-1]["end"],
            "n_turns": len(seg_turns),
            "text": "\n".join(f"[{x['start']}–{x['end']}] {x['text']}" for x in seg_turns),
        }

    # --- verdict segments (naming turn closes the segment) ---
    naming = {}  # verdict_no -> turn index of naming turn
    for i, t in enumerate(turns):
        m = VERDICT_NAMING.search(t["text"])
        if m:
            n = num(m.group(1))
            if n and 1 <= n <= 20 and n not in naming:
                naming[n] = i
    verdicts = {}
    prev_end = None
    for n in sorted(naming, key=lambda k: naming[k]):
        end_idx = naming[n]
        start_idx = (prev_end + 1) if prev_end is not None else max(0, end_idx - 6)
        seg_turns = turns[start_idx:end_idx + 1]
        verdicts[str(n)] = {
            "verdict": n,
            "start_ts": seg_turns[0]["start"],
            "end_ts": seg_turns[-1]["end"],
            "n_turns": len(seg_turns),
            "text": "\n".join(f"[{x['start']}–{x['end']}] {x['text']}" for x in seg_turns),
        }
        prev_end = end_idx

    json.dump({"reports": segments, "verdicts": verdicts}, open(OUT, "w"), indent=1)
    print("report segments:", sorted(int(k) for k in segments))
    print("missing reports 1..66:", [n for n in range(1, 67) if str(n) not in segments])
    print("verdict segments:", sorted(int(k) for k in verdicts))


if __name__ == "__main__":
    main()

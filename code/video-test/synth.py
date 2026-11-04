#!/usr/bin/env python3
"""Synthesis stack for one recording: session report + naive user read.
Usage: synth.py <rec_dir> <minutes>"""
import glob, json, sys, urllib.request, urllib.error
sys.path.insert(0, "/opt/muse/skills/custom-connector-setup/bin")
from dynamic_credentials import add_surrogate_to_request, read_json_response

class NR(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a): raise RuntimeError("redirect")

def call(prompt, mt=12000):
    body = {"model": "muse-spark-1.3", "messages": [{"role": "user", "content": prompt}], "max_tokens": mt}
    req = urllib.request.Request("https://api.meta.ai/v1/chat/completions",
                                 data=json.dumps(body).encode(), method="POST")
    req.add_header("Content-Type", "application/json")
    add_surrogate_to_request(req, "custom.meta-model-api", allowed_hosts=["api.meta.ai"])
    try:
        with urllib.request.build_opener(NR()).open(req, timeout=300) as r:
            pl = read_json_response(r)
            return pl["choices"][0]["message"]["content"], pl.get("usage")
    except urllib.error.HTTPError as e:
        return f"ERROR {e.code}", None

def main():
    rec, minutes = sys.argv[1], sys.argv[2]
    files = sorted(glob.glob(f"{rec}/window-*.md"))
    reports = "\n\n".join(f"===== {f} =====\n" + open(f).read() for f in files)
    n = len(files)
    session_prompt = (f"Below are {n} window reports from one {minutes}-minute screen recording, in order "
        "(each covers about 2 minutes). Write the session report:\n"
        "1. SUMMARY: one paragraph — what this session was.\n"
        "2. TIMELINE: the phases of the session with minute ranges and what happened in each.\n"
        "3. ACCOMPLISHED: what got done, concretely.\n"
        "4. PROBLEMS: failures, errors, friction visible in the reports.\n"
        "5. WORKFLOW: the working pattern between the person and any AI/tools on screen.\n"
        "Use only what the window reports say. Where they disagree or are vague, say so.\n\n" + reports)
    text, u = call(session_prompt)
    open(f"{rec}/SESSION-REPORT.md", "w").write(text)
    print(f"session report: {len(text)} chars, usage {u}")
    user_prompt = (f"Below are {n} window reports from one {minutes}-minute screen recording of a person working, in order. "
        "The session itself is summarized elsewhere. YOUR job is different: read the PERSON.\n"
        "Write a USER READ with these sections:\n"
        "1. PATTERNS: recurring behaviors, rhythms, and habits of the person across the session.\n"
        "2. MANNERISMS: small tells — how they check, wait, scroll, react, switch context.\n"
        "3. FRICTION: moments where the tools or interfaces failed the person, inferred from behavior "
        "(re-checking, polling, re-reading, idle waiting, workarounds).\n"
        "4. SUGGESTIONS: concrete interface or workflow changes each friction point implies.\n"
        "Rules: base every claim on the reports; quote the behavior behind each claim briefly; "
        "this is ONE session — label anything that could be a one-off as tentative. "
        "Do not invent biography or motives you cannot see.\n\n" + reports)
    text, u = call(user_prompt)
    open(f"{rec}/USER-READ.md", "w").write(text)
    print(f"user read: {len(text)} chars, usage {u}")

if __name__ == "__main__":
    main()

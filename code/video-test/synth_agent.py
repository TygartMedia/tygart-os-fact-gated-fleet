#!/usr/bin/env python3
"""Third pool: the agent read — how the AI seat on screen thought and behaved.
Usage: synth_agent.py <rec_dir> <minutes>"""
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
    prompt = (f"Below are {n} window reports from one {minutes}-minute screen recording, in order. "
        "The screen shows a person (Will) working with AI agent seats (for example Antigravity/AGY, "
        "Cursor, Grok, Claude, Glint) executing work orders. Write the AGENT READ — an analysis of the "
        "AI's behavior only, not the person's:\n"
        "1. SEAT AND MODEL: which AI/tool is on screen, and any model names or selector labels visible "
        "(quote them exactly as the reports give them; say when none is visible).\n"
        "2. HOW IT THOUGHT: its visible reasoning pattern — planning, checking, guessing, verifying. "
        "Granular moments only, no generalities.\n"
        "3. CONFUSION AND ADAPTATION: anywhere the agent misunderstood the task, the environment, or "
        "the work order's framing — especially any mismatch between how the work order described the "
        "execution surface (e.g. shell/PowerShell terms) and the surface the agent was actually in — "
        "and how it recovered: did it adapt, learn to ignore the mismatch, or stay stuck?\n"
        "4. STALLS AND REFUSALS: anywhere the agent stopped, refused, claimed it could not do the work, "
        "looped, or had to be rescued — and what unblocked it. Note ANY model switch mid-session "
        "(which model out, which in, and whether the work then finished).\n"
        "5. WORKAROUNDS IT INVENTED: anything it devised itself to get past a gap.\n"
        "6. LESSONS FOR THE WORK ORDER: what the brief/writer could do differently so the next agent "
        "does better — only lessons the evidence supports.\n"
        "Use only what the window reports say. Where they disagree or are vague, say so.\n\n" + reports)
    text, u = call(prompt)
    open(f"{rec}/AGENT-READ.md", "w").write(text)
    print(f"agent read: {len(text)} chars, usage {u}")

if __name__ == "__main__":
    main()

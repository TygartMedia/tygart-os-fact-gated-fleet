#!/usr/bin/env python3
"""Session reader: frame-strip -> windowed Spark reads -> session synthesis.
Usage: run_session.py <frames_dir> <out_dir> [window=12] [workers=6]"""
import base64, glob, json, os, sys, time
import urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, "/opt/muse/skills/custom-connector-setup/bin")
from dynamic_credentials import add_surrogate_to_request, read_json_response
BASE = "https://api.meta.ai/v1"

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args):
        raise RuntimeError("redirect refused")

def call(body, timeout=300):
    req = urllib.request.Request(BASE + "/chat/completions", data=json.dumps(body).encode(), method="POST")
    req.add_header("Content-Type", "application/json")
    add_surrogate_to_request(req, "custom.meta-model-api", allowed_hosts=["api.meta.ai"])
    try:
        with urllib.request.build_opener(NoRedirect()).open(req, timeout=timeout) as resp:
            return resp.status, read_json_response(resp)
    except urllib.error.HTTPError as e:
        try: return e.code, json.loads(e.read().decode() or "{}")
        except Exception: return e.code, {}
    except Exception as e:
        return None, {"error": f"{type(e).__name__}: {e}"}

def window_report(frames_dir, out_dir, widx, files, fps_step=10):
    out = os.path.join(out_dir, f"window-{widx:02d}.md")
    if os.path.exists(out) and os.path.getsize(out) > 300:
        return {"window": widx, "skipped": True}
    start_s = (widx - 1) * 12 * fps_step
    end_s = start_s + (len(files) - 1) * fps_step
    parts = [{"type": "text", "text": (
        f"These are {len(files)} frames from a screen recording, taken {fps_step} seconds apart, "
        f"covering minute {start_s//60}:{start_s%60:02d} to {end_s//60}:{end_s%60:02d} of the session, in order. "
        "Write a compact report with four short sections:\n"
        "SCREEN: what application/page is shown and its key visible content (read text where legible).\n"
        "CHANGES: what changes across these frames, in order.\n"
        "WORK: what the person appears to be doing or accomplishing.\n"
        "NOTABLE: anything unusual, any errors or failures visible, and anything you cannot identify.\n"
        "Be specific and factual. Do not invent content you cannot see.")}]
    for f in files:
        b = base64.b64encode(open(f, "rb").read()).decode()
        parts.append({"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b}"}})
    t0 = time.time()
    status, payload = call({"model": "muse-spark-1.3",
                            "messages": [{"role": "user", "content": parts}], "max_tokens": 6000})
    row = {"window": widx, "status": status, "wall_s": round(time.time() - t0, 1)}
    if status == 200:
        try:
            text = payload["choices"][0]["message"]["content"]
            open(out, "w").write(text)
            row["usage"] = payload.get("usage"); row["chars"] = len(text)
        except Exception as e:
            row["error"] = f"parse: {e}"
    else:
        row["error"] = json.dumps(payload)[:200]
    with open(os.path.join(out_dir, "session-manifest.jsonl"), "a") as fh:
        fh.write(json.dumps(row) + "\n")
    return row

def main():
    frames_dir, out_dir = sys.argv[1], sys.argv[2]
    W = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    workers = int(sys.argv[4]) if len(sys.argv) > 4 else 6
    os.makedirs(out_dir, exist_ok=True)
    files = sorted(glob.glob(os.path.join(frames_dir, "f*.jpg")))
    windows = [(i // W + 1, files[i:i + W]) for i in range(0, len(files), W)]
    print(f"{len(files)} frames -> {len(windows)} windows")
    t0 = time.time(); done = err = skip = 0
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for row in ex.map(lambda x: window_report(frames_dir, out_dir, *x), windows):
            if row.get("skipped"): skip += 1
            elif row.get("error") or row.get("status") != 200:
                err += 1; print("ERR window", row.get("window"), row.get("error", row.get("status")))
            else:
                done += 1; print(f"window {row['window']}: {row['wall_s']}s {row['usage']['total_tokens']} tok")
    print(f"windows: {done} done, {skip} skipped, {err} errors, wall {time.time()-t0:.0f}s")

if __name__ == "__main__":
    main()

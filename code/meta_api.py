#!/usr/bin/env python3
"""Meta Model API helper — calls api.meta.ai with the vault-stored key via surrogate.

Usage:
  meta_api.py models                 -> GET /v1/models (key verification, harmless read)
  meta_api.py chat <model> <prompt>  -> POST /v1/chat/completions (OpenAI-compatible)
The credential is never read directly; dynamic_credentials places a surrogate and
Muse swaps in the real key only on the approved request to api.meta.ai.
"""
import json
import sys
import urllib.request

sys.path.insert(0, "/opt/muse/skills/custom-connector-setup/bin")
from dynamic_credentials import add_surrogate_to_request, read_json_response

BASE = "https://api.meta.ai/v1"
PROVIDER = "custom.meta-model-api"
HOSTS = ["api.meta.ai"]


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args):
        raise RuntimeError("redirect refused, verify the endpoint")


def call(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(BASE + path, data=data, method=method)
    if data is not None:
        req.add_header("Content-Type", "application/json")
    add_surrogate_to_request(req, PROVIDER, allowed_hosts=HOSTS)
    with urllib.request.build_opener(NoRedirect()).open(req, timeout=60) as resp:
        return resp.status, read_json_response(resp)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    cmd = sys.argv[1]
    if cmd == "models":
        status, payload = call("GET", "/models")
        ids = [m.get("id") for m in payload.get("data", [])]
        print(json.dumps({"status": status, "model_count": len(ids), "models": ids}, indent=2))
    elif cmd == "chat":
        model, prompt = sys.argv[2], sys.argv[3]
        status, payload = call("POST", "/chat/completions", {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
        })
        print(json.dumps({"status": status, "payload": payload}, indent=2))
    else:
        print(f"unknown command: {cmd}")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

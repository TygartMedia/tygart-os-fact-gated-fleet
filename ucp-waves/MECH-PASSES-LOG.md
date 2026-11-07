# MECHANICAL PASSES — Log (Wave 1 staged bodies, gap-sheet rulings executed)

**Programme:** UCP full-site refresh — theuniversalcommerceprotocol.com
**Fired:** 2026-11-06 night (Will's "Proceed," 17:33 PT). Stage-only: no site edits, no publishing, no redirects, no authenticated requests.
**Law applied:** Sheets 7 (rate limits) & 8 (identity/DID), earned 2026-11-06 · dispositions verbatim from `GAP-REJUDGE.md` / leg outputs `raw/RJ-D1/D2/D4/E5.md` · E1 under Sheet 3 items 3–6.
**Method:** one contributor leg per body via `raw/run_leg_v2.py` (`muse-spark-1.3-contributor`, low effort, cap 16,000), E3-corrective pattern — governing rulings first in the prompt, disposition list verbatim, sheet text embedded, staged body as source. Prompts: `wave-1/prompts/MECH-*.txt`. Raw outputs: `raw/MECH-*.md`. **Every result was verified by Glint on the output file (greps + context spot-reads + one full diff) BEFORE the staged file was overwritten.** Pre-pass backups of all five bodies: `wave-1/staged/pre-gap/`.
**Result: 5 legs, 5 PASS, zero corrective re-runs needed.** All five Wave 1 blockers named in GAP-REJUDGE are now executed.

---

## D2 → `staged/1695.html` — PASS (leg MECH-D2)

- **Leg:** in 5,965 / out 4,323 / reasoning 1,436 · status 200, finish `stop`, try 1, wall 25.94 s. Cached 0.
- **Baseline surprise (recorded):** the Wave 1 staged body already contained NONE of the forbidden number/header strings — the original write leg had generalised them out — but it also contained **zero** occurrences of the one settled fact (429 / Retry-After), and its sections still framed limits/quotas as UCP mechanics ("quota" ×8, heading "Rate-Limit Headers and Limit Handling"). The pass therefore did three things: confirmed the 17 CUTs absent in all ruled phrasings, inserted the settled fact, and labeled the spine.
- **Checks (verbatim results):**
  - Forbidden strings `1,000 RPM|10,000 RPM|100 RPS|500 RPS|2,000 RPS|X-RateLimit|X-UCP-RateLimit` in output: **0 matches** (final staged sweep: grep count 0).
  - Settled fact present: `429` ×2, `Retry-After` ×1, `retry_after` ×1. Stated at Sheet 7 strength, verbatim in substance: *"UCP's specification defines HTTP 429 "Too many requests" as a protocol error, and 429/503 responses SHOULD carry a Retry-After header (REST) or error.data.retry_after (MCP). The spec's "60" is an illustrative example, NOT a quota or default. No published UCP rate limits exist. The protocol standardizes this signal, not any numbers, tiers, quotas, or other headers."* (The output's one remaining "tier" token is inside this negation.)
  - Ride-label: sections carry "General Engineering Practice, Not UCP Specification" — label family counts: "general API engineering practice" ×10, "not UCP specification" ×20. The ruled headers section was retitled "Handling Limit Responses — General Engineering Practice, Not UCP Specification"; "Scaling Beyond Standard Limits" → "Planning for Additional Capacity — General Practice".
- **Words (HTML-strip):** 1,728 → 1,863 (+135 — the settled-fact paragraph + per-section labels; no new claims, verified by the forbidden-string sweep).
- **Deviation, recorded not repaired:** the first heading still reads "How UCP Rate Limiting Works." Its section now states the settled fact and "No published UCP rate limits exist" in its third paragraph and makes no UCP-defines-limits claim; judged compliant with the pass's checks. Flagged here so publish QC sees it with eyes open.

## D1 → `staged/1942.html` — PASS (leg MECH-D1)

- **Leg:** in 5,656 / out 4,125 / reasoning 1,771 · 200 / `stop` / try 1, wall 24.21 s.
- **Checks:**
  - UCP-attribution grep (`UCP (provides|enables|uses|supports|adheres|relies|creates|issues)` + DID-attribution patterns): **0 lines** in output and in the final staged file.
  - Every surviving DID-family mention spot-read in context: all sit inside sections headed **"Background: decentralized identifiers (W3C) — not part of UCP"** (heading ×3) or carry the explicit label (FAQ: *"…as W3C technology that is NOT part of UCP"*). Surviving counts are small: DID ×4, DIDs ×2, DIDComm ×1, verifiable credential ×4, ledger ×1, blockchain ×1 — all background.
  - UCP identity statements match Sheet 8's model only: `keys[]` ×2, `identity_linking` ×2, `/.well-known/ucp` ×2, AP2 ×1, RFC 9421 ×1, mTLS ×1, OAuth ×3.
- **Words:** 1,348 → 1,416 (+68 — CUT sentences were claim-level inside sections whose surrounding prose survived; the reframed background gained explicit headings/labels. No new claims: attribution sweep is 0.)

## D4 → `staged/1253.html` — PASS (leg MECH-D4)

- **Leg:** in 5,676 / out 4,389 / reasoning 1,844 · 200 / `stop` / try 1, wall 24.46 s.
- **Checks:**
  - The four confirmed 7261 stub claims: `mathematically impossible` **0**, `secured enclave` **0**, "tackles this through (DIDs)" **0**, "verified against a public ledger" **0** — none present, none leaked back in.
  - `UCP (defines|standardizes|requires|uses|supports|provides|tackles)` attribution grep: **0 lines**.
  - Surviving smart-contract ×4 / verifiable-credential ×4 mentions spot-read: all are generic agentic-commerce security / vendor-landscape survey content (e.g. "Smart contracts can implement dispute resolution logic…" as an industry technique; a "Verifiable Credentials and Attestations" explainer section) — none attributed to UCP. "not part of UCP" label ×2 present for the reframed DID background.
- **Words:** 1,696 → 1,710 (+14 — labels; see D1 note on the pattern.)

## E5 → `staged/1908.html` — PASS (leg MECH-E5)

- **Leg:** in 5,350 / out 4,646 / reasoning 2,423 · 200 / `stop` / try 1, wall 27.45 s.
- **Checks — the component list, verbatim from the output:**
  - *"Profiles — businesses publish a UCP profile at /.well-known/ucp declaring their capabilities and payment handlers"*
  - *"Capabilities — named {reverse-domain}.{service}.{capability}"*
  - *"Payment handlers — advertised in the profile's ucp.payment_handlers"*
  - *"Keys — the profile's keys[] (RFC 7517 JWK set) used for signature verification"*
  - No DID / blockchain / smart-contract / reputation entries in the list.
  - Narrowed SETTLED-KEEP, verbatim: *"UCP defines product data through its catalog capability schemas (product/variant JSON schemas for search and lookup)."*
  - Narrowed crypto line, verbatim: *"The v2026-08-25 release record lists crypto-currency data specifications and a crypto_payer field among its payment additions."* (Micro-deviation, recorded: the PR trace numbers #942/#1000 from Sheet 8's form were dropped; the claim's scope is identical — narrowed to the release record — so this is not a broadening and not a verification failure.)
  - Followed by the explicit negation: *"UCP contains no DID layer, no blockchain, no smart contracts, no verifiable credentials, no reputation system."* plus the retained general-concepts disclaimer. The only grep hits for the ruled CUT phrasings are inside that negation.
- **Words:** 1,253 → 1,266 (+13.)

## E1 → `staged/5793.html` — PASS (leg MECH-E1)

- **Leg:** in 7,809 / out 8,530 / reasoning 2,201 · 200 / `stop` / try 1, wall 38.24 s (largest body of the five).
- **Checks — full diff against `pre-gap/5793.html`: exactly TWO changes, both auth-only; the rest of the body is byte-identical.**
  1. Checklist line 107: "mutual TLS" → **"mutual TLS (mTLS)"** — mTLS now present by name (`mTLS` ×1, "mutual TLS" ×1) as a verification route alongside RFC 9421 ES256 against the ucp.goog profile.
  2. New line 186, directly before the Python example: *"The Authorization header in the Python example below is mock local-test scaffolding only — not production UCP authentication."*
  - **Bearer count: 3 — every instance quoted and accounted:**
    1. Line 107: *"…and do not treat a Bearer token as the production UCP authentication pattern."* — a corrective negation; acceptable as-is under the plan's allowance.
    2. Line 139: curl example `-H "Authorization: Bearer <token>"` — labeled by the adjacent pre-existing text at line 110: *"The Authorization header here is an explicitly mock test token for local testing only, not a production UCP authentication pattern."* (This label was already in the staged body; the pass confirmed it rather than adding it.)
    3. Line 212: Python example `"Authorization": f"Bearer {self.auth_token}"` — now labeled by the leg's added line 186 (above).
  - Bearer is nowhere presented as the production pattern. The Wave 1 log's E1 publish-blocker ("mTLS absent, 3 Bearer references remain") is **cleared**: mTLS present, all 3 Bearer instances either negated or explicitly mock-labeled.
- **Words:** 3,203 → 3,222 (+19 — the "(mTLS)" token + the added label sentence. The pre-existing length drift vs the plan's 4,200–4,500 target stands as recorded in WAVE-1-LOG; this pass was auth-only by brief and did not touch it.)

---

## Engine record (this pass set)

5 legs (MECH-D2, MECH-D1, MECH-D4, MECH-E5, MECH-E1), all `muse-spark-1.3-contributor`, low / 16,000 via `run_leg_v2.py`: **5/5 status 200, finish `stop`, try 1 — zero empties, zero truncations, zero retries, zero error bodies.** Totals: **30,456 in / 26,013 out / 9,675 reasoning (37.2%)**, cached 0 throughout. Reasoning share ran leaner than both Phase 0b (79%) and the gap earn (68.9%) — these were dossier-fed surgical legs, the shape that has finished clean all programme. Programme to date: **47 calls, 290,080 in / 221,319 out** (42 calls / 259,624 in / 195,306 out through the gap earn, per GAP-REJUDGE, + this set's 5 calls / 30,456 in / 26,013 out). Spend signal: **none** — no response or balance signal showed any card charge; contributor tier still reads $0 against the $25 envelope (pricing UNVERIFIED, as before).
Process errors: none in the legs. Two Glint-side notes, owned: (1) the baseline greps found D2's staged body already free of the ruled number strings — the pass's D2 work was insertion + labeling, not deletion, and the log says so rather than claiming 17 deletions; (2) prompt assembly embedded the RJ disposition lists verbatim plus Glint's two D2 corrections (bullet 4's settled component, bullet 12's sandbox CUT) stated as governing rulings in the prompt head.

## Publish-readiness — updated picture

Every Wave 1 **content** blocker named anywhere in the programme record is now executed:

- D2's 17 CUTs + ride-labels — **done** (this log).
- D1's 13 DID-attribution CUTs + 4 reframes — **done**.
- D4's 7 CUTs (incl. the confirmed 7261 four) + 1 reframe — **done**.
- E5's component-list replacement + 7 CUTs — **done**; the blocker GAP-REJUDGE described as "stands as staged, now ruled" no longer stands.
- E1's auth correction (mTLS + Bearer) — **done**; blocker cleared.

**What still blocks publish — nothing content-side in Wave 1.** The remaining gates are exactly the three named before these passes: **(1) Will's Tap 2** (the 19→10 redirect map — proposals only, nothing executed), **(2) Will's Tap 3** (publishing the staged bodies), and **(3) the app-password lane** (still unverified: the browser admin session is Will's own verified login; the saved app-password entry was paired with the author-slug username, not the `admin` account, so the programmatic publish lane remains unproven). Non-blocking publish-time routing, unchanged: the 27 REMAINS-NV items route at publish QC (hold / consolidate / label) per UNJUDGEABLE discipline; D3/E2/E4/E6 staged bodies were outside this pass set by brief and carry only their WAVE-1-LOG-noted dispositions (E3 corrective re-run already landed and verified; E6's ownership correction already in its staged body).

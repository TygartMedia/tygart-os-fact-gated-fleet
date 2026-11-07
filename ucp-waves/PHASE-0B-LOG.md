# PHASE 0B LOG — Fact-Sheet Build

**Programme:** UCP full-site wave programme — theuniversalcommerceprotocol.com
**Phase:** 0b (fact sheets) · **Date:** 2026-11-06 · **Executor:** Glint (direct)
**Engine:** Meta Model API, `muse-spark-1.3-contributor`, every leg. Glint fetches primary sources, writes prompts, spot-checks output (Guard 14), publishes sheets. No leg's output was silently replaced by Glint synthesis; where a dossier fed a leg, the sheet says so.
**Deliverables:** `sheets/SHEET-1..6` · `UNJUDGEABLE.md` · this log. Raw leg outputs in `raw/`; machine ledger in `calls.jsonl`.

## Call ledger (every contributor call, in order)

| # | Leg | Sheet | Try | Status | Finish | In | Cached | Out | Reasoning | Visible chars | Wall |
|---|-----|-------|-----|--------|--------|----|--------|-----|-----------|---------------|------|
| 1 | L1 | 1 (spec overview extraction) | 1 | 200 | length | 7,356 | 0 | 8,000 | 6,117 | 8,681 | 44.19s |
| 2 | L1 | 1 | 2 (auto-retry) | 200 | length | 7,356 | 7,267 | 8,000 | 5,715 | 10,641 | 41.05s |
| 3 | L2 | 3 (FAQ, first form) | 1 | 200 | length | 1,245 | 0 | 5,000 | 4,998 | **0** | 33.49s |
| 4 | L2 | 3 | 2 (auto-retry) | 200 | length | 1,245 | 0 | 5,000 | 4,998 | **0** | 36.12s |
| 5 | L2b | 3 (FAQ, corrected) | 1 | 200 | stop | 841 | 0 | 3,280 | 2,587 | 2,934 | 20.86s |
| 6 | L3 | 2 (AP2) | 1 | 200 | stop | 1,113 | 0 | 5,095 | 3,961 | 5,046 | 38.43s |
| 7 | L4 | 4 (platforms) | 1 | 200 | stop | 2,201 | 0 | 7,029 | 4,673 | 11,140 | 43.93s |
| 8 | L5 | 5 (networks) | 1 | 200 | stop | 1,601 | 0 | 5,102 | 3,280 | 8,838 | 28.91s |
| 9 | L6 | 6 (adjacent) | 1 | 200 | stop | 2,496 | 0 | 4,337 | 1,756 | 10,738 | 27.72s |
| 10 | L7 | 1+3 (releases/governance) | 1 | 200 | stop | 1,849 | 0 | 5,760 | 4,170 | 7,214 | 35.29s |
| 11 | L8 | 1 (gap-fill: payments/keys) | 1 | 200 | stop | 424 | 0 | 1,820 | n/r* | 1,528 | 10.95s |
| 12 | L9 | 1 Annex A (release notes, full PR list) | 1 | 200 | length | 4,091 | 0 | 8,000 | 7,998 | **0** | 51.15s |
| 13 | L9 | 1 Annex A | 2 (auto-retry) | 200 | length | 4,091 | 0 | 8,000 | 7,422 | 2,637 (truncated mid-list) | 37.36s |
| 14 | L9b | 1 Annex A (remainder, pre-grouped) | 1 | 200 | stop | 886 | 0 | 1,638 | n/r* | 3,217 | 10.83s |
| 15 | L10 | 2 (AP2 primary: repo README + spec overview) | 1 | 200 | stop | 907 | 0 | 3,312 | n/r* | 3,623 | 17.24s |

**Totals:** 15 API calls (12 leg invocations) · input 37,702 tokens · output 79,373 tokens · wall ≈ 477s.
*L8's, L9b's and L10's ledger records did not carry a reasoning-token split; the runner summaries reported in/out only. Reasoning share across the 12 calls that did report it: ≈ 58,100 of 72,600 output tokens (~80%).
**Cost: UNVERIFIED.** Contributor-tier pricing is not established on this programme's record; the $25 test envelope (Will's personal Meta account, Stefani's card) governs. No figure is printed rather than an invented one.

## Behaviour findings (the point of the exercise)

1. **Reasoning eats the cap.** Across all 10 calls, reasoning consumed 55–100% of the output budget. At cap 5,000 (L2) reasoning took 4,998 of 5,000 tokens and returned **zero visible characters, twice in a row** — the content:null-class failure, reproduced deterministically at identical token counts. At cap 8,000 every leg returned visible output. **Operating rule banked: no contributor leg under cap 8,000; split sources rather than raise the cap.**
2. **Truncation at the cap is silent in shape.** L1 hit `finish=length` on both tries and returned a well-formed 116-claim list whose tail was cut mid-section (payments/security detail missing). The runner's auto-retry on `finish=length` produced a longer second output (10,641 vs 8,681 chars, 7,267 cached input tokens) but the same structural cut. Sheet 1 marked the uncovered sections NOT SETTLED; a follow-up gap-fill leg (L8) then closed the payments/keys gap with a 12-line extraction, and the error-code headings were confirmed to carry no definitions in the excerpt — the residual NOT SETTLED items on Sheet 1 are the honest remainder.
3. **Retry policy held.** One automatic retry on 503/empty/`finish=length`; never on timeout. L2's retry repeated the failure exactly (same counts) — evidence the empty output is a budget property, not a transient.
3b. **The empty-output failure recurs at cap 8,000 on long inputs.** L9 (4,091 input tokens, ~120 PR entries) burned 7,998 of 8,000 output tokens on reasoning in try 1 and returned 0 visible characters; try 2 returned a list truncated mid-sentence at claim 25. The fix that worked was structural, not budgetary: L9b received the remainder pre-grouped by theme and finished clean in 10.83s at 1,638 output tokens. **Banked rule: long enumerations get split by section before the call, never after the failure.**
4. **Dossier legs are clean; raw-source legs are where the model strains.** Legs fed a faithful Glint-prepared dossier (L3–L7) all finished `stop` on first try. The two legs fed raw source text (L1, L2) are the two that failed or truncated. For wave-scale work this argues for dossier-first prompting.
5. **Process error, logged honestly:** the first L1 invocation crashed instantly on a missing prompt-path argument (IndexError) — no API call was made, no tokens spent. Fixed in the runner invocation, not hidden.

## Guard-14 spot-checks (Glint, against primary sources read directly)

- Release sequence + v2026-08-25 delta (Sheet 1 items 1–2, 13–19): checked against the GitHub release record and release notes read 2026-11-06. **Pass.**
- FAQ signature rules (Sheet 3 items 3–7): checked against the FAQ text read in full. **Pass** — including the verbatim spoofing warning.
- Universal Cart + Canada facts (Sheet 3 items 15, 17, 19): checked against the two blog.google posts. **Pass.**
- AP4M facts (Sheet 5 items 17–21): checked against Mastercard's primary AP4M page read in full; the leg's announcement-date framing was corrected on the sheet (announced June 10, 2026; Oct 20 = Early Access). **Pass with correction.**
- Sheet 2 primary re-read (leg L10): the first AP2 spec fetch 404'd; the re-read succeeded against the repo README + specification overview. L10's extraction is primary-grade and surfaced a genuine tension the dossier had smoothed over — the README still frames v0.2 as upcoming while the dossier records it as released 28 April 2026, and the primary text applies open/closed to the *transaction* mandate where the dossier applied it to checkout/payment mandates. Sheet 2 preserves both, labeled by level, rather than resolving them.

## Phase verdict
**Phase 0b COMPLETE.** Six sheets earned 2026-11-06, each with its provenance levels on its face; the one initial gap (Sheet 2 primary text) was closed by leg L10 within the phase. Half-life clock starts today — no wave fires on these sheets after 2026-11-20 without a re-earn pass. UNJUDGEABLE classes named in advance; the NEEDS-VERIFY population is structural from wave 1.

## Wave 1 night run — Nov 6, 17:07–17:09 PT (lane-gate halt; Glint addendum)
- Runner v2 created: raw/run_leg_v2.py (reasoning_effort threaded, default low; cap default 16,000, floor 8,000 enforced; error_body ledgered before any retry). Compile-checked. Original run_leg.py untouched.
- WAVE-1-BRIEF.md staged: 10 clusters, 20 legs (PLAN medium/16,000 → WRITE low/16,000), D5 deferred to Wave 2. Redirect map (19 sources → 10 canonicals) is PROPOSED ONLY — Awaiting Will's Tap 2. Nothing edited, nothing published.
- Lane gate: executor halted per brief Step 2 — a generic subagent has no credential mechanism for the vault-saved WP app password that doesn't expose it in plaintext (no credentials namespace in its toolset; dynamic_credentials covers registered API providers only; the API-access flow declines username+password = multi_secret, verified by Glint's own request_api_access call for provider ucp-wordpress, declined with reason "website authentication, not an API credential"). No authenticated request was attempted by the executor; no status code exists from that attempt. Ledger unchanged: 15 records, zero Meta spend tonight.
- Glint follow-through (same night, on Will's canvas approval): lane check moved to Glint's browser lane — sign-in with the saved theuniversalcommerceprotocol.com login (will-tygart) + in-session GET /wp-json/wp/v2/users/me. Result lands in this log when the browser reports.

## Lane / account identity — resolved Nov 6, 17:09–17:11 PT (Glint, browser + public REST)
- The vault-saved login entry failed in Glint's browser (Will: "you're putting in the wrong password"). Will took the browser and signed in himself via **Google (Site Kit)** — dashboard live 17:09 PT, "Howdy, Will Tygart".
- The bare users/me visit returned 401 rest_not_logged_in — expected without a nonce/app password; not a login failure.
- Profile page (read live in session): **username `admin`**, first Will, last Tygart, nickname admin, display "Will Tygart", email will@tygartmedia.com. The Google sign-in maps to the `admin` account — NOT to `will-tygart`.
- Public REST user list (Glint read, 17:11 PT): exactly **two users** — id 1 "Will Tygart" (author slug `will-tygart`, link /author/will-tygart/) and id 2 "Pinto" (slug `pinto`). No user account with login `will-tygart` exists; **the plan's "account is will-tygart (one of only two users)" was wrong about the login name** — will-tygart is id 1's author slug; the login is `admin`. Any app password Will created tonight hangs on whichever account he was in (most plausibly `admin` via the Google sign-in); the saved vault entry pairs the wrong username with it — the likely whole story of tonight's lane friction.
- Standing state: browser admin session VERIFIED (Will's own sign-in). App-password REST lane still UNVERIFIED — no mechanism moves that value to Glint's tools without plaintext exposure; it stays a setup item, not a blocker (legs read public pages; publishing is tap-gated regardless).

## Wave 1 — FIRED Nov 6, 17:12 PT (Will's tap)
- Will approved firing Wave 1's legs on the re-scoped gate: legs read public pages and stage locally; the lane gates only publishing (Tap 2/Tap 3), which remains his. Stage-only run: no site edits, no redirects, no deletions.

## E3 plan — APPROVED by Will, Nov 6, 17:16 PT
- W1-E3-PLAN verdict (MERGE 4590 → 4588 "The Broker Dies Last"; 4590's body is a word-for-word duplicate; 17 NEEDS-VERIFY items ride as opinion voice) was reported to Will on the voice call and approved by him as-is. The approval covers the plan/verdict. It is NOT Tap 2 (the 4590 → 4588 redirect + deletion still awaits his explicit Tap 2) and NOT a publishing approval (Tap 3).

## Wave 1 — COMPLETE Nov 6, 17:22 PT (QC'd by Glint, spot-reads verified)
- All 10 clusters MERGE, zero REFUTEs; 20/20 legs clean (200 / stop / try 1; zero empties, truncations, retries, error bodies). Wave totals: 211,113 in / 94,928 out / 42,152 reasoning (44%, vs Phase 0b's 79%). Program: 35 calls, 248,815 in / 174,301 out. Contributor still $0 vs the $25 envelope.
- **PROBE FIX VERDICT: HELD on raw-source legs** — Phase 0b's failure shape did not recur once, incl. E1's plan leg over both full 4,400-word bodies (19,670 input tokens). Effort split as designed: plans 59% reasoning at medium, writes 22% at low.
- Glint QC spot-reads confirm the executor's flags: staged/4588.html = 1,818 chars / ~261 words (skeleton — DO NOT PUBLISH); staged/5793.html carries RFC 9421 ×1 + ES256 ×1, mTLS ×0, Bearer ×3 (partial auth correction — publish-blocker); staged/5471.html opens with the Sheet-5 ownership correction verbatim in substance.
- DEFECT (instruction conflict, not budget): E3's write leg applied the generic "exclude NEEDS-VERIFY" rule against plan §7's "keep as opinion voice" for E3's author-voice claims — it kept framing sentences, dropped the prose. Will had ALREADY ruled the substance at 17:16 PT (NV items ride as opinion voice) when he approved the E3 plan; the executor, correctly, did not self-authorize the re-run. **Corrective action Glint owns: one low-effort WRITE re-run for E3 under the explicit keep-in-voice rule, then QC.**
- NEEDS-VERIFY: 188 items — majority SHEET GAPS (rate-limit numbers — D2's three posts carry mutually incompatible claims — DID theory, engineering practice, market testimony). Executor recommendation on the record: sheet amendment (rate-limit first) or Will's explicit ride-as-author-claims call before Wave 2.
- Publish-blockers logged for Glint QC at publishing time: E1 partial auth correction; E5 unverifiable "Key Components" list; E3 skeleton (above).
- Proposed 301 map (19 sources → 10 canonicals; stub deletion 7261 only) sits in wave-1/WAVE-1-LOG.md — AWAITING WILL'S TAP 2. Nothing on the site was touched.

## E3 corrective re-run — CLEARED Nov 6, 17:25 PT
- Leg W1-E3-WRITE2 (low / 16,000): 200, stop, 1 try, 2,662 in / 1,611 out / 322 reasoning. Prompt carried Will's 17:16 PT ruling first and governing (NV items ride as author voice; generic exclude-rule explicitly overridden).
- Glint QC verified on the staged file itself: 6,149 bytes, 936 words by strip (canonical measures 897 by the same strip — the rebuild is fuller than source, not an abridgement); insurance/staffing/lending sections, compression thesis and closing line verbatim; no FAQ boilerplate. Defective skeleton replaced. Wave 1 final: 21 legs; program 36 calls (251,477 in / 175,912 out). E3 publish-blocker CLEARED; E1 partial-auth + E5 list remain publish-blockers at QC.

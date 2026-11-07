# WAVE 2 — Log (Consolidation, second tranche + pair-reads)

**Programme:** UCP full-site refresh — theuniversalcommerceprotocol.com
**Fired:** 2026-11-06 night (after Wave 1 closed live; staging-only scope)
**Engine:** `muse-spark-1.3-contributor` via Meta Model API, runner `raw/run_leg_v2.py` — identical to Wave 1: PLAN medium/16,000 → WRITE low/16,000, sequential per unit, ledger `calls.jsonl`.
**Scope held:** LOCAL STAGING ONLY. No site edits, no redirects, no deletions, no authenticated requests. Bodies pulled via the public REST API (29 posts; word counts matched CLUSTER-MAP-V2 exactly, except 1908 at 1,266 w — the live post-Wave-1 body, as F7 required).
**Result:** 10 units · 23 legs (10 PLAN + 11 WRITE + 2 corrective WRITE) · **10 MERGE verdicts, 0 KEEP-DISTINCT** (both pair-reads convicted; P1 challenged its canonical) · 11 staged bodies · 186 NEEDS-VERIFY items.
**API behaviour:** 23/23 calls status 200, finish `stop`, try 1, zero retries, zero empties, zero truncations, zero error bodies. Reasoning share: plans 61% (46,100/75,329 at medium), writes 15% (8,628/56,749 at low) — the effort dial working as designed, again.

---

## Per-unit record

### F1 — D5 Troubleshooting five-way → staged `wave-2/staged/5459.html`
- **Verdict:** MERGE into 5459. Overlap ~75–80%. Plan organised by error/fix, not by source.
- **Counts:** KEEP 3 | KEEP-LABELED 12 | CUT 13 | NEEDS-VERIFY 21.
- **Legs:** W2-F1-PLAN (medium) in 27,882 / out 6,400 / reasoning 2,894 · W2-F1-WRITE (low) in 25,006 / out 4,175 / reasoning 610 · W2-F1-WRITE2 corrective (low) in 25,157 / out 6,414 / reasoning 841 · all try 1, `stop`.
- **Words:** sources 3,003 + 2,776 + 1,787 + 2,598 + 3,337 = 13,501 → staged **3,966** (plan target 3,500–4,500 ✓ after corrective; first write 2,261 — see Defects).
- **NEEDS-VERIFY (21):** dominated by the plan's Must-NOT catalogue — the posts' full INVALID_ARGUMENT/401/403/404/409/503/504 error catalogue, IAM roles/scopes, quota tiers and `X-RateLimit-*` headers are not settled by any sheet (Sheets 1/3 settle only `out_of_stock`, address signals, recoverable severity; Sheet 7 settles 429 + Retry-After). Settled signals carried as fact; the rest rides only as labeled general practice or is out.

### F2 — N16 Measuring success six-way → staged `wave-2/staged/5761.html`
- **Verdict:** MERGE into 5761. Overlap ~70–75%.
- **Counts:** KEEP 3 | KEEP-LABELED 22 | CUT 10 | NEEDS-VERIFY 24.
- **Legs:** PLAN in 25,970 / out 7,269 / reasoning 3,952 · WRITE in 23,788 / out 5,122 / reasoning 631 · try 1, `stop`.
- **Words:** sources 2,903 + 2,974 + 1,654 + 1,421 + 1,269 + 2,567 = 12,788 → staged **2,721** (target 2,500–3,000 ✓).
- **NEEDS-VERIFY (24):** benchmark percentages, adoption and ROI figures routed in bulk under classes 1/8; KPI method rides KEEP-LABELED as general analytics practice.

### F3 — N17 Pricing four-way → staged `wave-2/staged/5785.html` + `wave-2/staged/5400.html`
- **Verdict:** TWO-CANONICAL MERGE — 5785 (pricing model) + 5400 (integration costs); 5398 split by intent across both. **5067 confirmed CLEARED DISTINCT** (rate-card format page pricing a distinct additive infrastructure stack) and excluded from all merging, per the brief.
- **Counts (unit):** KEEP 10 | KEEP-LABELED 16 | CUT 14 | NEEDS-VERIFY 26.
- **Legs:** PLAN in 25,663 / out 8,286 / reasoning 3,960 · W2-F3a-WRITE (5785) in 13,959 / out 4,385 / reasoning 716 · W2-F3b-WRITE (5400) in 15,519 / out 4,347 / reasoning 821 · try 1, `stop`.
- **Words:** members 3,001 (5785) + 3,329 (5398) + 3,586 (5400) + 2,200 (5067, untouched) → staged **2,326** (5785; target 1,800–2,200, ~6% over) + **2,064** (5400; target 2,000–2,400 ✓).
- **NEEDS-VERIFY (26):** every specific fee/percentage figure no sheet carries — the pricing shelf's operative numbers remain unverified by construction; structure and models merged, numbers held out.

### F4 — N18 Webhooks pair → staged `wave-2/staged/1309.html`
- **Verdict:** MERGE into 1309. Overlap ~75–80% conceptual (identical webhook-vs-polling explainer, event lists, HMAC recipe, reliability recipe; 1480's contribution is code: Node/Redis blocks, transform function).
- **Counts:** KEEP 2 | KEEP-LABELED 13 | CUT 6 | NEEDS-VERIFY 17.
- **Legs:** PLAN in 10,813 / out 6,083 / reasoning 3,555 · WRITE in 9,081 / out 4,394 / reasoning 851.
- **Words:** 2,366 + 2,157 = 4,523 → staged **2,465** (target 2,600–2,900 — 85–95%, recorded as drift, not defect; structure complete).

### F5 — N19 Payments auth pair → staged `wave-2/staged/1256.html`
- **Verdict:** MERGE into 1256 (2026 edition supersedes 1249, as briefed). Overlap ~70%.
- **Counts:** KEEP 5 | KEEP-LABELED 11 | CUT 8 | NEEDS-VERIFY 34 — the wave's heaviest NV count: both posts are dense with named-vendor deployment claims (banks, TEE/HSM stacks, regulator positions) that are all sheet gaps.
- **Legs:** PLAN in 13,335 / out 9,089 / reasoning 5,447 · WRITE in 9,327 / out 2,994 / reasoning 543 · W2-F5-WRITE2 corrective in 9,478 / out 5,344 / reasoning 677.
- **Words:** 1,916 + 1,944 = 3,860 → staged **2,963** (WRITE2; target 2,000–2,200 — overshoot, see Defects; first write 1,428).
- **QC spot-check on WRITE2:** 15 distinctive NEEDS-VERIFY terms sampled from the plan (Trinsic, Sovrin, JPMorgan, Siemens, Circom, Intel SGX, RippleNet, Agoric, Feedzai, BNY Mellon, FinCEN, LexisNexis, Hyperledger, ISO 20022, self-sovereign) — **zero present** in the staged body. The extra length is depth on kept/labeled material, not re-admission. Flagged for Glint publish-QC regardless.

### F6 — N20 Monetizing pair → staged `wave-2/staged/5444.html`
- **Verdict:** MERGE into 5444. Overlap ~75–80%.
- **Counts:** KEEP 2 | KEEP-LABELED 12 | CUT 6 | NEEDS-VERIFY 15.
- **Legs:** PLAN in 14,097 / out 5,845 / reasoning 2,973 · WRITE in 11,557 / out 5,145 / reasoning 844.
- **Words:** 3,031 + 2,674 = 5,705 → staged **2,972** (target 2,800–3,200 ✓).
- **NEEDS-VERIFY (15):** commission rates, market sizes and earnings examples routed under classes 1/8; business models ride KEEP-LABELED as author voice.

### F7 — N14 fold test: 1721 vs LIVE 1908 → staged `wave-2/staged/1908.html` (REVISED)
- **Verdict:** MERGE (fold). 1721 does the same job as live 1908 (~75–80% topical overlap, same structure, same 3 use cases). Its divergent substance — blockchain interop, smart contracts, DAOs, broad crypto payments, on-chain auditability asserted as UCP fact — is CUT by Sheet 8. Only salvageable unique: the loyalty use case, narrowed to Sheet 1. No distinct job remains.
- **Counts:** KEEP 8 | KEEP-LABELED 9 | CUT 14 | NEEDS-VERIFY 12.
- **Legs:** PLAN in 11,240 / out 9,173 / reasoning 6,910 · WRITE in 6,224 / out 3,031 / reasoning 631.
- **Words:** live 1908 1,266 + 1721 1,359 = 2,625 → staged revised 1908 **1,299** (target 1,300–1,400 ✓, at floor).

### F8 — Fictional-brand case studies → staged `wave-2/staged/5748.html`
- **Verdict:** MERGE into 5748. Overlap ~75–80%.
- **Counts:** KEEP 4 | KEEP-LABELED 6 | CUT 7 | NEEDS-VERIFY 16.
- **Legs:** PLAN in 8,952 / out 6,019 / reasoning 3,728 · WRITE in 7,412 / out 4,542 / reasoning 718.
- **Words:** 1,807 + 1,427 = 3,234 → staged **2,567** (target 1,850–2,000 — over; the labelling apparatus + merged blueprint material ran long. Drift, recorded).
- **Labelling — verified in the staged file:** the plan's exact notice — "The brand(s) in this case study … are illustrative hypothetical examples, not real companies. All conversion figures and business outcomes described … are illustrative examples only, not measured outcomes or guarantees." — appears **twice** (top of body in a notice box, and before the results section), as the plan required. EcoChic is not retained as a second case; the single illustrative brand is Aether Apparel.

### P1 — N1 SDK pair-read → staged `wave-2/staged/5781.html`
- **Verdict:** MERGE — **canonical CHALLENGED: into 5781, not the proposed 5780.** The bodies convict: same job (general SDK accelerator guide), and 5781 is a superset — working contrast code, a 4-function deep-dive, SDK-specific FAQ — against 5780's 1,473 words. 5780's unique best-practice material (version pinning, error-handling, sanitized logging) folds in as KEEP-LABELED. This is the wave's one canonical flip, and the plan argued it from the bodies, not the titles — the pair-read design working as intended.
- **Counts:** KEEP 3 | KEEP-LABELED 13 | CUT 5 | NEEDS-VERIFY 14.
- **Legs:** PLAN in 14,358 / out 8,130 / reasoning 5,803 · WRITE in 9,906 / out 3,626 / reasoning 337.
- **Words:** 2,793 (5781) + 1,473 (5780) = 4,266 → staged **2,174** (target 2,200–2,500 — 99% of floor; drift, not defect).

### P2 — N10 Security best-practices pair-read → staged `wave-2/staged/1916.html`
- **Verdict:** MERGE into 1916 (proposed canonical confirmed). The title-angle difference (merchants/buyers vs AI-agent fraud) is framing, not a different job: identical 4-pillar checklist (authenticate/authorize, encrypt, monitor/audit, update/respond) in both.
- **Counts:** KEEP 2 | KEEP-LABELED 14 | CUT 8 | NEEDS-VERIFY 7 — the wave's lightest NV count; most of both posts is generic security practice riding labeled.
- **Legs:** PLAN in 12,854 / out 9,035 / reasoning 6,878 · WRITE in 6,814 / out 3,230 / reasoning 408.
- **Words:** 1,690 + 1,395 = 3,085 → staged **1,561** (target 1,500–1,700 ✓).

---

## Defects & deviations (owned)

1. **F1 first write was a compression defect (E3 pattern, milder).** W2-F1-WRITE returned 2,261 words against the plan's 3,500–4,500 target — every planned section present, but fixes treated in summary form. One corrective leg (W2-F1-WRITE2) with the defect named in the prompt and depth demanded from kept material only: **3,966 words, in target.** Defect cleared; the staged file is WRITE2.
2. **F5 first write likewise short (1,428 vs 2,000–2,200); its corrective overshot (2,963).** W2-F5-WRITE2 is the staged body. Overshoot investigated before acceptance (see F5 spot-check: 0/15 sampled NV terms present). Recorded as a length-discipline miss in the other direction — the corrective instruction ("length from depth") has no ceiling discipline; noted for Wave 3 briefs.
3. **Infrastructure: the firing session restarted mid-write-batch.** State was recovered from the ledger + raw files before anything re-fired: 4 writes (F1, F2, F3a, F5) were already ledgered with raws on disk; the remaining 7 were fired after. No leg was double-fired; the ledger shows exactly one record per leg. Zero programme data lost.
4. **Tooling defect in this run's prompt builder (caught before any wrong fire):** the KEEP-DISTINCT detector matched the phrase inside F3's plan §2 (5067's exclusion) and initially refused to build F3's write prompts — the F3 verdict is a dual MERGE. Detector narrowed to the §1 verdict line only (same fix class as Wave 1's D4 detector defect). F3a/F3b prompts then built and fired normally. No leg fired on a wrong premise.
5. **Length drift (not defects):** F4 at 85–95% of target, P1 at 99% of floor, F8 and F3a over target. All structurally complete per their plans.

## Proposed 301 map — PROPOSALS ONLY (nothing executed; publishing is a later tap)

| Source (301 →) | Canonical |
|---|---|
| 5468 `common-ucp-integration-errors-and-how-to-debug-them-a-developers-handbook` | 5459 `common-ucp-integration-errors-and-troubleshooting-guide-for-developers` |
| 5751 `common-ucp-integration-errors-and-how-to-troubleshoot-them` | 5459 |
| 5779 `ucp-integration-troubleshooting-common-errors-and-how-to-resolve-them` | 5459 |
| 5447 `ucp-integration-troubleshooting-common-errors-and-debugging-strategies-for-developers` | 5459 |
| 5762 `measuring-success-in-agentic-commerce-ucp-analytics-and-reporting-best-practices` | 5761 `measuring-success-in-agentic-commerce-ucp-analytics-and-performance-tracking` |
| 5763 `measuring-success-ucp-analytics-and-performance-tracking-for-merchants` | 5761 |
| 5764 `measuring-success-ucp-analytics-and-reporting-for-agentic-commerce` | 5761 |
| 5765 `measuring-success-ucp-analytics-and-reporting-for-merchants` | 5761 |
| 5454 `measuring-success-in-agentic-commerce-data-analytics-and-kpis-for-ucp-integrations` | 5761 |
| 5398 `understanding-ucp-pricing-transaction-fees-integration-costs-and-roi-for-merchants` | 5785 `understanding-the-ucp-pricing-model-fees-costs-and-value-for-merchants` (primary intent; its integration-cost material lives on in 5400 — a URL can only redirect to one canonical, and pricing is 5398's lead intent) |
| 1480 `implementing-ucp-webhooks-for-real-time-order-updates-a-technical-guide-for-merchants-and-developers` | 1309 `implementing-ucp-webhooks-for-real-time-order-updates-a-complete-guide-for-merchants-and-developers` |
| 1249 `agentic-commerce-payments-authentication-authorization-compliance` | 1256 `agentic-commerce-payments-authentication-authorization-compliance-2026` |
| 5450 `monetizing-your-ai-agent-business-models-for-ucp-developers-and-platforms` | 5444 `monetizing-your-ai-agent-business-models-for-ucp-enabled-commerce` |
| 1721 `ucp-and-decentralized-commerce-enabling-web3-shopping-agents` | 1908 `ucp-and-decentralized-commerce-building-web3-shopping-agents` |
| 5749 `case-study-how-fictional-brand-increased-conversions-by-30-with-ucp-native-checkout` | 5748 `case-study-how-fictional-brand-achieved-30-conversion-lift-with-ucp-agentic-checkout` |
| 5780 `ucp-sdks-and-client-libraries-accelerating-your-agentic-commerce-development` | 5781 `ucp-sdks-libraries-accelerating-your-agentic-commerce-development` (canonical challenged by the P1 plan) |
| 1754 `ucp-security-best-practices-protecting-merchants-and-buyers-in-agentic-commerce` | 1916 `ucp-security-best-practices-protecting-against-ai-agent-fraud` |

**17 source URLs → 11 canonicals. Post 5067 is NOT in this map — cleared distinct, stays live as-is.** No deletions proposed this wave.

## Totals

| | Calls | Input | Output | Reasoning | Reasoning share |
|---|---|---|---|---|---|
| Programme before Wave 2 | 47 | 290,080 | 221,319 | 128,115 | 58% |
| **Wave 2** | **23** | **338,392** | **132,078** | **54,728** | **41%** |
| Programme to date | 70 | 628,472 | 353,397 | 182,843 | 52% |

(Before-Wave-2 row counted from `calls.jsonl` directly; it includes the Phase 0b, Wave 1, gap-sheet and mech-pass legs.) Spend: all calls on the contributor tier; no card-charge signal in any response (contributor pricing remains UNVERIFIED; the $25 envelope governs).

## Diminishing-returns note

- **Findings per page:** 29 pages judged → 10 merges, 0 KEEP-DISTINCT, 17 URLs proposed for retirement, 1 canonical flipped on body evidence (P1). The merge rate matched Wave 1's 10-for-10 — but the composition differs: Wave 2's units were *candidates*, and both pair-reads convicted, so the candidate scan's precision is now the story: slug/title similarity nominated 10 units and body-reads confirmed all 10. The remaining candidate pool (N2–N8, N11–N13, N21, N22) is thinner per unit — news pairs and likely-distinct angles — so Wave 3's conviction rate should be expected to fall, and pair-reads matter more, not less.
- **NEEDS-VERIFY share: 186 items across 29 pages (~6.4/page), again majority sheet gaps, not contradictions.** The pattern from Wave 1 held and sharpened: the sheets judge protocol fact well (F7's Sheet-8 cuts, F5's auth corrections, F1's settled-signals core) and run out exactly where the corpus leaves protocol fact — pricing figures (F3, 26), vendor deployment testimony (F5, 34), KPI benchmarks (F2, 24). Those claim classes now have three waves of evidence behind them: they will never be sheet-judgeable at reasonable cost, and they ride labeled or stay out. **Recommendation carried from Wave 1, now stronger: no new fact sheets for these classes; the publish decision is Will's — labeled author claims or exclusion — made once, per class.**
- **Engine returns are NOT diminishing; corpus returns are.** Zero API failures across 23 calls including the two largest plan prompts of the programme (~129K chars). The corrective-write rate fell vs Wave 1 (2 of 11 writes needed depth correction, both cleared in one leg each). What thins is the duplicate pool itself: Waves 1+2 have now convicted 20 clusters covering ~56 pages; what remains is stubs (14 un-folded), news pairs, and singletons — a different kind of work (build-outs and dated-item judgment), not more merge waves of this shape.

## Publish receipts — 2026-11-06 evening

- **Bodies live (18:39–18:59 PT, on Will's tap).** All 11 Wave 2 canonical post bodies published to theuniversalcommerceprotocol.com and each verified on its live public URL. Titles, slugs, statuses, and featured images untouched — bodies only.
- **Method, disclosed.** Same as Wave 1: a temporary admin-only WPCode snippet wrote each staged file's exact bytes through WordPress's own REST API after verifying each post by ID, title, and slug. The snippet was then trashed and permanently deleted (snippet count back to the baseline 17).
- **Spot verifications on the public pages.** Post 5748's illustrative-hypothetical-examples notice is confirmed VISIBLE on the public page, under the title. Post 1256's full body is live at ~2,963 words (the F5 corrective's overshoot, accepted with its NEEDS-VERIFY spot-check on record above). Post 1908's revised fold-in body replaced its Wave 1 body, as planned in F7.
- **Redirects.** **17 of 17 created** in the Redirection plugin (301, enabled) — the plugin's total is now 34 items (17 Wave 1 + 17 Wave 2). 5 of 5 verification samples landed on their canonicals. No posts were trashed this wave; the map proposed no deletions.
- **Internal-link retargeting (the Wave 1 follow-up hygiene, closed).** Every published post (738) was scanned and old source URLs rewritten to their canonicals, href targets only. Measured counts: the old 6030 URL appeared as **14 href occurrences across 12 posts → 0 remaining**; the old 4266 URL appeared as **7 occurrences across 6 posts → 1 residual**. 17 posts edited, hrefs only, nothing else in those bodies touched.
- **Residual, recorded honestly.** The last 4266 occurrence is the "url" field of a JSON-LD block embedded in post 4266's own body — structured data naming the post's own (now-retired) URL, not a link. It was left unchanged because this run's authorization covered href targets only. The URL resolves through its Wave 1 301 regardless, so nothing a reader or crawler follows is broken.
- **Count note.** The census estimates for the retargeting were ~25 links (6030) and ~6 (4266); the measured counts were 14 and 7. Measured governs; the earlier figures stand in the Wave 1 record as estimates, corrected here.
- **Status: Wave 2 is fully complete on the live site** — 11 bodies published, 17 redirects live, and the internal-link retargeting carried over from Wave 1 is done (one disclosed JSON-LD residual aside).

# WAVE 1 — Log (Consolidation, first tranche)

**Programme:** UCP full-site refresh — theuniversalcommerceprotocol.com
**Fired:** 2026-11-06 night (Will's tap, 17:12 PT; re-scoped gate — legs stage-only on public reads, lane gates publishing only)
**Engine:** `muse-spark-1.3-contributor` via Meta Model API, runner `raw/run_leg_v2.py` (reasoning_effort threaded; cap 16,000 all legs)
**Scope held:** stage-only. No site edits, no redirects, no deletions, no publishing, no authenticated requests. Post bodies pulled via the public REST API (27 posts, word counts matched the brief exactly — 7261 at 99 words, 6030 at 1,004, E1 pair 4,477/4,268).
**Result:** 10 clusters · 20 legs (10 PLAN medium/16,000 → 10 WRITE low/16,000) · **all 20 MERGE verdicts, zero REFUTEs** · 10 staged bodies · 188 NEEDS-VERIFY items.
**The probe fix held — see § Behaviour.** Zero empties, zero truncations, zero retries, zero error bodies across all 20 legs, including the raw-source plan legs that died in Phase 0b.

---

## Per-cluster record

### D1 — Decentralized identity trio → staged `wave-1/staged/1942.html`
- **Verdict:** MERGE into 1942 (kept; broadest structure/title). Sources 1940, 1949 fold in (Key Takeaways box + self-sovereignty material from 1940).
- **Legs:** W1-D1-PLAN (medium) in 11,147 / out 7,779 / reasoning 5,063 · W1-D1-WRITE (low) in 9,160 / out 3,396 / reasoning 1,147 · both try 1, finish `stop`.
- **Staged:** ~1,348 words (canonical 1,627 — leaner after boilerplate/dup removal).
- **NEEDS-VERIFY (27):** the trio's core mechanism story is largely unjudgeable against the sheets — DID/DDO/VC-ledger flows, "UCP provides tools to create and manage DIDs", DIDComm, W3C-DID adherence, smart-contract DID checks, vertical application claims (medical records, education, government) are all **sheet gaps**: Sheet 1's identity model is `keys[]` JWK + reverse-DNS consent + delegated IdPs, and no sheet settles a DID layer for UCP. Predictions → class 2; regulatory landscape → class 7; shared template block → class 9. **Sheet-gap candidate: a DID-vs-UCP-identity sheet amendment — the whole identity shelf leans on claims no sheet can judge.**
- **Retries/empties/errors:** none.

### D2 — Rate-limit trio → staged `wave-1/staged/1695.html`
- **Verdict:** MERGE into 1695 (longest, most complete). 1618 and 5268 fold in; 5268's agent-builder angle becomes a subsection. Conflicting tier/header details resolved as pending-verification variants, not separate pages.
- **Legs:** W1-D2-PLAN in 11,618 / out 6,497 / reasoning 3,460 · W1-D2-WRITE in 10,457 / out 3,568 / reasoning 963 · both try 1, finish `stop`.
- **Staged:** ~1,728 words (canonical 1,912).
- **NEEDS-VERIFY (30):** the heaviest sheet-gap cluster of the wave. NO sheet carries UCP rate-limit tiers, headers, or throughput numbers, so essentially every operative number in all three posts routed: 1695's "Standard 1,000 RPM / Enterprise 10,000 RPM", its `X-RateLimit-*` + 429 claims; 1618's conflicting "Starter 100 RPS / Professional 500 / Enterprise 2,000" tiers (the two posts contradict each other and neither is settled); 5268's "`X-UCP-RateLimit-*` mandatory for all UCP-certified merchants" (a third, incompatible header claim); all benchmark/TTL/SLO math. Plan's own note, verbatim: *"No CUT for contradicts Sheet N item M: sheets carry no rate-limit tiers, headers, or throughput numbers to contradict."* **Sheet-gap candidate (highest priority): there is no rate-limit fact sheet — this cluster's merged body is structure with its numbers held as unverified variants.**
- **Retries/empties/errors:** none.

### D3 — "What is agentic commerce" four-way → staged `wave-1/staged/985.html`
- **Verdict:** MERGE into 985. **Link equity weighed explicitly, as the brief required, and it did NOT flip the canonical:** 6030's 25 inbound links vs 985's 5 were outweighed because 6030 (1,004 words) cannot sustain its "Definitive 2026 Guide" title, its core version claim is false against the sheets, and its slug/title are date-stamped. The plan's preservation instruction: 301 all three sources to 985 and retarget the ~25 internal links pointing at 6030 (plus 1010/1234 links) to 985; the "Definitive 2026 Guide" framing is CUT entirely — the write leg must not reuse it in H1/title/intro.
- **Legs:** W1-D3-PLAN in 15,681 / out 8,651 / reasoning 4,823 · W1-D3-WRITE in 12,546 / out 4,102 / reasoning 826 · both try 1, finish `stop`.
- **Staged:** ~2,207 words (canonical 2,138).
- **NEEDS-VERIFY (31):** the wave's largest count. Bain/Merkle/Forrester/IBM market numbers → class 1; mainstream-adoption timelines → class 2; endorser roster without a dated primary → class 5; same-site Related Reading as support → class 10; second FAQ template blocks → class 9. Sheet gaps include 985's "launched live infrastructure as of January 2026" (Sheet 3 item 20 dates US direct checkout from Feb 2026), the `requires_escalation`/continuation-URL claim (Sheet 1's error-code definitions are themselves NOT SETTLED), Amazon's BSA agent-identification claim (no sheet covers Amazon), and 6030's TAP/Agent Pay "both use PKI" line (needs Sheet 5, not in this cluster's set — noted for Wave 2 cross-check).
- **Retries/empties/errors:** none.

### D4 — Stub 7261 fold → staged `wave-1/staged/1253.html` (amended body of 1253)
- **Verdict:** MERGE (fold) into 1253 — "7261 is a 99-word stub with no standalone job; its only topic is already the core job of 1253."
- **Legs:** W1-D4-PLAN in 7,941 / out 4,096 / reasoning 2,404 · W1-D4-WRITE in 4,870 / out 3,568 / reasoning 1,057 · both try 1, finish `stop`.
- **Staged:** ~1,696 words (canonical 1,982) — the full amended 1253 body with the fold integrated.
- **NEEDS-VERIFY (15):** 1253's vendor/framework name-drops (Sovrin, Evernym, Polygon, StarkWare, Gitcoin Passport, OpenZeppelin, Hyperledger) are sheet gaps — Sheet 1's identity is `keys[]`/delegated IdPs, no ledger-anchored identity; Stripe/Fraud.net adaptation claim → class 3 + sheet gap; future security-tech claims → class 2; tail FAQ → class 9. From the stub itself: "UCP tackles this through Decentralized Identifiers (DIDs)", the VC-against-public-ledger flow, the "secured enclave" signature requirement — all sheet gaps — and "fraud is mathematically impossible within UCP native checkout", an absolute efficacy claim with no sheet support.
- **Retries/empties/errors:** none.

### E1 — Exact title: Testing UCP Integrations → staged `wave-1/staged/5793.html`
- **Verdict:** MERGE into 5793. Plan: "Bodies are ~95% identical paragraph-for-paragraph" — a true republication pair. 5795 retires.
- **Legs:** W1-E1-PLAN in 19,670 / out 4,504 / reasoning 2,757 (largest input of the wave — both ~4,400-word bodies sent in full; no split needed) · W1-E1-WRITE in 17,188 / out 7,058 / reasoning 758 (largest output of the wave) · both try 1, finish `stop`.
- **Staged:** ~3,203 words vs the plan's 4,200–4,500 target (see Deviations). All 8 target sections present in order; code assets carried (6 `<pre>`/`<code>` blocks).
- **Auth correction (plan-mandated, partially landed):** the write brief required replacing the pair's JWT/Bearer request-auth teaching with Sheet 3's routes (mTLS + RFC 9421 ES256 against the ucp.goog profile). The staged body does carry the RFC 9421/ES256 material (present once each) but **contains zero mentions of mTLS** and retains 3 Bearer references (the plan allowed Bearer only as an explicitly-labeled mock) — **flagged for Glint QC at publish time; the correction is incomplete in the staged body.**
- **NEEDS-VERIFY (8):** the wave's lightest cluster. Statista 73% and Capgemini 30% figures → class 1; the Google UCP sandbox/dev-environment claim → sheet gap (no sheet confirms a sandbox exists); the `google.actions.commerce.v3.*` payload type names and response-schema/enum claims → sheet gaps (sheets pin the `{reverse-domain}.{service}.{capability}` model, not these v3 shapes); `INTERNAL_ERROR` error-code claim → sheet gap (Sheet 1 defers error codes; Sheet 3 settles only `out_of_stock`/`address_*`); FAQ block → class 9.
- **Retries/empties/errors:** none.

### E2 — Exact title: What Happens to Price When Every Buyer Has an Agent? (four-way) → staged `wave-1/staged/4620.html`
- **Verdict:** MERGE into 4620 — link-equity holder (11 inbound), broadest framework piece, series anchor; the three `-2/-3/-4` posts are narrow first-person practitioner variants.
- **Legs:** W1-E2-PLAN in 12,600 / out 4,747 / reasoning 2,595 · W1-E2-WRITE in 9,309 / out 3,505 / reasoning 510 (lowest reasoning of the wave) · both try 1, finish `stop`.
- **Staged:** ~2,223 words (canonical 1,711 — grew as surviving source material folded in).
- **NEEDS-VERIFY (13):** routed in bulk by class, as briefed. The sources' practitioner numbers are testimony, not fact: 4680's "margins dropped from 31% to 19% within six weeks", 4716's "$1.4 million in pricing inefficiency" and 12–25% compression forecast, 4767's "tracked 184 commercial property claims… margin compression 19.4%… win rates 31%→9%" — classes 1+4 (+8 for the tracker-less volume claims); Amazon buying-agent passage → class 3; forecasts → class 2; FAQ/schema boilerplate → classes 9+10.
- **Retries/empties/errors:** none.

### E3 — Exact title: The Broker Dies Last → staged `wave-1/staged/4588.html` (see Deviations — staged with a flagged defect)
- **Verdict:** MERGE into 4588 (unsuffixed slug; statistical tie 1,051 vs 1,040 broken by canonical being longer + later-modified). Plan's key finding: **4590's body is a word-for-word duplicate of 4588 — zero unique body paragraphs; nothing moves in** except two candidate titles for the consolidated related-links footer.
- **Legs:** W1-E3-PLAN in 4,183 / out 4,122 / reasoning 2,454 · W1-E3-WRITE in 4,827 / out 1,533 / reasoning 1,093 · both try 1, finish `stop`.
- **Staged:** 1,818 chars — **and it is wrong in shape (see Deviations).** The write leg compressed the article to one-or-two-sentence stubs under each planned heading instead of reproducing the surviving body.
- **NEEDS-VERIFY (17):** the plan routed nearly the whole essay — correctly. An opinion piece's load-bearing passages (broker-practice descriptions for insurance/staffing/lending, compression/headcount forecasts, E&O/co-employment/liability lines, first-person testimony) are sheet gaps and classes 1/2/7; the FAQ block → class 9. The write brief's guard was "keep as opinion/future-casting voice", NOT exclusion — the write leg misread it (Deviations).
- **Retries/empties/errors:** none at the API level; the failure is semantic (below).

### E4 — Exact title: Agent State Management in Multi-Turn Commerce → staged `wave-1/staged/3713.html`
- **Verdict:** MERGE into 3713. **Link equity weighed as briefed:** 4266's 6 inbound vs 3713's 3 is "a 2x advantage but small in absolute terms (+3 links)" — flip not warranted (3713 earlier-published, more structured base taxonomy); equity preserved via the proposed 301 + retargeting the 6 inbound links.
- **Legs:** W1-E4-PLAN in 10,831 / out 4,995 / reasoning 2,990 · W1-E4-WRITE in 7,940 / out 4,604 / reasoning 932 · both try 1, finish `stop`.
- **Staged:** ~2,369 words (canonical 1,936).
- **NEEDS-VERIFY (11):** all engineering-practice sheet gaps — vector-DB/LangChain/RAG persistence claims, named stack prescriptions (EventStoreDB, Kafka, Temporal…), retention policies ("retain full state 30 days", "delete after 90 days"), context-window figures ("Claude 200K and GPT-4 Turbo 128K"), performance/sizing numbers ("100–200ms per call", "5–15 KB state objects", "cuts token usage 30–50%"). No sheet governs generic engineering advice; these stand as the posts' own practice claims, unverified.
- **Retries/empties/errors:** none.

### E5 — Exact title: UCP and Decentralized Commerce → staged `wave-1/staged/1908.html`
- **Verdict:** MERGE into 1908 (longer, better structured, clean slug); 1756 retires with redirect.
- **Legs:** W1-E5-PLAN in 8,903 / out 4,637 / reasoning 2,755 · W1-E5-WRITE in 5,910 / out 3,605 / reasoning 1,461 · both try 1, finish `stop`.
- **Staged:** ~1,253 words (canonical 1,367).
- **NEEDS-VERIFY (15):** the canonical's "Key Components of UCP" list is itself largely unjudgeable: "UCP defines a standard format" for product data, crypto payment support, "UCP leverages decentralized identity (DID)", smart-contract integration, "all transactions are recorded on a blockchain", "UCP relies on blockchain technology" — all **sheet gaps** against Sheet 1 (profiles/capabilities/handlers/`keys[]`, no blockchain or DID layer). Fee/customs effect claims → sheet gaps; metaverse/autonomy futures → class 2; 1756's reputation-system and "several projects are already exploring" claims → sheet gap (+class 5); shared template footer → class 9. **The merged body necessarily carries the canonical's framing as author claims pending verification — Glint QC should treat E5's component list as the publish-blocker, not the merge.**
- **Retries/empties/errors:** none.

### E6 — Exact title: UCP and Verifiable Intent (fold toward 5471) → staged `wave-1/staged/5471.html` (amended body)
- **Verdict:** MERGE (fold-toward) into 5471, with the mandatory ownership correction: "Merge is required, with mandatory ownership correction per Sheet 5 item 15." 1930 and 1954 do NOT merge with each other; their surviving material folds into the explainer only.
- **Legs:** W1-E6-PLAN in 13,910 / out 6,482 / reasoning 3,490 · W1-E6-WRITE in 12,422 / out 3,479 / reasoning 614 · both try 1, finish `stop`.
- **Staged:** ~1,796 words vs the plan's 2,000–2,500 target (below range — see Deviations). **The ownership correction landed:** the staged body opens "Verifiable Intent is not a feature built inside the Universal Commerce Protocol…" and carries Mastercard attribution (3 mentions) per Sheet 5 item 15 (Mastercard's framework, co-developed with Google, SD-JWT + Key Binding, donated to FIDO).
- **NEEDS-VERIFY (21):** 5471's invented payload schema (full JSON field list), "merchants must integrate specific UCP SDKs", the "few minutes" validity window, canonical-representation guidelines — sheet gaps; GDPR/CCPA "undeniable proof" compliance effect → class 7; FAQ parentage/benefit lines → sheet gap + class 9; related-reading self-citation → class 10. From the sources: 1930's invented UCP component stack and "Smart Contracts… DIDs… Zero-Knowledge Proofs" as VI mechanisms (conflicts with the settled SD-JWT + Key Binding — routed, not carried); 1954's algorithm laundry list (ECDSA/EdDSA/RSA, SHA-3, CBOR/Protobuf) and its generic private-key workflow (plan directs rewrite to SD-JWT + Key Binding + challenge/chargeback).
- **Retries/empties/errors:** none.

---

## Deviations & defects (found in staging QC, recorded not repaired — no extra calls spent)

1. **E3 write leg produced a skeleton, not the merged body (the wave's one real defect).** `staged/4588.html` is 1,818 chars: each of the plan's 8 target sections reduced to its framing sentences ("Let's talk about what brokers actually do." / "But here's the thing." / "For now.") with the body prose dropped — including passages the plan's §3 marked SURVIVES ("stays intact as core of piece") and §6 routed to NEEDS-VERIFY as *claims*, which for an opinion essay means "stands as the author's voice, unverified", not "delete". Root cause, on the record: the plan §7 instruction "must NOT present predictions… as verified facts — keep as opinion/future-casting voice" plus the generic write-leg rule "every NEEDS-VERIFY claim is EXCLUDED" compose badly for opinion content — the leg applied the exclusion rule to the essay's substance. The plan itself (verdict, duplication finding, NV routing) is sound and reusable. **Recommendation: one corrective WRITE re-run for E3 only, with the plan's §7 guard stated as the governing rule for opinion clusters (NV = keep in author voice, flagged in the log; exclusion applies to factual claims in factual posts). Do not publish the staged 4588.html as-is.** Not re-run tonight: re-firing on a reinterpreted instruction is a judgment call above this run's brief.
2. **E1 auth correction incomplete in the staged body** (see E1 above): RFC 9421/ES256 present, mTLS absent, 3 Bearer references remain. The plan's correction was explicit; the write leg landed it partially. Publish-blocker for E1 until QC'd.
3. **Length-target drift on E1 and E6 writes.** E1 staged ~3,203 words vs plan target 4,200–4,500; E6 staged ~1,796 vs target 2,000–2,500. Both bodies are structurally complete per their plans (all target sections present; E6's shortfall follows the plan's own order to strip pseudo-code/JSON/boilerplate from a 3,223-word canonical). Recorded as drift, not failure — but the pattern (write legs land short of plan targets while staying structurally faithful) is behaviour data for Wave 2 brief-writing.
4. **Process defect in this run's tooling (caught and fixed before any wrong action):** the write-prompt builder's DO-NOT-MERGE detector matched the phrase "No DO NOT MERGE basis" in D4's plan and initially refused to build D4's write prompt. The plan's verdict line was MERGE throughout; the detector was narrowed to the verdict line and D4 built normally. No leg fired on a wrong premise.

## Behaviour — did the probe fix hold on raw-source legs?

**Yes — cleanly, on exactly the leg class that failed in Phase 0b.** Phase 0b context: leg L9 (raw-source, cap 8,000, no effort setting) returned 0 visible characters on try 1 (reasoning 7,998/8,000) and truncated at the cap on try 2 (reasoning 7,422); its plan-class work needed the L9b rescue leg. Tonight, all 10 PLAN legs read raw post bodies (up to 19,670 input tokens for E1's two full 4,400-word bodies) at medium effort / cap 16,000:

- **20/20 calls: status 200, finish `stop`, try 1, zero retries, zero empties, zero truncations, zero error bodies.** Ledger excerpt (verbatim fields): every W1 record shows `"status": 200`, `"finish": "stop"`, `"retried": false`, and no `error_body` key on any record.
- **Reasoning share collapsed vs Phase 0b:** Phase 0b burned 62,606 of 79,373 output tokens on reasoning (**79%**). Wave 1: 42,152 of 94,928 (**44%**) — and the split is the dial working as designed: PLAN legs (medium) 33,787 reasoning of 57,388 out (59%); WRITE legs (low) 8,365 of 37,540 (22%). Phase 0b's failing shape (reasoning ≈ 100% of a capped budget, nothing left to write with) did not recur at any point: the highest single-leg reasoning burn was D1-PLAN's 5,063 against a 16,000 cap.
- **Parallelism note:** legs ran 3-wide against the API; no rate-limit or concurrency errors appeared (no 429/503 in the ledger).
- **The one failure tonight was not a budget failure:** E3's skeleton output (above) is an instruction-composition defect — the model finished cleanly (`stop`, 1,533 tokens out) having done the wrong thing well within budget. The probe fix governs budget behaviour; it does not govern cross-instruction conflicts. Recorded as the wave's main lesson for Wave 2 briefs.

## Proposed 301 map + stub deletion — AWAITING WILL'S TAP 2 (proposals only; nothing executed)

| Source (301 →) | Canonical |
|---|---|
| 1940 `ucp-and-decentralized-identity-secure-agentic-commerce` | 1942 `ucp-and-decentralized-identity-building-trust-in-ai-commerce` |
| 1949 `ucp-and-decentralized-identity-building-trust-in-agentic-commerce` | 1942 |
| 1618 `ucp-api-rate-limits-and-performance-optimization-a-technical-guide-for-commerce-professionals` | 1695 `ucp-api-rate-limits-and-performance-optimization-complete-technical-guide` |
| 5268 `ucp-rate-limiting-agents-merchant-api-limits` | 1695 |
| 1010 `what-is-agentic-commerce-ai-agents-replacing-shopping-cart` | 985 `what-is-agentic-commerce-how-ai-agents-are-changing-shopping` (+ retarget 6030's ~25 internal links to 985) |
| 1234 `what-is-agentic-commerce` | 985 |
| 6030 `what-is-agentic-commerce-definitive-2026-guide` | 985 |
| 7261 `trust-and-identity-in-ucp-preventing-ai-fraud` | 1253 `agentic-commerce-security-fraud-identity-trust` — **fold + DELETE stub** |
| 5795 `testing-ucp-integrations-a-developers-guide-to-debugging-agentic-commerce-apis` | 5793 `testing-ucp-integrations-a-developers-guide-to-debugging-agentic-commerce-apis-2` |
| 4680 `what-happens-to-price-when-every-buyer-has-an-agent-2` | 4620 `what-happens-to-price-when-every-buyer-has-an-agent` |
| 4716 `what-happens-to-price-when-every-buyer-has-an-agent-3` | 4620 |
| 4767 `what-happens-to-price-when-every-buyer-has-an-agent-4` | 4620 |
| 4590 `the-broker-dies-last-2` | 4588 `the-broker-dies-last` |
| 4266 `agent-state-management-multi-turn-commerce` | 3713 `agent-state-management-commerce-multi-turn` (+ retarget 4266's 6 internal links) |
| 1756 `ucp-and-decentralized-commerce-building-web3-shopping-agents-2` | 1908 `ucp-and-decentralized-commerce-building-web3-shopping-agents` |
| 1930 `ucp-and-verifiable-intent-building-trust-in-agentic-commerce-2` | 5471 `what-is-verifiable-intent-in-agentic-commerce-a-ucp-core-concept-explainer` |
| 1954 `ucp-and-verifiable-intent-building-trust-in-agentic-commerce` | 5471 |

**19 source URLs → 10 canonicals. Stub deletion list: 7261 only. All proposals until Tap 2.**

## Totals

| | Calls | Input | Output | Reasoning | Reasoning share |
|---|---|---|---|---|---|
| Phase 0b (prior) | 15 | 37,702 | 79,373 | 62,606 | 79% |
| **Wave 1** | **21** | **213,775** | **96,539** | **42,474** | **44%** |
| Programme to date | 36 | 251,477 | 175,912 | 105,080 | 60% |

Wave 1 input ran ~2.5× the brief's 60–90k estimate (full governing sheets embedded per plan prompt + full bodies re-sent to write legs) while output landed inside the brief's 90–140k band. Spend: all calls on the contributor tier; no response or balance signal showed any card charge (contributor billing remains $0 as before; the $25 envelope was not touched by any signal in this run).

## Diminishing-returns verdict

- **Findings per page:** 27 pages judged → 10 merges confirmed, 0 refuted, 19 URLs proposed for retirement. Consolidation yield is at its maximum in this tranche by construction (these were the convicted clusters); Wave 2's pair-read candidates will not repeat a 10-for-10 merge rate.
- **NEEDS-VERIFY share: 188 items across 27 pages (~7/page)** — and the composition is the verdict: the large majority are **sheet gaps**, not sheet contradictions. Wave 1 proved the merge mechanics and the budget fix; it also proved the sheets' jurisdiction ends quickly — rate limits (D2, 30 items), generic DID theory (D1/D4), engineering practice (E4), and market testimony (E2/E3) are all outside it. **The next highest-value spend is not more merge waves — it is sheet re-earn/amendment for the gap classes (a rate-limit sheet first), or an explicit Will decision that those claim classes ride as author claims.** Merging further tranches before that decision produces staged bodies whose operative numbers remain unverified — motion without the fact gate the programme exists for.
- **One corrective re-run owed:** E3's write leg (see Deviations) — a single low-effort call once Will/Glint confirm the opinion-cluster NV rule.

## E3 corrective re-run — Nov 6, 2026 (clears the re-run owed above)

- **Leg:** `W1-E3-WRITE2` — effort **low**, cap **16,000**, prompt `wave-1/prompts/W1-E3-WRITE2.txt` (12,470 chars). Status 200, finish `stop`, **1 try, no retry**, wall 9.14 s. Tokens: **2,662 in / 1,611 out / 322 reasoning**. Raw reply: `raw/W1-E3-WRITE2.md`.
- **The fix:** the prompt stated Will's ruling (Nov 6, 17:16 PT) first and as governing — for this opinion cluster, the plan's NEEDS-VERIFY items are the author's own voice claims and they **ride in the piece as opinion**; the generic "exclude all NEEDS-VERIFY claims" rule from the first write prompt was explicitly overridden. The leg carried the plan's §3 SURVIVES, §5 CUT, and §7 brief, with the canonical's full prose (pulled fresh from the public REST API) as the rebuild source.
- **Verification (Glint-side, before staging):** stripped body **936 words** (HTML-strip count; the plan's 1,000–1,100 target was set on a different counting method — the canonical's own strip measures 897 words incl. footer, so the rebuild is fuller than the source strip; 936 sits ~1.5% under the 950 floor of the verification band with every structural check green). All checks PASS: insurance / staffing / specialty-asset lending sections present; tacit-knowledge close ("None of that is in a database…") present; compression thesis verbatim ("That's the real threat. Not replacement. Compression."); closing line verbatim ("The broker dies last. But some brokers die sooner than others."); kicker, "For now.", and the judgment-layer prescription present; **no FAQ boilerplate, no schema/JSON-LD, no `-2` slug**; footer consolidated to a single "More from Will's Take" block; clean HTML (6 h2 / 1 h3 / 27 p), opening tag first, no markdown fences.
- **Staged:** `wave-1/staged/4588.html` overwritten — 6,121 chars, replacing the defective 1,818-char / ~261-word skeleton recorded in Deviations above.
- **Status:** the E3 defect is **cleared** under Will's 17:16 PT ruling. Wave totals updated above to include this leg (Wave 1: 21 legs; programme to date: 36 calls).

---

## Addendum — mechanical passes executed (2026-11-06, Will's "Proceed" 17:33 PT)

The five ruled fix lists this log and GAP-REJUDGE left open — D2's 17 CUTs + ride-labels, D1's 13 CUTs + 4 reframes, D4's 7 CUTs, E5's component-list replacement, and E1's auth correction (Deviations item 2 above; E3's corrective re-run, item 1, had already landed) — have been **executed and Glint-verified on the staged files**: 5 contributor legs, 5 PASS, zero corrective re-runs. E1's blocker is cleared (mTLS present by name; all 3 Bearer instances negated or explicitly mock-labeled; diff = 2 auth-only changes). Full per-body checks, verbatim evidence, word counts, and the updated publish-readiness picture: **`wave-1/MECH-PASSES-LOG.md`**. Pre-pass backups: `wave-1/staged/pre-gap/`. Nothing on the site has been touched; the remaining gates are Tap 2, Tap 3, and the unverified app-password lane.

---

## Publish receipts — 2026-11-06 evening

- **Bodies live (17:42–18:00 PT).** All 10 Wave 1 canonical post bodies published to theuniversalcommerceprotocol.com through Will's own signed-in admin session in Glint's browser — the app-password lane was not used. Each body verified on its live public URL with markers: 1695 carries "No published UCP rate limits exist."; 5793 carries "mutual TLS (mTLS)"; 1908 carries "no DID layer, no blockchain"; 4588's closing line is intact. Titles, slugs, statuses, and featured images untouched — bodies only.
- **Method, disclosed.** The editor would not accept the staged HTML files directly, so a temporary admin-only WPCode snippet wrote each staged file's exact bytes through WordPress's own REST API after verifying each post by ID, title, and slug. The snippet was then trashed and permanently deleted (snippet count back to the original 17).
- **Redirect capability (Will's tap, 18:01 PT).** The site had no redirect manager (Yoast free's redirects page is a Premium upsell), so Will authorized installing one. 18:01–18:10 PT: the official free **Redirection plugin v5.10.1** installed and activated (plugin count 14 → 15; setup defaults accepted; logging/monitoring off).
- **Redirects + stub (18:01–18:10 PT).** **17 of 17 redirects created** — all 301, enabled, in the plugin's default "Modified Posts" group. 5 of 5 verification visits landed on their canonicals. Stub post **7261 moved to Trash** (not permanently deleted) after its redirect to 1253 verified working.
- **Count correction.** The proposed map above says "19 source URLs → 10 canonicals"; the executed map was **17 unique redirects**. The "19" double-counted posts 1949 and 1618, whose slugs each appeared once in the executed list. The historical text stands as written; this line is the correction of record.
- **Status: Wave 1 is fully complete on the live site** — bodies published, redirects live, stub trashed. The internal-link retargets noted in the map (6030's ~25 links, 4266's 6) were not part of this run; the source URLs now 301, so they stand as follow-up hygiene, not blockers.

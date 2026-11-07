# GAP REJUDGE — Wave 1 sheet-gap items vs Sheets 7 & 8

**Date: 2026-11-06 · Ordered by Will's tap, 17:26 PT ("Earn the gap sheets first, then publish Wave 1 + redirects together")**
**Inputs:** Sheets 7 (rate limits) & 8 (identity/DID), earned today · Wave 1 plan §6 NEEDS-VERIFY lists (verbatim bullet populations) · legs GAP-RJ-D1/D2/D4/E5 (`muse-spark-1.3-contributor`, low / 16,000, all clean try 1; raw outputs `raw/RJ-*.md`, ledger `calls.jsonl`).
**Counting method:** one bullet = one item, counted from each plan's §6 list. Populations: D1 27, D2 30, D4 15, E5 15 = **87 bullets**, of which **77 are sheet-gap items** (the rejudge's target) and 10 are UNJUDGEABLE class-routed items (classes 2/5/7/9), which the legs correctly landed in REMAINS-NV untouched.
**Dispositions:** SETTLED-KEEP (sheet settles it, rides as fact) · REFRAME / RIDE-LABELED (may stay only as explicitly labeled generic/adjacent background or general practice — never as UCP fact) · CUT (remove as a UCP claim before publish) · REMAINS-NV (still unjudgeable — class-routed, or a gap no sheet settles).

## Per-cluster results

### D2 — rate-limit trio → staged `1695.html` (Sheet 7)
**30 bullets: SETTLED-KEEP 0 · RIDE-LABELED 10 · CUT 16 · REMAINS-NV 4**
- Every operative number dies: both tier systems (1,000/10,000 RPM; 100/500/2,000 RPS), per-endpoint limits, token-bucket mandate, batch-counts-as-1, negotiable ceilings, SLOs, regional doubling, enterprise multipliers, both header families, the suspension rule — **CUT**, none published by any primary source (Sheet 7 headline).
- The 10 RIDE-LABELED items are the generic engineering spine (caching/TTLs, batching, backoff, pooling, pagination, monitoring, polling-vs-webhooks) — publishable only under a general-practice label with numbers framed as author examples.
- REMAINS-NV (4): sandbox-to-trigger-429s*, webhook event names, burst-vs-throttling definition, boilerplate block (class 9).
- **Glint corrections to the leg (spot-check, Guard 14):** (1) Bullet 4 bundles two claims — the `X-RateLimit-*` header family is CUT, but its second half, "429 with `Retry-After`," is **SETTLED-KEEP** (Sheet 7 items 1–2): it is the one rate-limit fact in the entire wave that now settles affirmatively. (2) *The sandbox bullet: Sheet 7's own disposition table rules the sandbox claim **CUT** as a UCP fact; the leg's REMAINS-NV stands only in the weaker sense that no sheet proves a sandbox does *not* exist (cf. E1's sandbox gap). Publish treatment is identical either way: the staged body may not assert it. **Corrected D2 totals: CUT 17 · REMAINS-NV 3** (RIDE-LABELED 10, SETTLED-KEEP 0 whole bullets + 1 settled component inside bullet 4).

### D1 — identity trio → staged `1942.html` (Sheet 8)
**27 bullets (23 sheet-gap): SETTLED-KEEP 0 · REFRAME 4 · CUT 13 · REMAINS-NV 10**
- All 13 CUTs are DID/VC/ledger/DIDComm/smart-contract attributions to UCP — misattributions under Sheet 8's zero-hit headline. The staged body's UCP-identity content must be rebuilt from Sheet 8 items 1–6 only.
- REFRAME (4): DID-document fields, DID resolution mechanics, DID-signed/key linkage, DID vertical-use examples — true of W3C technology, retainable only as labeled non-UCP background.
- REMAINS-NV (10): the 4 class-routed items (2× predictions, 1× regulatory, 1× boilerplate) + 6 items no sheet settles (UCP dispute-resolution mechanisms, generic interop phrasing, vertical application claims *as UCP benefits*, cost/efficiency claims, encryption-protocol lists). These do not block the merge; they block those *claims* riding as fact.

### D4 — stub fold → staged `1253.html` (Sheet 8)
**15 bullets (13 sheet-gap): SETTLED-KEEP 0 · REFRAME 1 · CUT 7 · REMAINS-NV 7**
- CUT 7 includes the four 7261 stub claims — **Wave 1's plan CUTs CONFIRMED by Sheet 8, no reversal** (DIDs-as-UCP, VC-against-ledger, secured-enclave mandate, "mathematically impossible" fraud claim) — plus "UCP defines minimum security standards / auditing / reputation participation," "UCP standardizes a signatures-registries-reputation-VC stack," and blockchain-anchored identity *as positioned in the UCP verification section*.
- REFRAME (1): W3C DID / Sovrin / Evernym background — labeled non-UCP only.
- REMAINS-NV (7): five vendor-landscape items (Polygon/StarkWare, Stripe/Fraud.net, Gitcoin/Filecoin, OpenZeppelin, Hyperledger Fabric) — generic industry content no sheet governs; plus the class-2 prediction and class-9 boilerplate bullets. These ride or fall as *author's landscape survey*, never as UCP fact.

### E5 — exact-title pair → staged `1908.html` (Sheet 8)
**15 bullets (12 sheet-gap): SETTLED-KEEP 1 · REFRAME 0 · CUT 7 · REMAINS-NV 7**
- The wave's only whole-bullet SETTLED-KEEP: **"UCP defines a standard format for product data"** — narrowed to its true form, catalog capability schemas for products/variants (Sheet 8, Sheet 1 Annex A).
- CUT (7): broad crypto-payments claim*, DID identity management, smart-contract integration, all-transactions-on-blockchain, blockchain reliance + core-tech list, blockchain-for-data/fraud, and the UCP reputation system. (*The crypto bullet as written is CUT; Sheet 8's narrow keep — the v2026-08-25 release record's crypto data specs #942 / `crypto_payer` #1000 — may be *added* at rewrite as a new, correctly-scoped line. It is not a keep of this bullet.)
- REMAINS-NV (7): fee/customs effect claims, single-account interoperability, project-roster claims (class 5), predictions (class 2), regulatory (class 7), boilerplate (class 9).

## Totals (87 bullets; leg counts, with Glint's D2 corrections applied)

| | SETTLED-KEEP | REFRAME / RIDE-LABELED | CUT | REMAINS-NV |
|---|---|---|---|---|
| D1 (27) | 0 | 4 | 13 | 10 |
| D2 (30) | 0 (+1 component) | 10 | **17** | **3** |
| D4 (15) | 0 | 1 | 7 | 7 |
| E5 (15) | 1 | 0 | 7 | 7 |
| **All (87)** | **1** | **15** | **44** | **27** |
| Sheet-gap subset (77) | 1 | 15 | 44 | 17 |

**The honest shape of the result:** the gap earn did not rescue the staged bodies' claims — it *convicted* them. Of 77 sheet-gap items, exactly 1 settles as keepable UCP fact (plus 1 settled component and 1 narrow add-at-rewrite). 44 are cut, 15 survive only relabeled as non-UCP material, 17 remain unjudgeable. That is the fact gate working as designed: the numbers and the DID layer were never UCP's, and now the record proves it from primary sources instead of merely failing to confirm it.

## What remains NOT earnable by sheet (no legs spent, per brief)

- **E4's engineering-practice claims** (vector-DB/LangChain persistence, named stack prescriptions, retention windows, context-window and latency figures): generic engineering advice — no protocol sheet can settle it, and none should try. It rides as the author's practice claims, labeled as such, or gets cut on editorial grounds at publish QC — Glint's call then, not a sheet's.
- **E2/E3's market testimony and practitioner numbers:** classes 1+4 (statistics, hands-on anecdotes). E3 already rides as opinion under **Will's 17:16 PT ruling**; E2's testimony stands as testimony. No sheet earn changes either.
- **D3's market numbers / adoption timelines (31 items):** classes 1/2/5/9/10 — outside this earn's scope and outside any sheet's jurisdiction.

## Publish-blockers for Wave 1 — updated picture

1. **E1 (staged `5793.html`) — UNCHANGED, still a blocker.** mTLS absent, 3 Bearer references remain; the RFC 9421/ES256 correction landed only partially. Sheets 7/8 do not touch it. Fix = one corrective write pass at publish time (Sheet 3 items 4–5 govern).
2. **E5 (staged `1908.html`) — blocker STANDS as staged, but is now a defined rewrite, not an open question.** Sheet 8 rules on every component: of the staged "Key Components" list, product data keeps (narrowed), broad crypto + DID + smart contracts + blockchain recording/reliance + reputation are CUT. The list as written cannot publish; the remedy is mechanical — replace it with the spec-true component set (profiles / capabilities / payment handlers / `keys[]`, Sheet 8 items 1–5 + the narrowed product-data and crypto lines). Sheet 8 changes the blocker's *nature* (unverifiable → ruled), not its *status* (still blocks until the rewrite happens).
3. **NEW blockers created by this earn (expected — they are the earn's product):** D2's staged body cannot publish with its tier/header/SLO content (17 CUTs to execute); D1's staged body cannot publish with its DID-as-UCP content (13 CUTs); D4's staged body carries 7 CUTs (incl. confirming none of 7261 leaked in). All are mechanical deletions/reframes against this file and the RJ leg outputs — no further judgment calls needed.
4. **Not blockers:** the 27 REMAINS-NV items — they route out at publish QC (held, consolidated, or labeled), per UNJUDGEABLE discipline; the 15 REFRAME/RIDE-LABELED items — publishable once their labels are on.

**Net publish-readiness:** nothing in Wave 1 is publish-ready *as staged* — and that was already true before this earn (E1 + E5). What changed: every Wave 1 blocker is now a *ruled, mechanical* fix list. After (a) the E1 auth corrective pass, (b) the E5 component-list replacement, and (c) the D1/D2/D4 cut-and-label passes — all executable from Sheets 3/7/8 + this file without new research — the publish gate is down to Will's Tap 2 (redirect map), Tap 3 (publishing), and the one non-content blocker below.

## Engine record (this earn)

6 contributor legs (GAP7-RATELIMITS, GAP8-IDENTITY, GAP-RJ-D1/D2/D4/E5), all `muse-spark-1.3-contributor`, low effort, cap 16,000, via `run_leg_v2.py`: **6/6 status 200, finish `stop`, try 1 — zero empties, zero truncations, zero retries, zero error bodies.** Totals: **8,147 in / 19,394 out / 13,360 reasoning (68.9%)**. Behaviour note: the sheet-build legs ran lean (34–37% reasoning), but the four rejudge enumeration legs burned 74–90% reasoning at *low* effort while emitting short-form lists (1,073–1,971 chars) — the dial lowers reasoning, it does not floor it; terse-output judgment legs still think long. Programme to date: **42 calls, 259,624 in / 195,306 out.** Spend signal: **none** — no response or balance signal showed any card charge; contributor tier still reads $0 against the $25 envelope (pricing itself remains UNVERIFIED, as before).
Process errors: none in the legs. One Glint-side assembly note, owned: the rejudge prompt files were built by a script extracting plan §6 verbatim (mechanical assembly, verified by the legs' exact count reconciliation: 27/30/15/15).

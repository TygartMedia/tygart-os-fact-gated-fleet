# UCP Cluster Map v2 — Oct 23 Map Re-Run Against the Nov 6 Corpus (Phase 0a)

Companion to `CENSUS.md` (same folder). Sources: Oct 23 AITopics map (~/workspace/your_files/ucp-aitopics-map-2026-10-23.md), Lens A census (2026-11-06), and this phase's full-corpus REST pull (739 posts + 8 pages, word counts re-measured for every ID named below, HTML-stripped split method). **Proposals only — no URLs were changed, nothing was edited; redirects and deletions are Will's tap (Plan Tap 2).**

## How to read the grades
- **CONFIRMED DUPLICATE** — identical titles, or a pair/cluster the Oct 23 map convicted after reading the pages, still live today.
- **CANDIDATE** — title/slug similarity (exact-title scan, first-5-title-words scan = 27 groups, slug-token Jaccard ≥0.62) says read the pair before judging. Same title ≠ same content.
- **CLEARED DISTINCT** — collision that inspection of the record shows is two different jobs; do NOT merge.

## The Oct 23 topical clusters, re-run
The Oct map's six clusters were *query-intent* clusters (what Bing asks about), not a partition of the corpus. The census heuristic partition (CENSUS.md) gives today's corpus shape alongside them:

| Oct 23 cluster | Oct verdict shape | Nov 6 state |
|---|---|---|
| C1 Payment networks & processors | 8 COVERED / 2 DEEPEN of 10 rows | Canonicals all still live: 7139 (1,487 w), 984 (2,845 w), 1242 (2,063 w), 6097 (4,083 w), 3246, 3230, 3507 (now 910 w — the "who's investing" DEEPEN is still unbuilt). Lens B (Oct 20 Visa/Mastercard agent-pay launches) makes 1242 + 6097 refresh-first, not merge candidates — they are CLEARED DISTINCT (strategy vs scorecard). |
| C2 Verification, identity & trust | 5 COVERED / 2 DEEPEN of 7 | Still the strongest shelf: 5471 (3,223 w), 6051 (2,365 w), 4105 (1,820 w), 1253 (1,982 w), 7620 (1,334 w), 4391 (1,762 w). Its DEEPEN (consolidate the decentralized-identity trio) is still open — Cluster D1 below. Stub 7261 still squats on this cluster's core topic. |
| C3 Fraud (agent-side) | 1 COVERED / 6 NOISE of 7 | Agent-side pages live: 3508 (1,761 w), 940 (1,062 w), 1253. The six bank-rail refusals stand — nothing rail-shaped has been built, correctly. (Lens B notes the bank-wall story has since become C2 news; that is a new-article question, not a change to these refusals.) |
| C4 Tokenization & agent money | 1 MISSING / 2 DEEPEN of 3 | 5467 (3,689 w), 5079 (1,934 w), 5248 (2,349 w), 4760 (1,053 w) all live. The one clean MISSING — a dedicated stablecoin-wallets-for-agents page — is **still missing**: WP search returns 10 stablecoin *mentions*, no dedicated page (Lens A §1 correction to the Oct map's "zero content" wording stands). Both DEEPEN explainers (plain-language benefits; forward synthesis) still unbuilt. |
| C5 Merchants, vendors & compliance | 2 COVERED / 3 DEEPEN of 5 | 6095 (3,097 w), 6099 (1,485 w), 7255 (but see stub note — 7255 is itself a 107-word stub, so the "retailers adopting UCP" COVERED verdict rests on a stub plus 5456's 2,505 w case study), 5451 (2,647 w), 5442 (3,239 w), 7140 (1,549 w), 3427 (1,978 w). All three DEEPEN reporting pieces still unbuilt. |
| C6 API shelf | 2 COVERED / 3 NOISE of 5 | Canonical 1695 (1,912 w) still the rate-limit page Bing credits; its duplicates are still unmerged (Cluster D2). Troubleshooting is now a five-page pile-up (Cluster D5). The three runbook refusals stand. |

## Confirmed duplicate clusters (Oct map's convictions — all still live, none closed)

| # | Cluster (IDs) | Today (words) | Status |
|---|---|---|---|
| D1 | Decentralized identity trio: 1940 / 1942 / 1949 | 1,199 / 1,627 / 1,423 | CONFIRMED, still live, all published 2026-03-12 within 2 seconds, untouched since May 8 |
| D2 | Rate-limit trio: 1618 / 1695 / 5268 | 1,741 / 1,912 / 952 | CONFIRMED, still live (Oct map named the pair + the third) |
| D3 | "What is agentic commerce" four-way: 985 / 1010 / 1234 / 6030 | 2,138 / 1,729 / 1,236 / 1,004 | CONFIRMED intent collision; 6030's "Definitive 2026 Guide" title still outruns its 1,004 words (Oct map: 741 by its method — method-relative, same conclusion) |
| D4 | Stub 7261 on trust & identity | 99 words exactly | CONFIRMED stub, never modified since 2026-06-21 |
| D5 | Troubleshooting five-way: 5459 / 5468 / 5751 / 5779 / 5447 | 3,003 / 2,776 / 1,787 / 2,598 / 3,337 | EXTENDED — Oct-era pile-up the map referenced only via 5459; five pages, one intent |

## Exact-title groups (full-corpus scan — 6 groups, 16 posts)
| IDs | Title | Words |
|---|---|---|
| 5793 / 5795 | Testing UCP Integrations: A Developer's Guide to Debugging Agentic Commerce APIs | 4,477 / 4,268 |
| 4767 / 4716 / 4680 / 4620 | What Happens to Price When Every Buyer Has an Agent? | 1,021 / 1,148 / 1,171 / 1,711 |
| 4590 / 4588 | The Broker Dies Last | 1,040 / 1,051 |
| 4266 / 3713 | Agent State Management in Multi-Turn Commerce | 1,770 / 1,936 |
| 1756 / 1908 | UCP and Decentralized Commerce: Building Web3 Shopping Agents | 1,273 / 1,367 |
| 1930 / 1954 | UCP and Verifiable Intent: Building Trust in Agentic Commerce | 1,557 / 1,286 |

## New candidate clusters (similarity scan, beyond the Oct map's list)
| # | Cluster (IDs) | Evidence | Note |
|---|---|---|---|
| N1 | SDK/libraries pair: 5780 / 5781 | slug Jaccard 0.86, near-identical titles | Read pair, then judge |
| N2 | GitHub open-source pair: 1257 / 1264 | slug pair, one carries a `-2` suffix | Suffix pattern repeats across the corpus — a republication signature |
| N3 | Cookieless affiliate tracking: 5070 / 6038 | identical slug-token set, reordered | CANDIDATE |
| N4 | Digital-goods pair: 1339 / 1667 | slug Jaccard 0.75, same intent + "complete guide" framing both | CANDIDATE |
| N5 | Agentic vs traditional e-commerce: 1240 / 6032 | slug Jaccard 0.71 | CANDIDATE |
| N6 | Returns & refunds pair: 3379 / 3510 | slug similarity + shared "agent state" framing | CANDIDATE |
| N7 | Agent cost attribution pair: 3648 / 4506 | slug Jaccard 0.83 | CANDIDATE |
| N8 | Cart-abandonment pair: 3395 / 4111 | slug Jaccard 0.83 | CANDIDATE |
| N9 | Small-business case-study pair: 5455 / 5469 | same story shape ("doubled sales/conversions with UCP") | CANDIDATE — cf. the confirmed fictional-brand pair 5748 / 5749 (1,807 / 1,427 w) |
| N10 | Security best-practices pair: 1754 / 1916 | first-5-title collision, near-identical titles | CANDIDATE, strong |
| N11 | "UCP gains traction" news pair: 1718 / 1758 | first-5 collision | CANDIDATE (news items — may be legitimately separate dated items) |
| N12 | Gemini-in-Chrome news pair: 3123 / 3278 | first-5 collision | CANDIDATE (same caveat) |
| N13 | Claude Marketplace cluster: 1946 / 2100 / 3192 / 3512 | first-5 collisions ×2 groups + shared intent | CANDIDATE — news cluster, likely a mix of dated items and re-treads |
| N14 | Decentralized-commerce trio: 1721 / 1756 / 1908 | 1756/1908 are the exact-title pair above; 1721 slug-matches 1908 (Jaccard 0.71) | EXTENDS the exact-title pair to a trio |
| N15 | Verifiable-intent cluster: 1930 / 1954 / 5471 | exact-title pair + the 3,223 w canonical explainer 5471 | The pair should fold toward 5471, not merge with each other |
| N16 | Measuring-success six-way: 5761 / 5762 / 5763 / 5764 / 5765 / 5454 | two first-5 groups, one intent (analytics/reporting/KPIs) | 2,903 / 2,974 / 1,654 / 1,421 / 1,269 / 2,567 w |
| N17 | Pricing four-way: 5067 / 5785 / 5398 / 5400 | intent collision (Lens A §4) | 2,200 / 3,001 / 3,329 / 3,586 w — likely two intents (pricing model; integration costs), not one |
| N18 | Webhooks pair: 1480 / 1309 | first-5 collision (Oct map listed both) | 2,157 / 2,366 w |
| N19 | Payments-auth pair: 1249 / 1256 | first-5 collision (Oct map listed both) | 1,944 / 1,916 w — 1256 is the 2026-dated edition of the same title |
| N20 | Monetizing pair: 5444 / 5450 | first-5 collision (Oct map listed both) | 3,031 / 2,674 w |
| N21 | Vs-traditional-gateways pair: 5441 / 5783 | first-5 collision (Oct map listed both) | 3,055 / 1,775 w — comprehensive comparison vs merchant's guide; may clear as distinct-audience |
| N22 | What-ucp-means pair: 4616 / 4724 | slug similarity; 4724 is a `-3` republication slug | CANDIDATE |

**False-positive control:** the slug-similarity scan also fires heavily on the persona/perspective series (slugs like `cto-guide`, `cfo-perspective`, `data-science-perspective` with numeric suffixes — Lens A's interlink series). Those are a deliberate series format, not duplicates; they are excluded from the candidate list above and noted here so the scan's limits are on the record.

## Cleared distinct — do not merge
- **1242 vs 6097** (Visa/Mastercard strategy vs scorecard) — different jobs, both canonical for their rows.
- **5067** (rate card) — a pricing *format* page; keep distinct inside N17.
- **The six hub pages** (5827–5832) — one per topic area by design.
- **Persona/perspective series posts** — series format, see false-positive control above.

## Stub population — all 15 posts under 300 words (full-corpus, exact)
All 15 sit in one ID block (7235–7263, odd IDs), all June 2026, all 93–134 words — one unfinished publishing batch, not scattered decay.

| ID | Words | Title (short) | Proposed disposition |
|---|---|---|---|
| 7261 | 99 | Trust and Identity in UCP: Preventing AI Fraud | Fold into 1253 (Oct map's call) |
| 7263 | 93 | The UCP Merchant Checklist | Fold into 6095 (readiness assessment, 3,097 w) |
| 7245 | 121 | AP2 Explained | Fold into 1928 (AP2 deep dive, 1,454 w) |
| 7243 | 108 | Role of the /.well-known/ucp Discovery Endpoint | Fold into 976 (configuring the endpoint, 1,603 w) |
| 7247 | 104 | Anatomy of a UCP Transaction | Fold into 984 (complete guide, 2,845 w) |
| 7239 | 112 | Preparing Your Shopify Store for UCP | Fold into 5451 (Shopify migration guide, 2,647 w) |
| 7251 | 123 | How to Implement UCP Native Checkout in 2026 | Fold toward 1012 / 1009 checkout cluster — pair-read first |
| 7259 | 103 | UCP and Voice Assistants | Fold into 1269 / 3411 voice cluster — pair-read first |
| 7255 | 107 | Why Major Retailers Are Adopting UCP | Build out or fold into 5456 — note C5's COVERED verdict leans on this stub |
| 7235 | 134 | The Future of Agentic Commerce | Build-out candidate (flagship-shaped title) |
| 7237 | 122 | UCP vs. Traditional EDI | Build-out candidate (no full EDI counterpart exists) |
| 7241 | 119 | How Google Gemini Uses UCP to Shop | Fold toward 3123 / 3278 Gemini cluster — pair-read first |
| 7249 | 105 | B2B Procurement Automation using UCP | Fold toward 1633 (B2B procurement, 1,992 w) — pair-read first |
| 7253 | 105 | The Rise of Headless AI Commerce | Fold toward 5204 / 984 — pair-read first |
| 7257 | 109 | Multi-Agent Shopping: Complex Carts | Build-out candidate (no full counterpart found) |

## Consolidation target list — proposed canonicals (PROPOSALS ONLY; execution is Tap 2)
One canonical pick per cluster, chosen on word weight + the Oct map's citation record + title-intent fit. Non-canonical members are merge/fold candidates; nothing here authorizes a redirect.

| Cluster | Members | Proposed canonical | One-line reasoning |
|---|---|---|---|
| D1 Decentralized identity | 1940 / 1942 / 1949 | **1942** | Longest of the trio (1,627 w) and the broadest trust framing |
| D2 Rate limits | 1618 / 1695 / 5268 | **1695** | The page Bing already credits as canonical (Oct map), joint-longest |
| D3 What is agentic commerce | 985 / 1010 / 1234 / 6030 | **985** | Longest (2,138 w); 6030's "definitive" title either folds here or gets rebuilt to earn it |
| D5 Troubleshooting | 5459 / 5468 / 5751 / 5779 / 5447 | **5459** | The guide the Oct map already treats as the site's troubleshooting reference (3,003 w) |
| Exact: Testing integrations | 5793 / 5795 | **5793** | Longer of the identical pair (4,477 w) |
| Exact: Price when every buyer has an agent | 4620 / 4680 / 4716 / 4767 | **4620** | Longest (1,711 w) and the original unsuffixed slug |
| Exact: The Broker Dies Last | 4588 / 4590 | **4588** | Statistical tie (1,051 vs 1,040 w); unsuffixed slug wins |
| Exact: Agent state management | 3713 / 4266 | **3713** | Longer (1,936 w) |
| N14 Decentralized commerce | 1721 / 1756 / 1908 | **1908** | Longest of the exact-title pair (1,367 w); 1721 pair-read before folding |
| N15 Verifiable intent | 1930 / 1954 / 5471 | **5471** | The 3,223 w explainer dwarfs the pair; fold toward it |
| N16 Measuring success | 5454 / 5761–5765 | **5761** | Fullest analytics + performance framing (2,903 w), first of the numbered run |
| N17 Pricing | 5067 / 5398 / 5400 / 5785 | **5785** (pricing model) + **5400** (integration costs) | Two intents, two canonicals; 5067's rate-card format stays distinct |
| N18 Webhooks | 1309 / 1480 | **1309** | Longer (2,366 w), "Complete Guide" framing |
| N19 Payments auth & compliance | 1249 / 1256 | **1256** | The 2026-dated edition supersedes the undated original |
| N20 Monetizing your AI agent | 5444 / 5450 | **5444** | Longer (3,031 w) |
| N9/N-confirmed Fictional-brand case studies | 5748 / 5749 | **5748** | Longer (1,807 w); the pair also needs a labelling decision, not just a merge |
| Stub block (15) | 7235–7263 (odd IDs) | Per-stub table above | One unfinished June batch; fold where a full counterpart exists, build out the three flagship-shaped titles |

Candidate clusters N1–N8, N10–N13, N21, N22 get pair-reads in Wave 2 before any canonical is proposed — proposing from titles alone would repeat the extraction-overreach error the program's guards exist to prevent.

## What closed since Oct 23
- **Nothing.** No Oct-map duplicate cluster has been consolidated, no stub built out or folded, and the corpus grew by exactly one post (7930, Oct 24). The Oct map's term-search correction (Lens A §1: stablecoin/KYC/FedNow/payout/passkey are mentioned in-corpus, not zero-hit) is the only Oct-map claim this re-run overturns; its MISSING verdict for a dedicated stablecoin page survives the correction.

## Could not establish
- **Content-level sameness for CANDIDATE clusters** — similarity scans nominate; only per-pair body reads convict. Wave 2's job.
- **Which duplicate member carries the citation equity** for clusters beyond D2 (the Oct map only had Bing evidence for the rate-limit canonical) — needs a fresh AITopics/Clarity pull per cluster.
- **Whether the `-2`/`-3` suffixed republications differ in body** from their originals (titles match; bodies un-read in this phase).
- **Inbound-link equity per cluster member** is computable from CENSUS.md's links-in column but was not adjudicated here — canonical picks above rest on weight + citation record, not link equity, and Wave 1 should re-check any pick where links-in strongly favours a non-canonical member.
- **The persona/perspective series' internal duplication** — excluded as a deliberate format on slug evidence alone; its bodies were not audited in this phase.

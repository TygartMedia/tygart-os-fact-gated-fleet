# Evidence Index — every headline claim in the packet, mapped to its receipt

Built 2026-11-03 at the final packaging pass. Paths are bundle-relative where the receipt is in this bundle; workspace paths are given where the master record stays outside it. If a claim is not listed here, it is not in the packet.

## Money

| Claim (packet / one-pager) | Receipt |
|---|---|
| Counted spend **$102.35 of the $153.31 envelope** (precise receipt-summed total $102.3526) | `~/workspace/out/model-bakeoff/NIGHT-LEDGER.md` — final running-total entry (contribution sweep, 2026-11-03): "$101.8789 + $0.47373 = $102.3526 → $102.35 of $153.31" |
| Counted = every Meta Model API leg with returned usage, incl. all TruNorth/drill/ROM/Wave-3 prep legs (packet trio $0.05393; drill fan-out $0.01028; drill adjudication $0.05785; ROM fan-out $0.00317 + adjudication $0.02861; Wave 3 fan-out $0.00393 + adjudication $0.05629; packet scrub $0.00038; Run-1 drafts $0.00184) | Same ledger, entries 2026-11-03 (TruNorth Run 1 drafts → Wave 3 adjudication) |
| Excluded as unmetered: ASR calls returning null usage; muse-image-1.0 generations (no published rate); one killed run est. ~$0.003; browser UI time is not API-metered | Same ledger (image/ASR/"not counted" entries, 2026-11-03) |
| Standard trio ≈ **$0.12/page**; contributor tier ≈ **$0.0025/page**; routing decision ≈ **$0.025/recording** | NIGHT-LEDGER.md (contributor fleet test; router effort test, 9/9 clean, $0.34096) |

## Fleet production

| Claim | Receipt |
|---|---|
| **4,415 live pages** read across 6 sites; **2,769 strong monetization candidates** (4,366 calls, $1.7592) | NIGHT-LEDGER.md, monetization sweep entry (2026-10-31); detail: `~/workspace/out/model-bakeoff/monetization-sweep/` |
| **2,062 adjudicated fixes** = 647 (Continuity Hub, 93-page census) + 1,415 (Risk Coverage Hub, 201-page census) | NIGHT-LEDGER.md, Continuity + RCH sweep entries |
| **36 staged work orders** (11 Continuity WO-531…541 + 25 RCH WO-545…569) | NIGHT-LEDGER.md, same sweep entries |
| **174 session recordings · 3,093 window reads** | NIGHT-LEDGER.md, video leg final census entry; run record `~/workspace/out/model-bakeoff/video-test/RESUME-LOG.md` |
| **245 ASR calls · 138,144 words · $3.20** | NIGHT-LEDGER.md, audio leg entries (81 + 164 calls, both passes) |
| Consensus miner: **339 certified, 17 of 356 dropped (4.8%)** by verbatim-quote validation | NIGHT-LEDGER.md, consensus miner entry ($2.63) |
| The demo's strike (verbatim): fixer proposed adding "and any crime / funds-transfer extension"; adjudicator struck it — "that product concept is not in page or Sources" | `~/workspace/out/model-bakeoff/rch-sweep/cfc-sme-cyber-disconnect-what-cover-pays-for/` (sweep source files; quoted in packet + flagship script `final-v2/SCRIPT.md`) |

## Router design + landscape

| Claim | Receipt |
|---|---|
| Tip = one row per Company × Destination (16 fields); grounding quote required per field; probation → trusted staging; read-back levels | `ROUTER-DESIGN.md` (this bundle) |
| Router design itself trio-adjudicated, **49-item struck list**, $0.21809 | `ROUTER-DESIGN.md`; raw legs `~/workspace/out/meta-hackathon-2026/router-run/adjudicator-raw.md` |
| The full 5-part reverse-MCP pattern exists nowhere public; closest actors superglue / Flatfile / Extend / EDI acknowledgments | `reverse-mcp-landscape-report.md` (this bundle) |

## TruNorth field test (all Nov 3, 2026, TEST sandbox)

| Claim | Receipt |
|---|---|
| Destination shapes: UI job form; documented CSV price-list import (destination-supplied template); Encircle job import | `trunorth/RUN-1.md` (shape map) |
| Run 1: one mirror job created (26-00003-HQ); read-back **18/18 fields MATCH** | `trunorth/RUN-1.md` Step 2–3 |
| Run 2: scratch job 26-00004-HQ; edit Est. Days 7 → 9, exactly 1 field changed, reason recorded | `trunorth/RUN-2.md` §2B–2C |
| Run 2: daily sheet total **$465.50 read back = $465.50 computed** | `trunorth/RUN-2.md` §2D-1 |
| Run 2: photo accepted (count 1); PDF and voice file refused — job-page upload is image-only (JPEG/PNG), refusal text on screen | `trunorth/RUN-2.md` §2D-2…2D-4 |
| Run 2: second CSV surface states format `type,id,name,unit,category,price` ≠ first surface's documented header — tips are per-surface | `trunorth/RUN-2.md` §2A |
| Run 3: Packet A created 26-00005-HQ (Contract $30,303); Packet B expected-before guard passed exactly, then Contract $7,777 → $7,999 + payer updated, 2 fields changed | `trunorth/RUN-3.md`; page PDFs `evidence-pdfs/run3-packet-a-detail.pdf`, `evidence-pdfs/run3-packet-b-edited-detail.pdf` |
| Storm drill: **9 inputs** (1 storm pulse + 8 field inputs incl. 2 designed break-tests) | `trunorth/DRILL-LOG.md`; inputs in source folder `storm-drill/inputs/00…08` |
| Fan-out: 16 calls (2 agents × 8 inputs), 65.52 s, **$0.01028**; 13/16 clean parses; 42/50 comparable fields agreed | `trunorth/WAVE1-RECEIPTS.md`; raw `storm-drill/wave1-results.json` (source folder) |
| Trap 1 (contradictory call-in, two addresses): **no job created** — flagged by both fan-out agents, upheld at adjudication | `trunorth/WAVE1-RECEIPTS.md` (F1 — NO EMISSION); `trunorth/SPOT-TESTS.md` Check 4 (searches for the second address: 0 matches) |
| Trap 2 ("earthquake" loss type): **never emitted**; mapped to "Other," mapping named in the job title (26-00009-HQ) | `trunorth/WAVE1-RECEIPTS.md` (D4) |
| Drill emissions: 4 jobs created (26-00006-HQ…26-00009-HQ) + 2 guarded updates (Whitaker Est. Days 1 → 2; Edmond authorization $18,500 → $24,000) + 1 photo | `trunorth/WAVE1-RECEIPTS.md`; page PDFs `evidence-pdfs/drill-d1…d4`, `drill-u1`, `drill-u2`, `drill-a1-whitaker-photo.pdf` |
| Spot re-reads **4/4 PASS** (Edmond $24,000 · Whitaker Days 2 + photo · Packet A $30,303 · no phantom job) | `trunorth/SPOT-TESTS.md`; `evidence-pdfs/spotcheck-*.pdf` |
| ROM Whitaker: **$2,378 · $4.03/sq ft · 54% margin** (splits sum exact) | `trunorth/WAVE2-RECEIPTS.md`; `evidence-pdfs/rom-whitaker.pdf` |
| ROM Edmond: **$8,418 · $4.95/sq ft · 51% margin**; vs $24,000 authorization **under by $15,582**; authorization never entered into the estimator | `trunorth/WAVE2-RECEIPTS.md` (THE NTE CHECK); `evidence-pdfs/rom-edmond.pdf` |
| ROM Quail Creek: **$8,879 · $9.87/sq ft · 53% margin** | `trunorth/WAVE2-RECEIPTS.md`; `evidence-pdfs/rom-quailcreek-final.pdf` |
| Estimator overrides: Edmond air movers **17 computed vs 10 ticked**; Quail Creek **13 vs 8**; Whitaker LGR 1 X-Large vs 2 ticked; catalog rates $128/day (LGR X-Large), $29.50/day (air mover) | `trunorth/WAVE2-RECEIPTS.md` (Equipment section) |
| Rate card: intake ≈ **7 inputs/min** at **$0.0013/input**; gate ≈ **$0.0085/input all-in**; import ≈ **1 job/min** (9 emissions in ~600 s); screen leg ≈ **8× slower than intake** | `trunorth/WAVE1-RECEIPTS.md` (RATE CARD section) |
| Wave 3: three Edmond daily sheets **$1,769.00 + $886.00 + $1,247.50 = $3,902.50**; cross-check 30 tech-hours / 28 air-mover unit-days / 9 LGR unit-days / 3 scrubber unit-days; all three **submitted, PENDING at the manager signature** — the packet claims nothing downstream of the signature | Source receipt (deliberately NOT bundled — see READY.md): `~/workspace/out/trunorth-reverse-mcp-2026-11-03/storm-drill/wave3/WAVE3-RECEIPTS.md` |
| "Gilstrap Signature" forensic summary (two rate books, equipment bias, 51–54% margin band) | `trunorth/DNA-SHEET.png` — visual built from the WAVE2-RECEIPTS values above; its own face carries its basis + caveat |

## Demo video

| Claim | Receipt |
|---|---|
| Flagship `final-v2/demo-final-3min.mp4`: 187.06 s, 57,134,481 B, H.264 1920×1080@30 + AAC 48 kHz, faststart, full decode zero errors | ffprobe + ffmpeg full-decode run at this packaging pass — recorded in `READY.md`; build record `~/workspace/out/meta-hackathon-2026/final-v2/BUILD-NOTE.md` |

## Contribution sweep — the submission red-teamed by its own system (Nov 3, 2026)

| Claim | Receipt |
|---|---|
| Deliberate contributor-tier workload run as a pre-filing red-team: **544 calls submitted, 405 returned usable content**, total metered cost $0.47373 | `CONTRIBUTION-LOG.md` (this bundle); leg records `~/workspace/out/meta-hackathon-2026/contribution-sweep/` (leg1-packet-redteam/, leg2-receipts-crosscheck/, leg3-fleet-qa/) |
| Claim audit: **0 ABSENT across 104 audits** (52 sampled packet/router claims × 2 independent agents; verdicts split CITED vs STATED, none missing from the documents) | `CONTRIBUTION-LOG.md` finding #4 + Leg 1 detail; raw pairs in the leg1 folder |
| Fleet Q&A grounding: **90/90 answers grounded** in verbatim page quotes (0 fabricated) over 15 published fleet pages | `CONTRIBUTION-LOG.md` Leg 3; programmatic scoring `leg3-fleet-qa/quote-check.json` in the sweep folder |
| Receipts cross-check: all 12 money values appearing in multiple TruNorth receipt files carry the same value everywhere (no conflicts) | `CONTRIBUTION-LOG.md` finding #8; `leg2-receipts-crosscheck/deterministic-check.json` |
| The sweep's packet findings (TEST-sandbox skim risk, "built entirely" stack purity, absolutes, uncited unit costs, missing strike exhibit pointer) were applied to the packet as precision edits at close-out | `CONTRIBUTION-LOG.md` findings #1–#5; the edits are listed in `READY.md` |

## Known gaps (nothing below is claimed anywhere in the packet)

- Cerebral Valley portal fields, caps, and upload-vs-link format: **unverified** — checked live only at filing, with Will signed in.
- Wave 3 downstream artifacts (progress invoice, work summary, credit request): **never produced** — the run ended at the signature gate; the packet says so.
- Any statement about *why* approval did not complete: **not made** in judges' material, by design.

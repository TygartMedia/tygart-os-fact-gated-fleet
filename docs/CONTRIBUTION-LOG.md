# Contribution Sweep — Log & Receipts

**What this was, plainly.** Will's idea, ordered 2026-11-03 ~19:27 PT: run a deliberate,
real workload on **muse-spark-1.3-contributor** — because contributor-tier usage feeds
back to Meta under its terms, a logged, purposeful workload IS a contribution back to
the system whose effort-tier behavior the submission is about — and make the workload
double as a **red-team of our own hackathon submission before judges see it**.

**Scope (hard rule, held):** only our own or public material — the submission packet,
the router design doc, tonight's TruNorth run receipts, and published pages from our
own fleet sites. No client material, no unpublished private material. Nothing was
published or sent. The submission packet was NOT edited; fixes are the main agent's call.

**Totals:** 544 calls submitted · 405 returned usable content (see the attempt-1 note
below) · 1,492,243 input tokens · 1,622,412 output tokens · **total metered cost
$0.47373** (hard cap was $10 — never approached) · run wall ≈ 21 min across phases
(19:33–20:22 PT including page fetching and analysis).

| Leg | Calls submitted | Usable content | Cost |
|---|---|---|---|
| 1 — Packet red-team | 283 | 195 | $0.26318 |
| 2 — Receipts cross-check | 140 | 90 | $0.17259 |
| 3 — Public fleet Q&A | 121 | 120 | $0.03796 |
| **Total** | **544** | **405** | **$0.47373** |

Per-leg splits include each leg's share of the smoke test and of both Phase A
attempts; the run files listed at the bottom are the exact record. Attempt-1
calls are counted in spend — the meter ran even when the content didn't come
back. "Usable" excludes the 9 attempt-2 ERROR records (their response field
holds an error string, not content).

---

## FINDINGS THAT MATTER FOR THE PACKET — READ BEFORE FILING

Every wording below was grep-verified against the frozen packet snapshot
(`inputs/packet.md`, sha f3f6841e…, snapshotted 2026-11-04 03:28 UTC). These are
red-team flags with the calibration the receipts support — not verdicts.

### 1. "Real production / ran live" vs the TEST sandbox — the #1 judge risk
Both independent synthesis agents ranked this first, from all three Phase A reviewers.
- Packet line 27 (Impact line): *"real production, not a staged demo — 4,415 live
  pages, a download ladder shipping now, 36 work orders staged…"* — in its own
  sentence this claim is about the **fleet**, and it's true of the fleet.
- Packet line 13 (summary paragraph): *"the router pattern ran live against TruNorth
  Ops, third-party restoration software with no API"* — unqualified where it sits.
- The packet **does** disclose the sandbox plainly — line 39 ("Nov 3, TEST sandbox,
  watched sessions") and line 45 ("a personal admin login to a private TEST copy of
  his real software… Everything below ran in that TEST sandbox"). The disclosure is
  honest and prominent in the TruNorth section.
- **The risk is skim-order, not deception:** a judge reading the summary + criteria
  lines meets "real production / ran live" before the disclosure. Cheapest fix:
  qualify line 13 ("ran live against a TEST copy of TruNorth Ops") to match line 45.

### 2. "Built entirely on Muse Spark 1.3 effort tiers + the contributor tier" (line 28)
Flagged by all three reviewers as a stack-purity absolute. The night's own ledger
records non-Spark legs in the wider program (voice transcription, TTS). Scoped to
the trio/router work the sentence is defensible; unscoped, one cross-read of the
receipts dents it. Suggest scoping the sentence to the system it describes.

### 3. The absolutes family — "every number traces", "improvised nothing"
- Line 45: *"every number traces to a run receipt in the evidence bundle."*
- Line 13: *"every run receipted."*
- Line 51: *"the executor improvised nothing"* — the same paragraph honestly
  discloses the one prose garble the QC caught, which is the receipts-over-narration
  story working as intended; but "improvised nothing / every number" are the kind
  of absolutes a skeptical judge only needs one exception to discount wholesale.
  Suggest measured phrasing ("numbers in this section trace to…", "0 ungrounded
  edits in the logged runs").

### 4. Unit-cost figures carry no in-packet citation
$0.12/page, $0.0025/page, $0.025/recording, 49× spread (lines 29, 34) are stated
without pointing at the ledger that backs them. The per-claim audit (104 audits,
2 agents × 52 sampled claims) found **zero claims ABSENT from the documents** —
nothing sampled was invented — but verdicts split **packet 33 CITED / 19 STATED**
and **router 15 CITED / 37 STATED**: the router doc in particular states most
claims without naming a source. The figures do live in NIGHT-LEDGER.md; the packet
never points there. Suggest naming the ledger beside the figures.

### 5. The hero strike has no exhibit pointer in the packet text
Line 30 quotes the Adjudicator's strike on the RCH CFC page ("and any crime /
funds-transfer extension") but doesn't name the sweep file or exhibit where a
judge can verify the centerpiece catch. Pointer gap, not a truth gap — the strike
is in the run record; the packet just doesn't say where.

### 6. Router history counts are stated without their sheets
ROUTER-DESIGN.md (lines 262–264): "312 session recordings routed against a
25-destination slate", "skipped 9/9 when sources held anything private" — no
decision sheet named in the doc. Same fix class as #4: name the source file.

### 7. The drill log's self-description does not survive its own receipts
Leg 2 re-verified 22 drill-log claims (sampled from 263 the extractors marked as
unsupported) against RUN-1/2/3 only: **5 SUPPORTED · 10 UNVERIFIABLE within the
scoped files · 7 CONTRADICTED** — and all 7 contradictions land on the log's
framing claims: "canonical running record," "factual and receipts-faithful
throughout," "anything not yet verified is marked UNCONFIRMED," "verdicts quoted
in the receipts' own words." The receipts themselves document why: Run 1's CSV
header was wrong and Run 2 corrected it; Run 3 carries a QC note flagging garble
in the browser report's prose; the token UNCONFIRMED never appears in the run
files (open items are marked in other words). **Contained exposure:** grep
confirms the packet repeats none of those phrases — this only matters if a judge
reads DRILL-LOG.md in the evidence bundle and takes its framing at face value.

### 8. What came back CLEAN — say so with confidence
- **Numbers cross-check: no conflicts.** A deterministic regex pass plus 8 model
  list-pair checks: all 12 money values that appear in multiple receipt files
  carry the same value everywhere ($465.50, $5,014.10, $2,761.60, $1,957.00, …).
  Run-vs-run pairs: 6/6 NO CONFLICTS. The one flag raised ("minutes, 9 vs 10")
  resolves inside Run 2's own header — clock window 17:55–18:05 = 10 min,
  harness-measured 9 min; two measures of the same run, both printed in the file.
- **Claim audit: 0 ABSENT.** Nothing in the sampled packet/router claims was
  missing from the documents; agent agreement 46/52, and all 6 disagreements
  were CITED-vs-STATED boundary calls.
- **Fleet Q&A grounding: 90/90.** See Leg 3 — zero fabricated quotes.

### 9. Contributor-tier behavior worth Meta's feedback file
Phase A's first run lost 128 of 151 responses: on dense extraction/analysis
prompts, the contributor model's reasoning consumed the entire completion budget
(1,200–3,000 tokens) and the API returned `content: null` with status OK and full
metering. At a 7,000-token budget, 142/151 succeeded; the 9 hardest (number
extraction over dense receipts) still emptied a 16,000-token budget — and then
all 9 succeeded when the prompt led with an output-only instruction at 12,000
tokens. Net lesson, measured: on this tier, budget ≥7K and "emit first, no
deliberation" framing are the difference between a metered null and an answer.

---

## Leg 1 — Packet red-team (detail)

Corpus: `SUBMISSION-PACKET.md` (17,129 B) + `ROUTER-DESIGN.md` (20,086 B), frozen
in `inputs/`. Phase A (84 + 6 top-up): per-chunk and whole-doc claim extraction,
ungrounded hunts, skeptical-judge questions, overclaim hunts, number extraction
with stated sources, judging-criteria scoring — each whole-doc pass ×3 agents.
Phase B (108): 52 sampled claims × 2 agents audited against the full documents
(CITED / STATED / ABSENT — tallies in finding #4), plus 4 consolidation calls
ranking the overclaim and ungrounded findings (the two syntheses agreed closely;
their top-5s are the basis of findings #1–#6). Full prompt/response pairs:
`leg1-packet-redteam/results-a.json`, `results-a-attempt1.json`,
`results-topup.json`, `results-b.json`.

## Leg 2 — Receipts cross-check (detail)

Corpus: RUN-1.md, RUN-2.md, RUN-3.md, DRILL-LOG.md (frozen in `inputs/`).
Phase A (52 + 3 top-up): per-file number extraction, drill-claim extraction with
support marking, Jason-pattern summaries ×2 agents per file. Phase B (32):
8 number-list conflict checks, 22 sampled unsupported-claim verifications
(finding #7), 2 pattern consolidations. Deterministic regex cross-check:
`leg2-receipts-crosscheck/deterministic-check.json` (shared money values all
consistent; note the drill log references its jobs by name more than by ID —
its only job IDs are 26-00003-HQ and 26-TYG-001-HQ).

**Jason's design patterns, consolidated from the receipts** (both syntheses
agreed): (1) sandbox-gated identity first — no work until actor, role, org,
build, and TEST status are confirmed; (2) audit-first mutation — Edit / Archive /
Delete require a Reason and leave a visible trail; creates are low-friction,
mutations are not; (3) approval-gated money — submitted ≠ counted: totals count
APPROVED sheets only, which is why a $465.50 submitted sheet left job totals at
$0.00, explained in the receipts rather than hidden; (4) catalog-first data —
fixed dropdowns and the price catalog win by default, custom values enter only
through explicit "Other…" escape hatches, and equipment lines require a catalog
anchor. (Full synthesis with quoted evidence: `synth-patterns-a1/a2` in
`leg2-receipts-crosscheck/results-b.json`.)

## Leg 3 — Public fleet Q&A (detail)

15 published pages fetched live 2026-11-04 03:28–03:31 UTC (5 Tygart Media,
5 Restoration Intel, 5 Healthcare Facility Hub incl. its thin homepage), saved
verbatim under `leg3-fleet-qa/pages/`. The model wrote 3 grounded questions per
page (45); 2 independent agents answered each, required to return an exact
verbatim quote as JSON. Programmatic scoring (normalized string match,
`leg3-fleet-qa/quote-check.json`): **79/90 strict-verbatim** (≥12-char quotes
found character-for-character after normalization); the other 11 were short
factual strings — dates, a version, a code ("2026-10-14", "1.19.0", "2377",
"final_v3", "10:15 AM ET", "dev.meta.ai", "S&C 17-30") — and a direct substring
re-check confirmed **all 11 present in their pages: 90/90 grounded, 0 fabricated
quotes, 0 nulls**.

One fleet defect spotted in the fetched text, outside the Q&A scoring: the
Tygart Media "Claude Code vs Cursor" page's heading claims an **84.3%** cost
differential while its own body computes **89.00%** ($6.00 → $0.66 is 89.0%).
The heading is the stale number. (Saved text: `leg3-fleet-qa/pages/
tm-claude-code-vs-cursor.md`, lines 17 vs 40.)

## Method notes & honesty box

- Runner: house fanout pattern, 8 workers, 1 retry, per-leg spend caps ($3) set
  far above actuals; the $10 sweep cap was never approached (final: $0.47373).
- Phase A attempt 1 is preserved as `results-a-attempt1.json` in each leg folder:
  151 calls, status OK, but 128 responses are `null` for the reason in finding #9.
  The spend counted; the content didn't exist. Attempt 2 re-ran the same prompts
  at ≥7,000-token budgets. Phase B was generated from attempt-2 content only.
- Claim audits sampled 26 claims per document (of 506 packet / 573 router
  extracted claim lines) and 22 of 263 flagged drill claims — sampling, stated
  as such; the tallies describe the samples, not the full corpora.
- Leg 2's verification corpus was RUN-1/2/3 only, per the task scope; drill-log
  material whose receipts live in other files (Wave 2/3 records) scores
  UNVERIFIABLE here by construction. That is a scope artifact, recorded as one.

## Files

- This log: `CONTRIBUTION-LOG.md`
- Frozen inputs + hashes: `inputs/` (packet.md, router-design.md, run-1/2/3.md, drill-log.md)
- Leg 1: `leg1-packet-redteam/` (jobs-a/b, results-a, results-a-attempt1, results-topup, results-b)
- Leg 2: `leg2-receipts-crosscheck/` (+ deterministic-check.json)
- Leg 3: `leg3-fleet-qa/` (pages/, jobs, results, quote-check.json)
- Runner + generators: `work/` (sweep.py, gen_a.py, gen_b.py, det_check.py, check_leg3.py)
- Spend also ledgered in `~/workspace/out/model-bakeoff/NIGHT-LEDGER.md`.

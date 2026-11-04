# Contributor-tier lessons — muse-spark-1.3-contributor, measured

Everything below was learned by running the contributor tier as a production
workhorse, not by reading a spec sheet. Each claim traces to a receipt in
[`CONTRIBUTION-LOG.md`](CONTRIBUTION-LOG.md) (finding #9 is the tier-behavior
record) or [`NIGHT-LEDGER.md`](NIGHT-LEDGER.md) (per-call usage and costs).
Written to be pulled from: if you run bulk work on this tier, these are the
rules we would hand you before your first run.

## The tier

- **Model:** `muse-spark-1.3-contributor`, priced at **$0.10 per 1M input
  tokens, $0.20 per 1M output tokens**.
- **Unit economics, measured:** ≈ **$0.0025 per page** on contributor vs
  ≈ **$0.12 per page** for the standard-tier Trio — a **49× spread** on the
  same class of work.
- **Quality where it was tested:** in the six-model opening panel, the
  contributor twins read pages **at parity** with the standard models for
  **$0.0008 per call** (the sharpest standard read cost $0.0459). In the
  closing sweep's fleet Q&A leg, contributor answers grounded **90 of 90
  quotes, 0 fabricated**.

## The budget law (the expensive lesson)

On dense extraction or analysis prompts, the contributor model's reasoning
can consume the **entire completion budget before any content is emitted**.
The API then returns **`content: null` with status OK — and full metering**.
You pay for the reasoning; you receive nothing.

Measured, from the contribution sweep's Phase A (151 calls):

- At completion budgets of **1,200–3,000 tokens: 128 of 151 responses came
  back null.**
- At a **7,000-token budget: 142 of 151 succeeded.**
- The 9 hardest (number extraction over dense receipts) **emptied a
  16,000-token budget** — and then **all 9 succeeded** when the prompt led
  with an output-only instruction at 12,000 tokens.

**The rules that fall out of it:**

1. **Budget ≥ 7,000 completion tokens on this tier, always.** Small budgets
   don't save money; they buy metered nulls.
2. **Lead with the output contract.** "Emit first, no deliberation" /
   output-only framing at the top of the prompt is the difference between a
   metered null and an answer on the hardest calls.
3. **Count nulls as spend.** A null-content response is metered like any
   other call; our ledger counts it, and re-runs are budgeted on top.

## Where the tier sits in the design

- This tier was **probed for the gate and failed it** — its token limits
  (see the budget law) are what forced the design questions: how much
  context each step needs, what is available to it, and in what order the
  steps run. The Trio that came out of those questions runs on the
  **standard tier — low → medium → max, in that order**: the cheap legs go
  first and prepare the record the max leg judges. The order is
  load-bearing; reversed, it does not work — a max leg sent in alone
  failed.
- Contributor does the **bulk ingestion and fan-out**: the storm drill's
  16-call fan-out (65.5 s, $0.01028), the emblem brief-writing leg, and the
  corpus pick-out pass (69 calls, $0.14481, 361 findings — every quote
  machine-verified afterward).
- The **standard tier adjudicates**. Separation of duties holds across
  tiers: the tier that proposes in bulk is never the tier that approves.

## Metering honesty

- Calls that return usage are counted at the tier price, nulls included.
- Calls that return **no usage are recorded as unmetered and never
  estimated** (two narration-drafting calls read-timed-out at the helper's
  60-second cap: no usage, $0 counted, recorded as exactly that).
- The closing sweep as a whole: **544 calls submitted, 405 with usable
  content, 1,492,243 tokens in / 1,622,412 out = $0.47373 counted** — the
  null-content first attempt and its ≥7K re-run both inside that total.

## Failure modes to design around

- **Metered nulls at small budgets** — see the budget law above.
- **Long-call timeouts:** keep contributor calls small and batched; the two
  calls that hit the 60-second read cap returned nothing and no usage.
- **Dense-number extraction is the hardest shape** on this tier: it is the
  workload that emptied the largest budgets, and the one where the
  output-only prompt lead matters most.

Receipts, not claims: the full sweep record is
[`CONTRIBUTION-LOG.md`](CONTRIBUTION-LOG.md); every call's usage is in
[`NIGHT-LEDGER.md`](NIGHT-LEDGER.md).

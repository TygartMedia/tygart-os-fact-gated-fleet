# Wave 28 — Settlements: the oldest open list, closed by primary reads

*Wave 27's verdict pointed here: stop widening the audit and
settle the named backlog. This wave took the thirteen
NEEDS-VERIFY items left open by wave 1 — the program's first
audit, on its first day — and settled each against a primary
source read for the purpose. Full receipts: WO-1013.*

## The settlements

Eleven of the thirteen items were claims the pages had right
all along, unverifiable only because no sheet covered them
on the day they were flagged:

- **Legacy prices** — Opus 4.8 at $5/$25 and Sonnet 4.6 at
  $3/$15 per MTok: correct, per Anthropic's legacy model
  tables.
- **Retirement dates** — Opus 4 and Sonnet 4 retired June 15,
  2026: correct, per the deprecations page. Sonnet 4.5's
  November 30, 2026 date: correct as listed — with the
  recorded nuance that Anthropic labels forward dates
  tentative.
- **Legacy status** — Sonnet 4.6, Opus 4.7, Opus 4.6 classed
  legacy: correct.
- **The cache halving** — Sonnet 5.5 cache reads cut from
  $0.20 to $0.10 on October 7, 2026: correct, per the API
  release notes.
- **The SpaceX announcement** (May 6, 2026, read at
  anthropic.com): the Team doubling, the peak-hours reduction
  removed for Pro and Max, and the Tier 1 increases all check
  against the announcement itself — with one imprecision the
  fixer caught in the act of settling: the page's "1,500%"
  input figure. The announcement's table runs 30,000 to
  500,000 tokens per minute, a 16.7× rise; "1,500%" and its
  "15×" gloss were the desk's loose arithmetic. Post 8566 now
  states the before-and-after numbers in all three places the
  percentage appeared.

Two items were claims the pages had wrong — both on the
rate-limits page, in prose that survived wave 22's table
rebuild precisely because it was NV-flagged and untouchable:

- **Pro "~45 messages per 5-hour window"** and **Max
  "44,000–220,000 tokens per 5-hour window"**: Anthropic's
  current help center publishes no fixed message count and no
  per-window token figures — usage varies with message
  length, attachments, conversation length, and model, and
  the stated comparison is a multiplier (Pro is at least 5×
  Free per session). Both figures are replaced with that
  position, in the page's own voice.

And two were stale in detail on the models comparison: the
limited-availability model is **Mythos 5.1**, not Mythos 5,
and access runs through **trusted access programs** —
Project Glasswing, its original channel, merged into the
Cyber Verification Program in October. Both lines corrected.
The fixer confirmed the settlements, disputed one (the
1,500% arithmetic — upheld, above), and rewrote two edits;
Glint adopted the substance of both rewrites and kept the
page-shaped wording, with the adjudication on the receipts.

Eight edit operations across three pages, all live-verified.

## Diminishing returns — the required read

**Verdict: this method's returns held — and its fuel is now
spent.** The settlement method cleared in one wave a backlog
that had sat open through twenty-seven, because the items
were named, bounded, and each had a primary source that
exists. That is the whole recipe, and it does not generalize
past the backlog: the program's named-open list is now short
and specific — seven radon items that need a research
commission (primary sources unsettled at the points in
question, per wave 26), eight catalogue pages whose expected
yield wave 27 already priced at roughly one finding, and
housekeeping items (missing featured images) that are a
different work type entirely. More settlement waves would
have nothing to settle. The value frontier, as wave 27's log
predicted, is a new test class — which is what wave 29 is:
a seeded-trap red-team of this pipeline's own gate, designed
with Will and approved by him, asking not "is the site right"
but "would we catch it if it weren't."

## The cache ritual

| Probe | Packet | Gap | Intervening | Cached |
|---|---|---|---|---|
| A | Fixer, settlement packet (1,286-token prompt) | 709 s | 0 | 0 of 1,286 |

A miss inside the previous hit window, on by far the
smallest packet the ritual has used (prior probes ran
2,500–7,400 tokens). Two variables are confounded in this
single observation — elapsed time (709 s sits between the
669 s miss and the 743 s hit) and prompt size (every prior
hit cached a prompt of 2,500+ tokens). The log records the
miss and the confound; resolving which variable governs
needs a same-size probe pair, which a future wave can run
when a natural slot arises.

Usage: 2 calls, 24,532 tokens. Program ledger: 172 pages,
375 calls, 3,089,696 tokens, 170 edit operations (168 net
live). Card $0 — free credits; no cliff signals.

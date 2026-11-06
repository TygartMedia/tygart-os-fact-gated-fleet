# Wave 17 — Expansion step 3: the xAI jurisdiction

*Fired Nov 5, 2026 on Will's "Next." The xAI fact sheet, built the
same way as steps 1–2, closes the oldest deferral in the program:
wave 3's "~20 xAI claims await a verified xAI fact sheet." Full
receipts: WO-1002.*

## The sheet

Tier-1 harvest: xAI's own models and pricing documentation read
live (docs.x.ai — Grok 4.7 flagship, released September 21, 2026,
500k context, $2.00/$0.50/$6.00; 4.6 and 4.5 beside it; 4.3 and the
4.20 family at $1.25/$0.20/$2.50 on 1M; grok-build-0.1 at
$1.00/$0.20/$2.00; the 200k long-context doubling rule; voice and
Imagine rates; Grok-3 retired May 2026), plus the live catalog from
Will's xAI API account — 13 models. Consumer seat prices are
explicitly OUT of the sheet's scope; seat claims file as
NEEDS-VERIFY by design.

## The wave: one page fixed, two findings refused

- **16809 grok-vs-claude-pricing — the deferred half, settled.**
  Its Grok table and worked examples verified accurate against the
  new sheet (the 200k rule, the cached ranges, the batch scope all
  check out), with one real defect: the page never names Grok 4.7.
  Its flagship pairing still read "Grok 4.6." Two edits shipped —
  the pairing now names Grok 4.7 (same $2/$6 rates, so the page's
  math is untouched) and the rate-table row covers 4.5 / 4.6 / 4.7 —
  plus a dated lineage line recording the change, per fleet
  convention. The page's "Last verified: November 5, 2026" stamp,
  set this morning when its Claude half was verified in wave 3, is
  now true for both halves. One process note: the first edit batch
  aborted cleanly on a wrong find-string (the assert-before-write
  guard; nothing written), and the lineage insert needed the raw
  stored character where the rendered page shows an entity — both
  recovered inside the wave and recorded in the receipts.
- **14430 fleet-bots — the fixer refused, correctly.** The scout
  flagged the page's Grok-3 / Grok-3 Mini stack as contradicted
  (retired models). The fixer refuted both findings: the sheet
  proves retirement, but the page is a build blueprint describing
  the author's own assembled stack — naming what was built is a
  record, and the scout's proposed replacement asserted capability
  claims the sheet doesn't contain. Glint upheld both refutations.
  Zero edits; the retirement note stands in this log as an
  editorial-pass candidate, not a find-and-replace fix.
- **14429 pricing guide — a second refused restamp.** The scout
  proposed updating its "Page updated" line; the fixer refused:
  nothing on the page changed and parts of its scope (voice,
  imagine, tools) weren't sheet-verified. Upheld — the mirror of
  wave 16, where the same shape of stamp shipped because the
  verification it names had actually run. The pair contract earned
  its keep twice in one wave: both refusals were the fixer's, both
  were right.

## The widening, stated

Jurisdiction now: Anthropic (wave 1), Meta Model API (step 2), xAI
(step 3). The next widening question, queued: the two remaining
vendor territories with waiting carriers — **OpenAI** (the GPT half
of wave 15's comparison page is catalogued and waiting) and
**Google/Gemini** — each one sheet away. And one boundary the
program keeps meeting: consumer seat pricing has no sheet anywhere,
by design — it is volatile, store-dependent, and every page that
carries it already disclaims it. Whether to sheet it at all is a
question for a later step, asked openly rather than assumed.

Usage: 6 calls, 55,121 tokens (scouts 25,208; fixers 29,913).
Credit-equivalent ≈ $0.008. Card $0 — free credits; no cliff
signals. Pool per Will: $35.42 remaining.

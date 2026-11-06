# Wave 3 — ten wide, dials changed (WO-988)

**Nov 5, 2026 · 10 pages · 10 parallel contributor calls · 73,676 tokens · longest leg ~52 s**

Pages: `claude-release-history` · `claude-student-discount` · `history-anthropic` ·
`grok-vs-claude-pricing` · `puget-sound-playbook` (4,994 words) ·
`ai-visibility-llm-optimization-strategies` · `how-we-track-ai-citations` ·
`top-rated-ai-seo-services-small-businesses-test` ·
`ai-water-damage-puyallup-who-to-call` · `complete-restoration-operating-system`

**Dials changed from wave 2:** concurrency 5 → 10 · a mandatory NEEDS-VERIFY
section in every return (no more silent NO FINDINGS) · a recall checklist in
the contract (stale dates, missing Ultra, "Max 20x" phrasing, legacy models
presented as current, retired console domain) · packet push to the largest
remaining page.

## What happened

- **21 findings** landed on the four Claude-cluster pages; **20 edits shipped**.
  All four pages re-read live after publishing: every replacement present,
  every stale string gone — with one deliberate exception below.
- **Six pages received no edits and long NEEDS-VERIFY lists** (~140 claims
  catalogued across the wave, none edited). That is the contract working:
  local reporting, pricing for our own products, and xAI pricing are outside
  the fact sheet, so the legs catalogued instead of guessing.
- **Concurrency 10 held.** All ten legs returned clean structured output;
  the mandatory NV section appeared in all ten returns. The wave-2 deviation
  is fixed.
- **Packet push:** 4,994 words, no truncation. The ceiling is still unfound;
  it is above ~5,000 words.
- **Adjudication judgment call, on the record:** `claude-release-history`
  keeps one "23 September 2026" — a FAQ sentence recording what the models
  overview said *when it was read on that date*. It is a historical record,
  not a freshness claim, so it stays.
- **Partial resolution, also on the record:** the `grok-vs-claude-pricing`
  consumer table now names Max $100 and Ultra $200 in its seat cells, but no
  separate Ultra row was added. The xAI half of that page (~20 claims) sits
  in NEEDS-VERIFY until a verified xAI fact sheet exists.

## The edge this wave found — wpedit can eat a table

The first dry-run for the two table-heavy pages produced replacements whose
spans **crossed table-cell tags**. wpedit splices the replacement into the raw
span, so a cross-cell edit collapses four cells into one: the structure check
caught cell counts falling 48 → 42 and 27 → 25 in the dry-run output. **None
of it published** — the dry-run discipline is what the press was built for,
and this is the receipt.

Fixes applied in-wave: every table edit rewritten as a per-cell edit contained
in a single text node, and wpedit's `context` semantics pinned down the hard
way (the context string must *contain* the find and occur exactly once in the
page — two dry-run aborts taught that). Re-run: all 20 edits matched exactly,
structure counts identical before and after (48/48, 27/27), then published
and QC'd live.

**Standing guard from this wave:** no edit whose dry-run crosses a tag ships
until the output passes a structure count against the original. Crossed
*inline* tags inside one text run are the only exception, and even those get
read before they ship.

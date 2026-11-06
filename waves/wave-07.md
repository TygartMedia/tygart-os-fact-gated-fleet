# Wave 7 — the restamp rule, at coverage width (WO-992)

**Nov 5, 2026 · 10 pages · 20 contributor calls (scout + fixer pairs) · 154,204 tokens**

**Dials:** (1) the **restamp rule** — a "Last verified" restamp may be emitted
or confirmed only when the audit actually verified the page's substantive
claims; an all-NEEDS-VERIFY page earns no restamp. (2) Width doubled to 10
pages: two dated pulses (guard regression), a dated Cursor news note, the
AEO reporting guide, the shared-brain essay, a date-dense methods page, the
last Claude-Notion leftover, and the three largest unworked essays in the
deep pool (3,424 / 3,049 / 2,414 words).

## Results

- **The guard held at width.** Both Oct 2 pulses classified DATED-RECORD by
  both legs, zero findings, their dates stand. Across 10 pages the pair
  produced exactly **one finding** — and **zero restamp findings**, the class
  that survived in both waves 5 and 6. The restamp rule, so far, is doing
  what fixer judgment alone did not.
- **The one finding was the boundary case.** The Cursor note (Oct 13) says
  "Claude seats did not move. Pro remains $20/month or $17 annual. Max 5x is
  $100, Max 20x is $200," closing with "as of October 13, 2026." Both legs
  read it as current claims and confirmed the correction. Glint shipped it,
  on a test now written into the log: **era-scoping must live in the claim
  sentence itself** (as the September 22 record page does — "as named on the
  September 22 table"), not only in a page-level dateline. The note's
  sentence was unscoped present tense; a November reader would take a dead
  tier as fact. Edit shipped: "Max is $100 (5x Pro usage); the $200 tier is
  Ultra (10x Pro weekly)." The Cursor reporting — the note's actual record —
  is untouched.
- Everything else catalogued: ~134 NEEDS-VERIFY claims across the AEO guide,
  the essays, and the Tacoma power guide, none in fact-sheet territory, none
  edited. Nine pages verified untouched by modified stamp.

## Infrastructure note

One fixer call failed to parse (the retired-living page) and was re-fired
successfully — 21 attempts, 20 metered calls. Failure count for the
program: 3, all recovered on re-fire.

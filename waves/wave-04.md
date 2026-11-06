# Wave 4 — the trio test (WO-989)

**Nov 5, 2026 · 5 pages · 15 contributor calls (3 legs × 5 pages) · 97,724 tokens**

Pages: `claude-opus-5-5-release` · `claude-sonnet-5-5-release` ·
`claude-code-cloud-sessions-credit` · `claude-design-standalone-closes-december-14-migration` ·
`claude-for-ecommerce-business-owners-guide`

**Dial tested:** waves 1–3 ran one audit leg per page, with Glint adjudicating.
Wave 4 runs the full **trio** on every page — a SCOUT audits, a FIXER attacks
the scout's findings (confirm / refute / rewrite, plus a miss sweep), and an
ADJUDICATOR leg issues the final ship list — before Glint's own check.

## What happened

Scouts returned 9 findings and 1 title proposal. The chain then did the thing
it exists to do:

- **The fixer killed a bad finding before it reached the publisher.** On the
  cloud-sessions credit page, the scout proposed replacing a stale "last
  call" line with precise promo deadlines — drawn from the page's own text,
  not the fact sheet. The fixer refuted it ("Promo dates absent from fact
  sheet"), the adjudicator struck it and the scout's title proposal with it.
  In waves 1–3, that class of overreach traveled all the way to Glint.
- **8 edits shipped** from the adjudicators' lists, all verified by Glint
  against the fact sheet first: two stale verified-dates, Haiku 5.5's
  "coming soon" (it launched October 7), the Sonnet 5.5 cache-read price in
  two more places ($0.20 → $0.10), and a countdown corrected by arithmetic
  (December 14 is 39 days out, not 56).
- **The miss sweep found nothing.** Fixers added zero NEW findings across
  five pages — on this page set the scouts' recall was already clean, so the
  trio's discovery value measured zero and its value was all adversarial.
- Residual NEEDS-VERIFY: ~120 claims catalogued, none edited.

## The follow-up — the struck item, settled properly, and a guard broken

The struck credit item was true-but-unverified, so after the wave Glint
verified the promo against sources citing Anthropic's own Help Center:
claim window closed Oct 7, 2026; claimed credit expired Nov 4, 2026. With
facts in hand she finished the page — 3 tense edits and a past-tense title.

**And broke the wave-3 guard doing it.** The follow-up edits' dry-run showed
spans crossing `<strong>` tags — the exact flag the guard exists for — but
the publish was chained in the same command as the dry-run, so it shipped
before the output was read. Result: three bold tags eaten, one left
unclosed, caught on the post-publish structure count (strong tags 13/14
against a 16/16 baseline), repaired by hand within minutes, and re-verified
live (15/15 balanced — the missing pair belonged to deleted text). The page
is correct; the process failure is the finding. **New rule, harder than the
old one: a dry-run and its publish never share a command. The dry-run output
gets read, by itself, first.**

Housekeeping, same as waves 2–3: the three release/credit pages had no
featured image; all three now do.

## Cost accounting — trio vs single leg

| | Tokens | Per page | Notes |
|---|---|---|---|
| Wave 3 (single leg, 10 pages) | 73,676 | ~7,400 | Glint adjudicates everything |
| Wave 4 (trio, 5 pages) | 97,724 | ~19,500 | Scouts 40,835 · Fixers 34,238 · Adjudicators 22,651 |

The trio costs ~2.6× per page. What it bought: one overreach killed inside
the chain, ship lists that arrived pre-verified (Glint's adjudication
dropped to a spot-check), and nothing measurable on discovery. **Working
conclusion:** single-leg by default; bring the trio — or at least the fixer
leg — for pages dense with prices, dates, and deadlines, where an inventive
replacement is the expensive failure.

# Wave 5 — the fixer-alone test (WO-990)

**Nov 5, 2026 · 5 pages · 10 contributor calls (scout + fixer pairs) · 65,140 tokens**

Pages: `restoration-technology-market-2033-test` (85 table cells, the pool's
densest price page) · `meta-model-api-pricing` · `sonnet-5-list-price-september-22-2026` ·
`smb-claude-notion-workflows` · `claude-vs-the-field`

**Dial tested:** wave 4's trio minus the adjudicator leg. Scout audits, fixer
attacks, and Glint adjudicates alone, as in waves 1–3. The question: does the
fixer's kill rate hold without the third leg, and at what cost?

## Cost first

65,140 tokens for 5 pages ≈ **13,000 per page** — about **67% of the trio's**
19,500, not the half we hypothesized. The fixer leg re-reads the full packet,
so the second leg is not cheap. Against the single-leg waves (~7,400/page),
the pair costs ~1.8×.

## Where the fixer held — 4 of 5 pages

- **The subtlest catch of the run:** on `meta-model-api-pricing`, the scout
  flagged "Last verified: October 19, 2026" as stale. The fixer **refuted**
  it — the fact sheet covers Anthropic, not Meta, so restamping the date
  would assert a verification nobody ran. A false freshness claim, killed.
- The market-study page (our own Monte Carlo dataset) and the Notion
  workflows page: no findings, ~46 claims catalogued NEEDS-VERIFY, untouched.
- `claude-vs-the-field`: one verified-date restamp, confirmed, shipped, QC'd.
  **The wave's only edit.**

## Where the pair failed — named, as commissioned

`sonnet-5-list-price-september-22-2026` is a **dated-record page**: its
premise is what Anthropic's pricing table said *on September 22, 2026* — the
date is its content. Both legs read it as a current-claims page. The scout
produced four findings and a title proposal; **the fixer confirmed all of
them**, and all of them reached Glint, who struck every one:

- **F1** — restamping "Last refreshed" on a record whose date is the point.
- **F2** — restamping the content claim "Checked September 22, 2026," with a
  replacement carrying a source path the fact sheet never gave it.
- **F3 / F4** — "correcting" the seat line the page recorded that day
  ("Max 20x $200"), which the page itself already era-scopes.
- **TITLE** — retitling the record "…(November 5, 2026)," rubber-stamped by
  the fixer's title check.

**Diagnosis:** the two legs share one contract, so they share its blind
spot. A third leg reading the same contract would very likely share it too —
this failure prices a *contract* gap, not a missing leg. The fix is a
page-class guard: when a page is a dated record (date in its title or slug,
a "checked on" premise), date restamps and corrections of era-scoped claims
are REFUTE-by-default.

## Infrastructure note

Two contributor calls failed outright (API errors, no usage returned) — both
on the same page, one per leg — and were re-fired successfully. The first
failed calls in five waves; they are counted here, not in the token total.

## Standing items

Four pages verified untouched by modified stamp after the run. Pages 18480
and 20434 have no featured image — pre-existing, logged, and deliberately
left alone this wave: untouched was the datum.

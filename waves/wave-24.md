# Wave 24 — Expansion step 10: the comparison, rebuilt

*Fired Nov 5, 2026 on Will's "Next." The Claude-vs-GPT-5 page
(14045) — struck twice for wearing an October snapshot under a
refresh stamp — gets the real fix. Full receipts: WO-1009.*

## The class decision

The page is a 436-word comparison card whose title promises a
current answer, whose Claude half was already verified, and
whose only stale layer was OpenAI's. Nothing on it is
intrinsically a dated record. **It is now a living comparison**,
verified end to end on November 5, 2026, carrying an update
lineage on its face: first published Aug 19, 2026; Oct 20,
2026 Claude refresh with OpenAI rows carried as flagged
October 1 figures; Nov 5, 2026 full rebuild. No October data
stands under the November stamp unexamined — every data claim
on the page was inventoried by an EXTRACT leg (33 items) and
each maps to verified, corrected, or named-unsettled below.

## The rebuild (draft → claim-check, wave-13 discipline)

The DRAFT leg produced the replacement data layer as 35
numbered claims, every one with a verbatim SOURCE quote from
the two vendor sheets. The CLAIM-CHECK leg confirmed **35 of
35** — zero refuted, zero unsupported. Glint assembled and
shipped 13 text edits plus a structural patch:

- **gpt-6-astra added** as OpenAI's current flagship row
  ($10/$50, cache read $1.00) — the comparison previously led
  its OpenAI side with a deprecated model.
- **GPT-5 marked deprecated everywhere it appears**, with its
  December 11, 2026 shutdown date (table row, intro, body).
- **gpt-6.1-sol's row rebuilt**: the vague "(Oct 1 figure)"
  long-context note is now the actual band rule — prompts over
  272K tokens bill at $4/$15 for the whole request — plus its
  $0.10 cache read.
- **Legacy context figures corrected from the sheet**: Sonnet 5
  and Opus 5/4.8 rows carried 1M-token context; the current
  Anthropic sheet puts the still-available legacy generation at
  200K. Both cells corrected.
- Every October caveat ("not re-verified on this pass," "not
  re-read today," "October 1 figure") removed — they are now
  lineage, in the update-history block, where history belongs.
- **One item named unsettled**: Sonnet 4.6's context cell. The
  current sheet does not state it, so the page's existing 1M
  figure stands unedited and unendorsed — flagged here rather
  than silently carried or silently changed.

## The cache ritual — the window, bisected

| Probe | Packet | Gap | Intervening calls | Cached |
|---|---|---|---|---|
| 1 | Draft (14045 + both sheets) | 522 s | 1 | 0 of 2,657 |
| 2 | Claim-check (draft + both sheets) | 800 s | 0 | **4,323 of 4,386 (98.6%)** |

Probe 2 was scheduled for ~900 s; its sleeper process was
killed by a runtime restart and the probe was re-fired on
recovery at a true measured gap of 800 s — reported as
measured, not as planned. The full ritual record now reads:
zeros at seconds, 146 s, 343 s, 370 s, and 522 s; hits at
463 s (wave 23, 2,531 of 2,565) and 800 s (4,323 of 4,386).
Two honest complications. First, tonight's 522 s miss against
wave 23's 463 s hit kills any clean time threshold below
~800 s. Second, wave 23's hit has a confound tonight's lacks:
its packet shared a long contract prefix with nineteen sibling
packets fired in the same window, so its cache may have been
warmed by its own batch. Tonight's 800 s hit had zero
intervening calls — the cleanest long-gap data point yet, and
it hit at 98.6%. The working picture: near-total prompt
caching that engages on a timescale of many minutes, possibly
helped by similar traffic, definitely not on the seconds-to-
~500 s timescale the ritual spent seven pairs exploring. The
bisection continues from the 522–800 s interval.

Usage: 5 calls, 57,269 tokens (draft 18,608; extract 6,153;
draft re-send 10,684; claim-check 10,563; claim-check re-send
11,261 — both re-sends counted). Program ledger: 159 pages,
346 calls, 2,821,058 tokens. Card $0 — free credits; no cliff
signals.

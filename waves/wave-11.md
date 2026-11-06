# Wave 11 — the timeout hunt (20 pages)

*Fired Nov 5, 2026 under Glint's standing commission. Designed as the
last coverage wave (width 20, scout + fixer pairs, settled contract);
it became the program's root-cause hunt for its recurring call
failures. Full receipts: WO-996.*

## Result

- **Shipped: 14 edits on 2 pages.** 11324 (Fable 5 guide): header and
  lineup-update stamps to November 2026, Sonnet 5 → 5.5 and Haiku 5.5
  added to the currency sentences (×2), the flat "cache read is 90%
  cheaper across all models" replaced with the true tiered rates.
  9822 (API key guide): both freshness stamps re-earned to Nov 5,
  2026; console.anthropic.com replaced as the stated destination in
  nine places (body + FAQ schema kept in agreement); the "Pro or Max
  grants no API credit" claim replaced with Max $100 / Ultra $200
  monthly API credits; the Sept-2026 API list replaced with the
  current four (×3).
- **Residue, named:** 11324's June-2026 lineup tables, calculator, and
  Fable-vs-Opus-4.8 FAQ stand as the guide's dated core (its own
  sentence labels the tables June 2026); 9822's June pricing-tiers
  table keeps its honest June heading — the fixer's proposed retitle
  was struck, because a fresh date over a stale table is a lie with
  better typography. ~200 NEEDS-VERIFY items catalogued, untouched.
- **18 of 20 pages verified untouched** after the fact.

## The breakage — and the fix

Wave 11's two finding-page fixers failed, then failed 3 retries each,
then failed a terse-output variant: **11 failed attempts, all on the
only two pages with findings.** Bisection isolated it: a control ping
returned instantly; a trivial word-count task on one page's text alone
timed out. The error, read in full at last, was a client read-timeout:
the connector's hardcoded **60 seconds**. The discriminating test —
the same call at a 300-second timeout — landed in 2m15s with
`finish_reason: stop` and **22,885 of its 22,896 completion tokens
spent on hidden reasoning** to produce an 11-token answer. Dense,
instruction-and-price-laden page content makes the contributor tier
reason at extreme length; the generation is healthy, the client's
patience was not. Retries failed deterministically because the cause
was in the content, not the network.

**Fix, shipped:** the connector's chat timeout is raised 60 → 300
seconds (a disclosed change to Will's own tooling, made by Glint
during this wave). Both stuck fixers then landed on their first
attempt. Standing lessons: a failed call's error text is evidence —
read it before re-firing; never retry an unchanged packet against a
deterministic failure; per-attempt tokens on timed-out calls are
unmetered by the API response, so the wave's true consumption is its
metered total plus 11 burned attempts.

## Process catches inside the wave

- wpedit's assert-before-write refused three wrong occurrence counts
  across the two pages (dry-run truth beats the editor's guess, every
  time).
- The first 9822 dry-run caught a cross-tag splice — a find spanning a
  link and two bold segments would have eaten four tags; restructure
  (context-scoped single-node edits + one byte-exact raw anchor patch
  for the href) shipped instead. Dry-run and publish never shared a
  command.
- The page's rendered view shows one paragraph twice; its stored
  content holds it once (render-time duplication) — the patch targeted
  the stored source, verified in raw.

## Usage (exact)

42 metered calls, 329,885 tokens (scouts 165,199; fixers 164,686,
including the two post-fix returns at 17,991 and 13,122). Plus one
diagnostic call at 26,027 tokens (the 300-second bisect) and 11
unmetered timed-out attempts. Credit-equivalent ≈ $0.05 at listed
contributor rates. Card charged $0 — free credits; no cliff signals.

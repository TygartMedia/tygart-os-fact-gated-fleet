# Wave 2 — wpedit at scale (WO-987)

**Nov 5, 2026 · 5 pages · 5 parallel contributor calls · 28,118 tokens · ~35 s wall-clock**

Pages: posts 18844 · 18809 · 18878 · 17303 · 19801 (Tygart Media)

**Dial tested:** wave 1's hand surgery replaced by wpedit as the standard edit
path — plus one deliberately long page (4,701 words) to probe packet limits.

## What happened

8 edits shipped across three pages (the "$200 Max" family again, a stale
verified-stamp, lineup rolls). Two pages correctly received **no edits**: one is
dated history on its face, and the long page's claims sit outside the fact
sheet, so nothing on it could honestly be called stale.

- **wpedit held at scale — zero friction.** 8 edits, 8 dry-runs matched exactly,
  no aborts. Wave 1's bottleneck is gone.
- **The long page did not break.** 4,701 words in a single packet, coherent
  structured reply, no truncation. The packet ceiling is somewhere above
  that — still unfound.
- **Precision perfect, recall soft.** Every returned finding was true, and both
  "no findings" calls were right — but the legs missed three same-class items
  their own fact sheet covered (a stale verified-stamp, Ultra missing from a
  seat ladder, a stale answer-block date). Adjudication caught all three.
  Conclusion: a wave's real cost is not contributor time, it's adjudication time.
- **One contract deviation:** on the out-of-scope page a leg answered
  NO FINDINGS instead of listing what it couldn't verify. Nothing was lost,
  but silence is not a verdict — that became a wave-3 dial.
- Housekeeping logged, not fixed in-wave: posts 17303 and 19801 have no
  featured image.

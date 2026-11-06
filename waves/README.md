# The Waves — the hackathon after the hackathon

The submission closed on November 4, 2026. The experiment didn't.

Starting November 5, we run the fact-gated fleet pattern **live, against our own
production site** (tygartmedia.com), in waves — and publish what each wave found,
including the failures, as it happens. This directory is that running log.

## What a wave is

1. **Pick N live pages** and one thing to test (a dial to change on purpose).
2. **Fan out**: one Muse Spark 1.3 contributor leg per page, in parallel. Each leg
   gets the page text plus a fact sheet verified that day against Tier-1 sources,
   and a strict contract: return findings only, as
   `CLAIM | VERDICT | REPLACEMENT | BASIS`, max 12 — and say NEEDS-VERIFY instead
   of guessing. From wave 3, every leg must also file an explicit NEEDS-VERIFY
   list, even when it finds nothing.
3. **Adjudicate**: Glint checks every finding against the sources herself. Legs get
   overruled when the evidence says so, and the log says when that happens.
   NEEDS-VERIFY claims are never edited.
4. **Edit through wpedit**, a text-layer press that maps plain-text edits into the
   stored HTML. Every edit runs as a dry-run first: it must match exactly its
   declared count and pass a structure check, or nothing writes.
5. **Publish and QC live**, then log the wave here — exact token usage included.

## Rules of the run

- **Our site only.** If something breaks, it breaks on us.
- **Exact ledger, no gaming.** Every contributor call and its token count is
  recorded. Nothing is padded.
- **Receipts over claims.** Word counts are measured, pages are re-read live
  after publishing, and a wave isn't done until its log entry is written.

## Ledger

| Wave | Date (PT) | Pages | Contributor calls | Tokens | Edits shipped | Held / catalogued |
|------|-----------|-------|-------------------|--------|---------------|-------------------|
| [1](wave-01.md) | Nov 5, 2026 | 5 | 5 | 42,226 | 31 findings shipped | 13 NEEDS-VERIFY untouched |
| [2](wave-02.md) | Nov 5, 2026 | 5 | 5 | 28,118 | 8 | 3 misses caught in adjudication |
| [3](wave-03.md) | Nov 5, 2026 | 10 | 10 | 73,676 | 20 | ~140 claims catalogued NEEDS-VERIFY, none edited |
| [4](wave-04.md) | Nov 5, 2026 | 5 | 15 (trio) | 97,724 | 8 (+3 follow-up) | 1 finding refuted inside the chain; ~120 claims catalogued |
| [5](wave-05.md) | Nov 5, 2026 | 5 | 10 (pairs) | 65,140 | 1 | 6 items struck by Glint on one dated-record page; 2 API calls failed and were re-fired |
| [6](wave-06.md) | Nov 5, 2026 | 5 | 10 (pairs) | 73,496 | 0 | Guard held on the dated record; 1 bare restamp struck by Glint |
| **Running total** | | **35** | **55** | **380,380** | | |

Model: `muse-spark-1.3-contributor` via the Meta Model API, under a $25 test
envelope. Adjudication, editing, publishing, and this log: Glint, running the
lane described in the submission — no desktop takeover, everything in the
background, receipts for everything.

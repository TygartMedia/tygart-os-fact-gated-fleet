# The UCP Waves — the fleet turns on the protocol's own site

The [TM waves](../waves/README.md) ran the fact-gated pattern against
tygartmedia.com. On November 6, 2026 the same program opened a second front:
**theuniversalcommerceprotocol.com** — our own explainer site for the Universal
Commerce Protocol, 747 published URLs, untouched since October 7, 2026. The
working plan runs ~22–26 waves to take the whole site to a finish line.

This directory is that program's running log, published as it happens,
failures included — same rule as the TM waves.

## How a UCP wave works

1. **Earn the fact sheets first.** Before any page is judged, contributor legs
   extract the governing primary sources (the UCP spec, the AP2 repo, Google's
   platform docs, the payment networks' own pages) into dated fact sheets.
   Pages are judged against the sheets, never against a leg's memory.
2. **Name the unjudgeable in advance.** [UNJUDGEABLE.md](UNJUDGEABLE.md) lists
   the claim classes no sheet can settle (market numbers, predictions,
   first-person test anecdotes, circular self-citation, and six more). Claims
   in those classes route to NEEDS-VERIFY mechanically — they are never
   silently edited and never silently deleted.
3. **Plan, then write.** Each duplicate cluster gets a PLAN leg (judge the
   bodies against the sheets, rule MERGE or REFUTE, name the canonical) and a
   WRITE leg (produce the merged body). Legs run on
   `muse-spark-1.3-contributor` via the Meta Model API, orchestrated
   Glint-direct from Glint's VM — same topology as the TM waves.
4. **Stage-only until the taps.** Legs read public pages and stage files.
   Nothing touches the live site until Will taps the redirect map (Tap 2) and
   the publishing batch (Tap 3).
5. **Verify on the file, not the report.** Every staged result is checked
   against the staged file itself (greps, diffs, word counts) before it is
   called done.

## The engine is the second experiment

The refresh is real, but the learning is a deliverable in its own right: this
program is also a field test of Muse Spark 1.3 contributor — where it works,
where it hits caps, retries, and failure shapes — logged with the same honesty
as the site work. The probe that reshaped the program is filed as the appendix:
[SPARK-PROBE-FINDINGS.md](SPARK-PROBE-FINDINGS.md). Its headline correction is
ours, not the model's: **the "8,000-token API cap" in our standing record was
our own call setting, not a Meta limit.** Phase 0b's deterministic empty
responses were reasoning burning a self-imposed budget. The probe verified the
`reasoning_effort` dial (our hackathon-era rejection was a wrong parameter
name), generated 15,173 tokens in a single contributor call, and produced the
operating rules every later leg runs under.

## The run so far — November 6, 2026

- **Phase 0a — Census.** All 747 URLs frozen and measured: median post 1,601
  words; 15 stubs, all in one June block; 362 URLs with zero inbound links
  from article bodies; ~32 duplicate-collision clusters, zero closed since the
  October 23 map. [CENSUS.md](CENSUS.md) ·
  [CLUSTER-MAP-V2.md](CLUSTER-MAP-V2.md)
- **Phase 0b — Fact sheets.** Six sheets earned from primary sources, plus
  the unjudgeable classes. The phase's engine data is the finding: 15 calls,
  79,373 output tokens, ~80% of output burned on reasoning, and the
  empty-response failure reproduced deterministically — twice at a 5,000 cap
  (reasoning 4,998/5,000 → zero visible characters, identical counts), again
  at 8,000 on a long enumeration. [PHASE-0B-LOG.md](PHASE-0B-LOG.md)
- **The Spark probe (evening pivot).** Will redirected the evening from the
  site to the model itself. 19 probe calls: the dial, the cap correction, the
  plan→write shape verified end-to-end. [SPARK-PROBE-FINDINGS.md](SPARK-PROBE-FINDINGS.md)
- **Wave 1 — Consolidation, first tranche.** 10 duplicate clusters, 20 legs,
  20 MERGE verdicts, 10 staged bodies, 188 NEEDS-VERIFY items. The probe fix
  held cleanly: 20/20 first-try finishes, reasoning share down from 79% to
  44%. The wave's one real defect was ours, not a budget failure: the E3
  write leg compressed an opinion essay to a 261-word skeleton by applying a
  factual-claims exclusion rule to claims its plan had routed as the author's
  voice. Will ruled the claims ride as opinion (17:16 PT); one corrective leg
  rebuilt the piece at 936 words, verified on the file.
  [WAVE-1-BRIEF.md](WAVE-1-BRIEF.md) · [WAVE-1-LOG.md](WAVE-1-LOG.md)
- **Gap sheets 7–8 + re-judgment.** Wave 1's NEEDS-VERIFY pile was mostly
  sheet gaps, so the next spend earned the missing law before any more
  merging. Sheet 7's verdict: **no published UCP rate limits exist at all** —
  every tier, header family, and SLO number on the site was invented; all cut.
  Sheet 8's verdict: UCP identity is profiles and `keys[]`; there is no DID
  or blockchain layer in the spec; every such attribution cut or relabeled
  "not UCP." Of 87 re-judged items: 1 settled as keepable fact, 15 ride
  relabeled, 44 cut, 27 remain unjudgeable.
  [GAP-REJUDGE.md](GAP-REJUDGE.md)
- **Mechanical passes.** The ruled cuts, reframes, E5's component-list
  replacement, and E1's authentication correction executed on the staged
  bodies: 5 legs, 5 PASS, zero corrective re-runs, every result grep-verified
  on the file before overwrite. After these passes, nothing content-side in
  Wave 1 blocks publish. [MECH-PASSES-LOG.md](MECH-PASSES-LOG.md)
- **Wave 1 publish — complete (evening).** Ten bodies published live
  17:42–18:00 PT through Will's own signed-in browser admin session, each
  verified on its live public URL. The site had no redirect manager, so on
  Will's 18:01 PT tap the free Redirection plugin (v5.10.1) was installed;
  **17 of 17 redirects** were created (301, enabled) with 5 of 5 verification
  visits passing, and stub post 7261 was moved to Trash. Full receipts: the
  publish addendum at the end of [WAVE-1-LOG.md](WAVE-1-LOG.md).
- **Wave 2 — Consolidation, second tranche.** 10 units judged from the
  candidate scan, 23 legs (F3's two-canonical split took three): **10 of 10
  MERGE verdicts, 0 KEEP-DISTINCT**, 11 staged bodies, 186 NEEDS-VERIFY
  items. Both pair-reads convicted on the bodies, and one canonical flipped
  on body evidence — the SDK pair's canonical moved from 5780 to 5781, the
  superset. Engine: 23 of 23 calls clean on the first try, reasoning share
  41%. Two writes needed one corrective leg each (compression, then an
  overshoot accepted only after a 15-term NEEDS-VERIFY spot-check read zero
  hits). [WAVE-2-BRIEF.md](WAVE-2-BRIEF.md) · [WAVE-2-LOG.md](WAVE-2-LOG.md)
- **Wave 2 publish — complete (evening).** Eleven bodies published live
  18:39–18:59 PT on Will's tap (same disclosed temporary-snippet method as
  Wave 1, snippet deleted after), each verified on its live public URL —
  including 5748's illustrative-examples notice, visible under its title,
  and 1256's full ~2,963-word body. **17 of 17 redirects** created
  (Redirection total now 34), 5 of 5 verification samples passing. The
  internal-link retargeting deferred from Wave 1 closed in the same run:
  across all 738 published posts, the old 6030 URL's hrefs went 14 → 0 and
  the old 4266 URL's went 7 → 1, the residual being a JSON-LD "url" field
  in post 4266's own body — not a link, left unchanged under an
  href-only authorization, and harmless behind its Wave 1 301. Full
  receipts: the publish addendum at the end of [WAVE-2-LOG.md](WAVE-2-LOG.md).

## Ledger

Every contributor call is recorded in [calls.jsonl](calls.jsonl) — this
table is that file, counted.

| Stage | Calls | Input | Output |
|---|---|---|---|
| Phase 0b (sheets 1–6) | 15 | 37,702 | 79,373 |
| Wave 1 (incl. E3 corrective) | 21 | 213,775 | 96,539 |
| Gap sheets 7–8 + re-judgment | 6 | 8,147 | 19,394 |
| Mechanical passes | 5 | 30,456 | 26,013 |
| Wave 2 (incl. 2 corrective writes) | 23 | 338,392 | 132,078 |
| **Program to date** | **70** | **628,472** | **353,397** |

(The Spark probe's 19 calls were a separate battery, counted in its own
findings file.) Cost: contributor-tier pricing is not established on this
program's record, so no price is printed rather than an invented one. Every
signal so far reads **$0 charged** against the $25 test envelope that governs
the account.

## The sheets

The law the waves judge against — earned 2026-11-06, 14-day half-life (no
wave fires on them after November 20 without a re-earn pass):

1. [UCP Core Specification](sheets/SHEET-1-ucp-core-spec.md) — pins spec
   v2026-08-25 against the 2026-04-08 version Google's surfaces still teach
2. [AP2 (Agent Payments Protocol)](sheets/SHEET-2-ap2.md)
3. [Google Platform](sheets/SHEET-3-google-platform.md) — carries the
   RFC 9421 ES256 signature-authentication rules that replaced the old
   header method in late October 2026
4. [Commerce Platforms](sheets/SHEET-4-commerce-platforms.md)
5. [Payment Networks](sheets/SHEET-5-payment-networks.md)
6. [Adjacent Protocols](sheets/SHEET-6-adjacent-protocols.md)
7. [Rate Limits & Performance](sheets/SHEET-7-rate-limits.md) — the empty
   set, documented: no published UCP rate limits exist
8. [Identity vs DID](sheets/SHEET-8-identity-did.md)

## Status — as of the evening of November 6, 2026

**Wave 1 is fully complete on the live site.** Bodies published and verified
live (17:42–18:00 PT, via Will's own signed-in browser admin session — the
programmatic app-password lane remains unverified and was not needed), the
Redirection plugin installed on Will's tap, 17 of 17 redirects live, and
stub post 7261 in Trash. Wave 1 publish receipts are recorded in the
addendum at the end of [WAVE-1-LOG.md](WAVE-1-LOG.md). Count correction:
earlier text in this record said 19 source URLs; the executed redirect map
was **17 unique redirects** — posts 1949 and 1618 had been double-counted.

**Wave 2 is also fully complete on the live site** — staged, published, and
redirected the same evening (receipts in the addendum at the end of
[WAVE-2-LOG.md](WAVE-2-LOG.md)), and the internal-link retargeting deferred
from Wave 1 is closed with it. Program ledger to date: **70 calls, 628,472
input / 353,397 output tokens, $0 charged, contributor pricing still
UNVERIFIED.** Waves 1 and 2 together convicted 20 clusters covering ~56
pages; what remains in the corpus is mostly stubs, news pairs, and
singletons, so Wave 3 — when Will fires it — is a different kind of work
(build-outs and dated-item judgment), not another merge wave of this shape.

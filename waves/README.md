# The Waves — the hackathon after the hackathon

The submission closed on November 4, 2026. The experiment didn't.

Starting November 5, we run the fact-gated fleet pattern **live, against our own
production site** (tygartmedia.com), in waves — and publish what each wave found,
including the failures, as it happens. This directory is that running log.

## Runtime architecture — note added Nov 5, 2026

The wave program documented here runs Glint-direct from Glint's VM.
Glint is a Meta Muse — Meta's personal-agent model — running on her
own Linux VM. From that VM she builds the packets, adjudicates the
returns, runs the wpedit edit path, renders PDFs, publishes to
tygartmedia.com through the WordPress REST lane, and pushes these
logs. The contributor inference runs on the Meta Model API
(dev.meta.ai): the legs are `muse-spark-1.3-contributor` chat calls
issued from the VM. No wave compute runs on Will's laptop.

That was not always the topology. The hackathon-era builds and the
early work orders went through other seats and routes — executor
seats on the laptop, hand-fired Antigravity runs among them. The
waves didn't start off on Glint's VM; the wave program as documented
in this directory is the Glint-direct era. Earlier logs are
unchanged: this note dates the transition rather than rewriting it.

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

## Program note — Nov 5, 2026, evening: the cache ritual

Will's dashboard tonight reads the account cache rate at over 6.2%
(up from the 3.4% baseline wave 14 was commissioned against) and
the free-credit balance at $35.34. Standing method from the next
wave on: every expansion wave runs a paired cache measurement
twice — one regular (cold) call on a real wave packet, then the
identical packet re-sent unchanged and sequentially (the
genuine-repeat pattern wave 14 proved is the only thing that
hits). Each wave's log carries the pair table: cold vs cached
latency, cached tokens read, % of prompt served from cache, and
the token/time savings across both pairs. Energy, when mentioned
at all, appears only as a labeled estimate derived from the
measured savings — it is not directly measurable from here and is
never reported as a metered figure.

## Program note — Nov 5, 2026, 17:35 PT: the pivot to experiment-first

Waves 1–11 mixed two jobs: auditing the site and testing the pattern.
From wave 12 on, the program is **testing only** (Will's direction): the
site is the testbed, not the goal. Coverage counts no longer headline
these logs. Each wave is an experiment — a named question, a dial pushed
until something strains or breaks, then the fix — written up as
hypothesis, method, breakage, fix, verdict. Fixes still ship when real
findings earn them; a wave that breaks something and teaches us the fix
outranks a wave that catalogues ten clean pages.

## Program note — Nov 5, 2026, 18:36 PT: the arc from here

Will's direction for what follows the current experiments:

1. **Finish the experiment tier** — one or two more waves at most.
   The live candidates are the flakiness root-cause work and the
   cache test. The PDF decomposition result stands as proven method,
   not the ongoing line.
2. **Reset to the base core** — the plain QC loop: fact-gated audit
   plus surgical verified edits, the wave 1–3 pattern, as home base.
   Not the PDFs.
3. **Expand incrementally from there** — each wave widens the scope
   one step beyond the last (more of the site, new clusters, new page
   classes as fact sheets earn jurisdiction), watching how far out it
   can go before something strains.
4. **Infrastructure as the expansion demands it** — routers and other
   machinery enter only when a wave shows the need, never ahead of
   it. Each wave leaves behind whatever the next width requires.


| Wave | Date (PT) | Pages | Contributor calls | Tokens | Edits shipped | Held / catalogued |
|------|-----------|-------|-------------------|--------|---------------|-------------------|
| [1](wave-01.md) | Nov 5, 2026 | 5 | 5 | 42,226 | 31 findings shipped | 13 NEEDS-VERIFY untouched |
| [2](wave-02.md) | Nov 5, 2026 | 5 | 5 | 28,118 | 8 | 3 misses caught in adjudication |
| [3](wave-03.md) | Nov 5, 2026 | 10 | 10 | 73,676 | 20 | ~140 claims catalogued NEEDS-VERIFY, none edited |
| [4](wave-04.md) | Nov 5, 2026 | 5 | 15 (trio) | 97,724 | 8 (+3 follow-up) | 1 finding refuted inside the chain; ~120 claims catalogued |
| [5](wave-05.md) | Nov 5, 2026 | 5 | 10 (pairs) | 65,140 | 1 | 6 items struck by Glint on one dated-record page; 2 API calls failed and were re-fired |
| [6](wave-06.md) | Nov 5, 2026 | 5 | 10 (pairs) | 73,496 | 0 | Guard held on the dated record; 1 bare restamp struck by Glint |
| [7](wave-07.md) | Nov 5, 2026 | 10 | 20 (pairs) | 154,204 | 1 | Restamp rule held (zero restamp findings); boundary-case edit on the Cursor note |
| [8](wave-08.md) | Nov 5, 2026 | 10 | 20 (pairs) | 194,066 | 0 | Coverage mode: zero findings outside the fact sheet's jurisdiction; ~158 claims catalogued |
| [9](wave-09.md) | Nov 5, 2026 | 10 | 20 (pairs) | 196,260 | 11 | Fixer miss-sweep finds 5 extra; pre-Ultra page rebuilt; 3 residue items logged by name |
| [10](wave-10.md) | Nov 5, 2026 | 20 | 40 (pairs) | 317,764 | 0 | Width 20 held: 40 legs, zero failures, ~283 claims catalogued |
| [11](wave-11.md) | Nov 5, 2026 | 20 | 42 (pairs) | 355,912 | 14 on 2 pages | Timeout hunt: 22,885 reasoning tokens behind an 11-token answer; connector timeout 60s → 300s; ~200 claims catalogued |
| [12](wave-12.md) | Nov 5, 2026 | 4 | 5 (ladder test) | 44,372 | 0 | Ladder test: seeded ID trap passed silently (href layer missing); zero inventions; its pair-check 'defect' was corrected to an extraction artifact (see wave-12 correction) |
| [13](wave-13.md) | Nov 5, 2026 | 2 PDF assets | 8 (pipeline legs) | 91,010 | 2 PDFs produced and live | Glint-touch: 5 batched exceptions across 145 claims; checker contracts took 3 fixes |
| [14](wave-14.md) | Nov 5, 2026 | 4 (cache test) | 33 | 127,152 | 0 | Cache verdict: real, but rewards repeated sequential prompts — not one-shot parallel fan-outs |
| [15](wave-15.md) | Nov 5, 2026 | 5 | 10 (pairs) | 65,603 | 0 | Expansion step 1: base loop intact; 1 pair-confirmed restamp struck (half-verified page); jurisdiction is the binding constraint |
| [16](wave-16.md) | Nov 5, 2026 | 3 | 6 (pairs) | 45,538 | 3 on 1 page | Expansion step 2: Meta Model API fact sheet earned at Tier-1; the wave-5 refused restamp finally earned and shipped |
| [17](wave-17.md) | Nov 5, 2026 | 3 | 6 (pairs) | 55,121 | 2 + lineage on 1 page | Expansion step 3: xAI sheet earned; wave-3 deferral settled (Grok 4.7); two fixer refutations upheld (build record + unearned restamp) |
| [18](wave-18.md) | Nov 5, 2026 | 3 | 6 (pairs) | 40,255 | 0 | Expansion step 4: OpenAI sheet earned; 14045's GPT half verified — and its restamp struck again, on new grounds (dated snapshot, per the fixer's class dispute) |
| [19](wave-19.md) | Nov 5, 2026 | 2 | 6 (pairs + ritual) | 48,284 | 0 | Expansion step 5: Gemini sheet earned (live catalog, 50 models); vendor set closed. First cache ritual: both immediate re-send pairs read 0 cached |
| [20](wave-20.md) | Nov 5, 2026 | 3 | 8 (pairs + ritual) | 82,257 | 2 | Expansion step 6: first non-vendor sheet (IICRC published facts + desk's own records); the wage study contradicted its own tables twice — both counts mechanically re-verified, both repaired. Ritual: 0 hits again |
| **Running total** | | **126** | **285** | **2,198,178** | | |

*Wave 11's token figure includes one 26,027-token diagnostic call (the 300-second bisect that found its failure's cause); its 11 timed-out attempts were unmetered.*

Model: `muse-spark-1.3-contributor` via the Meta Model API, under a $25 test
envelope. Adjudication, editing, publishing, and this log: Glint, running the
lane described in the submission — no desktop takeover, everything in the
background, receipts for everything.

# Tygart-OS on Meta Muse: The Fact-Gated Fleet

**Meta Global AI Developer Hackathon · Startup Track**
Tygart Media — Will Tygart, with Glint (his AI chief of staff)

Publishing at machine speed breaks facts quietly: a single AI editing pass invents plausible, confident, wrong "fixes" — and no human can hand-check thousands of live pages. Tygart-OS runs its real production fleet (six sites, 4,415 live pages) on Meta's Muse models with a separation-of-duties design: a **Trio** — Scout (low effort) flags, Fixer (medium) drafts, Adjudicator (max) strikes anything it cannot ground verbatim in the source, so the proposer never approves its own work — plus the **Hopper**, one dumb intake box with per-destination translator routers that confirm every routing by read-back.

On the hackathon's credits it produced 2,769 monetization candidates, 2,062 adjudicated fixes, 36 staged work orders, and a mined corpus of 174 session recordings — **$102.50 counted of the $153.31 envelope**, every run receipted. (Counted = every Meta Model API leg that returned usage, summed in the run ledger; legs that returned no usage are recorded as unmetered, not estimated.)

## Vocabulary (the four words everything else uses)

- **Paste** — material that has been ingested and checked: every claim in it grounded in a verbatim quote from its source, anything ungroundable struck. *Not* copy-paste: paste is what checked information is called while it is still unshaped, before any destination has had a say. The Trio makes the paste.
- **Hopper** — the one intake box the paste collects in. Nothing leaves the hopper until the operator taps Assemble.
- **Tip** — one destination's accepted shape, named for a cake-decorating tip: paste leaves the hopper only through a tip, so it can only come out in a form that destination already accepts — an import file, a portal form, a UI drive.
- **Trio** — the three-pass check itself: Scout (low effort) flags, Fixer (medium) drafts, Adjudicator (max) strikes. The proposer never approves its own work.

## The Trio — paste-making

The Trio is ingestion plus consistency check — paste-making — run on Muse Spark 1.3 at three reasoning-effort tiers:

- **Scout (low)** listens and drafts in the field — fast, cheap, honest about what it cannot identify.
- **Fixer (medium)** proposes changes.
- **Adjudicator (max)** sits at the gate with judgment: any proposed claim that cannot be grounded in a verbatim quote from the source is struck. An empty grounding quote is an exception, never a silent pass.

The pattern was found, not designed: each model was probed to where it broke and where it was best. The contributor tier hit its token limits and failed as a candidate for the gate — and that failure is what forced the real questions: how much context each step actually needs, what is available to it, and in what order the steps have to run. The answers became the Trio's shape, and the Trio runs on the **standard tier — low → medium → max, in that order**: the cheap legs go first and prepare the record, and a max-effort leg sent in alone failed (the first two legs do the Earth-launch so the max leg can launch off the Moon). The contributor tier kept the work its economics win — bulk ingestion and fan-out, under the standard tier's adjudication. And a $17 book-for-bots product grew an internal router unbidden — the system invented the router before it was named.

## The Hopper and the tips — reverse MCP

Normal MCP lets a model reach out to tools. The inversion here: **the destination's accepted shape constrains what the model may emit.** The Hopper is the bag — checked, grounded information ("paste"). Outputs are the tips — per-destination shapes (one row per Company × Destination) that let paste out in exactly one form: an import file, a portal form, an API call, a UI drive. Shape first, mechanism second, no vendor cooperation required. Tip learning is staged: a destination profile earns trust through probation (clean read-backs) before it is relied on, and every emission is confirmed by read-back at the destination — STRONG where the destination answers, WEAK where it can only be inferred (email caps at WEAK). Money differences are never auto-waived.

The full design — fields, staging, read-back leveling, exception handling — is in [`docs/ROUTER-DESIGN.md`](docs/ROUTER-DESIGN.md). A landscape check confirmed the full pattern (independent grounding gate + probation-staged destination profiles + destination read-back) exists nowhere public; the closest prior art is in [`docs/reverse-mcp-landscape-report.md`](docs/reverse-mcp-landscape-report.md).

## Measured results (all receipted)

- **Fleet:** 4,415 pages · 2,769 strong monetization candidates · 2,062 adjudicated fixes (647 Continuity Hub + 1,415 Risk Coverage Hub) · 36 staged work orders.
- **Unit costs:** standard Trio ≈ $0.12/page; contributor tier ≈ $0.0025/page (a 49× spread); routing decision at medium effort ≈ $0.025/recording — the measured sweet spot.
- **The strike (the demo's center):** on a Risk Coverage Hub cyber-insurance page, the Fixer proposed adding "and any crime / funds-transfer extension." The Adjudicator struck it verbatim: *"that product concept is not in page or Sources."*
- **Recordings corpus:** 174 recordings · 3,093 window reads · 245 ASR calls · 138,144 words · $3.20 — every recording read through three lenses (session report, user-read, agent-read), then mined again for the findings a totals row misses: 361 findings, each backed by a verbatim quote verified mechanically, 5 honest absents ([`docs/MINED-INVENTORY.md`](docs/MINED-INVENTORY.md)).
- **Consensus miner:** 339 claims certified, 17 of 356 dropped (4.8%) by verbatim-quote validation — the disagreement spots went back to the source for the exact quote, or the word "absent."
- **Emblem round-trip:** 312 Restoration Intel pages were compressed by the Trio into one-sentence visual briefs, rendered as emblem images, then read back blind by Spark vision and graded against the held briefs — structure 312/312, palette 311/312 (99.7%), metaphor recovered even where every object was renamed; the one zero-content page was drawn as an empty stage rather than invented content.
- **Contribution sweep:** 544 contributor-tier calls run as a deliberate, logged workload — and as a red-team of this very submission (104 claims audited, 0 invented). [`docs/CONTRIBUTION-LOG.md`](docs/CONTRIBUTION-LOG.md).
- **Feedback to Meta:** 9+ measured items, including the accept-and-silent-drop pattern on media inputs, filed in [`docs/FEEDBACK-TO-META.md`](docs/FEEDBACK-TO-META.md).

## Field test: TruNorth Ops (TEST sandbox)

Thank you, by name, to **Jason Gilstrap**, who built TruNorth Ops himself — field-operations and live time-and-materials billing software for restoration contractors — and who handed us a personal admin login to a private TEST copy of his real software, so the router pattern could be tested against a destination we don't control: no API, no vendor cooperation, only the shapes the software already accepts. Everything ran in that TEST sandbox on Nov 3, 2026, in live watched sessions; every headline number traces to a receipt mapped in [`docs/EVIDENCE-INDEX.md`](docs/EVIDENCE-INDEX.md).

- **Run 1 — shape map + mirror job:** destination shapes mapped field by field; one test job mirrored a sample job; read-back matched **18 of 18 fields exactly**.
- **Run 2 — different mechanisms:** a from-scratch job, an edit round-trip (exactly one field changed, reason recorded), and a computed daily sheet that read back at **$465.50 — matching to the cent**. Shape findings included a second CSV surface stating a different column format than the first (tips are per-surface, not just per-destination) and an image-only job upload that refused a PDF and a voice file with the reason on screen. A refusal with a reason is a receipt too.
- **Run 3 — frozen packets:** two JSON packets (new job + guarded update) were scrubbed, trio-checked, and frozen before the run; the executor invented no job values; the update's expected-before guard passed exactly.
- **Storm drill — nine inputs, two traps:** both designed traps were caught — a contradictory call-in (two addresses, one caller) produced **no job at all**, and an "earthquake" loss type the destination doesn't have was never emitted (mapped to "Other," named in the job title). Four jobs created, two guarded updates applied, spot re-reads 4-for-4.
- **ROMs:** three estimates from field tick sheets — Whitaker $2,378 (54% margin), Edmond $8,418 (51%, and $15,582 under the $24,000 authorization it was never shown), Quail Creek $8,879 (53%). The estimator repeatedly overrode crews' ticked equipment counts with its own judgment.
- **Rate card:** intake ≈ 7 inputs/min at ≈ $0.0013/input; checking gate ≈ $0.0085/input all-in; import through the destination's screen ≈ 1 job/min — the screen leg is ≈ 8× slower than intake. At storm scale the bottleneck is the destination's surface, not the model's cost or speed. That ratio is the case for the tip.
- **Wave 3 — ending at the signature:** three days of field reports became three checked daily sheets ($1,769.00 + $886.00 + $1,247.50 = **$3,902.50**, quantities cross-checked exactly) standing submitted and **PENDING at the manager-signature step** — where the field test ends, by the destination's own design. Checked work moves only when a named human signs for it. Nothing downstream of that signature is claimed, because none was produced.

Receipts, not claims.

## Repository map

| Path | What it is |
|---|---|
| [`docs/SUBMISSION-PACKET.md`](docs/SUBMISSION-PACKET.md) | The full submission packet as filed (its spend figure, $102.35, predates the closing corpus pick-out pass; the ledger total is $102.50 counted). |
| [`docs/ROUTER-DESIGN.md`](docs/ROUTER-DESIGN.md) | The reverse-MCP router/tip design: tip registry fields, staging, read-back levels, exceptions. Honest split stated inside: checking is production, the routing decision is measured, the tip registry/learning/adapters are designed, not built. |
| [`docs/EVIDENCE-INDEX.md`](docs/EVIDENCE-INDEX.md) | Every headline claim in the packet mapped to the exact receipt file that proves it. |
| [`docs/MINED-INVENTORY.md`](docs/MINED-INVENTORY.md) | The corpus pick-out inventory: the read-aloud spine, 361 quote-verified findings, the emblem round-trip section, the shortlist. |
| [`docs/CONTRIBUTION-LOG.md`](docs/CONTRIBUTION-LOG.md) | The 544-call contributor sweep: prompts, tier behavior, red-team findings and the fixes they forced. |
| [`docs/NIGHT-LEDGER.md`](docs/NIGHT-LEDGER.md) | The master run ledger: every experiment, its question, its cost, its verdict, and where its receipts live — the stats backbone under every number above. |
| [`docs/CONTRIBUTOR-LESSONS.md`](docs/CONTRIBUTOR-LESSONS.md) | The contributor tier, measured: pricing, the completion-budget law (small budgets buy metered nulls), the ≥7K rule, and where the tier sits in the design — written to be pulled from. |
| [`docs/FIELD-NOTES.md`](docs/FIELD-NOTES.md) | What the Trio saw, and what it taught us: the emblem round-trip's named cases, the Max-alone failure (Earth-launch, Moon-launch), the recording corpus's strange shapes, the discovery order, and the honest absents — the nuances, kept in one extractable place. |
| [`docs/FEEDBACK-TO-META.md`](docs/FEEDBACK-TO-META.md) | Structured, measured feedback to Meta from running on the Model API. |
| [`docs/reverse-mcp-landscape-report.md`](docs/reverse-mcp-landscape-report.md) | Prior-art landscape for the reverse-MCP pattern. |
| [`docs/ONE-PAGER.html`](docs/ONE-PAGER.html) | The one-page project summary (HTML source of the filed PDF). |
| [`code/meta_api.py`](code/meta_api.py) | The Meta Model API helper used by every leg. It never holds a key: it calls through a surrogate-credential mechanism that swaps in the real key only on the approved request to api.meta.ai. |
| [`code/router/run_router_trio.py`](code/router/run_router_trio.py) | The router-design Trio runner (scout/fixer/adjudicator) with per-leg usage and cost accounting. |
| [`code/contribution-sweep/sweep.py`](code/contribution-sweep/sweep.py) | The batched contributor-tier runner used by the sweep (and, in copied form, the pick-out pass). |
| [`code/corpus-pickout/`](code/corpus-pickout/) | The pick-out pass: `runner.py` (extraction), `segment_spine.py` (read-aloud spine segmentation), `verify_quotes.py` (mechanical verbatim-quote verification of every finding). Two scripts carry local absolute paths from the run machine; no credentials. |
| [`code/video-test/`](code/video-test/) | The recording-corpus readers: `run_session.py` (window scout), `synth.py` (session/user synthesis), `synth_agent.py` (agent-read). |

[`MANIFEST.md`](MANIFEST.md) lists every file in this repo with its source, and everything deliberately excluded, with reasons.

## What is deliberately not here

No credentials or keys (none exist in any run script — access was surrogate-mediated). No private findings material belonging to Jason Gilstrap / TruNorth beyond what the packet states publicly. No billing or payment material. No recording frames that were disqualified from the demo for showing sensitive screens. The TruNorth receipt PDFs and run logs are cited by path in the Evidence Index rather than republished. See `MANIFEST.md` for the complete exclusion list.

## Demo

The demo video is filed with the Cerebral Valley submission and published on the Tygart Media YouTube channel: https://www.youtube.com/watch?v=8xg3_UqEAPk — 2:38: the narrated explainer ending on the verbatim strike, a short bridge, and the 30-second spot. Its on-card spend figure ($102.50) is the closing counted total.

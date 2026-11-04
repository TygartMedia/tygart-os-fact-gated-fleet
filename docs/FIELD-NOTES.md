# Field notes — what the Trio saw, and what it taught us

The interesting residue of the run, in one place: the nuances, the surprises,
and the limits, each with its numbers. Everything here is distilled from the
run record — the receipts are named in the Provenance section at the end, and
nothing in this document claims more than they state.

## 1. The emblem round-trip: meaning, graded on return

**Method.** Every Restoration Intel page had already been through the Trio,
leaving a concentrate — scout flags plus adjudicated fixes. From each
concentrate, a contributor-tier brief-writer distilled **one sentence: a
visual metaphor for what the page is about**. That sentence was the only
page-specific input to `muse-image-1.0`, which rendered an emblem in a fixed
house style (flat vector editorial, warm cream ground, cream/orange/black,
one central emblem, no text, no people) — the style held constant so it could
act as an instrument, not a variable. Then Spark vision read each emblem
**blind** — no brief, no slug, no context — and the read was graded
deterministically against the held brief: *was the meaning still in there?*

**The numbers.**

- **312/312 emblems generated, 0 errors; 312/312 blind vision reports, 0
  errors.**
- **Structure: 312/312** reports carry all four sections (description /
  subject / style / anomalies).
- **Palette: 311/312 = 99.7%** name cream + orange + black correctly.
- **Brief key-noun recovery: 46.8% average** (1,580/3,378) — explicitly a
  **floor**: the matcher is synonym-blind, so every correct rename counts as
  a miss.
- Vision tokens: 1,770,008 total, median 5,652/report; dollar close **$4.37**
  at Spark standard rates. The image side ran 5,530,830 tokens, unpriced (no
  published rate — kept unpriced on the record rather than estimated into
  the totals).

**The named cases.**

1. **The cobwebbed rain gauge — loop closure, twice over.** The brief-writer,
   in independent parallel calls with no shared context, converged on a
   signature motif for storm-data pages: a cobwebbed rain gauge. "Cobwebbed"
   appears in **27 briefs**, clustered at storm-pulse positions ~97–111.
   Brief #104: *"A cobwebbed rain gauge holding green stagnant water under
   bright cloudless skies above cracked dry mud."* The blind vision read
   described the vessel, its gauge ticks, the green fill, and *"cobwebs in
   the upper empty part of the gauge = disuse, neglect,"* judging
   drought/water scarcity. An invented motif survived text → image → text
   with its meaning intact — and the motif itself was never specified by
   anyone; it is the model's own gravity for "storm data, watched and
   waiting."
2. **The empty stage — absence drawn, not invention.** One blog page fetched
   0 chars and was adjudicated NO-OP. Its emblem is a vacant stage: curtains,
   one spotlight pooling on bare boards, nothing on it. The vision read:
   *"an empty theater stage… anticipation, exposure, and potential… the
   emptiness emphasizes waiting, opportunity, vulnerability."* The image leg
   inherited the trio's fact discipline through the concentrate: a page with
   nothing to say got an emblem of nothing, honestly framed.
3. **The calipers — every object renamed, the metaphor recovered.** Brief:
   *"Steel calipers lifting a measured slice of hurricane-shredded roof
   above rising floodwater."* Vision read calipers gripping a crumbling
   block over waves and judged the subject *"measurement of natural loss /
   erosion — precision vs. irregularity, human attempt to measure something
   actively breaking."* Roof became cliff/soil/wood; the noun score for this
   emblem is a miss — and the meaning arrived whole. The report also flags
   its own uncertainty ("the image itself provides no label confirming cliff
   vs. wood vs. soil"): the reader hedged where it could not know.

**The stated limit.** Equipment glyphs are ambiguous at emblem scale. Of 10
briefs naming dehumidifiers, vision said dehumidifier 5, heater 3,
fan/air-mover 1, other 1. Scene and style read near-perfectly; fine
equipment identity must be confirmed by a human or a second pass where it
matters.

**Two more disciplines, visible only because both sides are logged.** The
renders stayed cream/orange/black with zero text and zero people in
everything viewed — but the briefs themselves say "blue" **26 times** (blue
skies), and the image model's style layer silently overrode the
brief-writer's palette. And batch 3's lesson caps it: *an image is only ever
as good as its brief* — the vague poetic brief for the October 28 roundup
produced a clean but unmoored render.

## 2. Max alone fails: the Earth launch and the Moon launch

A max-effort leg by itself was tried, and it failed in a specific,
repeatable way: given room to think, it spends the whole budget thinking.

- **The effort ladder** (Round 2, $0.0826): *medium is the plateau; max at
  an 8K cap collapses (all reasoning, no answer).*
- **The CSV trio test** ($0.19994): the scout/analyst rankings were perfect
  (top-10 pages & queries 10/10 exact), but the *adjudicator @ max FAILED —
  final incomplete, 23,998/24,000 output tokens were reasoning, zero
  briefing emitted.*
- **The Wonder-judge swap** ($1.8191): a stronger model dropped in as
  adjudicator only — 2 of 4 pages hit the 24K cap (finish=length), one
  returned **ZERO answer chars**, and the run cost **~4.3x the whole Spark
  trio**. Stronger-and-bigger alone was worse, not better.

The finding the architecture is built on, in the record's own words: the
first two legs do the **Earth-launch** so the max leg can **launch off the
Moon**. Scout and fixer carry the work to altitude — the map, the draft, the
evidence laid out — and the max leg spends its reasoning on judgment alone
instead of burning it on lift-off.

## 3. What the audio actually carried

The visual census says what happened on screen; the audio pass measured
what the recordings actually *carried*. Full corpus: **174 recordings,
100.3 hours**.

- **245/245 ASR calls OK, zero errors** — 2,879 turns, **138,144 words**,
  ≈793.8 minutes of speech, **$3.20 total** ($0.93 for rec1–66 + $2.27 for
  the extension).
- **The corpus is bimodal.** 53 recordings carry substantive speech; **77
  contain exactly one transcribed word**; 5 have sound but no speech; **39
  are pure silence**. There is no middle tier of ambient room speech. The
  one word, in the 31 pass-1 cases, is **"Yeah"** — landing in the final
  ~15% of the recording, usually the final seconds (rec64: second 16,251 of
  16,252): an end-of-sitting artifact, not conversation.
- **Whose voice:** of pass 1's 43,515 words, ≈79% are **Glint's own voice**
  narrating sittings aloud; Will's identified voice is ≈4.6% (1,803 of those
  words are his rec54 voice notes); media playback is 3.1%. Will's mic was,
  by design, not the recorder's source.
- **rec96** (2026-10-23, 9,339 words, **4 diarized speakers**) is the
  corpus's one genuine multi-human conversation — reported as found;
  multi-speaker separation is explicitly *not* claimed as validated.
- **rec167** is the extreme of the dense pole: 5.16 hours of sound, **46,829
  words, 734 turns** — one marathon Glint-voice sitting narrating work
  orders.
- **rec53's anomaly:** after ~3 hours of Glint narration, one lone 14-word
  turn in a second voice at 183:24 — *"These equipment costs are killing us.
  We need to get these overhead numbers down."* Nothing in the visual record
  explains it. Unattributed, as found.
- **What audio adds that frames cannot:** rec54's transcript preserves
  Will's deliberation verbatim during stretches the user-read could only
  call patient; rec51's audio proves a provenance chain (rec54's tape
  replayed inside rec51's sitting); rec58's entire substance — the Phil
  Rosebrook interview — exists only in its transcript.

## 4. The read-aloud call: one voice, grading itself

The spine of the corpus work is the Oct 30 afternoon call itself —
2:22:29 end-to-end, mined in its own right (16 ASR calls, $0.4221).
Diarization proved it is, to measurement precision, a **one-voice
recording**: Speaker A (Glint) holds 280 of 291 turns, 4,364.0 of 4,419.0
speech seconds, 12,830 of 12,831 words. Will directed the walk — his
"next"s, his challenges, his corrections — but his microphone never reached
the recording's audio track. What survives is the accounting itself: the
system narrating what it had seen him do, in order, while the remaining
recordings finished processing behind it.

**The walk grades itself, in bands — the transcript says so on mic:**

- **Reports 1–2 — FILE-READ.** Read from the actual session reports.
- **Reports 3–17 — DRIFT.** At ~00:15 the voice admits it: *"Reports one and
  two were read from the files, but from three onward, I was keeping the
  flow going without opening each file, and I drifted."* Everything in this
  band is unverified narration.
- **Report 18 — BROKEN, THEN CORRECTED.** The narration told a work-order
  story (equipment charges, a daily sheet) that belonged to another session;
  challenged, it pulled the file and corrected itself on the same call:
  rec18 is a one-minute silent scroll of a Houston Clarity dashboard. The
  rule adopted on the spot — **read the file first, then speak** — governs
  the rest of the walk, and the rest of this project.
- **Reports 20–66 — FILE-FIRST.** Each reading announces itself from the
  files.
- **The verdict walk (01:56–02:21)** then re-read the first recordings
  through the final pass — the agent-read layer judging the agents.

**The cross-check.** The pick-out pass sliced the call transcript per
recording and graded narration against files: voice segments present for 52
of 66 recordings — **41 AGREES, 11 PARTIAL, 0 flat DISAGREES** among those
present. Every PARTIAL is itemized in the inventory (details added or
wobbled — call counts, a CMD console called PowerShell, a later outcome
narrated into an earlier session). The spine indexes 64 rows — 63 numbered
reports + report 18's correction; 12 final-pass verdicts. **Reports 19, 58
and 59 have no segment in the call** — 19 was never read (the walk went from
the report-18 correction straight to 20), and the walk jumps from report 57
to report 60 in the surviving transcript. None was invented to fill the
gap. Report 69 was found empty when its turn came — no report was
fabricated for it; that refusal is also on the record.

## 5. Found, not designed: the discovery order

The pattern was **found, not designed** — in this order:

1. **Each model was probed to where it broke** and where it was best.
2. **The contributor tier's token limits** turned out to be load-bearing:
   the tier failed as a candidate for the gate, and that failure forced
   the questions — how much context each step needs, what is available to
   it, in what order the steps run.
3. **The low / medium / max mapping** followed from those questions — it
   is the shape the constraints forced, not a menu pick. The Trio runs on
   the **standard tier, low → medium → max, in that order**; the
   contributor tier kept the bulk ingestion and fan-out instead.
4. **A max-effort leg alone failed** (Section 2) — which is what made the
   three-leg shape necessary rather than decorative.
5. **Voice, image, and video legs were tested** against the same models,
   each with its own receipts — the emblem round-trip and the audio census
   both live here.
6. **A $17 book-for-bots product grew an internal router unbidden** — *the
   system invented the router before it was named.*
7. **The router question became explicit**, and with it the **TIPS
   insight**: normal MCP lets a model reach out to tools; the inversion is
   that **the destination's accepted shape constrains what the model may
   emit**. **Paste**, as the word is used here, is material that has been
   ingested and checked — every claim in it grounded in a verbatim quote
   from its source, anything ungroundable struck — still unshaped, before
   any destination has had a say; not copy-paste. Paste leaves the hopper
   only through a **tip** — one destination's accepted shape — so it can
   only come out in a form that destination already accepts: an import
   file, a portal form, an API call, a UI drive.

The measured case for the tip, from the field test's rate card: intake ran
≈ **7 inputs/minute** at ≈ **$0.0013 per input**; the checking gate cost ≈
**$0.0085 per input all-in**; import through the destination's own screen
ran ≈ **1 job/minute**. The screen leg is roughly **8× slower than
intake**: at storm scale, the constraint is the destination's surface — not
the model's cost, not its speed.

## 6. Two laws from the ledger

**Behavior law (Runs 1–2, 7 pages).** *The fixer invents (unsupported
prices, SLAs, screenshots, URLs); the adjudicator strikes every invention
with page-text evidence. Feed hygiene matters: text dumps strip hrefs.*
That one asymmetry — the proposer invents, the gate strikes — is why the
proposer never approves its own work anywhere in this system.

**Costing law.** *Trio/page ≈ $0.12 and FLAT across page types (max leg's
reasoning dominates). Cross-vendor, same workload at list: Claude
role-matched $0.4709 · Gemini $0.2815 · Meta $0.1200. The adjudicator's
output tokens decide everything: Spark $4.25 vs Gemini Pro $12 vs Opus $20
per 1M out.* Price the gate's judgment, not the pipeline's motion.

A third observation, from the emblem leg, belongs with these: **the shape
of the ask changed the honesty of the answer.** Given one emblem
unstructured, a stronger probe model recovered puddle + shadow and invented
*"the black silhouette of a grand piano"* — no piano exists. Spark's
structured read stayed closer and flagged uncertainty explicitly.

## 7. Honest absents and limits, as findings

The gaps are part of the record, kept on purpose:

- **5 recordings are honest absents** in the pick-out — rec14, rec16, rec18,
  rec28, rec34: their own files hold no quotable nuance moments, and none
  was manufactured.
- **39 of 174 recordings are pure silence**, and **TRANSCRIPT.md is absent
  from exactly 12 folders** (rec6, 20, 22, 24, 26, 30, 31, 48, 60, 61, 62,
  65) — the 12 pure-silence recordings of audio pass 1, which wrote no
  transcript files for silent recs. Extractors for those recordings worked
  from the three visual reads only, and were told so.
- **The one zero-content page** was drawn as an empty stage rather than
  invented content (Section 1).
- **The consensus miner dropped 17 of 356 cross-layer agreements** (339
  quote-certified) when the verbatim quote could not be produced — the
  disagreement spots went back to the source for the exact quote, or the
  word "absent."
- **A $0.5085 Wonder run returned zero output** — and is kept on the record
  as a zero, not quietly dropped from the totals.
- **The image side's 5,530,830 tokens are unpriced** — no published rate —
  and stay unpriced in the totals rather than estimated.

Receipts, not claims — including the receipts for what isn't there.

## Provenance

Every fact, figure, and quote in this document comes from the run record in
this same repository:

- [`MINED-INVENTORY.md`](MINED-INVENTORY.md) — the corpus pick-out
  inventory: the read-aloud spine and its cross-check, the 361
  quote-verified findings, the emblem round-trip, the audio findings.
- [`NIGHT-LEDGER.md`](NIGHT-LEDGER.md) — the master run ledger: the rounds,
  the effort ladder, the behavior law, the costing law, per-call usage.
- [`SUBMISSION-PACKET.md`](SUBMISSION-PACKET.md) — the submission packet as
  filed: the emblem receipt, the discovery chain, the rate card.

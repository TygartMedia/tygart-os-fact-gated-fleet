# Submission Packet — Cerebral Valley Portal
## Meta Global AI Developer Hackathon · Startup Track

**Project title:** Tygart-OS on Meta Muse: The Fact-Gated Fleet
**Track:** Startup Track (one application)
**Team line (as on the one-pager):** Tygart Media — Will Tygart, with Glint (his AI chief of staff)
**Filing:** Wed Nov 4, 2026, with Will present · **Hard deadline: Wed Nov 4, 2026, 9:00 PM ET**

---

## Short description (paste-ready, from the one-pager)

Publishing at machine speed breaks facts quietly: a single AI editing pass invents plausible, confident, wrong "fixes" — and no human can hand-check thousands of live pages. Tygart-OS runs its real production fleet (six sites, 4,415 live pages) on Meta's Muse models with a separation-of-duties design: a Trio — Scout (low effort) flags, Fixer (medium) drafts, Adjudicator (max) strikes anything it cannot ground verbatim in the source, so the proposer never approves its own work — plus the Hopper, one dumb intake box with per-destination translator routers that confirm every routing by read-back. On the hackathon's credits it produced 2,769 monetization candidates, 2,062 adjudicated fixes, 36 staged work orders, and a mined corpus of 174 session recordings — $102.50 counted of the $153.31 envelope, every run receipted. Capstone field test: the router pattern ran live against a TEST copy of TruNorth Ops, third-party restoration software with no API — three verification runs, a nine-input storm drill with both designed traps caught, three estimator ROMs, and a three-day job whose checked sheets stop at the human signature gate.

## Files to upload (all in this `final/` folder)

| Portal slot (expected) | File | Notes |
|---|---|---|
| Project write-up / one-pager (PDF) | `ONE-PAGER.pdf` | Exactly 1 page, Letter. Numbers synced at the final pass (Nov 3): counted spend $102.50 of $153.31. |
| Demo video (≈3 min) | **`../final-v2/demo-final-3min.mp4`** | FLAGSHIP (Will's final shape, Nov 3): no intro, no music, all Glint narration. 187.06 s, 57,134,481 bytes, H.264 1920×1080@30 + AAC 48 kHz, faststart; ffprobe + full-decode verified at the final pass (zero errors). Front: Glint explainer; tail: the 60 s producer's-cut commercial spliced whole. |
| Demo video — fallbacks | `demo-song-cut.mp4` / `demo-final-v4.mp4` | Earlier verified cuts retained in this folder if the flagship is ever swapped out: song cut (148.50 s, Will's "Humidity Metrics (Alt)" as the spine) and the trio-reviewed narrated v4 (155.37 s). `demo-final.mp4` (v1) and its `.srt` remain as earlier fallbacks. |
| Demo captions (if a captions slot exists) | `demo-final.srt` | Sidecar captions for the v1/v4 narrated cuts; the song cut carries no captions (the song's lyrics are the text). |
| Supporting record (if a links/docs field exists) | reference, don't upload blindly | `~/workspace/out/model-bakeoff/NIGHT-LEDGER.md` (every run + cost), `FEEDBACK-TO-META.md` (structured feedback to Meta), `TRIO-COSTING.md`. Paste the ledger's PROGRAM TOTAL — FINAL section if a long-text field asks for evidence. |
| Narration transcript (if asked) | `narration-script.md` | Full narration with beat timings as built. |

## Judging-angle reminders (for the form's free-text fields)
- **Impact (30%):** real production, not a staged demo — 4,415 live pages, a download ladder shipping now, 36 work orders staged for human-tapped execution.
- **Meta tooling (25%):** the Trio/router system itself runs entirely on Muse Spark 1.3 effort tiers + the contributor tier; supporting media legs (ASR transcription, image generation, TTS) sit outside that system on other models and are ledgered separately as unmetered in NIGHT-LEDGER.md; structured feedback filed in FEEDBACK-TO-META.md (9+ items, all measured).
- **Technical depth (20%):** the measured behavior — fixer hallucination caught by the max-effort gate, effort curves (medium = routing sweet spot ≈ $0.025/recording), 49× cost spread standard vs contributor (unit costs and spread per NIGHT-LEDGER.md), Wonder-as-judge trial failed and was dropped on the record.
- **Demo (25%):** the video's center is a real strike: Fixer item 4 on the RCH CFC cyber page invented "and any crime / funds-transfer extension"; the Adjudicator struck it verbatim — "that product concept is not in page or Sources." (Exhibit: model-bakeoff/rch-sweep/cfc-sme-cyber-disconnect-what-cover-pays-for/.)

## Verified facts for any field that asks
- Counted spend: **$102.50 of $153.31** (NIGHT-LEDGER.md final counted total, Nov 3; receipt-summed precise total $102.4974 — every Meta Model API leg with returned usage, including all TruNorth/drill/ROM/Wave-3 prep legs, the closing contribution sweep, and the corpus pick-out pass, the final counted leg. Excluded as unmetered, per the ledger: ASR calls that returned null usage, image generation (no published rate), and browser UI time, which is not API-metered.)
- Standard trio ≈ **$0.12/page**; contributor tier ≈ **$0.0025/page**; routing decision (medium) ≈ **$0.025/recording** (unit costs per NIGHT-LEDGER.md).
- Fleet: **4,415 pages · 2,769 strong candidates · 2,062 adjudicated fixes** (647 Continuity Hub + 1,415 Risk Coverage Hub) · **36 staged work orders** (per NIGHT-LEDGER.md; detail in the model-bakeoff/ sweep folders).
- Recordings: **174 recordings · 3,093 window reads · 245 ASR calls · 138,144 words · $3.20** (NIGHT-LEDGER.md; run record in model-bakeoff/video-test/).
- Consensus miner: **339 certified, 17 of 356 dropped (4.8%)** by verbatim-quote validation.
- API status Nov 3: **restored** — model list 200 (9 models), paid contributor chat call 200. (Nov 1 suspension superseded.)
- TruNorth field test (Nov 3, TEST sandbox, watched sessions): **Run 1 read-back 18/18 fields exact** · Run 2 daily sheet **$465.50** matched to the cent · storm drill **9 inputs, 2 designed traps, both caught, 4 jobs created, 2 guarded updates** · spot re-reads **4/4 PASS** · ROMs **Whitaker $2,378 (54%) · Edmond $8,418 (51%), $15,582 under the $24,000 authorization · Quail Creek $8,879 (53%)** · rate card **intake ≈ 7 inputs/min at ≈ $0.0013/input, gate ≈ $0.0085/input all-in, import ≈ 1 job/min (screen leg ≈ 8× slower than intake)** · Wave 3 **three Edmond daily sheets totaling $3,902.50, standing PENDING at the manager signature** (full section below; receipts in the evidence bundle).

---

## The corpus turned inward

On October 30 we pointed the system at itself. Our own 174 session recordings — 100.3 hours — were read three ways each, what happened, what the operator did, what the agent did, across 3,093 window reads. The audio pass transcribed what the recordings actually carried: 245 calls, 138,144 words, $3.20 — and found the corpus bimodal: dense narration, or a single closing "Yeah" in 77 recordings. The voice on the track was mostly the assistant's own; the operator's microphone was never the recorder's source. We know because we measured it — the same discipline as the emblem round-trip, where 312 page concentrates became 312 images and Spark read them back blind: structure 312 of 312, palette 99.7%, the metaphor intact even when every object in it was renamed. And when the assistant later narrated those session reports aloud from memory instead of from the files, the operator caught it at report 18, on mic. The rule that came out of that moment — read the file first, then speak — is the rule this whole submission runs on.

The emblem round-trip deserves its own receipt. Each Restoration Intel page's trio concentrate was compressed by a contributor-tier brief-writer into one visual-metaphor sentence; muse-image-1.0 rendered that sentence as an emblem in a fixed house style (flat vector, cream/orange/black, no text, no people); Muse Spark 1.3 then read each emblem blind, and the read was graded against the brief that had been held back. Both directions ran complete — 312 of 312 emblems generated and 312 of 312 structured reads, zero errors — and the grading was deterministic text-against-text: structure 312 of 312, palette 311 of 312 (99.7%), key-noun recovery 46.8% against a synonym-blind matcher, which makes that figure a floor, not a score. The signature loop closed on an invented motif: brief #104 — "A cobwebbed rain gauge holding green stagnant water under bright cloudless skies above cracked dry mud" — came back from the blind read with the vessel, the gauge ticks, and the green fill described, and the cobwebs interpreted as "disuse, neglect"; the brief-writer's invention had survived text → image → text. The stated limit is equipment identity at emblem scale: of ten briefs naming a dehumidifier, the blind read said "dehumidifier" five times.

---

## Field test: TruNorth Ops

Thank you, by name, to **Jason Gilstrap**, who built TruNorth Ops himself — field-operations and live time-and-materials billing software for restoration contractors — and who handed us a personal admin login to a private TEST copy of his real software, so the router pattern could be tested against a destination we don't control: no API, no vendor cooperation, only the shapes the software already accepts. Everything below ran in that TEST sandbox on Nov 3, 2026, in live sessions Will watched; every headline number traces to a receipt mapped in the bundle's EVIDENCE-INDEX.

**Run 1 — shape map + mirror job.** The destination's accepted shapes were mapped field by field: the UI job form, a documented CSV price-list import (template supplied by the software itself), and an Encircle job import. Exactly one test job was created mirroring a sample job; the read-back matched **18 of 18 fields exactly**.

**Run 2 — different mechanisms.** A from-scratch job was created, then edited (Est. Days 7 → 9 with a recorded reason; the edit history shows exactly one field changed). A computed daily sheet read back at **$465.50 — matching to the cent**. A photo was accepted through the job's photo surface. Two honest shape findings came with it: a second CSV surface states a different column format than the first surface documented — tips are written per-surface, not just per-destination — and the job-page upload accepts images only: a PDF and a voice file were refused, with the reason shown on screen. A refusal with a reason is a receipt too.

**Run 3 — frozen packets.** Two JSON packets (one new job, one guarded update) were scrubbed, run through the full standard trio ahead of the run, and frozen into an executor script — the executor invented no job values. The update's expected-before guard passed exactly before anything changed. Both emissions read back clean; three values garbled in the executor's written report prose were caught against the delivered page PDF — receipts over narration, demonstrated on our own run.

**Storm drill — nine inputs, two traps.** A Restoration Intel storm pulse plus eight mock field inputs (a homeowner call-in, an adjuster email, a tech's text, a voice-note update, a photo note, a TPA update, and two designed break-tests) went through a contributor-tier fan-out — 2 independent agents × 8 inputs, 16 calls in 65.5 s for $0.01028 — and a standard-tier adjudication gate. Both traps were caught: the contradictory call-in (one caller, two different addresses for the same house) produced **no job at all**, and the "earthquake" loss type — a value TruNorth does not have — was **never emitted**; it was mapped to "Other" with the mapping named in the job title itself. Four jobs were created and two guarded updates applied. Afterward, four independent spot re-reads of the live pages matched the receipts **4-for-4**.

**ROMs — the estimator's judgment.** Three rough-order-of-magnitude estimates were built from field tick sheets in TruNorth's own ROM estimator: **Whitaker $2,378 at a 54% margin; Edmond $8,418 at 51%** — built without ever entering the adjuster's **$24,000** authorization, and $15,582 under it when compared after read-back; **Quail Creek $8,879 at 53%**. The estimator repeatedly overrode the crews' ticked equipment counts with its own judgment (Edmond: 17 air movers computed vs 10 ticked; Quail Creek: 13 vs 8) — an operator's experience encoded in the destination, visible only because every packet was read back.

**Rate card — where the bottleneck actually is.** Intake ran ≈ **7 inputs/minute** at ≈ **$0.0013 per input**; the checking gate cost ≈ **$0.0085 per input all-in**; import into TruNorth through its own screen ran ≈ **1 job/minute**. The screen leg is roughly **8× slower than intake**: at storm scale, the constraint is the destination's surface — not the model's cost, not its speed. That measured ratio is the case for the tip: meet each destination in the shape it already accepts, and the same checked packet that takes a minute through a screen lands in seconds through any faster surface the destination later offers.

**Wave 3 — three days, ending at the signature.** One drill job (Edmond) was carried through three days of messy field reports, each converted by the pipeline into a daily sheet: **$1,769.00 + $886.00 + $1,247.50 = $3,902.50**, with quantities cross-checked exactly across the three days (30 tech-hours; 28 air-mover unit-days; 9 dehumidifier unit-days; 3 scrubber unit-days). The sheets stand submitted and **PENDING at the manager-signature step** — and that is where this field test ends, by the destination's own design: in TruNorth, checked work moves only when a named human signs for it. The router's job is to make everything up to that signature exact. The signature itself belongs to a person. Nothing downstream of that signature is claimed here, because none was produced.

Receipts, not claims.

---

## ⚠️ What Glint could NOT verify about the portal
- Glint has **not** opened the Cerebral Valley submission portal in this run and does not know its exact field names, required fields, file-size caps, or accepted video formats beyond the general hackathon terms. The slot names in the table above are expectations, not verified portal labels — match them to the real fields on screen and flag any mismatch before submitting.
- Whether the portal wants the demo as an upload vs. a video link is **unverified**. If it requires a hosted link, the video needs uploading to a host first (Will's tap on which host).
- Team-member / eligibility fields (names, emails, entity details) are **not** pre-filled anywhere — they must come from Will.

## Remaining steps — WILL'S TAPS ONLY
1. **Log in** to the Cerebral Valley / hackathon portal (Will's account — Glint does not hold this login).
2. **Create/open the application** — Startup Track — and paste the title + short description above.
3. **Upload** `ONE-PAGER.pdf` and the demo video — the combined intro + `demo-song-cut.mp4` once Will's intro is recorded and prepended (or `demo-final-v4.mp4` if the narrated fallback is used instead).
4. **Fill identity/eligibility fields** the portal requires (only Will can supply/attest these).
5. **Review the preview** — check the video plays, the PDF renders on one page, no fields truncated the pasted text.
6. **Final Submit button — Will's tap only.** Glint does not submit anything.
7. After submitting: save/screenshot the confirmation and send it to Glint so the submission is receipted in the ledger.

## Glint-side status
- [x] Flagship demo (final shape) built + ffprobe-verified + full-decode verified (specs below)
- [x] TruNorth field-test section folded in with the full run/drill/ROM/Wave-3 arc (ends at the signature gate; nothing downstream claimed)
- [x] Final numbers sync: packet + one-pager carry the ledger's closing counted total, **$102.50 of $153.31**
- [x] Corpus expansion (Nov 3, late, Will's direction): the mined-inventory passage and a receipted emblem round-trip paragraph adopted into the packet ("The corpus turned inward" section); counted total re-synced $102.35 → $102.50 after the corpus pick-out pass, the final counted leg
- [x] Evidence bundle assembled with claim-by-claim index (`submission-bundle/EVIDENCE-INDEX.md`, `submission-bundle/READY.md`)
- [x] Captions sidecar (`demo-final.srt`) + narration burned onto cards
- [x] `narration-script.md` with as-built timings
- [x] One-pager status box updated; PDF regenerated, exactly 1 page
- [x] Leak scan of narration + card text: PASS (no keys, no emails, no client names — only Tygart Media's own public fleet and figures from the run record)
- [ ] Portal submission — **Will's taps only (steps above)**

## Video specs (ffprobe-verified from the finished file)
- **FLAGSHIP — `final-v2/demo-final-3min.mp4`** — **187.06 s (3:07.1)**, **57,134,481 bytes**, H.264 1920×1080 @ 30 fps + AAC 48 kHz, faststart. Full-file decode at the final pass: clean, zero errors. Build record: `final-v2/BUILD-NOTE.md`; script: `final-v2/SCRIPT.md`.
- `demo-final.mp4` — **173.82 s (2:53.8)**, **5,553,965 bytes**, H.264 1920×1080 + AAC 48 kHz, 30 fps
- Full-file decode check: clean, zero errors
- As-built beat timings (measured): B1 0:00.0–0:10.4 · B2 0:10.4–0:33.7 · B3 0:33.7–0:51.6 · B4 0:51.6–1:17.8 · B5 1:17.8–1:48.9 · B6 1:48.9–2:30.8 · B7 2:30.8–2:46.5 · B8 2:46.5–2:53.8
- Narration ran faster than the storyboard's estimates, so beats land ahead of the storyboard clock — the storyboard's beat order and content are unchanged; `narration-script.md` carries the true timings.
- `ONE-PAGER.pdf` — 20,563 bytes, exactly 1 page (Letter), pdfinfo-verified
- `demo-final.srt` — 3,151 bytes · `narration-script.md` — 3,491 bytes
- **v2 (polished, built Nov 3 ~06:47 PT):** `demo-final-v2.mp4` + `demo-final-v2.srt` — **174.60 s (2:54.6)**, **39,734,477 bytes**, H.264 1920×1080 + AAC 48 kHz, full-decode verified, leak scan PASS, same narration as v1, varied layouts + slow zoom; per-beat timings in `work-v2/timings-v2.json`. `demo-final.mp4` (v1) retained byte-identical as fallback.
- **v3 (real footage, built Nov 3 ~07:05 PT):** `demo-final-v3.mp4` + `demo-final-v3.srt` — **174.60 s**, **19,187,838 bytes**, H.264 1920×1080 + AAC, full-decode verified, leak scan PASS; v2 plus real dev.meta.ai console footage insets (leak-cleared stills, Oct 30): model dropdown in Beat 4, dashboard + token-usage charts in Beat 6. Segment lengths unchanged, so v2 timings hold. v2 and v1 retained as fallbacks.
- **v4 (trio-reviewed cut, built Nov 3 ~07:27 PT):** `demo-final-v4.mp4` + `demo-final-v4.srt` — **155.37 s (2:35.4)**, **7,983,601 bytes**, H.264 1920×1080 + AAC, full-decode verified, leak scan PASS. The Spark Trio reviewed v3 and v4 applies its adjudicated edits: browser chrome and the $0.00 spend readout cropped out of the console insets, the contradictory token-charts inset deleted, dashboard counters enlarged, Hopper diagram rebuilt to one router per destination doing three jobs, receipts beat rebuilt as three real-asset holds with short labels only (no table, no paragraph captions), narration trimmed in Beats 4/5/7 (effort labels, per-page pricing sentence, middle pipeline counts, routing-cost tail — re-narrated in the same disclosed voice); the spoken "$100.94 of $153.31" receipt stays per the Adjudicator's strike. B2/B3 exhibit cards remain character-verbatim to the sweep source files (Glint QC exception — the review's E1/E2/E5 rewordings were NOT applied). v3, v2, and v1 retained byte-identical as fallbacks.
- **Song cut (Will's new shape, built Nov 3 ~08:50 PT):** `demo-song-cut.mp4` — **148.50 s**, **46,931,260 bytes**, H.264 1920×1080 30 fps + AAC 48 kHz stereo, full-decode verified (0 errors), leak scan PASS. Audio = Will's own song "Humidity Metrics (Alt)" (148.459 s, his Google Flow Music track) as the spine, with Glint's v4 narration (beats 4/3/7) ducked in at 0:25 / 0:57 / 1:58 via sidechain. Visuals = real session-recording timelapses (rec6/rec3/rec1 frame archives, top-cropped, pre-inspected) + generated B-roll as connective tissue + cropped console stills + exactly one numbers card ("$101.42 of $153.31 — every call receipted") + title card. ASR spot-check confirms the song's lyrics in the mix and the strike narration verbatim. Full record: `BUILD-NOTE-song-cut.md`. Will's 30 s intro (script: `INTRO-SCRIPT.md`) gets prepended when recorded — combined ≈ 2:58.

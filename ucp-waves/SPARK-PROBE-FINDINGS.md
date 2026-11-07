# Spark 1.3 contributor — probe findings (2026-11-06, Glint)

Will's pivot (16:52 PT): stop UCP site work; the contributor tokens exist to
test the model. The lead: Phase 0b's deterministic empty responses at token
caps + the model card's `reasoning_effort` dial (we had tried `reasoning`
during the hackathon and been rejected). 19 probe calls, all on
muse-spark-1.3-contributor unless noted. Raw results: battery1/2/2b/3/3d
-results.json in this folder; scripts spark_probe*.py.

## Battery 1 — the dial exists and works
Identical contradiction-check prompt (364 in / 28-char answer, ground truth
known), max_tokens 8000, all answers exact at every level:
- baseline x2: reasoning 2,586 / 2,635 (~2% spread — budgets are plannable), ~17.5 s
- low: reasoning 954 (-63% vs baseline), 7.8 s
- medium: reasoning 1,784, 15.6 s
- high: reasoning 2,855, 20.6 s
- xhigh: reasoning 2,743, 18.3 s
`reasoning_effort` is ACCEPTED on the contributor endpoint. The hackathon-era
rejection was the wrong parameter name. Unset behaves like the high/xhigh
band — the default thinks hard. Low still spends ~97% of its smaller output
on reasoning; the dial scales the amount of thinking, it doesn't switch it off.

## Battery 2 — 8,000 is not a parameter cap
max_tokens 16000 accepted (HTTP 200) on contributor AND standard
muse-spark-1.3. No rejection above 8000.

## Battery 2b — failed test, kept on the record
Brute-force enumeration (Items 1-3000) as a clamp test: BOTH tiers stopped
after 3 items and deflected — contributor offered code, standard offered
Items 1-100 chunks. finish_reason "stop", ~690 tokens. The model will not
brute-enumerate in chat; it pushes you to chunking. (Behavioral note, and
the reason 2b couldn't test the ceiling.)

## Battery 3 — the Phase 0b failure shape, 200 judged records
- 3a single / default / max 16000: 200/200 lines, 200/200 verdicts,
  completion 7,738 (reasoning 2,929), 40 s.
- 3b single / low / max 16000: 200/200, completion 6,180 (reasoning 1,571),
  21 s. Same accuracy, ~half the latency, ~20% fewer tokens.
- 3c Will's sequential shape (plan leg low -> verdicts externalized ->
  4 write legs of 50, low, max 8000): plan 200/200 verdicts correct;
  writes 200/200 lines, all correct; total completion 10,307 tokens,
  ~51 s serial. Works end-to-end. On easy per-item judgments it costs ~67%
  more tokens than 3b — its value is insurance and heavy-judgment staging,
  not efficiency on light work.

## Battery 3d — the ceiling test (decisive)
200 records, reasons forced to 40+ words, low effort, max_tokens 24000:
**completion 15,173 tokens, finish_reason "stop", 200/200 lines.**
There is NO 8,000 generation ceiling on the contributor tier.

## The correction
Our standing memory said "Meta API: max_tokens 8000 cap." That was wrong.
8,000 was OUR OWN call setting, carried as if it were Meta's limit. Phase
0b's empty responses were real — reasoning burning a budget — but the
budget was self-imposed. Wrong attribution, now corrected in MEMORY.md.

## Revised operating rules (verified, supersede the Phase 0b pair)
1. `reasoning_effort` is the control: extraction/mechanical legs -> low;
   judgment legs -> medium/high; unset = high-band default.
2. max_tokens is one budget covering reasoning + writing. Size it to the
   task; there is no 8,000 API ceiling (verified to 15,173 generated).
3. Empty responses are a budgeting failure: at default effort, reasoning
   scales with task hardness (2,586 on 24 judgments; 4,998 on the Phase 0b
   leg). Lower the effort or raise the budget — both levers are ours.
4. Sequential plan->write verified; use it when per-item judgment is heavy
   or one leg's budget would be tight. For light judgments, one low-effort
   call is cheaper and faster.
5. Repeated identical calls land within ~2% on reasoning tokens —
   near-deterministic; budget planning can rely on a first run's numbers.

## Cost
19 calls; ~61k completion + ~15k prompt tokens total. At published standard
rates (~$4.25/M out) that's ~$0.26; contributor-tier billing remains
unverified. Far inside the $25 envelope.

## Still open
- Confirm the fix on a real fact-sheet/Wave-1 leg (default vs low on a
  raw-source leg — the class that actually died in Phase 0b).
- Where the effort dial's quality floor is: Battery 1/3 tasks were
  mechanical judgments. A genuinely hard reasoning task at low vs xhigh
  (quality delta) is untested.
- Standard-tier comparison at scale (2/2b suggest same behavior family).

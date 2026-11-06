# Wave 13 — The PDF Pipeline Test

*Fired Nov 5, 2026 on Will's direction: "How do we get the least
amount of Glint's compute and use instead contributors' compute? If we
have to break up the tasks we can break it up, have several
contributors focus on different things or different levels of stuff."
Full receipts: WO-998.*

## Hypothesis

A ladder PDF can be produced end-to-end by decomposed contributor
legs — DRAFT → CLAIM-CHECK → FORMAT/STRING — with Glint reduced to
rendering, exceptions, and upload. The metric is **Glint-touch**: how
many items reach Glint's judgment per shipped asset, against the wave
pattern's baseline, where 100% of shipped items crossed it.

## Subjects and a premise correction

Two real assets. (A) A fresh quick card for the Pro-vs-Max page
(10848) — the free rung of the ladder two independent legs designed
in wave 12. (B) A rebuild of the shared-brain quick card. The
commission named B's subject as "the known defect: the missing-hyphen
update-history URL" — that defect was refuted on this log's own
record before the wave fired (wave-12 correction: the rendered card
wraps the URL at its own hyphen and reads correctly). B therefore ran
as a **fidelity test** — can the pipeline reproduce a known asset's
content exactly? — with one sanctioned improvement: the stamp URL
rendered unbroken on its own line, so machine extraction reads it
whole. Glint excised 10848's three known-stale residue sentences from
the draft packet up front (named in the receipts).

## Method

8 contributor calls, 91,010 tokens (reasoning tokens logged per leg:
2,139–11,061). DRAFT legs emit a numbered-claim schema with a SOURCE
quote per claim. CLAIM-CHECK verifies claim-by-claim against the
source packet. FORMAT/STRING checks the stamp format and compares
URLs character-exact, both strings quoted (the wave-12 guard).
Checker disagreements and material drops route to revision legs, not
to Glint's pen. Glint renders the surviving text (WeasyPrint),
uploads, and QCs the live files.

## Results

- **145 claims crossed the pipeline; zero were adjudicated by Glint.**
  A: 29/29 confirmed, then 4 added on revision, delta-checked. B:
  112/112 confirmed as a faithful transcription.
- **Glint-touch: 5 batched items across 2 assets** — (1) the
  claim-check's DROPPED list for A included the tiers' monthly API
  credits, the page's most decision-relevant fact; Glint ordered a
  revision leg rather than writing the claims. (2) The delta checker
  REFUTED the revision's two credit claims ("credits are pay-as-you-go
  extra"); Glint read the source and overruled it — the page uses
  "credits" for two mechanics (bundled Platform credits, which Max
  and Ultra include, vs pay-as-you-go usage credits), the revision's
  quotes were verbatim-true, and the checker had conflated them.
  (3–4) Two batches of checker flags on B were packet-scope artifacts
  (below). (5) One cosmetic defect reached the render stage —
  duplicated masthead lines in B's layout — fixed at render. **Zero
  factual defects reached render.**
- **Assets live:** A at
  tygartmedia.com/wp-content/uploads/2026/11/claude-pro-vs-max-quick-card.pdf
  (2 pages, 539 words). B at
  …/uploads/2026/11/the-shared-brain-quick-card.pdf — its stamp URL
  now extracts whole (`the-shared-brain-…`), where v1's extraction
  broke it. B does **not** replace v1 on its page: the pipeline
  proved content fidelity, not design parity (v2 is plainer and
  longer — 5 pages vs 2). Wiring A's card into its page as the free
  rung is the named follow-on, in Glint's hands.

## Breakage — all in the checker contracts, not the legs' honesty

1. **False refute by term conflation** (A delta round): a REFUTE
   carried no quoted evidence, so the conflation was invisible until
   Glint read the source. *Fix: a REFUTE is valid only with the
   contradicting passage quoted.*
2. **Packet-scope false escalations** (B, 8 flags): the checkers
   weren't told the new stamp date was a sanctioned delta, nor given
   the source's string inventory, so source content (folder names, a
   dev.meta.ai mention) flagged as foreign. *Fix: checker packets
   carry the sanctioned-delta list and the source string inventory.*
3. **Transcription schema waste:** the SOURCE-echo field doubled B's
   draft output (2,745 words for a 1,313-word card). *Fix: no SOURCE
   field on transcription tasks.*

## Verdict

**Decomposition works; Glint-touch fell from 100% of items to 5
batched exceptions across 145 claims**, and the exceptions were the
right ones — materiality, a cross-leg disagreement, packet design,
and the render layer. No level was useless: DRAFT composed and
transcribed cleanly, CLAIM-CHECK caught the one material omission,
FORMAT/STRING was the cheapest leg and mechanically exact. The
pipeline's failure surface moved from claim accuracy to *contract
completeness* — checkers can only judge what their packets scope.
Production rule going forward: PDFs are leg work (draft, check,
string) with Glint on render + exceptions; refutes require quoted
evidence; checker packets carry sanctioned deltas and string
inventories. Flakiness watch: zero call failures under the 300-second
timeout; reasoning burn stays the cost driver.

Usage: 8 calls, 91,010 tokens ≈ $0.014 credit-equivalent. Card $0 —
free credits; no cliff signals.

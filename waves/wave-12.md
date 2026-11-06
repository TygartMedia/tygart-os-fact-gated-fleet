# Wave 12 — The Ladder Test (WO-997)

**Nov 5, 2026 · 4 pages · 5 contributor calls · 44,372 tokens**

**Will's question:** "Can they try to do the ladders? Is there a way to have
them try and break and come up with a way that they can do the ladders?"

**Hypothesis:** contributor legs can verify and draft monetization ladders
(the series ladder: free PDF / $7 pack / $17 book-for-bots) under the fact
gate — provided identifiers stay verify-only.

**Method:** Three ladder-carrying pages got VERIFY legs (governing record
extracted verbatim from the live page + its free PDF, supplied in the
packet; legs compare, never recall). One ladder-less monetization page got
two independent DRAFT legs (ladder built from the page's own substance;
checkout links forbidden — a literal placeholder instead). One VERIFY
packet carried a **seeded trap**: a governing-record checkout ID with one
character flipped. Every return was then scanned mechanically: any
checkout ID or price not present verbatim in its packet counts as an
invention, by name.

## Breakage — the trap went through

On the seeded page, the leg returned **R3: MATCH** on the corrupted ID
item — quoting only the product name and button text. It never compared
the strings, because it couldn't: **page text extraction carries no
hrefs.** ID verdicts on text-only packets degrade to presence checks
wearing verification's clothes. A second leg on an unseeded page showed
the honest version of the same limit — it reported the ID items as
unverifiable-in-text rather than matching them. The failure mode is not
invention; it is **unverified agreement**.

## What held

- **Zero inventions.** Across all five returns, every checkout ID and
  price that appears exists verbatim in its packet (mechanical scan,
  reported in the receipts). The compare-only rule and the
  placeholder discipline — both draft legs used `[SQUARE LINK — GLINT
  WIRES]` and emitted no link or ID — held completely.
- **The pair checks caught a real production defect, unseeded:** the
  shared-brain quick card PDF prints its update-history URL as
  `the-sharedbrain-…` (missing hyphen) against the page's
  `the-shared-brain-…` — a one-character dead pointer of exactly the
  class the pairing rule exists to catch, found by character-for-
  character comparison of PDF vs page. (Fix queued with Glint: the PDF
  regenerates at the same URL; it does not ship inside a test wave.)
- **Drafting works.** Two independent drafters, given only the article,
  converged on the same ladder architecture — quick-card from the
  comparison sections, working pack from the worksheets, bot book from
  the full text — all contents traceable to page substance. One
  inheritance flaw, named: a draft carried the page's own stale
  break-even line into the $7 pack. Drafts inherit the source page's
  residue verbatim; the source must be audit-clean first.

## Verdict — contributor ladders: possible, with these guards

1. VERIFY packets must include the **href layer** (the extracted
   anchor→URL map). ID items require quoting BOTH strings; a MATCH
   without both quotes is contract-invalid.
2. PAIR checks (PDF↔page, character-for-character) work as-is and earn
   their place in every ladder packet — with scheme normalization so an
   `https://` prefix doesn't false-fire.
3. DRAFT legs may build ladder contents from an audit-clean page's
   substance, placeholder for every link, prices only as given.
4. All wiring — PDF builds, link placement, publish — stays with Glint.
   The legs produce verdicts and paste, never doors.

## Correction — Nov 5, 2026 (same day, after rendered-source verification)

The PAIR-URL "real defect" above is **downgraded: it was an extraction
artifact, not a PDF defect.** Rendered inspection of the card shows the
update-history URL wraps at its own hyphen — "…/the-shared-" / "brain-a-
company-brain-any-model-can-read/" — and reads correctly to a human; the
card also prints the full URL correctly on one line elsewhere. The
"the-sharedbrain" string existed only in pdftotext's join (it drops
line-break hyphens), which the packet's PDF record inherited and both
the leg and Glint read as ground truth. The follow-up PDF regeneration
is cancelled — there is nothing to regenerate.

The method verdict survives with one guard added: **a string defect
flagged from extracted text is a lead, not a catch, until the rendered
source confirms it** — the extraction-vs-DOM lesson this program has
now hit in two mediums. Residual truth, lesser but real: machine
readers that join lines the way pdftotext does will misread a
mid-slug-wrapped URL, so future cards should not break URLs mid-slug.
The seeded-trap and zero-invention results are unaffected.

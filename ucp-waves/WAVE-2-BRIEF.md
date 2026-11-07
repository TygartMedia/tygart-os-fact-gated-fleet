# WAVE 2 — Execution Brief (Consolidation, second tranche + pair-reads)

**Programme:** UCP full-site refresh — theuniversalcommerceprotocol.com
**Written:** 2026-11-06 (night run, after Wave 1 closed live) · **Scope: LOCAL STAGING ONLY.**
**Hard scope:** staged bodies + this log only. No site edits, no redirects created, no deletions, no authenticated requests. Bodies pulled via the public REST API (`GET /wp-json/wp/v2/posts/<id>`, `content.rendered`).

**Engine:** `muse-spark-1.3-contributor` via Meta Model API, runner `raw/run_leg_v2.py` — identical to Wave 1: PLAN legs `reasoning_effort=medium`, WRITE legs `reasoning_effort=low`, `max_tokens=16000` every leg, sequential plan→write per unit, one retry max and only after reading the actual error. Every call appended to the programme ledger `calls.jsonl` (47 calls at wave start).

**Judging material:** Sheets 1–8 (`sheets/`, earned 2026-11-06; half-life — no firing on them after 2026-11-20 without re-earn) + `UNJUDGEABLE.md` (10 classes → NEEDS-VERIFY by class, no argument) + `CLUSTER-MAP-V2.md`.

**Claim rule (Wave 1, carried):** claims no sheet covers → NEEDS-VERIFY and OUT of the staged body, UNLESS plainly author-voice/opinion or generic engineering practice, which rides LABELED as such (plan disposition KEEP-LABELED). A plan that contradicts a sheet loses to the sheet.

## Units

| Leg IDs | Unit | Members → canonical | Special contract |
|---|---|---|---|
| W2-F1 | D5 Troubleshooting five-way | 5459/5468/5751/5779/5447 → **5459** | CONSOLIDATE not concatenate: tight guide ~3,500–4,500 w, each distinct fix once |
| W2-F2 | N16 Measuring success six-way | 5761/5762/5763/5764/5765/5454 → **5761** | KPI/market numbers route by UNJUDGEABLE class |
| W2-F3 | N17 Pricing four-way | 5785/5398/5400/5067 → **5785 + 5400** (two canonicals, two staged bodies) | 5067 CLEARED DISTINCT (rate-card format) — plan confirms, excludes from merging; 5398's claims split by intent |
| W2-F4 | N18 Webhooks pair | 1480/1309 → **1309** | — |
| W2-F5 | N19 Payments auth pair | 1249/1256 → **1256** | 2026 edition supersedes |
| W2-F6 | N20 Monetizing pair | 5444/5450 → **5444** | — |
| W2-F7 | N14 fold test | 1721 vs **1908 LIVE body** (fetched live tonight; 1,266 w post-Wave-1) | Duplicate subset → staged REVISED 1908 folding unique material; distinct → KEEP-DISTINCT, no body |
| W2-F8 | Fictional-brand case studies | 5748/5749 → **5748** | Merged body MUST label brands/results plainly as illustrative/hypothetical — plan states exact labelling language, write applies it verbatim |
| W2-P1 | N1 SDK pair-read | 5780/5781 | Merge ONLY if plan convicts (near-identical, same job); else KEEP-DISTINCT, no write |
| W2-P2 | N10 Security best-practices pair-read | 1754/1916 | Same rule |

## Outputs
- `wave-2/staged/<canonical-id>.html` per merged canonical (F3: two files; F7: `1908.html` only if folding).
- `wave-2/WAVE-2-LOG.md` — Wave 1 format: per-unit verdicts, claim counts (keep/cut/NV), word counts (sources + staged), PROPOSED redirect map (not executed), per-leg engine data, programme running totals, diminishing-returns note.
- Raw replies in programme `raw/` as `W2-*.md`; prompts in `wave-2/prompts/`.

## Failure doctrine
A halted unit never halts the run: an API failure is logged verbatim and the run continues with the next unit. A skeleton write (far shorter than the plan's outline — the Wave 1 E3 defect) earns ONE corrective write leg, logged honestly.

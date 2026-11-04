# MANIFEST — repo staging for the Cerebral Valley submission

Staged 2026-11-03 (PT) for the Meta Global AI Developer Hackathon filing on Nov 4, 2026.
This folder is a **staging area only**: no GitHub repo has been created, nothing has been
pushed or published from it. Sources are cited by their path on the build machine so any
file can be diffed against its origin before the repo is created.

## Included files

| Repo path | Source | Notes |
|---|---|---|
| `README.md` | Written for this repo from `final/SUBMISSION-PACKET.md` (public text) + `model-bakeoff/NIGHT-LEDGER.md` | Spend figure is the current ledger counted total, **$102.50 of $153.31**; the packet's synced figure ($102.35) predates the closing corpus pick-out pass ($0.14481) — the delta is stated in the README and in the staged packet's own status lines. |
| `docs/SUBMISSION-PACKET.md` | `~/workspace/out/meta-hackathon-2026/final/SUBMISSION-PACKET.md` | Byte copy. |
| `docs/ROUTER-DESIGN.md` | `~/workspace/out/meta-hackathon-2026/ROUTER-DESIGN.md` | Byte copy (includes the Nov 3 correction of the "312 recordings" line to the verified scope, with pointers). |
| `docs/ONE-PAGER.html` | `~/workspace/out/meta-hackathon-2026/final/ONE-PAGER.html` | Byte copy (HTML source of the filed one-pager PDF). |
| `docs/reverse-mcp-landscape-report.md` | `~/workspace/research_notes/reverse-mcp-landscape-20261103-1735/report.md` | Copy with **one redaction**: a third-party company's public contact email was removed under the staging rule that only two email addresses appear in this repo (will@tygartmedia.com, jason@findingtrunorth.com — both already public in the packet's context). Redaction marked in place. |
| `docs/FEEDBACK-TO-META.md` | `~/workspace/out/model-bakeoff/FEEDBACK-TO-META.md` | Byte copy. |
| `docs/CONTRIBUTION-LOG.md` | `~/workspace/out/meta-hackathon-2026/contribution-sweep/CONTRIBUTION-LOG.md` | Byte copy. |
| `docs/NIGHT-LEDGER.md` | `~/workspace/out/model-bakeoff/NIGHT-LEDGER.md` | Byte copy, added Nov 4 on Will's direction to publish the full stats backbone — every experiment, its question, its cost, its verdict. Scan-checked on inclusion: no email addresses, no credentials, no card/phone data; carries run-machine paths like the other run records. |
| `docs/CONTRIBUTOR-LESSONS.md` | Written for this repo Nov 4 on Will's direction (the contributor-tier takeaways in one pull-able place) | Distilled strictly from `docs/CONTRIBUTION-LOG.md` finding #9, the ledger's per-call usage, and the packet's unit costs — every figure traces to those receipts, which are included alongside. No new claims. |
| `docs/MINED-INVENTORY.md` | `~/workspace/out/meta-hackathon-2026/corpus-pickout/MINED-INVENTORY.md` | Copy with **two redactions**: (1) the operator's personal Gmail address (quoted once from a session read-aloud summary, rec45) replaced with `[personal Gmail redacted]`; (2) a family member's first name in two read-aloud spine-table context cells replaced with "family". No other change; every verified finding quote is untouched. |
| `docs/EVIDENCE-INDEX.md` | `~/workspace/out/meta-hackathon-2026/submission-bundle/EVIDENCE-INDEX.md` | Byte copy. It cites receipt files by their build-machine paths; those receipts are deliberately not republished here (see Excluded). |
| `code/meta_api.py` | `~/workspace/custom-connectors/custom.meta-model-api/bin/meta_api.py` | The API helper every leg used. Contains **no key**: it routes through a surrogate-credential mechanism (`dynamic_credentials`, a platform module not included) that substitutes the real key only on the approved request to api.meta.ai. |
| `code/router/run_router_trio.py` | `~/workspace/out/meta-hackathon-2026/router-run/run_router_trio.py` | Router-design Trio runner. Secret scan: only token-*usage* field names; no credential values. |
| `code/contribution-sweep/sweep.py` | `~/workspace/out/meta-hackathon-2026/contribution-sweep/work/sweep.py` | Batched contributor runner. Same surrogate pattern; no credential values. |
| `code/corpus-pickout/runner.py` | `~/workspace/out/meta-hackathon-2026/corpus-pickout/work/runner.py` | Pick-out extraction runner (copy of the sweep runner pattern). |
| `code/corpus-pickout/verify_quotes.py` | `~/workspace/out/meta-hackathon-2026/corpus-pickout/work/verify_quotes.py` | Mechanical verbatim-quote verifier. Carries local absolute paths from the run machine (`/home/hatch/...`) — paths, not credentials. |
| `code/corpus-pickout/segment_spine.py` | `~/workspace/out/meta-hackathon-2026/corpus-pickout/work/segment_spine.py` | Read-aloud spine segmentation. Same local-path note. |
| `code/video-test/run_session.py` | `~/workspace/out/model-bakeoff/video-test/run_session.py` | Window scout over recording frames. |
| `code/video-test/synth.py` | `~/workspace/out/model-bakeoff/video-test/synth.py` | Session/user synthesis pass. |
| `code/video-test/synth_agent.py` | `~/workspace/out/model-bakeoff/video-test/synth_agent.py` | Agent-read pass. |

## Excluded — with reasons

**People and third parties**
- **Jason Gilstrap's private findings material** — `trunorth-reverse-mcp-2026-11-03/` Wave 3 receipts (`WAVE3-RECEIPTS`) and the notes inbox (`NOTES-INBOX.md`), and the private findings note prepared for Jason: **excluded.** They were prepared for Jason personally, were deliberately kept out of the judges' bundle for the same reason, and are not ours to publish. The packet's public TruNorth section states only what the receipts support, ending at the signature gate.
- **TruNorth run receipts and evidence PDFs** (`RUN-1/2/3.md`, drill receipts, ROM receipts, spot tests, and the 18 job-page PDFs in the bundle's `evidence-pdfs/` and `trunorth/` folders): **excluded from the repo.** They show the inside of a private TEST workspace belonging to a third party's real product; the Evidence Index cites them by path so the chain of proof is documented without republishing another company's screens.
- **Names/contacts beyond the packet's public text**: crew names from the TEST workspace (e.g., the sample job's PM and the imported test users), the raw drill receipts carrying full payer identities, street addresses, and claim numbers, and all email addresses other than the two public ones: **excluded or redacted** (see the redactions under Included). The drill scenario labels themselves (Whitaker / Edmond / Quail Creek) appear only as the submission packet's own public text already states them.

**Money and credentials**
- **Billing/payment material**: billing-console frames and any card data (a payment card is visible in the disqualified demo frames): **excluded, always.** Nothing in the staging tree contains a card number, a billing screenshot, or an account identifier.
- **Credential material**: no API keys, tokens, passwords, or vault contents exist in any included file — every runner used the surrogate mechanism, so there was nothing to redact. The platform's `dynamic_credentials` module itself is **excluded** (Muse platform internals, not project code).
- **TruNorth sign-in material** (reset emails, vault entries, the Oct 31 login-delivery email): **excluded.**

**Recordings and demo assets**
- **Disqualified recording frames** (rec4 — live API key on screen; billing frames — payment card; rec6 f0090; rec5 — a third-party application and a phone number; rec2 — API-key handling): **excluded.** They were disqualified from the demo's leak scan and are disqualified here.
- **The raw recording corpus** (~36,000 frames, per-recording transcripts and window reads): **excluded as bulk.** The curated, quote-verified layer is `docs/MINED-INVENTORY.md`; the raw corpus is working material from the operator's own sessions and is not published wholesale.
- **Demo videos** (flagship and all fallback cuts): **excluded from the repo.** The flagship is hosted as the submission's YouTube demo; 57 MB binaries don't belong in the repo.
- **The 9-slide deck** (`meta-hackathon-submission.pptx`): **excluded** — a presentation binary filed through the portal, not repo material.

**Working papers and one-off scripts** (excluded as scaffolding; the distilled public forms are included instead)
- Router run raw legs, attempts, and the input brief (`router-run/*-raw.md`, `BRIEF.md`, `runs.jsonl`) — superseded by `docs/ROUTER-DESIGN.md`.
- Contribution-sweep prompt generators and graders (`gen_a.py`, `gen_b.py`, `det_check.py`, `check_leg3.py`), job JSONLs, logs, and the frozen input snapshots under `contribution-sweep/inputs/` — the log (included) is the record; the snapshots duplicate the packet/router text they audited.
- Corpus pick-out job files, results JSONs, and section generators (`build_jobs.py`, `gen_sections.py`, `jobs-*.jsonl`, `results-*.json`) — the inventory (included) is the deliverable.
- Other video-test leg utilities (transcription runners, consensus-miner chain, report-stats and spend-tally scripts) — real run code, but the three included readers are the method the submission describes; the rest is one-leg scaffolding. Available on request from the run record.
- `ONE-PAGER.pdf` and its pre-sync backups — the PDF is a portal upload; its HTML source is included instead.
- `submission-bundle/READY.md` and the bundle folder itself — an internal filing checklist and container, not project documentation; its claim map (the Evidence Index) is included.
- `PLAN.md`, `STORYBOARD.*`, `VALUE-CHAIN-ANALYSIS.md`, narration scripts, build notes, and all `work*`/`final-v2` build folders — production scaffolding for the demo, not the project's public record.

## Leak scan

Run over the entire staging tree before this manifest was finalized. Patterns checked:
API-key shapes (provider key prefixes, bearer headers, key-assignment literals),
phone-number shapes, a payment-card suffix, all email addresses, a hosting-provider
name tied to the private TEST workspace, the name of a TEST-workspace crew member, and
every "password" mention reviewed by eye. (The scan's target strings are deliberately
not reprinted here — a manifest certifying an absence shouldn't carry the strings it
certifies against.) Any hit not resolved by redaction or exclusion would be listed
here — **none remain unresolved.** The surviving "password" mentions are narrative —
a login-friction quote and the API helper's docstring explaining that the key is
vault-stored and never read by the script. No values, no locations, no hints that
retrieve anything. The only email addresses in the tree are the two public ones named
in the Included table above.

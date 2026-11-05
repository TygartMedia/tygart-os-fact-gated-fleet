# For the Judges — Tygart-OS: The Fact-Gated Fleet

**Tygart Media · Startups track · Problem statement: Build for Your World**
Meta AI Developer Hackathon — submitted November 4, 2026.

This page maps the entry to the four judging criteria. Every number below traces to a file in this repo — start with [docs/EVIDENCE-INDEX.md](docs/EVIDENCE-INDEX.md).

**Demo first:** [Tygart-OS on Meta Muse: The Fact-Gated Fleet — demo](https://www.youtube.com/watch?v=8xg3_UqEAPk) (2:38 filing cut)

## Impact — 30%

- This is a production system running a real business, not a prototype built for the hackathon. Tygart Media is an AI-first agency serving restoration contractors, and the fleet in this repo does its daily work: research, drafting, checking, and publishing across a network of niche sites whose pages live on being cited by AI answers.
- Corpus processed end-to-end during the build: **312 pages** and **174 session recordings** — checked, routed, and read back, with receipts for each leg.
- Of the entries publicly visible during judging week, this is the only one we could verify that is already operating a business rather than demonstrating a concept.

## Use of Meta AI Tooling — 25%

- The core is a **Muse Spark trio**: a scout at low reasoning, a fixer at medium, and an adjudicator at max. Each stage checks the previous one against source material; the adjudicator can strike anything ungrounded.
- The contributor tier was tried first and **failed the gate on token limits** — that failure is what forced the low → medium → max mapping. Contributor now handles bulk ingestion under a contributor-first rule, with every run logged by purpose in [docs/CONTRIBUTION-LOG.md](docs/CONTRIBUTION-LOG.md) and the lessons written up in [docs/CONTRIBUTOR-LESSONS.md](docs/CONTRIBUTOR-LESSONS.md).
- Filed feedback to Meta from real use — including video input silently flattening to a still frame — is in [docs/FEEDBACK-TO-META.md](docs/FEEDBACK-TO-META.md).
- The full spend is public: **$102.50 of the $153.31 envelope**, itemized in [docs/NIGHT-LEDGER.md](docs/NIGHT-LEDGER.md).

## Technical Depth — 20%

- **Fact gates:** every emitted field must carry its grounding quote from the source. An empty quote means the field doesn't ship. In the run documented in the submission packet, the fixer proposed adding "and any crime / funds-transfer extension" to a coverage page; the adjudicator struck it verbatim — that product concept was in neither the page nor its sources.
- **Reverse-MCP routing:** the destination's accepted shape constrains what the model may emit, instead of the model free-writing and a formatter cleaning up after it. Design: [docs/ROUTER-DESIGN.md](docs/ROUTER-DESIGN.md).
- **Emblem round-trip test:** 312 site emblems described by the model and regenerated from the descriptions alone — structure recovered 312/312, palette 311/312. Named failures and edge cases are in [docs/FIELD-NOTES.md](docs/FIELD-NOTES.md).
- **Honest split, stated plainly:** the checking pipeline is production and runs daily. The routing decision is measured. The tip registry and tip-learning layer are designed, not built — the design doc says so, and so do we.

## Demo — 25%

[Watch the demo](https://www.youtube.com/watch?v=8xg3_UqEAPk) — 2:38, with chapters:

- **0:00** The fact-gated fleet
- **1:54** By the numbers: $102.50 of $153.31
- **2:01** Saying it plain
- **2:07** Receipts, Not Claims

The full submission packet is [docs/SUBMISSION-PACKET.md](docs/SUBMISSION-PACKET.md).

---

Receipts, not claims.

# SHEET 2 — AP2 (Agent Payments Protocol)

**Earned: 2026-11-06 · PHASE 0b, UCP wave program**
**Purpose:** judge every site claim about AP2 mandates, status, and its relationship to UCP.
**Sources:** AP2 specification repository README + specification overview (ap2-protocol, GitHub — primary text below the line) · AP2 project documentation/status synthesis (dossier level) · Google UCP FAQ — https://developers.google.com/merchant/ucp/faq · UCP specification (AP2 extension) — https://www.ucp.dev/latest/specification/overview/
**Provenance codes — read them before trusting a line:** [L10] = contributor leg L10's extraction of the **primary spec-repo text** (README + spec overview), Glint spot-checked · [L3] = contributor leg L3 (documentation/status dossier — one level below primary) · [Glint] = read directly by Glint.
**Version-status warning (Glint, from the primary text itself):** the repo README says AP2 was "first published by Google in September 2025 with version 0.1" and that "our next step is to launch v0.2" — while the dossier records v0.2 as released 28 April 2026. The repository's own front door lags its release record. Waves judge AP2 claims against the mandate model below and treat any version claim with this lag in mind.

## What AP2 is [L10 primary + L3]

1. AP2 is an open protocol providing the foundation for secure, reliable agentic commerce; first published by Google in September 2025 (v0.1).
2. AP2 lets an AI agent prove a person authorized a specific purchase: signed mandates provide strong evidence of the user's actual intent, intended to mitigate LLM nondeterminism, prompt injection, malicious tools, and errors in planning/tool calling.
3. AP2 is an authorization and evidence layer, **not a settlement rail** — it does not move money.
4. AP2 is rail-agnostic: it defines how parties transact across Cards, Real-Time Payments, Digital Wallets, Push Payments, and Direct Debit & Credit Transfers. It separates authority (who can pay, for what, up to how much, until when) from mechanism (which rail moves the money).
5. Its three stated aims: **authorization, authenticity, accountability**.

## Mandates — the primary-text model [L10]

6. The **root mandate** is an object signed by the user on a **Trusted Surface**, granting the agent authority to perform the protocol's operations according to specified constraints.
7. Mandate types in the specification overview: **transaction mandate**, **checkout mandate**, **refund mandate**, **recurring payment mandate**, plus **credential requests**.
8. The **transaction mandate** instructs a payment processor to execute a transaction; it contains a cryptographic hash of the mandate(s) it references; it is distinguished as **open** (tasks/target not yet fully determined) or **closed** (tasks/target fully determined).
9. The **checkout mandate** records the user's consent to the final checkout contents and payment; it is signed by the user on a Trusted Surface and **verified by the Merchant**.
10. The **refund mandate** (open or closed) instructs a payment processor to refund a previously executed transaction; the **recurring payment mandate** (open or closed) instructs it to set up a payment schedule.
11. **Credential requests** enable a payment processor to request payment credentials from a Credential Provider.
12. The transaction mandate is ensured to reference at least one checkout mandate, at least one payment mandate (which itself references the checkout mandate), at least one refund mandate, and at least one recurring payment mandate — forming a **chain of mandates**.
13. **Payment mandates are secured using SD-JWTs.** The complexity of signing and SD-JWT processing is handled by Credential Providers, so Merchants implement only the simpler JWT validation over the transaction and payment mandates.
14. Delegation is modeled with **User Present** and **User Not Present** sessions; User Not Present sessions may optionally reference User Present sessions, validated by the Credential Provider — enabling delegation to agents and charging without the user actively participating.
15. The **Trusted Surface** must be a deterministic interface for displaying mandate content and capturing cryptographic approval signatures; it is **never an LLM**.

## The v0.1 → v0.2 vocabulary shift [L3 — dossier level]

16. v0.1 defined three mandate types as W3C Verifiable Credentials: Intent Mandate, Cart Mandate, Payment Mandate.
17. v0.2 (released 28 April 2026 per the dossier) reshaped the vocabulary: Intent and Cart Mandates became open and closed forms of a Checkout Mandate and a Payment Mandate. **Note the tension with item 8:** the primary spec overview applies open/closed to the *transaction* mandate. A site page is judgeable on which vocabulary it uses and whether it dates it; the two vocabularies must not be blended.
18. v0.2 added human-not-present flows (pre-authorize now, agent completes later) and uses OpenID for Verifiable Presentations 1.0 for user credential delegation. SD-JWT was published as RFC 9901 in November 2025.
19. The core primitive framing in project documentation: the Verifiable Digital Credential (VDC) — tamper-evident, cryptographically signed, W3C VC conventions, verifiable offline, revocable via standard VC revocation lists.

## Status and governance [L3 + L10]

20. On 28 April 2026 Google **donated AP2 to the FIDO Alliance**; FIDO announced an Agentic Authentication Technical Working Group and agent-commerce work in its Payments Technical Working Group. (Not stated in the spec-repo text — [L10]'s own NOT IN THIS TEXT finding; dossier-level only.)
21. Status as of 31 October 2026: **no FIDO specification has been published; no live Google product is documented as using AP2 in production.** Pre-1.0 — mandate schemas can still change.
22. The A2A x402 extension is described as production-ready for crypto settlement carrying AP2 mandates; card-based AP2 paths are described as maturing through 2026 (pilots, rolling availability — not universal merchant support).

## Relationship to UCP [Glint + L10]

23. The AP2 spec overview itself positions AP2 "for use by existing commerce protocols such as the Universal Commerce Protocol (UCP) as a specialized payment layer."
24. UCP carries AP2 as an extension: `dev.ucp.common.payment.ap2_mandate` (integrated into the UCP spec by PR #788 in v2026-08-25 — Sheet 1, Annex A); UCP's autonomous-agent payment scenario (Scenario C) runs on AP2 mandates.
25. Google's FAQ, verbatim sense: AP2 is "our standard for secure, agent-led payment transactions… a specialized payment layer within UCP," while UCP orchestrates the broader purchase lifecycle.

## Risks named in the sources [L3]
Wide open mandates; double spend; weak agent key custody; constraint bugs; unit mismatches; liability left to payment networks.

## NOT SETTLED BY THESE SOURCES
- Field-level mandate schemas (the spec overview settles the model, not the fields).
- Whether the current spec text is v0.2 (the README still frames v0.2 as upcoming — item-level conflict preserved above, not resolved).
- Any production deployment of AP2 anywhere; any FIDO publication date.
- Independent corroboration of the "production-ready" A2A x402 claim beyond project materials.

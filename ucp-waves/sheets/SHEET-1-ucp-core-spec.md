# SHEET 1 — UCP Core Specification

**Earned: 2026-11-06 · PHASE 0b, UCP wave program**
**Purpose:** the sheet every UCP wave judges against. Pins the current specification, its extension/capability model, and the Aug-2026 release that supersedes the version Google's merchant surfaces still teach.
**Sources read (primary):** UCP specification overview, latest line — https://www.ucp.dev/latest/specification/overview/ · UCP GitHub release record — https://github.com/Universal-Commerce-Protocol/ucp/releases · Google merchant FAQ (payments/identity context) — https://developers.google.com/merchant/ucp/faq
**Provenance codes:** [L1] / [L8] = contributor legs' extractions of the spec overview (Glint spot-checked) · [Glint] = verified by Glint directly against the primary source this session · [L7] = contributor leg L7's extraction of Glint's release-record dossier.

## The pinned version fact

1. The current published specification is **v2026-08-25**, marked "Latest" on the project's GitHub release record. [Glint — release list read 2026-11-06]
2. The full release sequence is: 2026-01-11 · 2026-01-23 · 2026-04-08 · 2026-08-25. There is **no March 2026 release**; any site claim of a "March 2026 update" adding named features is false on its face. [Glint]
3. Google's merchant surfaces and documentation implement and teach **2026-04-08**; the version gap is structural and recurs under a quarterly cadence. (Sheet 3 carries the platform side of this split.) [L7, Glint]

## Discovery and profiles [L1, Glint spot-checks]

4. A business MUST host its profile at `/.well-known/ucp`; a platform advertises the URI of its own profile in the `UCP-Agent` header on every request.
5. `ucp.version` is a REQUIRED field of every profile; `ucp.services` and `ucp.payment_handlers` are likewise required.
6. Capabilities are named `{reverse-domain}.{service}.{capability}`; the `dev.ucp.*` namespace is reserved to the specification itself.
7. Schema URLs are authority-bound: a platform MUST NOT fetch schemas on authority mismatch and MUST NOT follow HTTP 3xx redirects on schema fetch (SSRF guards are part of the spec, not implementation taste).
8. A capability's `version` field is a date string in `YYYY-MM-DD` form.
9. Since v2026-08-25, capabilities version independently of the core release, and capability maps order by `namespace` (`map_order`).

## Payments [L8 + L1 + Glint]

10. The spec defines three payment scenarios: **A** Digital Wallet (Business Advertisement → Token Execution, platform side → Complete Checkout); **B** Direct Tokenization with Challenge / SCA (same, plus Challenge Required); **C** Autonomous Agent / AP2 (Business Advertisement → Agent Execution → Complete Checkout).
11. Payment handlers are advertised in the business profile's `ucp.payment_handlers`; a handler entry carries `id`, `version`, `spec`, `schema`, `available_instruments`, and `config` (example: a CARD instrument with a PUSH tokenization specification). The `{reverse-domain}.{service}.{capability}` naming shape governs capabilities and does **not** apply to payment handlers.
12. Payment moved out of the shopping namespace in v2026-08-25: split payments, payment terms/schedules, and AP2 mandates live under `dev.ucp.common.payment.*`.
13. The **AP2 Mandates Extension** is part of the specification: `dev.ucp.common.payment.ap2_mandate`. (Sheet 2 carries AP2 itself.)
14. v2026-08-25 payment additions: deferred payments, deposits, installment schedules, and multi-instrument Split Payments; vendor-agnostic 3DS2 via the new Actions primitive (Device Data Collection + Challenge), response-carried `$requestConstraints`, and split PAN / network-token credentials. [Glint — release notes read 2026-11-06]

## Identity, keys, consent [L8 + Glint]

15. v2026-08-25 overhauled identity & consent: reverse-DNS consent, delegated IdPs, and **canonical profile keys `keys[]`** (a JWK set) replacing the legacy `signing_keys[]`. Every verifier reads `keys[]`.
16. Example key material in the spec: an Ed25519 OKP key for HTTP transport identity (Web Bot Auth), and an ECDSA P-256 key for AP2's `ap2.merchant_authorization`.
17. A business not using AP2 or Web Bot Auth may publish a single ES256 key.

## The v2026-08-25 delta, condensed [Glint — release notes]

18. Multi-vertical refactoring: Food/Lodging foundation, polymorphic token binding, vertical-agnostic payment.
19. Grocery readiness: Location Search & Lookup capabilities, deterministic operating hours, fractional quantities.
20. Loyalty extension formalized across Catalog, Cart, and Checkout (with a backport to 2026-04-08 noted in the release notes).
21. Governance/cadence detail (councils, quarterly cadence, verticals) is carried in Sheet 3, items sourced from the same release record via leg L7.

## Wave-facing corrections this sheet settles

- Any page teaching header-only or DNS-based merchant authentication for UCP is superseded — verification is signature-based (Sheet 3 carries the full RFC 9421 ES256 rules).
- Any page describing the spec as "three core capabilities" (checkout, identity linking, order management) understates the capability model above.
- Any page attributing Mastercard's Verifiable Intent framework to UCP is wrong — VI is Mastercard's, co-developed with Google (Sheet 5).
- Any page saying "Google launched AP2 alongside UCP" reverses the chronology: AP2 is September 2025, UCP is January 2026 (Sheet 2).

## NOT SETTLED BY THESE SOURCES
- The normative definitions under the spec overview's Error Handling / Error Codes / `continue_url` headings — leg L8 confirms the excerpt lists the headings without providing the definitions; error-code claims in waves judge against Sheet 3's FAQ-derived codes until a deeper spec extraction is logged.
- Full Platform Requirements, Business Requirements, and Intersection Algorithm steps (leg L1's own NOT SETTLED list) — the spec-overview extraction truncated at the 8,000-token cap twice; both attempts are ledgered in PHASE-0B-LOG.md.
- Spec content on `main` after 2026-08-25 (e.g., the return-policy extension that landed Oct 23, 2026) — post-release, not part of the pinned version.

## Annex A — v2026-08-25 release-notes extraction, PR-traceable [L9 + L9b]

*Source: the verbatim "What's Changed" body of the official v2026-08-25 GitHub release. Each line is a release-notes entry; PR numbers are the trace. Note what the extraction method cost: leg L9's first try returned 0 visible characters (reasoning 7,998/8,000) and its second try truncated mid-list at the cap — the remainder was completed by leg L9b on a pre-grouped subset. Both behaviours are ledgered in PHASE-0B-LOG.md and `calls.jsonl`.*

**Structural:** UCP Commons (Core) introduced (#765); core negotiation improvements (#789); Version / Version Negotiation strategy (#957) with version-negotiation changes (#974); Version Freeze and Change Management Strategy (#958); change-management readme alignment (#799); required plugin/extension support guidelines (#843); structured scope documentation (#815); scope endorsement bonus interactions (#818); developer controlled regions (#820); idempotency keys in core primitives (#884); protocol HTTP headers and signing keys (#955); explicit absolute timezone offsets, algorithm 1 (#849); API request types / error handling and status-code specs (#950, #900, #1007); ontology ttl/owl superclass fix (#663); `srv` field removed from binary artifacts (#850); `checkout.reverse_dns` marked deprecated (#851); sample profiles fixed (#751, #903); frontend spec updated (#864).

**Catalog:** generic product search lookup fixed/added (#747); product path in search results (#971); product vs variant titles differentiated (#747); page metadata and variant details (#963); location capabilities for inventory, tax, pricing, pickup availability (#749); inventory levels handled (#750); location autocomplete (#868); currency units and location-based pricing (#870); payment information incl. payment plans in catalog (#844); weight-based products and fulfillment lines (#846); max quantity markup (#739); `max_selling_quantity` (#852); eligibility/lifetime-unit copy (#828); zeta-code province/state variants (#810); featured products (#983); `dev.ucp.common.shopping.products` added to catalog (#996); ISO 4217 currency exponent in catalog and checkout (#886); currency code in cart/checkout totals (#917).

**Cart & Checkout:** **Breaking Change in Cart (#659)**; checkout cleanup (#666); invalid `line_items` returns 422 (#593); variant order restricted (#812); line items distinct from checkout line identifiers (#813); `delay` option for multi-line-item updates (#698); rollback of quantity additions (#889); cart quantity-update best practices (#921); structural total-order-amount representation (#787); subtotal with currency code (#827); handles for customization options — *extraction truncated here in L9's second try; the entries below the cut are covered by L9b where grouped, otherwise not extracted*.

**Payments:** `dev.ucp.payment.instruments` schema refactor (#933); placeholder fields in payment handlers (#940); idempotency key header for payment handlers (#946); EBT/SNAP support in payment handlers (#925); crypto-currency data specs (#942); `crypto_payer` for crypto payments (#1000); in-store pickup payment method (#1019); query available payment methods across a range of amounts (#1008); **Split Payments in Checkout (#1001)**; partial capture (#1024); one instrument across multiple authorizations (#890); multiple payment instruments (#891); recurring payments (#954); instalment payment plans extension (#853); SEPA payments cross-document spec (#1026); `dev.ucp.common.payment.validation` (#1027); payment credentials specification (PCI-DSS) (#875).

**Identity, consent & trust:** identity linking consent flow added (formerly RFC) (#753); Buyer Consent Extension (#775); trust chain specifications in profile exchange (#923); Trust Models (#837); profile max-age cache policy / key TTL (#1005); **AP2 integration (#788)**; identity-linking OAuth scope + consent-flow docs (#951).

**Orders:** Order management documentation in the Order extension (#909); protocol orders webhook (#956); Order Total Amount Adjustment (#1016); Order Change Summary (#1017); order CTA total amount (#992); order example postal_code requirement (#748); namespaced metadata in validation_errors and fulfillment events (#782).

**Other extensions & checkout features shipped in this release:** fulfillment preferences (#920); B2B checkout requirements (#879); B2B invoices extension (#1023); recurring buys and subscriptions (#883); Tokenized Checkout Flow for Represented Parties (#910); buy-one-get-one extension (#967); post_purchase_extensions (#988); embedded checkout extension (#989); RFQ (Resource for Quote) extension (#947); Reservation extension (#808); coupon extension (#767); loyalty programs in Catalog/Cart/Checkout (#949); Loyalty integration specs (#1022); certifications/awards in merchant profiles (#911, #941); address line 3 + confidence interval in address verification (#859); required human authentication UX trigger (#874, #924); per-checkout readiness checks (#898).

**NOT IN THESE NOTES (L9's own finding, preserved):** the release-notes body is a PR list. It does **not** itself state the programme-level prose an auditor might expect — no directed marketing language, no versioning-policy narrative beyond the PR titles, and no vertical names beyond what individual PR titles name (Food/Lodging scaffolding, #825). Any sheet line about the Aug-25 *narrative* (multi-vertical framing, grocery readiness, 3DS2/Actions, payment schedules) rests on Glint's direct read of the release record and the spec overview (items 14, 18–20 above), not on this annex.

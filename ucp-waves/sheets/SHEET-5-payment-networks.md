# SHEET 5 — Payment Networks (Visa, Mastercard)

**Earned: 2026-11-06 · PHASE 0b, UCP wave program**
**Purpose:** judge site claims about Visa's Trusted Agent Protocol / Intelligent Commerce and Mastercard's Agent Pay family, including Agent Pay for Machines.
**Sources:** Visa TAP specification/repo and Intelligent Commerce materials; Mastercard Agent Pay and Agent Pay for Machines primary pages and announcements (mastercard.com read directly for AP4M); co-developed-framework materials for Verifiable Intent.
**Provenance:** [L5] = contributor leg L5 (ran clean, finish=stop; networks kept strictly separate) · [Glint] = read directly by Glint this session.

## VISA [L5]

1. **Trusted Agent Protocol (TAP)** was released 14 October 2025, developed with Cloudflare. TAP is the merchant-side identity specification of **Visa Intelligent Commerce** (Visa's agentic-commerce umbrella; Visa's own page describes Intelligent Commerce as "currently in the process of deployment").
2. TAP is built on **HTTP Message Signatures (RFC 9421)**. The merchant's primary task is to validate the agent's signature: parse `Signature-Input`/`Signature`, fetch the key by `keyId` from an agent registry, verify the signature.
3. TAP signature algorithms are **Ed25519 or RSA-PSS-SHA256** — **not ES256**. (ES256-over-RFC-9421 is Google UCP's choice; conflating the two is a known site error class — keep them separate.)
4. The signature's `tag` distinguishes intent: `agent-browser-auth` (browsing) vs `agent-payer-auth` (payment). The Agent Recognition Signature's `Signature-Input` covers `@authority`, `@path`, `created`/`expires` (maximum ~8-minute validity), `keyid`, algorithm, a unique `nonce`, and the tag.
5. TAP's three components: **Agent Recognition Signature**, **Consumer Recognition**, and the **Agentic Payment Container** (a request-body payload carrying payment credentials).
6. Visa publishes agent public keys at `https://mcp.visa.com/.well-known/jwks`.
7. **Licensing:** TAP's repository code is governed by the **Visa Developer Center Terms of Use** — proprietary, **not an open-source license**. The underlying RFC 9421 is an open IETF standard; the protocol-specific layers (registration, key management, three-signature model) are Visa's design.
8. Production TAP use is **enrollment-gated**: Intelligent Commerce vetting plus Visa Developer Platform approval. The reference registry is self-hostable, but actual Visa TAP status requires Visa's vetting.
9. Intelligent Commerce issues agent-specific pass-through payment tokens bound to a consumer's passkey, via APIs and a self-hosted MCP server on Visa Developer. Visa positions itself as **protocol-agnostic**: TAP, x402, MPP, ACP, and UCP through one integration.
10. **Intelligent Commerce Connect** (announced 8 April 2026) lets merchants accept agent payments across **TAP, ACP, UCP, and MPP** (Visa and non-Visa cards) through one Visa Acceptance Platform integration. Status October 2026: **pilot with select partners**.
11. **First live TAP pilot — 20 October 2026:** Visa, BILL, and Billtrust: a registered BILL Payment Agent authenticates via TAP and Visa's Agentic Directory, then pays pre-approved supplier invoices with tokenized credentials — real money between two real platforms. TAP also has live transactions in Europe (reported October 2026).
12. **Disputes:** for transactions processed on or after **24 October 2026**, Visa's Compelling Evidence 3.0 (Dispute Condition 10.4) includes an agent-specific clause: an agent provider's login ID can serve as one of the matching data elements tying an earlier undisputed transaction to a disputed one.
13. Visa is **not** on Google's AP2 partner list.

## MASTERCARD [L5 + Glint]

14. **Agent Pay** was announced 29 April 2025 (partners Microsoft, IBM, Braintree), built on two pillars: **Agentic Tokens** (an extension of MDES) and **Verifiable Intent**. By 2026 the framework is available through Mastercard-certified processors; Mastercard's CEO confirmed the first agentic transaction completed on the network in Q4 2025.
15. **Verifiable Intent** is co-developed with **Google**, formally introduced 5 March 2026, with pilots from February 2026. Format: **SD-JWT + Key Binding (RFC 7800)**. It is protocol-agnostic and was **donated to the FIDO Alliance**. Any party can challenge an unauthorized transaction, with existing chargeback processes resolving disputes. (Site claims attributing VI to UCP invert this — VI is Mastercard's framework.)
16. Skyfire's **Know Your Agent** scoring was added to Agent Pay 30 September 2026; Mastercard is also working with Visa and Ant International on a KYA framework.
17. **Agent Pay for Machines (AP4M)** was **announced 10 June 2026** (Mastercard press release) — the October date is its Early Access opening, not the announcement. AP4M is a service for machine-to-machine, always-on, high-frequency low-value payments (including microtransactions and fractions of a cent), permissioned, orchestrated, and settled at machine speed; 30+ industry participants at announcement (incl. Adyen, Checkout.com, Coinbase, Stripe, Tempo, OKX, Ripple).
18. **Early Access opened 20 October 2026** at Cloudflare Connect: first buyer- and seller-side APIs, a developer toolkit, a sandbox and documentation (ap4m.build), enrollment by request; **not commercially available**. Seven end-to-end pilots were completed ahead of the opening: Cloudflare, Ant International, AIsa, Base, BVNK, Coinbase, Hype.
19. The public demo (Mastercard's own account, read by Glint): agency **Hype** gave an AI agent a campaign task and a defined budget; after a two-step plan (social research from AIsa; campaign images through Cloudflare AI Gateway) and **one approval of the funding**, the agent completed **nine payments to two independent merchants** with no per-payment human approval and no separate accounts, API keys, or invoices.
20. AP4M's mechanism: on a `402 Payment Required` response, the agent creates a **digitally signed payment voucher** — a secure promise to pay within its approved limit; the provider verifies the voucher and delivers the service; interactions happen **off-chain at machine speed**; providers can combine vouchers and redeem them later (deferred settlement). Coinbase Developer Platform provides wallet infrastructure; Base provides on-chain settlement; BVNK acts as the agent wallet via Mastercard Global Money Platform; settlement in fiat or stablecoins.
21. AP4M **builds on x402** (Mastercard's words: "an open protocol that lets digital services request payment online") and supports credentialing, controls, and guaranteed settlement across payment types, cards to stablecoins.
22. AP4M status: pilot-stage; no commercial availability date announced.

## NOT SETTLED BY THESE SOURCES [L5]
- Visa: full enrollment/vetting criteria, timelines, fees; scale and value of European transactions and the BILL/Billtrust pilot; registry/Agentic Directory governance and key rotation/revocation mechanics; liability outcomes beyond the CE 3.0 login-ID clause; commercial dates for Intelligent Commerce / Connect.
- Mastercard: the certified-processor list, pricing, commercial dates; scale of the Q4 2025 transaction and the seven pilots; full technical specs for Agentic Tokens and Verifiable Intent; KYA scoring methodology; voucher redemption timing and failure handling; FIDO status of the donated Verifiable Intent; the joint KYA framework's status.

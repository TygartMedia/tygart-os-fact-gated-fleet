# SHEET 8 — Identity: DID / Decentralized Identity vs UCP's Actual Identity Model

**Earned: 2026-11-06 · UCP wave program, gap-sheet earn (Will's tap, 17:26 PT)**
**Purpose:** settle what UCP's specification actually defines for identity, and whether DIDs, DID documents, verifiable credentials on ledgers, DIDComm, smart-contract DID checks, or blockchain transaction recording are part of UCP — the claims Wave 1 clusters D1 (27 items), D4 (15), and E5's component list lean on.
**Sources read (primary):** UCP specification, latest line, pinned v2026-08-25 — https://www.ucp.dev/latest/specification/overview/ ("Identity & Authentication" section read in full; complete text searched) · UCP Core Concepts — https://ucp.dev/documentation/core-concepts/ · Google UCP merchant FAQ (identity-linking entry) · W3C Verifiable Credentials Data Model (for what a DID/VC *is* — primary for the concepts, not for UCP support) · Sheet 1 (this programme, earned 2026-11-06) items 15–17 + Annex A.
**Provenance codes:** [Glint] = verified by Glint directly against the primary source this session · [G8] = contributor leg GAP8-IDENTITY's structured verdict on Glint's dossier (spot-checked by Glint; no leg-added facts) · [S1] = already earned on Sheet 1.

## HEADLINE VERDICT

**UCP's identity model is profile-and-key based. It contains no decentralized-identity layer at all.** Full-text searches of the complete spec overview found **zero** occurrences of "decentralized identifier," "blockchain," "smart contract," and "verifiable credential," and no substantive occurrence of "DID." Every DID/VC/ledger/smart-contract claim the site's posts attribute to UCP is a **misattribution**: those are real, separate technologies (W3C DID/VC, DIF DIDComm) that UCP does not adopt, reference, or build on. [Glint + G8]

## What UCP's identity model actually is (settled)

1. **Profiles do double duty.** A UCP profile declares capabilities *and* publishes signing keys. Businesses publish at `/.well-known/ucp`; platforms advertise their profile URL per-request in the `UCP-Agent` header. Discovery and authentication resolve from the same document — this is what enables "permissionless onboarding." [Glint — spec Identity & Authentication + Core Concepts profile structure]
2. **Authentication mechanisms — the complete spec list:** API Keys (pre-shared, out-of-band), OAuth 2.0, mTLS, and HTTP Message Signatures (RFC 9421). Only HTTP Message Signatures enable permissionless interaction; the others imply a pre-established relationship. [Glint]
3. **Keys:** verifiers read the top-level **`keys[]`** — a canonical RFC 7517 JWK Set in the profile. Defined key types: EC (ECDSA P-256/P-384) and OKP (EdDSA Ed25519). [Glint + S1 item 15]
4. **Identity binding:** regardless of mechanism, verifiers MUST ensure the authenticated identity is consistent with the `UCP-Agent` header. [Glint]
5. **The only identity capability is `dev.ucp.common.identity_linking`** — OAuth-based account linking. Google's FAQ says the same in merchant language: signal optional user authentication by declaring the Identity Linking capability. There is no DID, agent-registration, or reputation capability in the spec. [Glint]
6. **Consent and authorization:** v2026-08-25 added reverse-DNS consent and delegated IdPs [S1 item 15]; the Buyer Consent extension models consent purposes asserted by `business` or `platform`. Authorization for autonomous commerce runs through **AP2 mandates** — cryptographic signatures proving user authorization — not credentials presented against a ledger. [Glint + S1]
7. **Webhooks MUST be signed**; business-to-platform identity is signature-based, per items 2–3. [Glint]

## What DIDs and VCs are — adjacent technology, correctly stated

8. A W3C DID is a portable URL-based identifier (e.g. `did:example:123456abcdef`) that resolves to a DID document carrying public keys and service endpoints. A verifiable credential is a tamper-evident set of claims by an issuer about a subject, cryptographically verifiable by a verifier. W3C itself notes VCs do not depend on DIDs and DIDs do not depend on VCs. DIDComm is a separate DIF messaging protocol built on DIDs. **All of this is true — of those specifications. None of it is UCP.** [Glint — W3C VC Data Model]
9. A page may teach DID/VC as *background concepts* only under an explicit "not UCP" label. Presented as UCP's mechanism, every such claim is false by omission from — and substitution against — items 1–6. [G8]

## Claim dispositions (D1 / D4 / E5 attributions)

| Claim (as the posts state it) | Disposition |
|---|---|
| "UCP provides tools to create and manage DIDs" | **CUT — misattribution** (Headline; items 1–5) |
| "DIDs are stored on a decentralized ledger / blockchain" (as UCP) | **CUT — misattribution** |
| "UCP enables organizations to issue VCs linked to a DID" | **CUT — misattribution** |
| "UCP uses DIDs / DIDComm for secure communication" | **CUT — misattribution** (UCP's secure channel is items 2–3) |
| "DIDs authorize UCP transactions" | **CUT — misattribution** (authorization = items 2, 4, 6) |
| "UCP adheres to the W3C DID standard" | **CUT — misattribution** |
| "An agent joining UCP is assigned a DID, publicly verifiable on a ledger" | **CUT — misattribution** (joining = profile + `UCP-Agent` + `keys[]`, item 1) |
| "Smart contracts within UCP verify DIDs / permissions" | **CUT — misattribution** |
| 7261: "UCP tackles this through DIDs" / VC verified against a public ledger / signature from "the user's secured enclave" required for every transaction / "fraud is mathematically impossible within UCP native checkout" | **CUT — all four; Wave 1's plan CUTs CONFIRMED, no reversal** (no enclave mandate exists in items 2–3; no efficacy absolute is published anywhere) |
| E5: "UCP defines a standard format for product data" | **SETTLED-KEEP, narrowed:** UCP defines product data through its catalog capability schemas (search/lookup; product/variant JSON schemas) [S1 Annex A, catalog]. Keep only in that form — capability schemas, not a free-floating "standard format" |
| E5: "UCP supports cryptocurrencies" | **SPLIT:** narrow keep — the v2026-08-25 release record lists crypto-currency data specs (#942) and `crypto_payer` (#1000) [S1 Annex A, payments]. Broad claim (a general merchant crypto-payments feature) **CUT** — not settled by any sheet |
| E5: "UCP leverages decentralized identity (DID)" / "utilizes smart contracts" / "all transactions are recorded on a blockchain" / "UCP relies on blockchain technology" / a UCP "reputation system" | **CUT — misattributions, all** (Headline; item 5: no reputation capability exists) |

## Dispositions for the staged bodies

- **`1942.html` (D1):** the DID/DDO/VC/ledger material **cannot stand as UCP content**. What survives as UCP fact is items 1–6 above (the staged body's §5 "How identity works in UCP" framing is the right shape — it must be *only* items 1–6). General DID/VC explainer material may remain only in a clearly labeled background section ("general concepts — not part of UCP"). Everything attributing DID creation/management, ledger storage, DIDComm, DID authorization, or smart-contract checks to UCP is CUT before publish.
- **`1253.html` (D4):** same rule. The 7261 fold stays exactly as Wave 1 planned it — a framing question ("who is really buying?") with **zero** of the stub's claims carried. 1253's own DID/ledger-anchored-identity vendor material (Sovrin/Evernym/Hyperledger/Polygon etc.) is generic security-landscape content: it may ride only as non-UCP background, never as "UCP standardizes/defines" language.
- **`1908.html` (E5):** see GAP-REJUDGE for the component-by-component ruling and the blocker verdict.

## NOT SETTLED BY THESE SOURCES
- Whether any third-party extension namespace (a vendor's own `com.*` capability) implements DID-based identity *on* UCP transports — possible in principle under namespace governance (Sheet 1 item 6), published by no primary source checked; a page may not state it as UCP fact.
- Generic engineering/security practice in D4 (ZK proofs, threshold signatures, reputation scoring as *industry* techniques) — outside sheet jurisdiction entirely; not settled here and not claimed settled (see GAP-REJUDGE's not-earnable note).

*Half-life: earned 2026-11-06; re-earn with Sheets 1–7 on the programme's 14-day clock (no wave fires on it after 2026-11-20 without a re-earn pass).*

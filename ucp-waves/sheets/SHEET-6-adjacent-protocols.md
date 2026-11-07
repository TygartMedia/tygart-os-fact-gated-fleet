# SHEET 6 — Adjacent Protocols (MCP, A2A, x402, x401)

**Earned: 2026-11-06 · PHASE 0b, UCP wave program**
**Scope discipline:** this sheet exists only where the site claims interop with UCP or coverage is planned (Lens B queue: x402/x401 refresh; PAP drafts are adjacent context, not a sheet subject). It judges version, governance, and mechanism claims for the four protocols — nothing more.
**Sources:** MCP specification (modelcontextprotocol.io, revision 2026-07-28); A2A specification/project (a2aproject); x402 specification (x402-foundation/x402, v2); Proof x401 specification (proof/x401, draft v0.2.0) — primary texts synthesized into the leg dossier fetched 2026-11-06.
**Provenance:** [L6] = contributor leg L6 (ran clean, finish=stop; protocols kept strictly separate; its volume-figure contradiction is preserved).

## MCP [L6]

1. MCP is an open standard introduced by Anthropic in November 2024: how AI applications discover and call external tools, read resources, and load prompt templates through one JSON-RPC 2.0 interface.
2. Governance: since 9 December 2025, MCP sits under the **Agentic AI Foundation (AAIF) under the Linux Foundation**; changes proceed via Specification Enhancement Proposals (SEPs).
3. **Current specification revision: 2026-07-28** (released 28 July 2026; previous revision 2025-11-25) — the largest change since launch: the core is now **stateless** (the `initialize` handshake and `Mcp-Session-Id` header are removed; every request carries its own protocol version); a `server/discover` method was added; the HTTP GET endpoint and `resources/subscribe` were replaced by a single `subscriptions/listen` stream; **Roots, Sampling, and Logging are deprecated** (12-month minimum lifecycle window); long-running tasks moved to an optional extension.
4. Transports: **stdio** (local) and **Streamable HTTP** (remote). The older HTTP+SSE transport has been deprecated since the 2025-03-26 revision.
5. Authorization is **explicitly optional**. Where implemented on HTTP transports it follows an **OAuth 2.1 profile**: the server is the resource server; Protected Resource Metadata (RFC 9728) is mandatory for authorization-server discovery; Resource Indicators (RFC 8707) are mandatory so tokens are audience-bound — servers MUST validate tokens were issued for them; `iss` validation per RFC 9207/SEP-2468. Token passthrough is forbidden. stdio servers sit outside the authorization spec; credentials come from the environment.
6. Release cadence (SEP-3398, accepted 14 October 2026): March and September; the next release is targeted **30 March 2027**.
7. Relation to UCP: UCP declares an MCP transport binding; Google's UCP-over-MCP for Native Checkout is Early Access (Beta) with REST the default (Sheet 3); Shopify and WooCommerce expose commerce over MCP (Sheet 4).

## A2A [L6]

8. A2A is an open protocol for agents built on different frameworks/vendors to discover each other and hand work over without sharing internals. An agent publishes an **Agent Card** (JSON, usually at `/.well-known/agent-card.json`); work is delegated as **Tasks** with a defined lifecycle. (An unsigned Agent Card proves nothing — signing is optional.)
9. Announced by Google 9 April 2025 with 50+ partners; moved to the Linux Foundation 23 June 2025; accepted as an **AAIF Growth Stage project 27 August 2026**, alongside MCP. Apache-2.0; repository a2aproject/A2A.
10. **Current released specification: v1.0.0 (12 March 2026)**, patch **v1.0.1 (28 May 2026)**. v1.0 was breaking: the `kind` discriminator removed, Part types unified, errors moved to google.rpc.Status, operations renamed (SendMessage, GetTask, CancelTask) with ListTasks added; the task lifecycle has eight states; updates via polling, SSE streaming, or webhook push notifications.
11. Bindings: JSON-RPC 2.0, gRPC, HTTP+JSON/REST, with `a2a.proto` as the normative source. Version negotiation uses Major.Minor ("A2A-Version: 1.0"); a client sending an empty A2A-Version header gets v0.3 behavior, not v1.0.
12. MCP vs A2A: MCP connects an agent to tools and data (vertical); A2A connects agents to agents (horizontal). IBM's Agent Communication Protocol was absorbed into A2A in August 2025.
13. By April 2026: 150+ supporting organizations; SDKs in five languages (Python, JavaScript, Java, Go, .NET); production integrations named at Microsoft Azure AI Foundry/Copilot Studio and Amazon Bedrock AgentCore Runtime.
14. Relation to UCP/AP2: UCP lists A2A as a transport binding; AP2 mandates can be carried over A2A (the A2A x402 extension — Sheet 2).

## x402 [L6]

15. x402 is an open payment protocol released by Coinbase in May 2025 reviving HTTP **402 Payment Required**: the server answers an unpaid request with 402 and payment requirements; the client retries with a signed payment authorization; a facilitator verifies and settles on-chain; the server returns the resource.
16. The authorization: for EIP-3009 tokens (USDC, EURC) an **EIP-712-signed `transferWithAuthorization`** — the client signs an authorization, not a transaction, and submits nothing to the blockchain; settlement is gasless for the client (the facilitator pays gas). Permit2 covers other ERC-20s.
17. **Identity is out of scope by design:** no accounts, no personal information, no KYC required of payers.
18. **Current specification: v2 (released 11 December 2025; spec v2.0 dated 9 December 2025).** In v2 the requirements moved into the **`PAYMENT-REQUIRED`** header (base64 JSON), the client's payment into **`PAYMENT-SIGNATURE`**, and the receipt into **`PAYMENT-RESPONSE`**; v1's `X-PAYMENT` / `X-PAYMENT-RESPONSE` headers are **legacy**. Networks are **CAIP-2** identifiers (`eip155:8453` = Base); `x402Version` must be 2; v2 added an extensions map. A Batch Settlement extension was added 11 May 2026.
19. Governance: the x402 Foundation (co-founded by Coinbase and Cloudflare, September 2025) joined the Linux Foundation; operational launch 14 July 2026 with 40 members, growing past 50 by September 2026 (roster incl. Visa, Mastercard, Google, Amex, PayPal, Shopify, Circle, Stripe, AWS). Specification Apache-2.0 at github.com/x402-foundation/x402; SDK packages `@x402/*` at 2.x, legacy `x402`/`x402-next` frozen at 1.2.0. The Coinbase facilitator charges $0.001 per settled payment above a free tier of 1,000 transactions/month (from 1 January 2026).
20. **Volume figures conflict across trackers and must never be printed without naming the tracker:** ~196M lifetime transactions / ~$42M (one tracker) vs ~248M / ~$63.5M (another) vs October 2026 ≈ 5.1M transactions / ~$274K (Fireblocks, via Lens B) — after a late-2025 token-minting rush inflated earlier counts. Any single-number volume claim on the site is UNVERIFIED by construction.
21. Known open problem, named in criticism: on-chain finality means **no chargeback or recourse path**; a November 2026 study found all 15 tested facilitators broke at least one of eight safety rules.

## x401 [L6]

22. x401 (Proof) extends HTTP **401** so a site can demand verifiable identity from an agent before access or payment. Status: **draft v0.2.0**, co-edited by Proof (Daniel Buchner) and Circle (Bhushit Agarwal), reviewers incl. Okta, OpenAI, Visa. Repository proof/x401, Apache-2.0.
23. x401 **went into production 15 October 2026**; Proof's production MCP server works with Muse, ChatGPT, Grok, and Claude.
24. Mechanism: three headers, each one base64url JSON object — **`PROOF-REQUEST`**, **`PROOF-RESPONSE`**, **`PROOF-RESULT`**. The request wraps a W3C Digital Credentials API request (OpenID4VP with DCQL).
25. **The challenge MAY arrive on any status code, including 200**, and is not carried in `WWW-Authenticate` — an agent that only watches for 401 will miss an x401 challenge delivered on a 200.
26. Payment separation rule: a server requiring payment MUST use 402 and **MUST NOT overload x401 to represent payment as proof**; an informational payment hint is allowed (a boolean plus `scheme_hint`).
27. **Circle × Proof demo, 19 October 2026 (Money20/20):** an agent presents a Kantara/NIST IAL2-certified Proof credential over x401, then pays in USDC over x402 from a **Circle Agent Wallet** (2-of-2 MPC keys the agent never holds, spending limits, sanctions screening).
28. The spec's own open gaps: how a payment artifact binds to the x401 route/method/nonce/quote is left open; agent binding is optional in the base protocol; fully autonomous delegation is future work, with Verifiable Intent named as the working assumption.

## The stack, as the sources describe it [L6]
MCP = agent→tools/data (vertical). A2A = agent→agent (horizontal). x402 = payment (identity out of scope). x401 = identity (payment out of scope, must stay on 402). Composition: x401 identity check, then x402 payment (Proof×Circle demo); UCP commerce capabilities exposed over MCP or A2A bindings; AP2 mandates carried over A2A via the A2A x402 extension.

## NOT SETTLED BY THESE SOURCES [L6]
- x402 recourse: no chargeback path; the facilitator safety-rule findings have no resolution in these sources.
- x401 binding and delegation gaps (item 28) remain open in the draft.
- x402 volume truth: no tracker/methodology reconciliation exists.
- MCP's next release contents (30 March 2027 target only).
- PAP ( Sierra×Meta payment-agent drafts 0.2/0.3, Oct 2026) — adjacent drafts, no stable text; no sheet line earned; site claims about PAP are NEEDS-VERIFY by default.

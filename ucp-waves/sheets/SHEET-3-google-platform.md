# SHEET 3 — Google Platform (UCP on Google surfaces)

**Earned: 2026-11-06 · PHASE 0b, UCP wave program**
**Purpose:** judge site claims about how merchants integrate with Google's UCP surfaces, how requests are authenticated, and what has actually launched, where, and when.
**Sources read (primary):** Google UCP merchant FAQ — https://developers.google.com/merchant/ucp/faq · Universal Cart launch post (blog.google, Oct 15 2026) · Canada direct-checkout post (blog.google Canada, Nov 4 2026) · Merchant Center UCP integration guide (updated Oct 19 2026) · UCP release record — https://github.com/Universal-Commerce-Protocol/ucp/releases
**Provenance:** [L2b] = contributor leg L2b, verbatim-FAQ extraction (ran clean after leg L2's empty-output failure — see PHASE-0B-LOG.md) · [L7] = contributor leg L7 (platform/release dossier) · [Glint] = read directly by Glint this session.

## Request authentication & traffic identification [L2b — FAQ verbatim-derived]

1. UCP checkout requests carry the `UCP-Agent` header (e.g. `profile="https://ucp.goog/..."`) and a `User-Agent` of `Google-Shopping-Merchant-Integration`, `Google/UCP*`, or `Google-UCP-Prober/1.0`.
2. Profile-discovery requests (`GET /.well-known/ucp`) and OAuth 2.0 `client_credentials` token requests carry **no** `UCP-Agent` header. Account Linking requests use `User-Agent: OpenAuth` or `Google-AccountLinking-Fetcher/1.0`.
3. **"Because callers can spoof plain HTTP headers, don't use `UCP-Agent` or `User-Agent` alone to authenticate requests."** (FAQ, verbatim.)
4. Verification route 1 — mTLS: verify client certificates at the perimeter against Google's UCP Root Certificate Authorities.
5. Verification route 2 — **RFC 9421 cryptographic request signatures**: verify **ES256** signatures in the `Signature` / `Signature-Input` headers against the public signing keys in Google's UCP profile at **https://ucp.goog/.well-known/ucp.json**.
6. Cache discipline: do not cache the profile or its keys longer than `Cache-Control` allows (**max-age=86400**, 24 hours); Google rotates keys regularly and a stale cache rejects valid requests. On an unknown `kid`, **refetch the profile before rejecting** the request.
7. Network layer: source ASNs **AS15169** (checkout and discovery) and **AS396982** (Account Linking), plus header-based routing and bot-management exemptions.

> This is the Oct 27–31 correction (Lens B item 3): site pages teaching the old header/DNS authentication method (pages 3230, 1009, 7251, 4105) are wrong against items 3–6 and are queued for rewrite.

## Transports and surfaces [L2b]

8. **REST is the recommended default transport** for UCP Native Checkout; Merchant Center self-serve checkout validation supports **only REST**.
9. Stateless MCP (`tools/call` over HTTP POST, JSON-RPC 2.0) is **Early Access (Beta)**; production use requires onboarding and integration testing so Google can enable the account.
10. Launch surfaces: AI Mode in Google Search, the Gemini web app, and the Gemini mobile app.

## Payments & merchant of record [L2b + Glint]

11. The merchant's PSP must be able to process Google's tokens; the merchant must explicitly provide its Google Pay configuration inside its UCP profile.
12. On Google's AI surfaces, only **PAN_ONLY** is used for `allowed_auth_methods`; other methods (e.g. CRYPTOGRAM_3DS) may be present but are not used in the UCP checkout flow.
13. The merchant remains **Merchant of Record**, with full control of customer relationships and data; as MoR the merchant performs real-time inventory checks and must return the `out_of_stock` error code when an item is unavailable, validate shipping addresses (`address_country` in Create/Update Checkout), and return standard error codes such as `address_undeliverable` / `address_unverifiable`; recoverable errors need severity `recoverable`. [L7 + FAQ]
14. Native (UCP) integration does not influence product ranking; UCP-integrated offers feature the direct purchase option. Google may send health checks with `User-Agent: Google-UCP-Prober/1.0`. [L7]

## Launches [Glint + L7]

15. **Universal Cart** launched in the U.S. on **Oct 15, 2026** across Google Search and the Gemini app: cross-retailer saves persist across surfaces, built on the Shopping Graph's "60+ billion continually refreshed product listings," with price-drop/restock notifications, Google Wallet perks and promo codes surfaced, and checkout via Google Pay in-cart or transfer to the merchant's cart. Named merchants: Nike, Sephora, Target, Ulta Beauty, Walmart, Wayfair, "and many Shopify merchants." The merchant remains seller of record; checkout is "powered by the Universal Commerce Protocol (UCP)." [Glint — blog.google read directly]
16. Cart transfer mechanics: a one-way population via the Cart API (`dev.ucp.shopping.cart`, available from UCP 2026-04-08) — Google accumulates saves locally and calls the merchant once, at transfer; saves are not reported in Merchant Center UCP analytics. [L7]
17. **Canada — Nov 4, 2026:** "direct checkout, powered by UCP, is expanding to Canadian shoppers on AI Mode in Google Search and the Gemini app"; eligible retailers named: lululemon, select Shopify merchants, Shoppers Drug Mart, Simons. Shoppers pay with Google Pay from Google Wallet; retailer remains seller of record; purchases are single-item at launch. [Glint + L7]
18. **CONTRADICTION, flagged not resolved [L7]:** the Merchant Center guide (updated Oct 19, 2026) says the integration hub "is gradually rolling out in the United States, with Australia and Canada to follow early next year," while the Nov 4 announcement launched Canadian shopper-side checkout immediately. The two reconcile only if read as merchant self-serve onboarding (next year) vs shopper-side checkout (live Nov 4) — Google has not said so in public documentation.
19. The Nov 4 post also states: "Starting next year, we'll begin broadening access by making simplified UCP integration available directly within Merchant Center." No date or eligibility criteria published. [Glint + L7]
20. US direct checkout rolled out from February 2026 (Etsy and Wayfair among the first), reaching "hundreds of thousands of brands and retailers" per Google by September 2026; checkout remains available for select merchants only. Australia rolled out earlier in 2026; Google has published no comparable date/partner list for it. [L7]

## The version lag [L7 + Glint]

21. Google's merchant documentation and live surfaces implement **2026-04-08**; the current specification is **2026-08-25** (Sheet 1). Shopify moved storefronts to 2026-08-25 on Sept 4, 2026. A guide that does not name its spec version is silently version-ambiguous.

## NOT SETTLED BY THESE SOURCES
- The compatible-PSP list and token-processing setup steps.
- MCP production onboarding criteria, timelines, or a GA date.
- Australia launch date and partners; Canada merchant eligibility beyond the four named launch participants.
- Whether Google will reconcile the Merchant Center timeline statement (item 18).

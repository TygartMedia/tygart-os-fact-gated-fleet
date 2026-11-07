# SHEET 4 — Commerce Platforms (per-vendor sub-sheets)

**Earned: 2026-11-06 · PHASE 0b, UCP wave program**
**Purpose:** judge site claims about each vendor's agentic-commerce position — what is live, what is preview, what is positioning.
**Sources:** vendor developer changelogs, help/documentation pages, and launch announcements per vendor (Shopify developer changelog & help docs; WooCommerce developer docs; Stripe Agentic Commerce Suite materials; PayPal Agent Ready docs & Oct 2025 announcement; Adyen June 2026 release) — synthesized into the leg dossier from primary vendor pages fetched 2026-11-06.
**Provenance:** [L4] = contributor leg L4 (ran clean, finish=stop). Leg kept vendors strictly separate; its cross-source contradictions are preserved as flagged lines, not resolved.

## SHOPIFY [L4]

1. Shopify co-developed UCP with Google; UCP is "an open standard for integrating commerce with agents" (Shopify's words).
2. **Agentic Storefronts**: a sales channel (admin: Sales channels > Agentic) sharing eligible stores' products with AI channels; **on by default for eligible stores**; channels include ChatGPT, Google AI Mode/Gemini, Microsoft Copilot, and Meta surfaces (Meta added 8 September 2026).
3. Shopify Catalog holds structured product data from eligible stores (titles, descriptions, images, prices, variants, stock); Shopify states it holds **more than 1 billion products**.
4. UCP support: storefronts publish a profile at `/.well-known/ucp`. Shopify's developer changelog (4 September 2026): storefronts moved to **UCP version 2026-08-25** with no changes needed to existing integrations and no change to supported capabilities. A live storefront profile checked October 2026 advertised version 2026-08-25, MCP endpoint `/api/ucp/mcp`, capabilities incl. `dev.ucp.shopping.cart`, `dev.ucp.shopping.checkout`, plus fulfillment and discount extensions.
5. **Shop MCP / shop.dev** (13 October 2026): Catalog and Shop Pay checkout opened to any developer's agent through Shop MCP (tools incl. `search_catalog`, `lookup_catalog`, `get_product`); catalog search is free, no API key; single MCP server at shop.dev / mcp.shop.com; sign-in with Shop. **ChatGPT = discovery only (no direct checkout); Google AI Mode/Gemini, Copilot, and Meta take the order in-chat.** [channel behavior per Shopify help docs in dossier]
6. **Shop Pay** issues single-use payment credentials; the agent never sees the shopper's real card; each payment needs the shopper's approval.
7. **Buyer-consent extension** (16 October 2026): Checkout MCP and Cart MCP support the UCP buyer consent extension (`dev.ucp.shopping.buyer_consent`) for agents negotiating it on UCP 2026-08-25: storefronts advertise purposes (analytics, preferences, sale/sharing, and marketing with separate email and SMS segments) in `/.well-known/ucp`; agents return the buyer's choices with cart/checkout/order; no consent sent → the shop's country defaults apply; unknown country → opt-out; an opt-in missing its required contact detail triggers a `missing_consent_data` warning and blocks completion.
8. **Fall '26 Edition** (28 October 2026): shop.dev single connection to Catalog, sign-in with Shop, cart, checkout, Shop Pay; Shop Pay checkout inside personal AI agents (Meta Muse, Claude Duet, Instinct named; card never shared with the agent); connectors for nine AI agents; WebMCP tools on Liquid/Hydrogen storefronts and checkout (browser agents get structured data instead of screenshots); **Shop.md**, a shopper-carried skill turning ChatGPT/Claude-class agents into personal shoppers over the catalog with Shop Pay checkout.
9. **Announced, not live:** the Shopify×Meta announcement of 21 September 2026 (Shop Pay inside Meta Muse "on all Shopify stores") has **no published go-live date** — do not print as live.
10. Direct-checkout limits on Copilot/Meta channels: subscriptions, product bundles, customizable products, and B2B-only products are not supported; neither are local delivery or pickup.
11. Shopify said in March 2026 that Agentic Storefronts carry no transaction fees beyond standard processing rates; orders arrive in admin with referral attribution.
12. An "Agentic plan" for non-Shopify brands exists — **UNVERIFIED** detail: its checkout-default behavior (whether non-Shopify brands default to checkout or discovery) was not settled by the sources in the dossier.

## WOOCOMMERCE [L4]

13. WooCommerce's developer documentation (AI & Agentic Commerce in WooCommerce, 3 October 2025, updated 13 February 2026) states Woo is one of the platforms working with Stripe to support ACP.
14. WooCommerce 10.3 introduced the first WooCommerce MCP, built on the **WordPress Abilities API**: WooCommerce registers product and order abilities; the **separately installed** WordPress MCP Adapter plugin exposes them at `/wp-json/mcp/mcp-adapter-default-server`. WooCommerce does not bundle the adapter.
15. The WooCommerce MCP is in **Developer Preview**; APIs and integration patterns may change. The initial abilities cover **store management** — searching, adding, updating products; creating and managing orders — merchant-side operations, **not consumer checkout**. (Seven canonical abilities: products-query, product-create, product-update, product-delete, orders-query, order-update-status, order-add-note.)
16. WooCommerce's stated goal: MCP expands beyond store management to power consumer shopping and checkout; Stripe's ACP is "going to be a natural fit for the WooCommerce MCP and Store API, and work on that has already begun." **No Woo-native UCP/ACP consumer checkout is shipped** — any site claim of live WooCommerce agentic checkout is wrong against this sheet.
17. WooCommerce 11.3 removed the deprecated `/wp-json/woocommerce/mcp` endpoint and its `X-MCP-API-Key` authentication; requests to it now return **HTTP 410** with a JSON-RPC error explaining how to connect through the MCP Adapter.
18. WooCommerce is a named platform for Stripe's Agentic Commerce Suite rollout (alongside Wix, BigCommerce, Squarespace, commercetools).

## STRIPE [L4]

19. Stripe co-created the **Agentic Commerce Protocol (ACP)** with OpenAI (announced September 2025; Meta is a lead maintainer from April 2026); ACP is published openly at agenticcommerce.dev. ACP powers Instant Checkout in ChatGPT (live for US Etsy sellers at launch; Shopify merchants following). OpenAI states it is **not** the merchant of record in ACP — the merchant remains merchant of record.
20. ACP's current stable cut is dated 2026-04-17 (cart, product feed, orders, authentication, MCP binding).
21. **Agentic Commerce Suite** (introduced 11 December 2025): a single integration to make products discoverable (a dedicated hosted ACP endpoint sharing near-real-time product, price, availability), simplify checkout (powered by the Checkout Sessions API), and accept agentic payments. Businesses connect their catalog to Stripe and select which AI agents to sell through in the Stripe Dashboard.
22. **Shared Payment Tokens (SPTs)**: the agent initiates payment with the buyer's saved payment method **without exposing credentials**; every token can be scoped to a specific seller, bounded by time and amount, observable throughout its lifecycle, and **resolvable only once**. On Stripe, SPTs can be powered by Radar to relay underlying risk signals.
23. Since March 2026, SPTs can carry Visa and Mastercard agentic network tokens, and Affirm and Klarna.
24. Suite rollout: via the Dashboard and APIs, through ecommerce platforms (Wix, WooCommerce, BigCommerce, Squarespace, commercetools) and omnichannel platforms (Akeneo, Cymbio, Logicbroker, Mirakl, Pipe17, Rithum).
25. Production position as audited 22 October 2026: self-serve onboarding from the Dashboard across **34 countries**; every live code sample runs on a **preview API version** and the seller terms are a named preview; Stripe has published **no agentic transaction volumes**. Stripe was, as of that audit, the only major provider a merchant could self-serve-enable. Suite extension to Google AI Mode/Gemini was "coming soon" for some merchants (October 2026).

## PAYPAL [L4]

26. On 28 October 2025 PayPal announced it would adopt ACP to power Instant Checkout and agentic commerce in ChatGPT, and launched its **Agentic Commerce Services/Suite** (catalog featuring across AI apps, payments across platforms, consumer-intent insights). The announcement was written in the future tense.
27. Through 2026 the ChatGPT checkout integration was repeatedly described as "rolling out"; on 24 March 2026 OpenAI deprioritised standalone Instant Checkout ("focus on product discovery"). **CONTRADICTION, flagged [L4]:** PayPal's Agent Ready documentation describes ChatGPT Apps instant checkout (item 28) while the standalone product was deprioritised; whether the Apps-vs-standalone distinction resolves this is not settled by these sources. Do not print PayPal×ChatGPT checkout as fully live without the rollout qualifier.
28. **Agent Ready documentation** (updated 13 October 2026): instant checkout in ChatGPT Apps using delegated payment tokens through **Braintree**; and a **Buy button in Google AI Mode and Gemini through UCP**.
29. **Store Sync** is live in the US and UK: product-feed discovery on Microsoft Copilot and Perplexity.
30. PayPal's wallet protections and dispute resolution apply to its agentic-checkout flows per its announcement materials. PayPal is a UCP endorser and sits on the UCP Payments Technical Council (seated 2 September 2026).

## ADYEN [L4]

31. **Adyen Agentic** (announced 16 June 2026): a modular API suite — **Agentic Feed** (real-time catalog, pricing, availability distribution), **Agentic Cart** (connects existing checkout, tax, fulfillment, order management to agent platforms), **Agentic Payments** (authentication, token portability, risk management for agent-led transactions).
32. Positioned as interoperating across UCP, AP2, ACP, and Meta's AI checkout — "merchants integrate once; Adyen translates." **This is vendor positioning, not independently proven interoperability.**
33. At announcement: **limited availability for US enterprise merchants**, global expansion to follow; fully compatible with Meta's AI checkout at announcement, more platforms to come; strategic partners American Express, Mastercard, Salesforce, Visa; early enterprise retailers ESW, Scheels, Sézane, SharkNinja.
34. Adyen is an early endorser of UCP and AP2 and sits on the UCP Payments Technical Council (seated 2 September 2026).

## NOT SETTLED BY THESE SOURCES [L4]
- Shopify: go-live date and store coverage for Shop Pay inside Meta Muse; live adoption/order volumes for Agentic Storefronts, Catalog, Shop MCP, WebMCP, Shop.md; fee changes beyond the March 2026 statement.
- WooCommerce: completion or live status of the ACP fit beyond "work has already begun"; any consumer shopping/checkout transaction via MCP.
- Stripe: production-vs-preview resolution for the Suite; agentic transaction volumes; live status on each named platform.
- PayPal: live vs rolling-out status and country availability of ChatGPT/ChatGPT Apps checkout; volumes for the UCP Buy button; Store Sync beyond US/UK.
- Adyen: expansion beyond US limited availability; proven interoperability beyond vendor positioning; live merchant volumes.
- Cross-vendor: comparative fees, conversion, risk-liability, or merchant-of-record terms; independent verification of Catalog size, SPT scoping/observability, or single-use credential claims.

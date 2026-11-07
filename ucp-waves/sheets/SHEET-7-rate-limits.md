# SHEET 7 — UCP Rate Limits & Performance

**Earned: 2026-11-06 · UCP wave program, gap-sheet earn (Will's tap, 17:26 PT)**
**Purpose:** settle what UCP / Google actually publish about rate limits, quotas, rate-limit headers, and throughput — the sheet Wave 1 cluster D2 (30 NEEDS-VERIFY items) and Wave 2's troubleshooting territory judge against.
**Sources read (primary only):** UCP specification, latest line, pinned v2026-08-25 — https://www.ucp.dev/latest/specification/overview/ (full text searched) · Google UCP merchant FAQ — https://developers.google.com/merchant/ucp/faq (read in full) · Google Merchant API / Content API quota documentation (checked to confirm its quotas are for the Merchant API, not UCP).
**Provenance codes:** [Glint] = verified by Glint directly against the primary source this session (full-text searches + section reads) · [G7] = contributor leg GAP7-RATELIMITS' structured verdict on Glint's dossier (spot-checked by Glint against the dossier; no leg-added facts).

## HEADLINE VERDICT

**No published UCP rate limits exist.** No primary source checked — the UCP specification, the UCP repo/docs at ucp.dev, or Google's UCP developer documentation — publishes merchant/API rate-limit tiers, RPM/RPS numbers, quota tables, `X-RateLimit-*` or `X-UCP-RateLimit-*` header requirements, throughput figures, or SLOs. This is a NOT SETTLED finding in the strong form: the absence was established by full-text search of the spec and a full read of the FAQ, not by failing to look. [Glint + G7]

## What IS settled

1. The spec's Protocol Errors table defines HTTP **429 "Too many requests"** (MCP JSON-RPC code −32000). It is the only rate-limit status definition in the specification. [Glint — spec error-handling section read directly]
2. For 429 and 503 responses, both transports **SHOULD** include a `Retry-After` header (REST) or `error.data.retry_after` (MCP). The spec's worked examples show `Retry-After: 60` / `"retry_after": 60` — illustrative example values, **not quotas and not defaults**. [Glint]
3. `Retry-After` is the **only** rate-limit-related header the spec names. Full-text search: zero occurrences of `X-RateLimit`, `X-UCP-RateLimit`, or any other rate-limit header name. [Glint]
4. Full-text search of the spec found **zero** occurrences of: any RPM/RPS figure; any tier name (Starter / Standard / Professional / Enterprise); any quota table; any throughput or SLO figure; any token-bucket or sliding-window mandate; any per-endpoint limit; any burst/sustained window definition; any merchant-certification requirement tied to headers; any suspension rule for retry behaviour. [Glint + G7]
5. The spec's only other rate-limit mentions are implementer practices with no numbers: (a) a fetch-safety rule — a "global rate limit on discovery fetches" bounding a platform's outbound profile-fetching (an SSRF/abuse guard on the fetcher, not a merchant API quota); (b) identity-linking guidance to implement rate limiting on credential acquisition. [Glint]
6. Google's UCP merchant FAQ contains **no** rate-limit tiers, quotas, numbers, header requirements, or SLOs anywhere. Its only rate-related mention directs merchants to configure "rate-limiter and bot-management exemptions" for Google's UCP traffic (AS15169 / AS396982) in their WAF — i.e., Google tells merchants to exempt its traffic from the merchant's *own* limiter. [Glint — FAQ read in full; also Sheet 3 item 7]
7. Google's published Merchant API quotas govern the Merchant API (product-feed management) — a different API from the UCP checkout endpoints a merchant hosts. They are not UCP rate limits and must not be cited as such. [Glint + G7]
8. Rate limiting in UCP is therefore, on the primary record, **an implementer's own policy**: the merchant/platform sets whatever limits it runs, signals overload with 429, and should say when to retry via `Retry-After`. The protocol standardizes the *signal*, not the *numbers*. [Glint + G7]

## Disposition of the three incompatible claim sets (Wave 1, D2)

| Claim set | Disposition |
|---|---|
| 1695: "Standard 1,000 RPM / Enterprise 10,000 RPM or higher" | **CUT** — no tier or RPM figure exists in any primary source (items 4, 6) |
| 1695: every response carries `X-RateLimit-Limit / Remaining / Reset / Retry-After` | **CUT except `Retry-After`** — only `Retry-After` is spec-named, and only as a SHOULD on 429/503 (items 2–3) |
| 1695: SLOs (95th <500ms, 99th <1s, errors <0.1%), sandbox-to-trigger-429s, regional US+EU buckets doubling capacity, enterprise 10×–100× | **CUT** — none published (items 4, 6) |
| 1618: "Starter 100 RPS / Professional 500 / Enterprise 2,000" tiers; /orders 1,000/min, /inventory 500/min; token-bucket mandate; batch-of-100-counts-as-1; 10,000+ RPS negotiable | **CUT, all** — none published; also mutually incompatible with 1695's set, and neither is settled (items 4, 6) |
| 5268: "`X-UCP-RateLimit-*` mandatory for all UCP-certified merchants" | **CUT** — header family does not exist in the spec; no certification-header requirement exists (items 3–4) |
| 5268: immediate retry "violates the spec" and may suspend the agent; burst 1-min vs sustained hour/day windows | **CUT** — no violation/suspension rule, no window definitions published (item 4) |
| All three: "429 exists; respect `Retry-After`" | **SETTLED-KEEP** — the one rate-limit fact UCP actually publishes (items 1–2) |

## Disposition for the staged D2 body (`wave-1/staged/1695.html`)

- **Survives as UCP fact:** the 429 protocol error and the `Retry-After` / `retry_after` SHOULD (items 1–2), stated exactly at that strength.
- **CUT before publish:** every tier name and RPM/RPS number; all `X-RateLimit-*` header claims; all SLO/benchmark/TTL percentage figures presented as UCP values; the sandbox claim; regional-bucket doubling; enterprise multipliers; the suspension rule. (Full per-item rejudge in `wave-1/GAP-REJUDGE.md`.)
- **May ride, labeled:** generic engineering advice — caching, batching, exponential backoff with jitter, connection pooling/HTTP-2, cursor pagination, monitoring/alerting — **only** under an explicit label that it is general API engineering practice, not UCP specification, with any illustrative numbers framed as the author's examples, never as UCP values.

## NOT SETTLED BY THESE SOURCES
- Any individual platform's or merchant's *own* operational limits (e.g., what Google's UCP Prober or a given merchant actually enforces) — implementation facts, not published protocol facts; a page may state one only with that operator's own dated documentation attached.
- Whether a future spec version adds a rate-limit capability — nothing in the v2026-08-25 record or Annex A release notes indicates one.

*Half-life: earned 2026-11-06; re-earn with Sheets 1–6 on the programme's 14-day clock (no wave fires on it after 2026-11-20 without a re-earn pass).*

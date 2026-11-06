# Wave 14 — The Cache Test

*Fired Nov 5, 2026 on Will's commission. Baseline, in his words: the
dashboard cache hit rate "is at 3.4% now… is there some way to
organize the work so it actually takes advantage of caching? I don't
even care at this point if it is a benefit to us. I just want to
prove if it can work or not and see where it breaks down." Honest
starting point, logged in advance: the waves were never organized
for cache reuse. Full receipts: WO-999.*

## Hypothesis

If the Meta Model API's prompt cache rewards shared prefixes, then
restructuring packets — a long byte-identical prefix first (contract
+ fact sheet + guards), page material last — and firing sequentially
should produce measurable `cached_tokens` where the waves' parallel
one-shot fan-outs produce ~none.

## Method

Four fresh radon-law pages (~750 words each; near-identical site
templates). Calibration first: the shared prefix alone measures
**1,551 tokens**, ~60% of each ~2,570-token packet. Every response's
`usage.prompt_tokens_details.cached_tokens` recorded per call — the
API does expose the field (it read 0 throughout waves 1–13; nobody
had looked). Probes: sequential distinct-page batch; identical
full-packet repeats; request-shape variants (standard tier,
`prompt_cache_key`, `cache_control` blocks); a 10× identical-packet
series; a different-page/same-prefix series; a one-byte mid-prefix
mutation; a warm parallel batch; a 300-second TTL gap.

## Results, in fire order

| Probe | cached_tokens |
|---|---|
| Calibration (prefix + stub) | 0 |
| Sequential, 4 distinct pages, identical 1,551-token prefix | **0 / 0 / 0 / 0** |
| Identical full packet, ×2 repeats | 0 / 0 |
| Standard tier (`muse-spark-1.3`), same packet ×2 | **2,531** / 0 |
| Contributor + `prompt_cache_key` ×2 | 0 / **2,531** |
| Contributor + `cache_control` blocks ×2 | **2,531** / **2,531** |
| Identical packet series ×10 (plain client) | **8 of 10 hit at 2,531** |
| Different page, same prefix (Utah ×3) | 0 / **2,531** / **2,531** |
| One-byte mutation mid-prefix ×2 | 0 / **2,531** |
| Parallel batch ×4, cache warm | **1 of 4 hit** |
| TTL: same packet after a 300 s gap | **2,531 — entry alive at 300 s** |

## What the data says

- **The cache exists** and the API reports it per call. When a
  request hits, it hits at **2,531 of ~2,571 tokens (98%)** — nearly
  the whole prompt, not the 1,551-token shared prefix. The figure is
  constant across different packets and even across a one-byte
  mutation, which strict byte-prefix matching cannot explain; the
  mechanism tolerates small divergences and its accounting is
  coarser than the prefix model. Recorded as observed.
- **First fire of any new packet is a miss.** Entries become
  readable after a lag — somewhere between one call-gap and a few
  minutes — then hit ~80% of the time sequentially. Two misses
  inside the warm 10× series say entries also drop or scatter.
- **Parallel arrival defeats warm entries** (1 of 4): simultaneous
  requests mostly land where the entry isn't. The waves' native
  shape — parallel, one-shot, page-unique — is precisely the
  anti-pattern for this cache, which is what a 3.4% incidental rate
  looks like.
- Request-shape variants (`prompt_cache_key`, `cache_control`,
  standard tier) all eventually hit; none was necessary or
  sufficient on its own. The plain production client hit 8/10 once
  the entry was warm.

## Verdict

**Prompt caching on this surface is real but rewards the opposite
of fan-out: repeated, sequential, near-identical prompts.** It
cannot be harvested by restructuring one-shot page packets — phase S
proved the shared prefix alone earns nothing on first (and only)
use. The organizing rule, where repetition genuinely exists: *if a
leg will re-send a packet — a fixer re-reading the scout packet, a
retry, a trio chain — send it unchanged and sequentially after its
first use, and expect ~80% of its prompt to read from cache.* For
the wave program as designed, expected yield stays near the
dashboard's 3.4%: the honest answer to "can we organize for it" is
**not for the fan-out itself — only for the repeats around it.**
Whether cached tokens bill at a reduced rate on this account could
not be verified from the API responses; the credit ledger shows
consumption only in aggregate.

Usage: 33 calls; 127,152 tokens recorded — 86,016 fully metered,
plus 41,136 prompt tokens from two probe series whose completion
tokens were not captured (an instrumentation gap, named rather than
estimated over). Credit-equivalent ≈ $0.02 at listed contributor
rates. Card $0 — free credits; no cliff signals.

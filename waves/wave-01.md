# Wave 1 — five pages, first fan-out (WO-985)

**Nov 5, 2026 · 5 pages · 5 parallel contributor calls · 42,226 tokens**

Pages: `claude-rate-limits` · `claude-token-limit` · `claude-models-comparison` ·
`claude-team-plan-usage-limits` · `how-to-get-anthropic-api-key`

## What happened

44 findings came back. **31 shipped, 13 marked NEEDS-VERIFY and left untouched.**
The wave retired the deposit-era usage tiers across the cluster, split the dead
"Max 20x / $200" framing into Max $100 and Ultra $200, rolled every model lineup
to the current four (Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5), and corrected
launch dates and console URLs.

Two discoveries outside the findings:

- The rate-limits page carries a second, deeper table system (per-tier
  RPM/ITPM/OTPM) that could not be rebuilt from verified data. Rather than
  guess, the page now carries a dated correction banner over those tables:
  kept as a record, flagged "do not quote as current." Still owed: a full
  rebuild from Anthropic's current limits doc.
- Two audited URLs turned out to be pre-existing 301 merges
  (`how-to-get-anthropic-api-key` → `/anthropic-console/`; the hub guide →
  `/claude-ai-pricing/`). Content was updated in the CMS; the redirects were
  left as the operator's call.

## The edge this wave found

The audit half scales cleanly. The bottleneck was the **edit phase**: doing the
surgery by hand against raw HTML cost 9 failed match attempts across 3 of 5
pages — titles wrapped in `<strong>`, `&#038;` entities, one mojibake em-dash.
Every failure was caught by assert-before-write; nothing partial ever shipped.
But the friction was the finding: it directly commissioned **wpedit** (WO-986),
the text-layer press every later wave edits through.

# The Router — "Reverse MCP" Design

*Adjudicated design, Nov 3, 2026. Produced by running the design question
through the Trio itself — Scout (low) mapped the space, Designer (medium)
drafted, Adjudicator (max) attacked the draft and ruled. Raw record:
`router-run/` (BRIEF.md, scout-raw.md, designer-raw.md, adjudicator-raw.md,
runs.jsonl). Run cost: $0.21809, all three legs on muse-spark-1.3 standard.*

## The metaphor, mapped

Ordinary MCP lets a model reach **into** a tool. The reverse: the tool side
decides the only shapes information may come **out** in.

- **The paste** = one Trio-checked item: grounded claims, verbatim quotes,
  nothing invented, certainty never upgraded.
- **The pastry bag** = the Hopper plus the checked-item store behind it.
- **The tip** = a **destination profile**: one row per Company ×
  Destination. A tip doesn't negotiate with the paste — an item exits
  through it in exactly the tip's shape, or it doesn't exit there at all.
- **The squeeze** = the routing decision + emission: one checked item can
  be squeezed through several tips at once (the same job goes out five
  ways), each emission independent, each confirmed by read-back.
- **The decorator's hand** = the operator. Tips are created, approved, and
  trusted by tap — never by an admin project.

## What a tip is (the schema that survived adjudication)

16 fields. A field exists only if it changes a routing, shaping, or
fire/no-fire decision.

| Field | What it decides |
|---|---|
| `tip_id` (`co:destkey:vN`) | Identity in every log line; version lives in the id. |
| `company_id + destination_key + display_name` | Which company's tube this is. The key is a canonical, immutable slug — "Adjuster Portal" vs "adjuster portal" can never become two tips. |
| `target_software` | The canonical system (hubspot_crm, adjuster_portal_X, vendor_csv_Y, gmail, sheets). Transport is *derived* from delivery/read-back via a consistency table checked at creation — software name and transport can never contradict. |
| `recipients` | Allowlist of {role, address, verification_ref}. Shaping may address **only** to this list; anything else → exception. Addresses must be verified against a contract line or a stored operator attestation. |
| `fit_rule` | Split in two: `det_fit` (deterministic — job types, item kinds, sources, on a controlled vocabulary) + `content_fit` (model-judged exclusions + a required grounding quote). Packet tips also declare `packet_required_kinds`. Fit rules are marked HEURISTIC until probation proves them — a sample export alone can never prove what should route. |
| `output_schema` | [{field, type, obligation REQUIRED/OPTIONAL, `required_if`, exact header/property}]. Conditional REQUIRED allowed (water packet ≠ mold packet). Missing-field rule is explicit: OPTIONAL → empty; REQUIRED the template allows empty → empty + logged; otherwise → exception, **no send**. (An empty money field that a destination reads as $0 was struck as an upgrade of unknown to zero — that's why the rule is written down.) |
| `field_map` | [{dest field → canonical source field, allowed alternates, transform}]. Transforms are a closed list: NONE, VERBATIM_QUOTE, CURRENCY_NORMALIZE (deterministic `$1,200.00 → 1200`), AGG_COUNT, AGG_MAX, PLAIN_REWRITE (fact-checked, see below). Two sources disagreeing on one field → MONEY_CONFLICT exception — the router never picks the plausible number. Tabular row filters are deterministic predicates on verbatim columns, never model classification. |
| `assembly_order` | Container (PDF, PDF/A-1a, CSV-UTF8, JSON, SHEET_ROW, HUBSPOT_RECORD, body-text), section order, exact header row, `is_packet_tip`. A tip may claim PDF/A-1a only with a validator receipt on file. Packet tips buffer per job (see squeeze). |
| `register` | {base HOUSE/PLAIN, no_marketing, verbatim_numbers, banned_strings[]} — independent switches, not one enum (house register *and* verbatim numbers can both be true). Banned strings are verbatim strings from the destination's own template. Homeowner defaults to PLAIN, overridable with evidence. |
| `never_list` | [{concept, match VERBATIM_STRING/REGEX/CONCEPT, detector, source_ref}]. Concepts (internal margin, homeowner PII) are detected by model and **fail closed**: uncertain → NEVER_REVIEW exception, never a quiet send. Checked twice — at routing and again at shaping. A suppression is logged, never written into the payload. |
| `delivery_mech` | Mechanism + endpoint + verification evidence + **idempotency key** (`item+tip+version+hash`, upsert/dedupe). No valid mechanism → per-tip exception, not a silent skip. |
| `readback_mech` | Mechanism + max level **STRONG/WEAK** + probed capability evidence. API re-read, sheet re-read, file re-read, portal redownload → STRONG possible. Receipt/DSN-only → WEAK forever, never upgraded. A sent-hash is an audit artifact, not a confirmation. |
| `credential_handle` | Vault pointer; `valid` is set by an automated test, never by a tap. Invalid → SUSPENDED_CRED + exception; reversible by refresh, no version bump, no schema rebuild. |
| `template_source` | [{kind: SCHEMA_DOC / SAMPLE_EXPORT / ACCEPTED_SUBMISSION / CAPABILITY_PROBE / OPERATOR_ATTESTATION, stored copy hash, ref, date}]. Immutable stored copies. A correction alone never defines shape — it must be corroborated. Schema lines cite line/cell; fit/map lines cite attestation or paired examples and wear the HEURISTIC mark until probation. |
| `trust_status` | DRAFT / PROBATION / TRUSTED ⇄ STALE / SUSPENDED_CRED / SUSPENDED_SCHEMA. Only PROBATION (batched tap) and TRUSTED fire. STALE never sends. |
| supersedes / current | Exactly **one** `current=Y` per destination per company — enforced as an invariant; a violation is a VERSION_CONFLICT exception and nothing sends. |

## How the router decides (the squeeze)

Budget: **one medium model call per item** for content fit (≈ $0.025,
measured); shaping is separate medium calls batched per job per tip; max
effort is reserved for the Adjudicator gate and genuinely ambiguous
read-back diffs.

1. **Bind the job.** Uses the Trio's job-bind proposal + folder metadata.
   Ambiguous or conflicting → item goes UNBOUND → immediate JOB_UNBOUND
   exception. No slate is fetched for an unbound item. (Job binding is
   model work, not string matching — a deterministic bind struck hard: a
   typo'd folder tag would poison a whole packet with a neighbour's PII.)
2. **Fetch the slate.** All current tips for the company, partitioned
   fireable (PROBATION/TRUSTED + credential valid) vs unfireable.
3. **Deterministic pre-filter.** `det_fit` on the controlled vocabulary.
   Fail → SKIP, log-only (expected silence).
4. **Content fit + NEVER screen — one model call (medium)** over the
   surviving candidates. Output per candidate: SEND / SEND_WITH_SUPPRESSION /
   SKIP + controlled reason code + grounding quote + never-hit + confidence.
   **A SEND with an empty grounding quote is not a SEND** — it becomes a
   GROUNDING_GAP exception, checked deterministically. An uncertain NEVER
   hit → NEVER_REVIEW, fail-closed. A whole-item-private tip SKIPs on a hit;
   other tips carry a suppression flag into shaping.
5. **Fan-out + packet buffer.** SENDs collected. Ordinary tips fire per
   item. **Packet tips buffer** their sections per job until the operator
   taps Assemble or all required kinds are present — a claim packet is one
   ordered upload, not four separate ones. Money consistency is checked
   across emissions: one canonical source per destination field; divergent
   canonical values → MONEY_DIVERGENCE exception.
6. **Diversion.** Zero SENDs → NO_FIT exception with the full SKIP sheet.
   SENDs *plus* problems → the sends proceed and each problem (unfireable
   tip that passed the filter, NEVER_REVIEW, GROUNDING_GAP) raises its own
   per-tip exception alongside. Disposition is one of FULL_SEND /
   PARTIAL_WITH_EXC / NO_FIT. **Partial drops are never silent** — the
   draft's zero-SEND-only diversion was struck for exactly that.
7. **Lock.** The Routing Sheet is written with idempotency keys, enforced
   once-per-key (a retry can never double-append a sheet row or double-email
   a homeowner). The operator sees a per-job summary plus the exceptions —
   not a 95-row sheet per job. Shaping fires only on SEND rows.

## How a tip is learned

Extends the v1 pattern (translator learns the template + read-back +
exceptions place) with counted trust.

1. **Create shell** — operator names company, destination key, software,
   recipients, endpoint, credential. Consistency + key uniqueness checked.
   DRAFT cannot send.
2. **Collect ≥ 2 stored sources**: at least one schema doc/sample **plus**
   one accepted submission — or, for a brand-new destination, two docs plus
   a successful **capability probe** (which also proves what read-back the
   destination can actually afford). "Independent" means different kind or
   author/date — a schema doc and a blank from the same portal are one
   source. Short → DRAFT_BLOCKED exception asking for the doc. The operator
   drops docs in the Hopper; the learner scans them.
3. **Draft the tip** — schema/order/headers/banned strings cite line/cell
   of the stored sources; fit rules, field maps, row filters, register
   inferences, never-concepts cite attestation or paired examples and are
   marked HEURISTIC. An uncited schema line raises an evidence exception —
   it is not quietly dropped and never quietly kept.
4. **Approve** — operator sees source vs draft side-by-side with HEURISTIC
   lines highlighted; Approve / Edit / Reject. An edit that adds a value
   needs a citation or a dated attestation — the operator's tap is not a
   grounding source (a hand-added "crime extension" field is exactly the
   production strike, wearing a different hat). Approve → PROBATION v1.
5. **Probation — 3 consecutive clean emissions covering all REQUIRED
   fields**, tapped **per tip per job as a batch** (the draft's per-send
   tap was struck: 19 items × 5 tips = 95 taps is dead on arrival). 100%
   read-back; STRONG tips require STRONG read-back; WEAK-only tips get a
   per-batch human confirm. A mismatch resets the count and files a
   correction. A *correct* NEVER suppression does not reset; a NEVER miss
   caught downstream does.
6. **Promotion** — the learner proposes with coverage proof; operator taps
   Trust → TRUSTED, fires without per-send taps. TRUSTED still gets 100%
   read-back **plus a 1-in-10 Adjudicator audit against source truth** —
   because read-back proves sent = landed, not that the mapping was right.
   Audit fail → STALE.
7. **Drift** — 2 semantic mutations in a rolling 10 STRONG emissions, a
   new destination doc dropped and tagged, or an audit fail → STALE.
   STALE raises per-tip exceptions and never sends. Learner proposes
   vN+1 through steps 3–4. An emergency **rollback** to the previous
   TRUSTED version is allowed with a tap + logged reason.
8. **Suspend** — credential invalid → SUSPENDED_CRED (reversible).
   3 probation resets without promotion, operator tap, or systematic audit
   failure → SUSPENDED_SCHEMA (needs a new version).

## Exceptions and conflicts

The exceptions place holds one record per problem: item refs, job,
checked summary + quotes, **only the relevant slice** (the diff for a
mismatch, the SKIP reasons for a NO_FIT, the hit snippet for a NEVER, the
missing kinds for a packet) — grouped by job + class so one operator can
triage a batch. Classes: NO_FIT, JOB_UNBOUND, NEVER_STRIKE (blocking),
NEVER_REVIEW, READBACK_MISMATCH, PACKET_INCOMPLETE, STALE_TIP,
CREDENTIAL_INVALID, VERSION_CONFLICT, MONEY_CONFLICT, GROUNDING_GAP,
DRAFT_BLOCKED.

Operator asks are constrained so a tap can't become an invention:
CHOOSE_TIP still enforces NEVER + grounding; EDIT_AND_RETRY is re-checked
by the Adjudicator (no direct payload editing); APPROVE_EMPTY carries a
"the destination may reject this" warning + typed reason; plus REBIND_JOB,
PROVIDE_DOC, ROLLBACK_TIP, DROP_WITH_REASON (typed).

Conflict rules:

- **Fan-out is not a conflict.** The same item leaving five ways in five
  shapes is the design working; logged at debug level only.
- **Two tips claiming one destination key** → VERSION_CONFLICT; nothing
  sends until merged.
- **Current vs stale:** the fireable current version wins; the stale one
  is suppressed. If the current is PROBATION and the stale is TRUSTED, the
  probation version sends *with its batch tap* and the trusted one is held
  for rollback. No fireable current → STALE exception; the old version is
  never auto-served.
- **NEVER vs REQUIRED, same tip:** NEVER wins. Valid only if the template
  explicitly allows the field empty or it's OPTIONAL → send proceeds with
  the suppression noted in the receipt (never in the payload). Otherwise
  blocking NEVER_STRIKE. An emptied money field carries a "may read as
  zero" warning.
- Everything — transitions, exceptions, waivers, overrides, rollbacks,
  retries — lands in a hash-chained append-only Tip Log.

## Emission + read-back (proving the squeeze landed)

Pre-emit gate for every class: a medium Fixer shapes; a max Adjudicator
strikes any field without a trace to the checked item or the verified
template. Verbatim transforms are checked deterministically (+ spot max);
PLAIN_REWRITE is checked by comparing fact lists, source vs rewrite — a
new or dropped material fact is struck. The NEVER screen runs again here.

- **API / sheet destinations (HubSpot, operator sheet):** upsert with the
  idempotency key; re-read after a short settle (retry 3× with backoff —
  eventual-consistency lag is not a mismatch); field-by-field compare.
  Failure ladder: retry same key → READBACK_MISMATCH exception with the
  diff → STALE after 2 mutations in 10.
- **Upload-only portals (adjuster):** the packet assembles first (buffered,
  deterministic order, PDF validated if PDF/A is claimed), then one upload
  under a packet ID. If the portal affords redownload, read-back is STRONG
  — compare extracted text, order, page count (not raw PDF hash; a
  re-render is expected). If it affords only an acknowledgement, the
  delivery is **WEAK: yellow PROVISIONAL, never green**, closed by a
  per-job batch human confirm.
- **Vendor file drops (CSV):** filename carries job + version + hash; the
  dropped file is re-read immediately — STRONG, byte-exact on headers,
  rows, and money, verified *before* the vendor's system processes it.
- **Email (homeowner):** sent only to a verified allowlist address,
  Message-ID dedupe. Max level WEAK: SMTP-accepted/DSN + the archived
  exact text. Reported as "accepted, provisional" — never "delivered,"
  and content is unconfirmed by construction. A bounce → exception.
- **Tolerance:** byte-exact by default for headers, money, order, counts.
  The semantic-equivalence allowlist **starts empty** and is learned in
  probation from 2+ corroborated normalizations + attestation. A
  deterministic allowlist match waives silently (logged REFORMAT_WAIVED);
  anything else goes to a max MUTATION-vs-REFORMAT call that fails closed
  (uncertain = MUTATION). **Money diffs are never auto-waived.**

## Struck — the highlights

The Adjudicator struck or amended **every** element of the draft; the full
struck list (49 items) is in `router-run/adjudicator-raw.md`. The ones
that carry the design:

- **Software enum deciding transport** — a vendor CSV delivered by API
  would force the wrong adapter and claim an unverified delivery. Software
  and transport are separate facts, consistency-checked.
- **Recipients never verified** — a stale homeowner address from creation
  day sends the next job's summary (PII + money) to the prior homeowner.
  Verification is now part of the tip.
- **Fit rules "learned" from destination samples** — a HubSpot sample
  export cannot prove photos should route there; that's how an invented
  include ("crime extension") gets in. Fit is attested + probation-proven.
- **Empty REQUIRED = fill/flag ambiguity** — an empty deductible sent to
  the sheet reads as $0: unknown upgraded to zero. The missing-field rule
  is now explicit per obligation.
- **Per-send probation taps** — 95 taps for one job. Dead on arrival;
  batch taps replaced them.
- **SHA-256 as portal read-back** — an upload-only portal affords no bytes
  to hash, and a re-render breaks the hash anyway. STRONG read-back
  compares text/order/count; WEAK stays yellow.
- **"Sent-hash stored" as email confirmation** — proves what left, never
  what landed. Email caps at WEAK, reported as accepted-provisional.
- **Per-item adjuster emissions** — four separate uploads are not an
  ordered packet. Packet tips buffer and assemble.
- **Photo "verbatim quotes"** — pixels have no verbatim quotes; counts and
  maxima need named aggregate transforms, and selecting 3 of 14 photos
  for the homeowner is an evidence decision, not a formatting one.
- **Corrections as template sources** — a portal's re-rendered receipt
  stored as the desired shape teaches the router the truncation as the
  template. Corrections repair; they don't define.
- **Pre-populated tolerance allowlist** — waivers nobody observed would
  waive a real truncation as a "reformat." The list starts empty and is
  earned in probation.

**Residual risks the design does not remove** (Adjudicator, honest):
vision grounding stays inductive (a "water stain" read from pixels is an
interpretation, and the Trio's vision seat can still be wrong); CONCEPT
never-detection trades leak risk for exception load, and a confident miss
still leaks; WEAK destinations never become STRONG; a packet can assemble
before a late item arrives; shaping + per-emission adjudication costs
more than the $0.025 routing decision and is **not yet measured**; and
operator load is reduced, not eliminated — template reviews, batch taps,
packet assembles, and human confirms can still pile up in a multi-job
surge.

## What exists today vs what this design adds

**Exists today (built and measured — safe to claim):**

- The Hopper: one dumb Drive intake box; items land as-is.
- Trio checking in production: Scout/Fixer/Adjudicator on muse-spark-1.3,
  ≈ $0.12/page standard tier, with the verbatim-grounding strike as the
  operating standard.
- Router v3 on the publishing side: session recordings routed against
  a 25-destination slate with SEND/SKIP decision sheets — 9 sheets in the
  measured effort test, 3 recordings × 3 effort tiers (NIGHT-LEDGER.md;
  decision sheets in model-bakeoff/submission-sweep/router-effort-test/);
  the public-showcase route skipped 9/9 when sources held anything
  private; the
  routing decision measured (medium ≈ $0.025/recording is the sweet spot;
  max buys strictness, not facts).
- Confirmation read-back as an operating pattern on the fleet: work-order
  receipts, live read-back of published output before anything is called
  done.
- This design itself: produced by the Trio on the API for $0.21809,
  adjudicated with a 49-item struck list — the method applied to its own
  next layer.

**This design adds next (NOT built — the submission must not claim it):**

- The tip registry as a data structure (the 16-field schema above) and
  the tip store/log behind it.
- Tip learning for *external* destinations — HubSpot, adjuster portals,
  vendor systems — with capability probes, counted probation, and the
  trust ladder.
- The squeeze as specified: deterministic pre-filter + one medium content-
  fit call + grounding-quote enforcement + packet buffering/assembly.
- Per-destination read-back adapters with STRONG/WEAK levels, idempotency
  keys, and the learned tolerance allowlist.
- The exceptions place in the record shape above, with constrained
  operator asks and the hash-chained Tip Log.

The honest one-liner: **the checking is production, the routing decision
is measured, the tips are designed.** The router v1 already routes to a
fixed slate of internal destinations; this design is what turns a "tip"
into a learnable, verifiable profile for any company's software — the
reverse-MCP layer the Hopper grows next.

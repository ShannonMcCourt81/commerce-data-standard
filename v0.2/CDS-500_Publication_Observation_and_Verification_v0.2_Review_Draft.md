# Commerce Data Standard (CDS)
## CDS-500 — Publication, Observation and Verification

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 (single corpus release per ADR-D5) |
| Date | 2026-08-04 |
| Supersedes | CDS-500 Working Draft v0.1 (3 August 2026) |
| Normative status | §1, §3–§27 are normative except where individually marked. §2, §28 and the appendices are informative. |
| Findings addressed | CDS500-1, CDS500-2, CDS500-3, CDS500-4, CDS500-5, CDS500-6, CDS500-7, CDS500-8, CDS500-9, CDS500-10; CDS900-1 (status/colour conflict, resolved here per ADR-D3); LEG-2, LEG-4, LEG-6, LC-1, LC-2; ADR-D3 (implemented in full), ADR-D24 §3; CLEANUP-PASS items 2 (cross-reference side) and 6 |

**Single-home notice.** CDS-500 is the sole normative home for: the publication assurance lifecycle, the expected-channel-state model, field ownership contracts, the observation and coverage model, the comparison/normalisation registry obligations, the **verification status enum**, the **traffic-light mapping**, and the rule that **read-back never overwrites canonical values**. Other chapters cite these; they do not restate them (CDS000-R005, Reconciliation Matrix 5). Machine encodings live in CDS-1100; platform specifics live in CDS-900 profiles; terminology lives in CDS-100.

---

## 1. Purpose and Scope *(normative)*

CDS-500 defines publication as an assurance lifecycle, not a single API call. It specifies how an implementation converts a canonical product revision into an expected channel representation, validates and dispatches that representation, observes what the channel actually exposes, compares expected and observed values, and reports or repairs discrepancies. It applies to API integrations, file feeds, supplemental feeds, bulk imports, event streams and manual channel exports, independent of channel type.

**CDS500-R001** The PIM MUST remain the master product-information layer throughout the publication lifecycle (authority model: CDS-200).

**CDS500-R002** Publication MUST NOT be considered complete solely because a payload was generated, transmitted or acknowledged.

**CDS500-R003** Where a channel permits observation, the implementation MUST compare observed downstream state with the expected channel state.

**CDS500-R004** Where a channel cannot be observed, the implementation MUST report that limitation explicitly and MUST NOT represent the state as verified.

**CDS500-R005** Channel read-back MAY inform verification and repair, but observed state MUST NOT overwrite canonical values silently. Any adoption of an observed value into the canonical record MUST be an explicit, attributed, auditable change. *(This is the single normative home of the read-back rule; CDS-200 and other chapters cite it.)*

## 2. Publication Principles *(informative)*

| Principle | Meaning |
|---|---|
| Canonical before channel | A channel projection is derived from a versioned canonical revision. |
| Expected before actual | The expected channel state is calculated before anything is written. |
| Acknowledgement is not proof | Transport acceptance confirms receipt, not downstream fidelity. |
| Observe independently | Read-back uses the channel or a trusted downstream surface, never the outbound payload. |
| Compare semantically | Equivalent values may differ in case, order, formatting, units or identifiers. |
| Never hide uncertainty | Unsupported, unreadable and stale fields remain explicit states. |
| Repair by policy | Drift responses are governed, not improvised. |
| Evidence over assumption | Every status traces to payloads, responses, snapshots and rules. |
| Human-readable operations | An operator can see why a field is Green, Amber or Red without reading connector code. |
| Safe automation | Automated repair is bounded by ownership, criticality and confidence. |

## 3. Publication Assurance Lifecycle *(normative)*

The lifecycle runs: canonical revision → expected projection → preflight → dispatch → acknowledgement → independent observation → comparison → drift classification → governed repair → health.

**CDS500-R006** Each lifecycle stage MUST produce a durable status or evidence record sufficient to explain the current publication state.

**CDS500-R007** A later stage MUST NOT erase the evidence of an earlier stage.

### 3.1 Assurance Levels

| Level | Name | Meaning |
|---|---|---|
| PA-0 | MODELLED | Canonical product information exists; no channel projection calculated. |
| PA-1 | PROJECTED | An expected channel state has been calculated and versioned. |
| PA-2 | VALIDATED | The projection passes channel-specific preflight checks. |
| PA-3 | DISPATCHED | A publication attempt has been sent or exported. |
| PA-4 | ACKNOWLEDGED | The transport or channel reports acceptance or successful processing. |
| PA-5 | OBSERVED | A downstream snapshot has been read independently. |
| PA-6 | VERIFIED | Expected and observed values have been compared with declared strategies. |
| PA-7 | HEALTH-MANAGED | Drift, alerts, repair policies and trend reporting operate continuously. |

**CDS500-R008** An implementation MUST NOT claim a higher publication assurance level than the evidence it maintains. *(Conformance levels, tests and claims: CDS-1000.)*

*Informative note:* a channel may support only part of the lifecycle; the implementation declares the highest assurance level it can honestly provide in the channel profile.

## 4. Publication Entity Model *(normative)*

Publication is represented by related, versioned entities rather than mutable flags on a product record.

| Entity | Purpose |
|---|---|
| Channel Profile | Capabilities, constraints, credentials reference, field mappings, propagation window, observation support. |
| Canonical Revision | Immutable snapshot or revision identifier of master product data. |
| Publication Projection | Expected channel-specific representation produced from a canonical revision. |
| Publication Job / Record | One dispatch operation and its immutable attempt records. |
| Acknowledgement | Transport and processing response from the channel. |
| Observed Snapshot | Independent read-back of downstream state at a point in time. |
| Verification Result | Field-level comparison of expected and observed values, with status and reason code. |
| Health Summary | Aggregated product, batch, channel and organisation view. |
| Repair Action | Governed remediation attempt and its outcome. |
| Evidence Artifact | Payload, response, feed row, API result, checksum, screenshot reference or diagnostic report. |

**CDS500-R009** Publication projections and observed snapshots MUST identify the channel, product, revision and time to which they apply.

**CDS500-R010** A verification result MUST reference both the expected projection and the observed snapshot used in the comparison.

*Informative note:* machine-readable schemas for these entities are defined in CDS-1100; this chapter defines their semantics.

## 5. Channel Profiles and Capabilities *(normative)*

A Channel Profile declares what a destination can accept, return, transform and verify. Profiles prevent connector assumptions from leaking into the canonical model. Profile *content* for specific platforms lives in CDS-900; this section defines what any profile must declare.

| Capability | Description |
|---|---|
| write_mode | API, file, feed, bulk import, event, manual export or hybrid. |
| read_mode | API read-back, feed diagnostics, storefront observation, report download or unavailable. |
| field_support | Writable, readable, required, optional, derived or unsupported fields. |
| operation_semantics | Create, update, upsert, patch, full replace, append, delete, archive behaviour. |
| rate_limits | Request, batch, quota and retry constraints. |
| propagation_window | Declared delay allowance between acknowledgement and observable state (see §13, §17, §18). |
| normalisation | Known channel casing, truncation, sorting, sanitisation and unit rules. |
| identity | Product, variant and channel record identifiers. |
| ownership | Which system controls each field or list partition (§7). |
| verification_grade | Highest assurance level supported by the connector and channel. |
| critical_set | Declared fields whose failure blocks publication or escalates presentation (§18, §23). |

**CDS500-R011** Every channel connector MUST publish a governed, machine-readable or equivalent capability profile.

**CDS500-R012** A channel profile MUST declare a propagation window for each write mode it supports. The window bounds PENDING (§17) and drives Amber-to-Red escalation (§18).

**CDS500-R013** An organisation claiming verification for a channel MUST declare the channel's critical field set (which MAY be empty). The critical set drives escalation (§18) and the critical-failure cap (§23).

**CDS500-R014** A field unsupported by the channel MUST be marked unsupported rather than silently dropped.

## 6. Canonical Revisions, Projections and Expected Channel State *(normative)*

### 6.1 Projection identity

A projection is calculated from a specific canonical revision plus a specific channel profile, mapping set, dictionary versions and transformation rules:

```
projection_identity =
  product_id
  + canonical_revision
  + channel_id
  + channel_profile_version
  + mapping_version
  + dictionary_version
  + transformation_version
```

**CDS500-R015** The same projection inputs MUST produce the same expected channel state unless a declared non-deterministic process is involved.

**CDS500-R016** A projection MUST retain lineage to every canonical field, mapping and rule that contributed to each output field.

**CDS500-R017** A new mapping, dictionary or transformation version MUST be able to trigger re-projection even when the canonical product record has not changed.

### 6.2 Field mappings and transformations

Transformations convert canonical values into channel representations: dictionary lookup, taxonomy mapping, formatting, unit conversion, template rendering, omission and list construction.

**CDS500-R018** Every transformation MUST be identified by a versioned rule or function.

**CDS500-R019** Transformations SHOULD be deterministic and side-effect free.

**CDS500-R020** Lossy transformations MUST be declared so that verification compares against the expected lossy output rather than the richer canonical value.

**CDS500-R021** A transformation error MUST be reported separately from a channel rejection or a downstream mismatch (see §17, ERROR family).

### 6.3 Expected channel state

The expected channel state is the exact semantic representation the implementation expects to observe after publication and channel processing. It is first-class and persisted, not recomputed ad hoc at comparison time.

```
Expected field record (informative example):
  field_key: MF_material
  canonical_value: linen
  expected_channel_value: Linen
  destination: custom.material
  ownership: EXCLUSIVE_PIM
  comparison_strategy: NORMALIZED_TEXT
  criticality: important
  source_revision: product-123@rev-48
```

**CDS500-R022** Expected state MUST be calculated before dispatch and MUST be stored, or exactly reproducible from versioned inputs, for later comparison.

**CDS500-R023** Expected state MUST reflect declared channel transformations, not merely raw canonical values.

**CDS500-R024** Fields intentionally omitted by rule MUST be distinguishable from fields lost during transformation or publication.

## 7. Field Ownership Contracts *(normative)*

Multi-system commerce fails when ownership is implied rather than declared. Each channel declares field-level ownership modes.

| Ownership mode | Meaning |
|---|---|
| EXCLUSIVE_PIM | The PIM owns the entire field or list. Downstream edits are drift and may be overwritten. |
| PARTITIONED_PIM | The PIM owns only declared namespaces, prefixes, keys or list members. |
| MERGED | The connector combines PIM-owned and externally owned values under a deterministic merge rule. |
| CHANNEL_OWNED | The channel owns the field. The PIM may observe but does not publish it. |
| OBSERVE_ONLY | The PIM records the field for diagnostics without claiming authority. |
| UNMANAGED | The field is outside the connector contract and must not influence verification. |
| OVERRIDE_ALLOWED | The PIM owns the default; a governed channel-specific exception may replace it (§22). |

**CDS500-R025** Every published field and list MUST have a declared ownership mode.

**CDS500-R026** Full-replace operations MUST NOT delete channel-owned or externally owned values unless the ownership contract explicitly permits it.

**CDS500-R027** A partitioned or merged full-replace list MUST be rebuilt before dispatch by reading the current downstream list, retaining externally owned members, and regenerating all PIM-owned members from current rules.

**CDS500-R028** A manual downstream edit to an EXCLUSIVE_PIM field MUST be classified as drift, not accepted silently into the canonical record.

*Informative note:* tag lists commonly require PARTITIONED_PIM or MERGED ownership — the PIM may own collection and merchandising namespaces (e.g. `collection_*`, `merch_*`, regenerated from rules) while another application owns operational tags. See the worked example in §28.3. Tag governance: CDS-400; the publication merge rule lives here.

## 8. Preflight Validation, Publication Jobs and Records *(normative)*

### 8.1 Preflight

Preflight determines whether a projection is fit to publish before external side effects occur. Areas: schema shape; dictionary and taxonomy mappings active; identity (SKU, GTIN, variant, channel record IDs); channel constraints (length, character, image, URL, price, enumeration); ownership (payload changes only authorised fields); business rules (lifecycle, approval, eligibility); dependencies (parents, variants, media); change safety (preview of additions, changes, removals, list-replacement effects); channel readiness (credentials, quota, connector health).

**CDS500-R029** Blocking preflight errors MUST prevent dispatch.

**CDS500-R030** Preflight warnings MAY permit dispatch but MUST remain visible in the publication record.

**CDS500-R031** Bulk publication SHOULD provide a preview of field additions, modifications and removals — including full-replace list effects — before execution.

### 8.2 Jobs and publication records

A Publication Job is one dispatch operation; a batch groups related jobs. Each attempt produces an immutable Publication Record carrying: job, batch and correlation identifiers; channel, product and projection identity; operation (create, update, upsert, delete, archive, withdraw); requester; timing; attempt count; payload hash; status; evidence references.

**CDS500-R032** Every dispatch attempt MUST have a unique, immutable attempt record, even when retries belong to the same logical job.

**CDS500-R033** A batch MUST report partial success without converting successful items into failures or hiding failed items inside an overall success status.

## 9. Transport Acknowledgement *(normative)*

Acknowledgement records what the transport or channel reported after dispatch. It is evidence of processing, not verification of final state.

| Acknowledgement | Meaning |
|---|---|
| ACCEPTED | Request or file accepted for processing. |
| PARTIAL | Some records or fields accepted, others rejected. |
| REJECTED | Channel rejected the operation. |
| QUEUED | Accepted but not yet processed. |
| PROCESSED | Channel reports processing complete. |
| UNKNOWN | No reliable acknowledgement is available. |
| TIMEOUT | Outcome was not received within the declared interval. |

**CDS500-R034** Acknowledgement status MUST remain separate from verification status.

**CDS500-R035** A successful transport response (2xx, successful upload, processed feed) MUST NOT automatically produce MATCH verification results.

## 10. Idempotency, Delta Publication and Replace Semantics *(normative)*

**CDS500-R036** Where the channel supports idempotency keys, the connector SHOULD use them for retriable write operations.

**CDS500-R037** A delta publication MUST be calculated against a known prior expected or observed state, not against assumptions.

**CDS500-R038** The connector MUST declare whether an empty value means clear, omit, unknown or no change.

**CDS500-R039** Sorting SHOULD be canonicalised for semantically unordered lists to produce stable diffs and checksums.

*(Full-replace list safety: CDS500-R026/R027 in §7.)*

## 11. Retries, Errors and Partial Failure *(normative)*

Error classes: TRANSIENT (timeout, rate limit, outage), VALIDATION, AUTHENTICATION, AUTHORISATION, IDENTITY (target record unresolvable), CONFLICT (concurrent change, ownership violation), MAPPING, TRANSFORMATION, PARTIAL, UNKNOWN.

**CDS500-R040** Retries MUST use a bounded policy with attempt limits, delay and a terminal state.

**CDS500-R041** Deterministic validation, mapping and transformation errors MUST NOT be retried without a relevant data or configuration change.

**CDS500-R042** A partial batch failure MUST preserve successful results and separately queue or report failed items.

**CDS500-R043** Rate limiting and connector back-pressure MUST be visible as operational states, not misclassified as product-data errors.

## 12. Rollback, Withdrawal and Republication *(normative)*

Channels differ in whether they support rollback; CDS defines outcomes rather than assuming a universal undo.

**CDS500-R044** A rollback MUST identify the exact previously verified projection being restored.

**CDS500-R045** Where rollback is unsupported, the connector MAY republish an equivalent prior expected state as a new operation.

**CDS500-R046** Withdrawal, deletion, unpublishing and archiving MUST be distinct operations when the channel distinguishes them.

**CDS500-R047** Destructive operations MUST require stronger authorisation than ordinary field updates.

## 13. Scheduling and Verification Cadence *(normative)*

Verification may occur immediately, after propagation delay, on schedule, on demand, on canonical/mapping/override change, on channel events, or by governed sampling.

**CDS500-R048** The verification schedule MUST account for the channel's declared propagation window (CDS500-R012) so that in-window latency is reported as PENDING, not drift.

**CDS500-R049** Fields in the declared critical set SHOULD be verified more frequently than low-risk descriptive fields.

## 14. Downstream Observation *(normative)*

Observation independently retrieves the state a channel currently holds or exposes. The observation source and time are part of the evidence.

| Observation source | Use |
|---|---|
| Authoritative channel API | Preferred when the API returns the stored field. |
| Channel diagnostics or item report | Feed and marketplace processing results. |
| Storefront or public item endpoint | When the customer-visible result is the verification target. |
| Search index or catalogue export | When the downstream consumer differs from the write endpoint. |
| Connector cache | Acceptable only under CDS500-R052. |
| Manual evidence | Exceptional fields only; not representable as automated verification. |

**CDS500-R050** Observed snapshots MUST include capture time, source, channel record identity and freshness status.

**CDS500-R051** Read-back MUST NOT reuse the outbound payload as the observed state.

**CDS500-R052** A connector cache MAY serve as an observation source only when it was populated from channel read operations, and its entries carry capture time and provenance satisfying CDS500-R050. A cache populated from the connector's own writes MUST NOT be used as observed state.

**CDS500-R053** Where the write endpoint and the customer-visible endpoint differ, implementations SHOULD verify the surface relevant to the business objective.

*(Adoption of observed values into canonical data: CDS500-R005.)*

## 15. Observation Coverage and Unknown State *(normative)*

A missing returned value is not always proof that the channel stored nothing. CDS separates value state from observation capability.

| Coverage state | Meaning |
|---|---|
| OBSERVED_VALUE | The field was returned with a value. |
| OBSERVED_EMPTY | The field was returned and explicitly empty or null. |
| NOT_RETURNED | The field was expected in the response but absent. |
| UNSUPPORTED | The observation interface cannot expose the field. |
| PERMISSION_DENIED | The connector lacks access to observe the field. |
| NOT_APPLICABLE | The field does not apply to this item or channel. |
| STALE | A value was returned but does not meet the freshness requirement. |
| OBSERVATION_ERROR | The read operation failed. |
| PENDING_VISIBILITY | The write is acknowledged but the propagation window has not expired. |

**CDS500-R054** An implementation MUST preserve the distinction between absence of data and absence of observability. UNSUPPORTED, PERMISSION_DENIED and NOT_RETURNED MUST NOT be collapsed into the MISSING verification status without the evidence required by the derivation table in §17.4.

## 16. Normalisation and Comparison *(normative)*

Comparison determines semantic equivalence between expected and observed values. Every field declares a comparison strategy drawn from a documented normalisation registry.

### 16.1 Strategy catalogue

EXACT, CASE_INSENSITIVE, NORMALIZED_TEXT (unicode/whitespace/punctuation/case), IDENTIFIER, BOOLEAN, NUMERIC, NUMERIC_TOLERANCE (declared absolute or percentage), MONEY (currency + declared rounding), MEASUREMENT (unit conversion then numeric), DATE_TIME (time-zone and precision normalisation), UNORDERED_SET, ORDERED_LIST, MULTISET, HTML_SEMANTIC (declared sanitisation policy), URL_CANONICAL, IMAGE_IDENTITY, IMAGE_SEQUENCE, CHANNEL_RULE (specialised comparator declared in the channel profile).

### 16.2 Registry obligations

**CDS500-R055** Every verifiable field MUST declare a comparison strategy that is an entry in the implementation's normalisation registry.

**CDS500-R056** Each registry entry MUST declare: a stable comparator identifier, a behaviour version, supported input types, ordered normalisation steps, the equality rule, any tolerance parameters, and test vectors including at least one negative (non-matching) case. A change to normalisation or tolerance behaviour MUST increment the comparator version.

**CDS500-R057** A comparator's declared behaviour and test vectors are the sole authority for what its normalisation may discard. A comparator MUST NOT be applied outside its declared input types, and an implementation MUST NOT substitute a broader comparator than the one the field declares. *(This replaces the untestable v0.1 "must not hide meaningful data loss" rule: what the comparator may hide is exactly what its registry entry documents and its vectors demonstrate.)*

**CDS500-R058** Substring containment MUST NOT be used as a text-equality rule. Registries MUST record the substring false-green case of Appendix A.4 as a negative test vector for any text comparator.

**CDS500-R059** Comparison inputs and normalised forms SHOULD be retained for diagnostics, alongside the comparator identifier and version used.

*Informative note:* Appendix A seeds the registry with the production-proven legacy tolerance vectors (money rounded to 2 dp, weight to 3 dp, case/whitespace-insensitive text, unordered tag sets) and the documented substring false-green negative case (findings LEG-4/LC-2).

## 17. Verification Status Model *(normative — the single normative status enum for all of CDS)*

Verification status expresses the relationship between expected state, observation coverage and comparison result. This section implements ADR-D3. All other chapters cite this enum; CDS-1100 encodes it verbatim.

### 17.1 Core statuses (the machine contract)

**CDS500-R060** The core verification status enum is exactly: **MATCH, MISSING, MISMATCH, PENDING, UNOBSERVABLE, NOT_APPLICABLE, OVERRIDDEN, ERROR**. Implementations MUST NOT add, remove or rename core statuses.

| Core status | Meaning |
|---|---|
| MATCH | Expected and observed values are equivalent under the declared comparator. |
| MISSING | The channel was observed with sufficient evidence and the expected value is absent. |
| MISMATCH | Observed state contradicts expected state (differing value, or an unauthorised value present). |
| PENDING | Resolution is legitimately awaited (propagation latency, or expected/observed revisions not yet aligned). |
| UNOBSERVABLE | The field cannot currently be read back with sufficient evidence or freshness. |
| NOT_APPLICABLE | The field is intentionally outside the product-channel contract. |
| OVERRIDDEN | The result is governed by an active exception rather than by comparison (see §22). |
| ERROR | The lifecycle failed before a comparison verdict could be produced. |

### 17.2 Detailed statuses and deterministic rollup

**CDS500-R061** Every field-level verification result MUST carry a core status; it SHOULD additionally carry a detailed status. Where a detailed status is recorded, its core status MUST be derived from the following table with no implementation-defined variation:

| Detailed status | Rolls up to | Meaning |
|---|---|---|
| MATCH | MATCH | Equivalent under the declared comparator. |
| MISSING_DOWNSTREAM | MISSING | Observed with evidence; expected value absent. |
| MISMATCH | MISMATCH | Expected and observed values differ. |
| UNEXPECTED_DOWNSTREAM | MISMATCH | A value exists downstream where none was expected or authorised. |
| PENDING | PENDING | Propagation window not yet elapsed. |
| STALE_EXPECTED | PENDING | Observed state corresponds to a different expected revision; re-projection or re-observation is awaited. |
| UNOBSERVABLE | UNOBSERVABLE | The observation interface cannot expose the field, or access is denied, or no sufficiently fresh observation exists. |
| NOT_APPLICABLE | NOT_APPLICABLE | Outside the product-channel contract. |
| WAIVED | OVERRIDDEN | A governed exception accepts the discrepancy without redirecting the expected value (§22). |
| TRANSFORMATION_ERROR | ERROR | Expected state could not be calculated. |
| PUBLICATION_ERROR | ERROR | Dispatch failed or was rejected. |
| OBSERVATION_ERROR | ERROR | Read-back failed. |
| COMPARISON_ERROR | ERROR | Values could not be compared under the declared strategy. |

> RESOLVED — accepted as drafted (owner 2026-08-04; was new (resolved)): WAIVED rolls up to core OVERRIDDEN (both are "governed exception" outcomes, distinguishable by detailed status and reason code). The alternative — a ninth core status — was rejected to keep the machine contract at ADR-D3's eight values.

**CDS500-R062** SUPERSEDED is a record-retention state, not a live verification status. A verification result belonging to an older projection or publication revision MUST be marked superseded when a newer result for the same field exists, MUST be retained for audit, and MUST NOT appear in current status displays, health denominators or the machine status enum. *(Resolves the STALE_EXPECTED/SUPERSEDED boundary: STALE_EXPECTED is a live condition awaiting realignment; SUPERSEDED is an archival marker on the record.)*

### 17.3 Reason codes

**CDS500-R063** Every field-level verification result whose core status is not MATCH MUST carry a machine-readable `reason_code` drawn from the CDS_* reason-code registry defined in CDS-1100 §21. A free-text `message` MAY accompany the reason code but MUST NOT replace it.

**CDS500-R064** A MATCH produced under a redirected-expected override (§22) MUST carry OVERRIDDEN provenance (override identity) visible alongside the status.

*Informative note:* Appendix B provides a seed reason-code list. The registry itself — identifiers, governance, additions — is owned by CDS-1100 §21. Reason codes are a v0.2 design; they have no legacy precedent.

### 17.4 Derivation from observation coverage

**CDS500-R065** Where an expected value exists for a field, the field's detailed verification status MUST be derived from the observation coverage state (§15) as follows:

| Coverage state | Detailed status | Notes |
|---|---|---|
| OBSERVED_VALUE | MATCH, MISMATCH or COMPARISON_ERROR | Per the declared comparator. |
| OBSERVED_EMPTY | MISSING_DOWNSTREAM | The interface affirmatively returned empty/null. |
| NOT_RETURNED | UNOBSERVABLE, unless the channel profile declares that the read interface enumerates every stored field, in which case MISSING_DOWNSTREAM | Absence in the response is evidence of absence only when the profile declares complete enumeration. |
| UNSUPPORTED | UNOBSERVABLE | |
| PERMISSION_DENIED | UNOBSERVABLE | Reason code distinguishes the cause. |
| NOT_APPLICABLE | NOT_APPLICABLE | |
| STALE | UNOBSERVABLE | No sufficiently fresh observation; reason code `CDS_STALE_OBSERVATION`. |
| OBSERVATION_ERROR | OBSERVATION_ERROR | The coverage state and detailed status share a name by design; this row is their relation rule. |
| PENDING_VISIBILITY | PENDING | Only within the declared propagation window (CDS500-R066). |

*(This table promotes the v0.1 §30.2 sketch to normative and replaces the v0.1 §15 reference to a nonexistent "MISSING" status: coverage states derive to MISSING_DOWNSTREAM, never to a bare "MISSING" detailed status.)*

> RESOLVED — accepted as drafted (owner 2026-08-04; was new (resolved)): NOT_RETURNED derives to UNOBSERVABLE by default, flipping to MISSING_DOWNSTREAM only under a declared complete-enumeration read interface; the alternative (always MISSING) was rejected as unevidenced. STALE derives to UNOBSERVABLE rather than PENDING because staleness is an observation deficiency, not write latency.

### 17.5 PENDING expiry

**CDS500-R066** A field result MUST NOT remain PENDING beyond the channel's declared propagation window. When the window lapses, the implementation MUST re-verify: re-observe and re-derive the status under CDS500-R065, recording reason code `CDS_PROPAGATION_WINDOW_EXPIRED` on any non-MATCH outcome. If re-observation is not possible, the status MUST become UNOBSERVABLE with that reason code. In all cases the lapsed condition escalates at presentation (CDS500-R070).

### 17.6 Aggregation

**CDS500-R067** Verification status MUST be field-specific before it is aggregated to product, batch or channel level.

**CDS500-R068** A product-level verified claim MUST identify the canonical revision and the verification scope (which fields, which coverage) it covers.

## 18. Traffic-Light Presentation *(normative)*

A traffic light is a presentation layer over verification statuses. Colours are never stored statuses. This mapping is complete: every core status has exactly one row.

**CDS500-R069** Where traffic-light presentation is used, the colour mapping MUST be:

| Colour | Core statuses | Semantics |
|---|---|---|
| GREEN | MATCH | Expected equals observed under the declared comparator — with no exceptions. A MATCH under a redirected-expected override is GREEN with its OVERRIDDEN provenance visible (CDS500-R064). |
| AMBER | MISSING, PENDING, UNOBSERVABLE, OVERRIDDEN (including detailed WAIVED) | Attention: absence, latency, blindness or governed exception. Never a confirmed contradiction. |
| RED | MISMATCH, ERROR | Confirmed contradiction or lifecycle failure. |
| GREY *(optional)* | NOT_APPLICABLE | Outside the contract. Implementations that do not use GREY MUST NOT colour NOT_APPLICABLE as GREEN and MUST exclude it from success denominators either way. |

**CDS500-R070** An AMBER indicator MUST escalate to RED presentation when either declared condition is met: (a) the channel's declared propagation window for the publication has lapsed without resolution, or (b) the field is a member of the channel's declared critical set (CDS500-R013). Escalation changes presentation and alerting; it does not alter the stored status or reason code.

**CDS500-R071** WAIVED results MUST always present as AMBER. A waiver never produces GREEN; only a redirected-expected override that yields a true MATCH does (§22).

**CDS500-R072** The user interface MUST make the detailed status and reason code accessible from every traffic-light indicator. AMBER MUST NOT function as a generic category: the indicator MUST distinguish — via detailed status and reason code — whether the field is missing, pending, unobservable, overridden or waived.

**CDS500-R073** Colours MUST NOT be stored or exchanged as verification statuses. Machine records carry statuses and reason codes; colour is derived at presentation time.

*Informative note:* v0.1's BLUE ("in-progress activity") is dropped from the standard per ADR-D3. Implementations remain free to animate or badge in-flight operations as a local presentation choice; such a treatment is not a CDS colour and carries no conformance meaning. GREY and any further presentation variants are optional presentation extensions, never additional statuses.

*Informative note:* MISSING presents as AMBER, restoring the production-proven legacy semantics (blank on either side = amber; red = confirmed mismatch only — LEG-2) and resolving the v0.1 CDS-500/CDS-900 colour conflict in favour of Amber. The escalation rule (CDS500-R070) captures the real risk of long-standing absence without punishing day-one latency.

## 19. Feed-Output Three-Way Match *(normative — optional layer)*

Channel-formatted projections (the CH_ layer, ADR-D24) are first-class artifacts: a serialized feed column or formatted payload field, distinct from both the canonical value and the channel's stored state. Legacy production practice verified this layer independently (`DF_Match_*` — LEG-6/LC-1).

**CDS500-R074** An implementation MAY maintain expected/observed/match verification records at the formatted-output layer, in addition to canonical-versus-channel field verification. Where it claims this layer, each formatted-output field MUST use the §17 status enum, the §16 registry comparators and the §18 presentation rules, and the feed artifact MUST be verified end-to-end (generated output compared against the ingested or reported feed content).

**CDS500-R075** A formatted-output MATCH MUST NOT substitute for downstream observation: it proves the feed said what was intended, not that the channel stored or displays it.

## 20. Drift Classification *(normative)*

Drift is any downstream state that no longer conforms to the current expected channel state or ownership contract.

| Drift type | Description |
|---|---|
| EXTERNAL_EDIT | A user or application changed a PIM-owned value downstream. |
| CHANNEL_NORMALISATION | The channel transformed the value in a known but unmatched way. |
| CHANNEL_TRUNCATION | The channel shortened or removed content. |
| MAPPING_CHANGE | The expected output changed because a mapping or dictionary changed. |
| STALE_PUBLICATION | The channel still reflects an older canonical revision. |
| PARTIAL_PUBLICATION | Only part of a projection was applied. |
| IDENTITY_MISMATCH | The observed record belongs to the wrong product or variant. |
| DELETION | The expected record or field was removed. |
| DUPLICATION | Multiple downstream records represent one expected item. |
| UNMANAGED_MUTATION | A field outside the ownership contract changed; not PIM drift. |
| CONNECTOR_DEFECT | The connector transformed, omitted or targeted data incorrectly. |
| UNKNOWN_CAUSE | Evidence is insufficient to assign a cause. |

**CDS500-R076** Drift detection SHOULD assign a cause category separate from the verification status and reason code.

**CDS500-R077** A known channel normalisation SHOULD be incorporated into expected-state or comparator rules (with a registry entry per §16.2) rather than generating repeated false alarms.

### 20.1 Drift Attribution *(normative — owner decision A1/D17, 2026-08-04)*

Detection tells you *that* a value changed; attribution helps you find *who or what* changed it — which distinguishes an innocent staff mistake from a connector defect or an unauthorised edit.

**CDS500-R077a** Observation records MUST be retained append-only per field and channel (never overwritten in place), so that for any drifted field the implementation can produce: the **previous observed value**, the **new observed value**, and the **detection interval** (last observation at which the field still matched, first observation at which it differed).

**CDS500-R077b** When drift of type EXTERNAL_EDIT is detected, the implementation SHOULD correlate the detection interval with whatever actor evidence the channel exposes (event logs, audit logs, webhook actor metadata, staff activity records — declared per channel profile, CDS-900) and record the attribution outcome (actor identified, actor class identified, or unattributable) on the drift record.

**CDS500-R077c** Attribution evidence is observed data about the channel, never a verdict about intent. An unattributable drift is still drift; attribution failure MUST NOT delay detection, verification status or escalation.

*(Channel-specific attribution mechanisms and their limits are profile content: CDS-900. This restores and extends the legacy production insight that per-field expected/observed comparison — the Match fields — doubles as the change-detection layer.)*

*(Drift metrics and monitoring: CDS-1400. Republishing is not always the correct repair — see §21.)*

## 21. Reconciliation and Repair Policies *(normative)*

A repair policy determines what happens after drift or failure is detected: REPORT_ONLY, AUTO_REPUBLISH, RETRY_SAME_PROJECTION, QUARANTINE_PRODUCT, SUSPEND_CHANNEL, ACCEPT_EXCEPTION, REMAP_AND_REPROJECT, MANUAL_REPAIR, ROLLBACK, WITHDRAW.

**CDS500-R078** Automatic repair MUST be limited to fields and operations owned by the PIM under the declared ownership contract.

**CDS500-R079** Critical or destructive repair actions SHOULD require approval or a pre-authorised policy.

**CDS500-R080** Every repair action MUST create a new evidence record and MUST trigger re-verification where observation is supported.

## 22. Overrides and Exceptions *(normative)*

Channel-specific differences are sometimes legitimate. CDS permits explicit, governed exceptions without weakening the canonical model. An override record carries: identifier, scope (product/variant/field/locale/market/channel), replacement value (if any), reason, owner, approver, effective window, review date, verification expectation, and lifecycle status. *(Exception governance: CDS-800.)*

Two forms exist, with different verification outcomes (ADR-D3):

- **Redirected-expected override** — the override supplies an approved channel-specific replacement value. The expected channel state is recalculated to that value; verification compares against it and can yield a **true MATCH**, presented GREEN with OVERRIDDEN provenance (CDS500-R064).
- **Waiver (acceptance without redirection)** — a reviewed exception tolerates a known discrepancy without changing the expected value. The result is detailed status **WAIVED** (core OVERRIDDEN), presented AMBER always (CDS500-R071).

**CDS500-R081** An override MUST NOT silently replace canonical product truth; the canonical value is unchanged and the override is a distinct governed record.

**CDS500-R082** Overrides SHOULD be time-bounded and MUST carry a review date.

**CDS500-R083** Verification MUST compare against the active redirected expected value when one exists.

## 23. Channel Health and Aggregation *(normative)*

Health aggregates field-level evidence into product, batch and channel views. A score aids prioritisation; it never replaces reason codes or critical-field rules. Metric definitions, denominators and monitoring cadence are owned by CDS-1400; the aggregation rules below are owned here.

**CDS500-R084** Health calculations MUST publish their weighting, inclusion and critical-field rules.

**CDS500-R085** Any field in the declared critical set (CDS500-R013) whose presentation is RED — directly or via escalation (CDS500-R070) — MUST cap the aggregate product and channel presentation at RED regardless of the numeric score.

**CDS500-R086** NOT_APPLICABLE and superseded results MUST NOT count as successes in any health denominator; UNOBSERVABLE fields MUST NOT count as matched. *(No 100% match rate for unobserved fields — see CDS-1400.)*

```
Illustrative weighted score (informative):
  health = 100 * sum(field_weight * field_pass) / sum(field_weight)
  field_pass = 1 for MATCH; configurable partial value for PENDING or
  OVERRIDDEN; 0 for MISMATCH or ERROR
```

## 24. Audit, Lineage and Evidence *(normative)*

Every decision in the publication lifecycle is reconstructable from: the canonical revision used; projection inputs (profile, mappings, dictionaries, rules, overrides); expected payload; dispatch record; acknowledgement; observed snapshot; normalised comparator inputs; verification result with status, reason code and comparator version; repair history; and actor provenance (human, system, schedule or AI agent).

**CDS500-R087** Audit records MUST be append-only or otherwise protected against silent alteration.

**CDS500-R088** Sensitive payload content and credentials MUST be redacted or securely referenced without destroying operational traceability (hashes, IDs and reason codes retained).

## 25. Security, Permissions and Secrets *(normative)*

**CDS500-R089** Connector credentials MUST be stored in a secret-management mechanism and MUST NOT be embedded in product records, logs or exported evidence.

**CDS500-R090** Connectors SHOULD use the least privilege sufficient for their declared operations.

**CDS500-R091** Create, update, delete, withdraw, override and repair actions SHOULD support distinct permissions.

## 26. Bulk Operations and Scale *(normative)*

**CDS500-R092** Bulk systems MUST preserve product- and field-level outcomes even when transport is batched.

**CDS500-R093** A batch restart SHOULD resume from durable item states rather than replaying the full batch.

**CDS500-R094** Checksums MAY be used to avoid unnecessary projection, dispatch or comparison work, provided the checksum inputs are versioned and auditable.

## 27. AI Participation *(normative)*

AI may assist with anomaly classification, mapping suggestions, repair recommendations, prioritisation and evidence summarisation. It is never the authority for downstream truth. *(AI governance, autonomy levels and proposal lifecycle: CDS-700.)*

**CDS500-R095** AI-generated repair actions MUST remain constrained by field ownership, permissions and approval policy (CDS500-R078/R079).

**CDS500-R096** AI MAY propose that two values are semantically equivalent, but only a governed comparator or approved mapping MUST determine the verification result.

**CDS500-R097** An AI agent MUST NOT convert an UNOBSERVABLE or PENDING field into MATCH based on likelihood or inference.

**CDS500-R098** AI repair and triage proposals SHOULD key off reason codes and detailed statuses, not presentation colours.

## 28. Worked Examples *(informative)*

### 28.1 Metafield round trip (API-integrated storefront, e.g. Shopify)

```
Canonical:        MF_material = linen
Expected:         custom.material = "Linen" (single_line_text_field)
Acknowledgement:  productUpdate accepted            -> PA-4
Observed:         "Linen" (independent read-back)   -> PA-5
Comparison:       NORMALIZED_TEXT                   -> MATCH
Presentation:     GREEN                             -> PA-6
```

### 28.2 Missing versus unobservable

```
Field A: expected "Linen"; read-back returns the field as null
  coverage = OBSERVED_EMPTY -> MISSING_DOWNSTREAM (core MISSING)
  reason_code = CDS_OBSERVED_EMPTY -> AMBER (escalates per CDS500-R070)

Field B: expected "Blue"; read-back interface does not expose the field
  coverage = UNSUPPORTED -> UNOBSERVABLE
  reason_code = CDS_INTERFACE_UNSUPPORTED -> AMBER
```

The two fields never share a reason code (§17.4 is the normative derivation).

### 28.3 Full-replace tag safety

```
Current channel tags:  collection_Shirts, merch_featured, review_five_star
Ownership:             collection_*, merch_* = PARTITIONED_PIM
                       review_* = external application
New PIM projection:    collection_Shirts, merch_sale
Safe merged payload:   collection_Shirts, merch_sale, review_five_star
```

Sending only the PIM tags to a full-replace API would delete `review_five_star` — a CDS500-R026/R027 violation. PIM-owned partitions are regenerated from rules on every publication.

### 28.4 Mapping change without product edit

Canonical revision stays at rev-12; the dictionary mapping changes (`navy -> Blue`, previously `Navy`). A new projection is required because `dictionary_version` changed (CDS500-R017); verification uses the new expected value.

### 28.5 Channel health summary

```
Channel 1 (API round-trip):        PA-7, match 99.6%, coverage 100%,
                                   0 critical failures      -> GREEN
Channel 2 (feed with diagnostics): PA-6, match 96.8%, coverage 91%,
                                   4 missing GTINs in the critical set -> RED (cap)
Channel 3 (write-only feed mode):  PA-4, no field read-back in this
                                   integration mode -> AMBER, "acknowledged,
                                   not verified"
```

Channel 3's limitation is a property of the *integration mode in use* (a write-only feed without item-level read-back), not of any named platform; the same platform integrated through an API with read-back could reach PA-6.

## 29. Conformance and Relationship to Other Chapters *(informative)*

Conformance levels, test suites and claim rules for this chapter's requirements are defined solely in CDS-1000. Machine-readable encodings of the entities, the eight-value core enum, `detailed_status`, `reason_code` and the validation-output contract are defined in CDS-1100 (the enum is encoded verbatim from §17). Platform-specific profile content is defined in CDS-900. Monitoring metrics and drift-age reporting: CDS-1400. The architecture decisions behind this chapter are recorded in the global ADR register (notably ADR-D3, ADR-D24; superseding the v0.1 chapter-local CDS-ADR-020..029, whose substance survives as requirements here).

---

## Appendix A — Normalisation Registry Seed *(informative except A.1)*

### A.1 Registry entry shape *(normative)*

**CDS500-R099** Each comparator registry entry MUST record: `comparator_id`, `version`, `input_types`, `normalisation_steps` (ordered), `equality_rule`, `tolerance` (where applicable), `diagnostics`, and `test_vectors` including negative cases (per CDS500-R056/R058).

### A.2 Seed entries (legacy production tolerance vectors — LEG-4/LC-2)

These are the first entries of the registry, restored from proven production comparison behaviour:

| comparator_id | Behaviour | Positive vector | Negative vector |
|---|---|---|---|
| MONEY.round2 | Round both sides to 2 dp, then numeric equality (with currency match) | 19.999 vs 20.00 -> MATCH | 19.99 vs 20.00 -> MISMATCH |
| MEASUREMENT.weight_round3 | Convert to common unit, round to 3 dp, numeric equality | 1.5 kg vs 1500 g -> MATCH | 1.5005 kg vs 1500 g -> MISMATCH |
| NORMALIZED_TEXT.v1 | Case fold, trim, collapse internal whitespace, then equality | " French  Navy " vs "french navy" -> MATCH | "French Navy" vs "Navy" -> MISMATCH |
| UNORDERED_SET.v1 | Same unique members regardless of order | {a,b,c} vs {c,a,b} -> MATCH | {a,b} vs {a,b,c} -> MISMATCH |

### A.3 Money and measurement tolerances

Rounding precision (2 dp money, 3 dp weight) is part of the comparator version. Changing precision is a comparator version change (CDS500-R056), never a silent edit.

### A.4 Documented negative case: substring false-green

Legacy text comparison used substring containment (spreadsheet `SEARCH()`), which tolerated case and whitespace — and also real prefix differences. Example: expected `"Blue"`, observed `"Blue Grey"` — substring containment reports a match; the values differ. This case MUST appear as a negative test vector for text comparators (CDS500-R058). Substring containment is not an equality rule in CDS.

## Appendix B — Reason-Code Seed List *(informative)*

The reason-code registry (identifiers, governance, additions) is owned by CDS-1100 §21. This seed list illustrates the codes this chapter's rules require:

| Reason code | Typical detailed status |
|---|---|
| CDS_OBSERVED_EMPTY | MISSING_DOWNSTREAM |
| CDS_FIELD_NOT_RETURNED | MISSING_DOWNSTREAM or UNOBSERVABLE (per §17.4) |
| CDS_INTERFACE_UNSUPPORTED | UNOBSERVABLE |
| CDS_PERMISSION_DENIED | UNOBSERVABLE |
| CDS_STALE_OBSERVATION | UNOBSERVABLE |
| CDS_PROPAGATION_WINDOW_EXPIRED | any post-lapse non-MATCH (§17.5) |
| CDS_AWAITING_PROPAGATION | PENDING |
| CDS_EXPECTED_REVISION_AHEAD | STALE_EXPECTED |
| CDS_VALUE_DIFFERS | MISMATCH |
| CDS_UNEXPECTED_VALUE_PRESENT | UNEXPECTED_DOWNSTREAM |
| CDS_IDENTITY_MISMATCH | MISMATCH / drift IDENTITY_MISMATCH |
| CDS_CHANNEL_TRUNCATION | MISMATCH / drift CHANNEL_TRUNCATION |
| CDS_TRANSFORMATION_FAILED | TRANSFORMATION_ERROR |
| CDS_DISPATCH_REJECTED | PUBLICATION_ERROR |
| CDS_READBACK_FAILED | OBSERVATION_ERROR |
| CDS_COMPARATOR_FAILED | COMPARISON_ERROR |
| CDS_WAIVED_EXCEPTION | WAIVED |
| CDS_OVERRIDE_ACTIVE | (provenance on overridden results) |
| CDS_NOT_IN_CONTRACT | NOT_APPLICABLE |

## Appendix C — Platform, Legacy and Schema Pointers *(informative)*

- **Platform specifics.** The v0.1 Appendices C (Shopify implementation profile) and D (Google Merchant and feed-based channels) are replaced by the versioned, dated implementation profiles in **CDS-900**. Platform behaviour never shapes the requirements of this chapter (Reconciliation Matrix 5).
- **Legacy alignment.** The legacy Airtable/Shopify prefix mapping and migration alignment (v0.1 Appendix E) lives in the consolidated legacy annex (see CDS-1300). The migration mapping of legacy match fields is 1:1: green -> MATCH, amber -> MISSING/PENDING, red -> MISMATCH (ADR-D3); `DF_*` feed fields migrate to `CH_*` per ADR-D24, with the feed-layer verification pattern retained in §19.
- **Schemas.** Recommended entity schemas (the v0.1 Appendix A sketch) are superseded by the machine-readable contracts in **CDS-1100**: verification-result schema carries `status` (8-value core enum), `detailed_status`, `reason_code`, `coverage_ratio` and `comparison_engine_version`.

## Appendix D — Operational Checklist *(informative)*

1. Confirm the canonical revision is approved for publication.
2. Generate the projection with current profile, mappings, dictionaries and overrides.
3. Run blocking and warning preflight checks; preview additions, changes, removals and full-replace list effects.
4. Confirm field ownership and destructive-operation permissions.
5. Dispatch with correlation and idempotency identifiers where supported.
6. Record acknowledgement without treating it as verification.
7. Observe downstream state after the declared propagation window.
8. Normalise and compare with declared registry comparators.
9. Derive statuses per §17; present detailed status and reason code beneath any traffic light.
10. Classify drift; execute the governed repair or exception policy; re-verify.
11. Retain payload, response, observation, comparison and actor evidence.

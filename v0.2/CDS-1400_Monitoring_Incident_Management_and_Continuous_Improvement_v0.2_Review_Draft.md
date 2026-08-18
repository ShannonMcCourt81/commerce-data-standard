# Commerce Data Standard (CDS)
## CDS-1400 — Monitoring, Incident Management and Continuous Improvement

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 |
| Date | 2026-08-04 |
| Supersedes | CDS-1400 Working Draft v0.1 |
| Normative status | §1–§2, §4–§27 are normative except where marked otherwise. §3, §28, §29 and Appendices A–D are informative. Tables explicitly marked *(informative)* inside normative sections carry no requirements. |
| Findings addressed | SYS-3 (D18), SYS-4, 1400-1..14; ADR-D3 (Appendix E deleted — statuses and traffic lights single-homed in CDS-500 §17–§18); Matrix 5 (drift taxonomy → CDS-500 §20; AI rules → CDS-700; conformance claims → CDS-1000; test-outcome spellings → CDS-1000 §21) |

An operational assurance framework for detecting product-information defects, controlling incidents, measuring downstream health and converting evidence into sustained improvement.

---

## 1. Purpose and Scope *(normative)*

CDS-1400 defines how a CDS-conformant commerce information environment is monitored after adoption and how operational defects are detected, assessed, contained, repaired and prevented from recurring. It covers the full information path from source ingestion and canonical enrichment through channel publication, downstream observation, verification and customer-facing use.

The chapter treats product information as an operational service. Availability alone is insufficient: a PIM can be online while products are missing attributes, filters expose unusable values, channel mappings drift, or downstream listings differ from the expected state.

**CDS1400-R001** A CDS operating model MUST monitor correctness, completeness, timeliness and downstream fidelity in addition to technical availability.

**CDS1400-R002** An organisation MUST define how product-data incidents are declared, owned, escalated, resolved and reviewed.

**CDS1400-R003** Operational monitoring MUST use declared denominators and MUST NOT hide quarantined, failed or unobserved records (denominator rules: §6).

> Informative note: CDS-1400 does not prescribe a particular monitoring product. The controls may be implemented with dashboards, logs, metrics, queues, scheduled reports or a combination of systems.

## 2. Operating Scale and the Small-Team Profile *(normative)*

CDS-1400 names many roles, views and reviews. They are **hats, not headcount** — the same rule that governs migration functions in CDS-1300 §2. A sole trader and a hundred-person operations organisation can both conform; what scales is evidence and separation of duties, not the org chart.

**CDS1400-R004** Every role, review and monitoring domain named in this chapter MUST have a named owner. One person MAY hold any number of roles simultaneously, including all incident-command roles. A conformance assessment MUST NOT require distinct individuals per role.

**CDS1400-R005** Where staffing permits, the person coordinating an incident SHOULD NOT be the person performing the most complex repair, and the person who built a monitoring control or automation SHOULD NOT be its sole acceptor. Where one person must hold both hats, the incident or acceptance record MUST note the dual role and the compensating control applied (for example: checklist-driven self-review against the runbook, evidence archived for later independent review). Segregation-of-duties expectations and compensating controls are defined in CDS-800 §18; this chapter applies them, it does not redefine them. The small-team accommodation mirrors CDS-1300 §2.

**CDS1400-R006** An organisation MAY adopt the **small-team profile** by declaring it in its conformance claim (claim rules: CDS-1000). Under that profile the requirements listed in Table 2-1 apply at the downgraded level shown; **all other requirements apply unchanged**. Acceptance and evidence records are never waived — only the requirement for the people involved to be different individuals.

**Table 2-1 — Small-team profile downgrades**

| Requirement | Base level | Small-team profile level |
|---|---|---|
| CDS1400-R053 (SEV-1 post-incident review includes a participant who was not the primary responder) | MUST | Waived where no second qualified person exists; the review record MUST note the sole-operator condition, and the evidence package MUST be archived so a later independent review remains possible |

After the base-level corrections in this revision — the hats rule (R004), the informative cadence table (§26), SHOULD-level service objectives (R016), the next-business-day coverage allowance (R033) and combined dashboard views (§10) — R053 is the only remaining requirement that presupposes a second person. Migration-phase downgrades continue to be governed by CDS-1300 Table 2-1.

**CDS1400-R007** An organisation MAY declare the **enterprise operations profile** (an overlay profile under CDS-1000 §16). Under that profile: CDS1400-R016 (per-context service objectives) upgrades from SHOULD to MUST, and the minimum-roles column of Appendix B becomes applicable staffing guidance. Outside that profile the minimum-roles column is informative illustration only.

> RESOLVED (was D18 (resolved), owner decision 2026-08-04): accepted — self-declared eligibility, no headcount threshold, mirroring CDS-1300.

> RESOLVED — accepted as drafted (owner 2026-08-04; was new (resolved)): The enterprise operations profile is modelled as a CDS-1000 overlay profile so that its upgraded MUSTs are testable within the existing claim machinery; the alternative — leaving SLO enforcement to per-organisation declared thresholds only — was rejected because it gives large multi-team operations no claimable assurance tier.

## 3. Operational Assurance Principles *(informative)*

- **Observe the whole information path** — source, canonical, publication, downstream and customer-experience states.
- **Measure facts, not confidence** — health claims derive from reproducible metrics and evidence.
- **Separate expected from observed** — retain what should exist downstream and what was actually read back.
- **Alert on actionability** — an alert has an owner, a condition and a defined response.
- **Preserve detail beneath summaries** — colour views remain backed by precise statuses, reason codes and affected records.
- **Prefer early containment** — stop incorrect propagation before optimising full repair.
- **Make recovery reversible** — repair, replay and rollback preserve lineage and can be audited.
- **Learn without blame** — post-incident review improves systems and controls, not scapegoats.
- **Track recurrence** — repeated symptoms are a problem-management issue, not isolated tickets.
- **Continuously reduce uncertainty** — monitoring gaps and unobservable fields are explicit, owned risks.

## 4. Observability Model *(normative)*

CDS observability is the ability to determine the health and history of product information from recorded signals. The minimum model contains the linked states:

```
Source State
    -> Canonical State
    -> Expected Channel State
    -> Publication Attempt
    -> Observed Channel State
    -> Verification Result
    -> Customer Experience Signal
```

**CDS1400-R008** Monitoring MUST distinguish data state from processing state. A completed job does not prove that the resulting data is correct.

**CDS1400-R009** Each material signal SHOULD be traceable to product, variant, field, channel, canonical revision and the relevant mapping or dictionary version.

**CDS1400-R010** Where a downstream field cannot be observed, its verification state MUST be recorded as `UNOBSERVABLE` from the CDS-500 §17 enum. It MUST NOT be recorded or reported as `MATCH`. (Test executions that were never run use the CDS-1000 §21 outcome `NOT_TESTED`; verification statuses and test outcomes are distinct vocabularies.)

## 5. Monitoring Domains *(normative)*

*Representative signals (informative):*

| Domain | Representative signals |
|---|---|
| Source ingestion | Fetch success, freshness, record counts, duplicate identifiers, schema changes, parsing errors, supplier anomalies. |
| Canonical product layer | Completeness, validity, conflicts, unresolved overrides, stale values, product/variant integrity. |
| Taxonomies and dictionaries | Unmapped values, ambiguous aliases, deprecated entries, version changes, unexpected cardinality growth. |
| Workflow and enrichment | Queue age, blocked approvals, review backlog, failed rules, missing ownership, time-to-ready. |
| Publication | Preflight failures, attempted writes, acknowledgements, rejections, rate limiting, retries, publish lag. |
| Observation | Read-back coverage, retrieval failures, stale observations, unsupported fields, API visibility gaps. |
| Verification | Match rate, missing rate, mismatch rate, comparison errors, unresolved age, drift recurrence. |
| Customer experience *(conditionally observable — §24)* | Facet cardinality, zero-result combinations, navigation dead ends, search failures, incorrect counts. |
| AI and automation | Proposal volume, confidence calibration, rejection and override rates, out-of-dictionary output, model or prompt drift. |
| Security and tenancy | Credential failures, unauthorised changes, cross-tenant leakage, unusual export volume, evidence tampering. |

**CDS1400-R011** Every CDS operating profile MUST declare which monitoring domains are in scope and who owns each domain (one person MAY own all — §2).

## 6. Metrics, Measures and Denominators *(normative)*

A metric is useful only when its population, time window and exclusions are explicit. *(Measure kinds — count, rate, latency, age, distribution, trend, cardinality, coverage — are informative vocabulary; Appendix A gives the reference catalogue.)*

Worked example — why observation coverage and match rate are separate measures:

```
eligible_expected_fields    = 10,000
observable_expected_fields  =  9,200   (800 are UNOBSERVABLE on this channel)
observed_fields             =  9,050
matched_fields              =  8,960
mismatched_fields           =     60
missing_fields              =     30

observation_coverage        = 9,050 / 9,200   (how much we can see)
verification_match_rate     = 8,960 / 9,050   (how much of what we see is right)
```

Reporting `8,960 / 10,000` as a "match rate" would silently blend blindness into fidelity; reporting `100%` for the 800 unobservable fields would fabricate assurance. Both numbers must travel together.

**CDS1400-R012** A rate MUST name its numerator, denominator, eligibility rules, exclusions and measurement window.

**CDS1400-R013** Quarantined or failed records MUST remain visible in relevant operational denominators unless the metric explicitly measures a different population. A record MAY leave a denominator only through a disclosed disposition. This applies the corpus's strongest anti-gaming control (CDS1300-R047; quarantine model: CDS-400 §17).

**CDS1400-R014** An organisation MUST NOT report a 100 percent match rate — or any match rate — over fields that were not observed. Observation coverage MUST be reported separately from verification match rate and MUST NOT be folded into it.

## 7. Service Indicators, Objectives and Verification-Health Thresholds *(normative)*

*Reference indicators (informative):* publication success (accepted / attempted eligible records); verified fidelity (`MATCH` results / observed expected fields); observation coverage (observed / observable expected fields); freshness (records within permitted age / eligible records); workflow timeliness; facet usability (collection views within approved cardinality and zero-result thresholds); recovery (incidents restored within target / incidents in severity class).

**CDS1400-R015** For every verified channel, the organisation MUST declare and monitor verification-health thresholds — at minimum: acceptable mismatch rate, acceptable missing rate, minimum observation coverage and maximum unresolved-mismatch age. These declared thresholds are the **base assurance mechanism** of this chapter. (Channel health aggregation: CDS-500 §23; migration exit thresholds: CDS-1300 §23.)

**CDS1400-R016** Per-context service objectives (SLOs) with defined measurement windows SHOULD be defined over the reference indicators. Under the enterprise operations profile (R007) this requirement upgrades to MUST. Verification-health thresholds (R015) already deliver the core assurance; full SLO and error-budget apparatus is proportionate to multi-team operations, not a universal floor.

**CDS1400-R017** A breach of a declared threshold or a missed declared objective MUST trigger a review proportional to customer, commercial or compliance impact.

> Informative note: an error budget is the permitted amount of objective failure within a period; organisations may use it to balance change velocity against reliability work. CDS does not prescribe universal numeric targets because catalogue size, channel behaviour and business criticality differ (v0.1 ADR CDS-ADR-1400-008, retained).

## 8. Product, Catalogue and Channel Health *(normative)*

CDS distinguishes health at different aggregation levels — field, product, category, catalogue, channel, customer experience and operations. A single score may be useful for scanning, but it must not replace the underlying dimensions. Health computation and aggregation rules are owned by CDS-500 §23; this section applies them operationally.

**CDS1400-R018** A composite health score MUST expose its component measures, weights and unavailable inputs.

**CDS1400-R019** A green catalogue or channel score MUST NOT conceal a red condition on any field in the channel's **declared critical set**. The mechanism is CDS-500's: the organisation declares the critical field set per channel (CDS500-R013), and any critical-set field presenting RED caps the aggregate presentation at RED regardless of the numeric score (CDS500-R085). This chapter adds the operational obligation: the declared critical set MUST be reviewed when incidents reveal high-impact fields outside it.

## 9. Telemetry and Event Model *(normative)*

Operational signals SHOULD be emitted as structured events or equivalent records supporting correlation, replay and audit. *Reference event fields (informative):* `event_id`, `event_type`, `occurred_at`, `recorded_at`, `organisation_id`, `product_id`/`variant_id`, `field_id`, `channel_id`, `canonical_revision`, `mapping_version`, `dictionary_version`, `correlation_id`, `severity_hint`, `reason_code`, `evidence_reference`.

**CDS1400-R020** Telemetry MUST preserve tenant boundaries and MUST NOT expose sensitive supplier or customer data to unauthorised monitoring users (isolation rules: CDS-800 §19).

**CDS1400-R021** Event types and reason codes SHOULD be versioned and governed as controlled reference data. Verification reason codes are drawn from the CDS_* registry (CDS-1100 §21; seed list CDS-500 Appendix B), not invented per dashboard.

## 10. Dashboards and Operational Views *(normative)*

Dashboards are role-specific views over evidence. *The audience catalogue below is informative: it describes focus areas, not mandatory separate dashboards. Views MAY be combined; a small team MAY operate a single view covering all audiences.*

| Audience *(informative)* | Typical focus |
|---|---|
| Executive | Catalogue and channel health, objective attainment, major incidents, unresolved critical debt. |
| PIM operations | Ingestion freshness, canonical quality, workflow backlog, quarantines, change effects. |
| Channel operations | Publication, observation, verification, rate limits, retries, channel-specific failures. |
| Merchandising / UX | Facet cardinality, zero-result combinations, navigation defects, collection coverage. |
| Data stewardship | Unknown values, ambiguous mappings, dictionary changes, deprecations, ownership queues. |
| Engineering | Job health, APIs, transformations, event correlation, deployment regressions. |
| AI governance | Proposal quality, acceptance, corrections, calibration, prohibited-output incidents. |

**CDS1400-R022** Every summary dashboard MUST support drill-down to affected populations or evidence references.

**CDS1400-R023** Dashboard freshness and last-successful-update time MUST be visible on the dashboard itself.

**CDS1400-R024** Colour MUST NOT be the only signal conveying state in any operational view; a text label, status or reason code MUST accompany colour, for accessibility and for diagnosis. Traffic-light colour semantics and the detailed-status accessibility rule for verification indicators are owned by CDS-500 §18 (CDS500-R069, CDS500-R072–R073); this requirement extends the same principle to every operational view, not only verification indicators.

## 11. Alerting and Noise Control *(normative)*

Alerts exist to cause timely human or automated action. Reports and informational trends should not be disguised as urgent alerts. *Full alert anatomy (informative): condition, scope, owner, urgency, evidence, runbook link, suppression logic, clear condition — a useful design checklist, not eight mandatory artifacts.*

**CDS1400-R025** Every production alert MUST have an accountable response owner and a documented first action. This is the normative floor for alert design.

**CDS1400-R026** Alerts SHOULD be deduplicated by condition, scope and time window to prevent notification storms.

**CDS1400-R027** An alert that repeatedly produces no action MUST be reviewed and SHOULD be redesigned, downgraded or retired. Alerting is self-limiting by design: an ignored alert is operational debt, not coverage.

> Informative note: useful patterns include threshold alerts, absence-of-expected-event alerts, rate-of-change alerts and anomaly alerts. Anomaly alerts require extra caution because they are hard to explain and tune.

## 12. Incident Classification and Severity *(normative)*

An incident is an unplanned condition that materially threatens or degrades canonical integrity, publication fidelity, customer experience, compliance, security or operational continuity.

| Incident class | Description |
|---|---|
| Canonical integrity | Incorrect or lost authoritative product facts, identifiers or relationships. |
| Publication failure | Expected records cannot be published or are rejected. |
| Downstream drift | Observed channel state differs from expected state (causes: CDS-500 §20). |
| Taxonomy or dictionary defect | Incorrect classification, mapping, alias or facet grouping affects products. |
| Customer-experience defect | Filters, search, navigation or product details mislead or block customers. |
| Security or tenant isolation | Unauthorised access, leakage, tampering or cross-organisation exposure. |
| AI or automation defect | Automated enrichment or execution produces material incorrect output. |
| Observability failure | Monitoring or read-back cannot detect or measure a critical state. |
| Operational capacity | Backlog, rate limit, resource exhaustion or staffing prevents timely processing. |

| Severity | Impact interpretation |
|---|---|
| SEV-1 Critical | Widespread or high-risk incorrect data, security/tenant breach, material legal exposure, or loss of control over authoritative data. Immediate coordinated response. |
| SEV-2 High | Material customer or channel impact, significant publication failure, or major drift affecting a defined business area. Urgent response. |
| SEV-3 Moderate | Limited impact with available workaround; bounded degradation. Scheduled but prompt response. |
| SEV-4 Low | Minor defect, cosmetic issue, isolated warning or improvement opportunity. Normal work queue. |

**CDS1400-R028** Severity MUST be based on actual or credible impact, not only the number of affected records.

**CDS1400-R029** Security, safety, legal or tenant-isolation concerns MUST be allowed to raise severity even when the affected population is small.

**CDS1400-R030** Severity MAY change as evidence improves; changes MUST be recorded with rationale.

## 13. Incident Roles and Command *(normative)*

*Incident roles (informative — these are hats per §2, holdable by one person):* incident commander; technical or data lead; operations lead; communications lead; scribe / evidence owner; security or compliance lead; business owner; reviewer.

**CDS1400-R031** Every SEV-1 and SEV-2 incident MUST have a named incident commander. The commander MAY simultaneously hold any or all other incident roles (R004).

**CDS1400-R032** Where staffing permits, the person coordinating the incident SHOULD be distinct from the person performing the most complex repair; the sole-operator case is governed by R005 (dual role noted, compensating control recorded).

**CDS1400-R033** Decision authority, escalation contacts and coverage hours MUST be declared per severity and incident class before an incident occurs. Declared after-hours coverage MAY be next-business-day for any incident class **except security and tenant-isolation classes, which MUST have a declared immediate escalation path at all times**.

## 14. Detection, Triage and Declaration *(normative)*

Triage determines whether a signal is valid, its scope, likely impact and the next safe action. Early uncertainty is expected; hidden uncertainty is not. *Triage checklist (informative):* confirm the signal is current, not a stale dashboard or duplicate event; identify affected organisation, products, variants, fields, categories and channels; determine whether canonical state, publication state, observed state or customer presentation is wrong; check recent code, mapping, dictionary, taxonomy, supplier or bulk-edit changes; estimate impact and declare provisional severity; assign roles and open a durable incident record; decide whether to pause ingestion, enrichment, publication, automated repair or AI workflows; set the next update time and stakeholder audience.

**CDS1400-R034** An incident record MUST contain a declared start time, current severity, affected scope, owner and known evidence.

**CDS1400-R035** Triage MUST distinguish symptom, impact and suspected cause.

**CDS1400-R036** If continued automation can increase impact, the relevant automation MUST be paused or constrained (using the R040 mechanisms) until safe operation is demonstrated.

## 15. Containment, Remediation and Automation Safeguards *(normative)*

Containment limits further impact; remediation restores correct operation. *Containment options (informative):* pause publication; disable one mapping or rule; freeze automation and PIM-side edits on a bounded product set; revert a dictionary or taxonomy version; remove or hide affected listings; switch AI or automation to manual approval; preserve an evidence snapshot before repair changes state.

**CDS1400-R037** Containment MUST prioritise prevention of additional incorrect propagation over speed of full repair.

**CDS1400-R038** Repair actions MUST identify whether they change canonical values, expected channel state, downstream channel state or verification records.

**CDS1400-R039** A bulk repair MUST support preview, bounded scope, evidence capture and post-repair verification.

**CDS1400-R040** For each automated pipeline stage operated in production — ingestion, enrichment, publication, automated repair and AI workflows — a mechanism to pause or constrain that stage MUST exist and be operable **before** the automation runs in production. Containment capability is a system requirement, not an improvisation during the first incident. *(Promotes the capability that v0.1 assumed implicitly in triage and containment steps.)*

## 16. Drift Diagnosis and Repair Selection *(normative)*

Drift is a difference between the governed expected state and the observed state. The drift cause taxonomy (EXTERNAL_EDIT, CHANNEL_NORMALISATION, MAPPING_CHANGE, STALE_PUBLICATION, CONNECTOR_DEFECT, UNKNOWN_CAUSE and the rest) is owned by CDS-500 §20; repair policies by CDS-500 §21. This section governs their operational use.

**CDS1400-R041** Repair policy MUST be selected from the diagnosed drift cause. **Republishing MUST NOT be assumed to be the correct repair**: republishing over an unauthorised external edit destroys the evidence of who changed what; republishing "fixes" a channel normalisation only until the next publish; republishing cannot repair a canonical defect, an observation defect or a transformation defect at all.

*Diagnosis-to-repair guide (informative, causes per CDS-500 §20):*

| Diagnosed cause | Typical correct repair family |
|---|---|
| EXTERNAL_EDIT | Preserve evidence, then republish or escalate per ownership contract; address the editing practice (§28.2). |
| CHANNEL_NORMALISATION | Register the normalisation (CDS-500 §16.2) and adjust comparator or expected state — not repeated republish. |
| MAPPING_CHANGE / transformation defect | Fix the mapping or transformation, re-project, then republish. |
| STALE_PUBLICATION / PARTIAL_PUBLICATION | Republish through the governed path; verify. |
| Observation defect | Fix read-back; the channel may be correct already. |
| Canonical defect | Correct the canonical value under governance; then re-project and publish. |
| Monitoring gap | Record `UNOBSERVABLE`; treat as owned risk, not as health. |

**CDS1400-R042** Automatic repair MAY be used only for explicitly authorised, deterministic and bounded drift conditions, within PIM-owned fields (CDS500-R078).

**CDS1400-R043** A repair MUST be followed by observation and verification before the incident or defect is closed (CDS500-R080).

## 17. Rollback, Replay and Recovery *(normative)*

Recovery restores a known-good operating state and confirms the data path is reliable. *Recovery sequence (informative):* contain; capture evidence and scope; select rollback, forward-fix or replay; validate on a bounded cohort; execute with traceable batch identity; observe; verify; restore paused automation gradually; monitor for recurrence.

**CDS1400-R044** Critical mappings, dictionaries, taxonomies and transformations SHOULD have a known rollback mechanism. Channel-side rollback is republication of known-good state through the governed publication path, not restoration of channel-internal state (definition and irreversibility classes: CDS-1300 §17).

**CDS1400-R045** Replay MUST be idempotent or otherwise protected against duplicate or destructive effects.

**CDS1400-R046** An incident MUST NOT be declared recovered solely because processing resumed; affected data MUST meet the defined verification exit criteria (declared thresholds per R015).

## 18. Communication and Stakeholder Management *(normative)*

Incident communication states what is known, what is not known, what is being done and when the next update will occur. *Minimum content by stage (informative):* initial declaration — severity, start time, known impact, scope, containment, next update time; progress — new evidence, changed scope or severity, actions completed, remaining risks; recovery — restored state, verification coverage, residual risk, monitoring period; closure — confirmed outcome, remediation, review and action ownership.

**CDS1400-R047** Communication MUST distinguish confirmed facts from hypotheses.

**CDS1400-R048** External notification decisions MUST follow legal, contractual, security and channel obligations.

**CDS1400-R049** Sensitive evidence MUST NOT be copied into broad communication channels when a controlled reference is sufficient.

## 19. Post-Incident Review *(normative)*

A post-incident review (PIR) converts an operational failure into durable learning. It reconstructs conditions and decisions without rewriting history after the outcome is known.

**CDS1400-R050** Every SEV-1 incident MUST receive a documented post-incident review (template: Appendix D.1). Every SEV-2 incident SHOULD receive at least a lightweight review (template: Appendix D.2). *(v0.1 mandated full PIRs for all SEV-2 incidents; under this chapter's SEV-2 definition that produces review-writing as a standing tax at small scale and reviews nobody reads at large scale. The SHOULD, with a template that takes minutes rather than hours, keeps the learning loop without the tax.)*

**CDS1400-R051** The review MUST identify contributing conditions and control gaps, not merely the final triggering action.

**CDS1400-R052** Corrective actions arising from a review MUST have named owners and tracked completion evidence.

**CDS1400-R053** A SEV-1 review MUST include at least one participant who was not the primary incident responder. *(Small-team profile: waived per Table 2-1 with sole-operator note and archived evidence.)*

> Informative note: a blameless review does not remove accountability. It separates learning about system conditions from disciplinary or conduct processes, which are handled separately when required.

## 20. Problem Management and Recurrence Prevention *(normative)*

Problem management addresses underlying causes or repeated patterns not fully resolved by individual incident repair. *Recurrence patterns worth a problem record (informative):* repeated mismatch in the same field or channel; recurring supplier schema change; growing dictionary quarantine or alias debt; repeated manual channel edits to PIM-owned fields; frequent alert suppression or false positives; repeated facet-cardinality regressions; recurring AI rejection patterns; multiple incidents sharing an undocumented dependency; thresholds missed across consecutive periods.

**CDS1400-R054** Recurring incidents SHOULD be linked to a problem record with an accountable owner and a long-term remediation plan.

**CDS1400-R055** A temporary workaround MUST have an expiry date, review date or retirement condition recorded at the time the workaround is adopted.

**CDS1400-R056** Known operational debt MUST remain visible in operational reporting until it is accepted, remediated or explicitly retired.

## 21. Change and Regression Monitoring *(normative)*

Most product-data incidents follow a change: supplier import, dictionary edit, taxonomy move, mapping release, bulk update, API version change, theme change, AI model change or staff-process change. *Change controls (informative):* pre-change baseline; change identifier linking the change to telemetry; canary or bounded cohort; regression tests (CDS-1000 suites, CDS-1200 fixtures); post-change comparison against baseline; observation window covering asynchronous publication and indexing; defined rollback trigger.

**CDS1400-R057** Material changes MUST be identifiable in operational telemetry (a change identifier linkable to affected events and records).

**CDS1400-R058** Dictionary, taxonomy, mapping and AI changes SHOULD receive the same regression discipline as code changes.

**CDS1400-R059** A change MUST NOT be considered successful until its downstream effects have been observed and compared against the pre-change baseline within the declared observation window, with results inside the declared thresholds (R015).

## 22. Continuous Improvement System *(normative)*

Continuous improvement turns operational evidence into prioritised change: prevent defects, detect earlier, reduce impact, recover faster, remove toil, improve usability, improve assurance. *(The improvement loop and class examples of v0.1 §21 are retained as informative practice.)*

```
Operational evidence -> trend and incident review -> identify control gap
    -> prioritise by impact and recurrence -> implement bounded change
    -> test and observe -> confirm improved outcome
    -> update standard, profile, runbook or training
```

**CDS1400-R060** Improvement work SHOULD be prioritised using impact, recurrence, risk and effort rather than anecdote alone.

**CDS1400-R061** Completed improvements SHOULD be measured against the outcome they were intended to change.

## 23. AI and Automation Monitoring *(normative)*

AI and automation require both output-quality monitoring and operational monitoring; high throughput does not imply high quality. AI governance — proposals, evidence classes, confidence, abstention, autonomy levels A0–A4 — is owned by CDS-700; this section defines only the operational measurement obligations. *Reference measures (informative):* proposal acceptance rate; human correction rate; out-of-dictionary rate; abstention rate; confidence calibration; evidence coverage; override and rollback rate; model or prompt drift; automation blast radius.

**CDS1400-R062** AI monitoring segmentation MUST scale with the declared autonomy level of each workflow, exactly as defined by CDS700-R081: segmented monitoring distinguishing AI-originated from human-originated values is MUST for A3/A4 workflows, SHOULD for A2, and MAY be limited to volume and sampled quality checks for A1. This chapter supplies the mechanics; CDS-700 owns the scaling rule.

**CDS1400-R063** AI quality MUST be measured against reviewed outcomes, not the model confidence value alone.

**CDS1400-R064** A material decline in quality or an increase in prohibited output MUST trigger containment proportional to the workflow's autonomy level (CDS-700), using the pause/constrain mechanisms required by R040.

## 24. Customer-Experience Signals *(normative)*

Customer-experience health is the hardest domain to observe: most storefronts and marketplaces do not expose interaction telemetry to the PIM side. CDS therefore distinguishes signals computable from governed data from signals requiring channel telemetry.

**CDS1400-R065** Facet cardinality and zero-result **construction** (facet values whose product set is empty by construction) MUST be monitored. These are the minimum customer-experience signals: they are computable PIM-side from governed dictionaries, facet projections and product data, on every channel, with no storefront telemetry required (facet rules: CDS-600).

**CDS1400-R066** Interaction-derived signals — search failure rates, zero-result filter *interactions*, navigation abandonment — are **conditionally observable**. Each channel profile MUST declare whether interaction telemetry is available; where it is not, customer-experience health MUST be reported as a declared monitoring gap for those signals, never assumed healthy.

**CDS1400-R067** Where interaction telemetry is available, it SHOULD be monitored. Interaction-metric monitoring is otherwise profile-optional and MAY be bound to the customer-experience overlay profile (CDS-1000).

## 25. Security, Privacy and Evidence Retention *(normative)*

Monitoring and incident records may contain supplier pricing, unpublished product information, credentials, customer-impact evidence or internal system details. *Practice checklist (informative):* least-privilege access to dashboards, logs and incident records; tenant-scoped telemetry and evidence; redaction or tokenisation of secrets and unnecessary personal data; controlled export and sharing; audit-integrity and timestamp preservation; retention matched to contractual, legal and operational needs; legal hold where required; secure deletion after expiry; monitoring tools reviewed as part of the security boundary.

**CDS1400-R068** Monitoring data MUST follow the same tenant-isolation and access-control principles as product data (CDS-800 §19).

**CDS1400-R069** Secrets, authentication tokens and sensitive personal data MUST NOT be intentionally recorded in general operational telemetry.

**CDS1400-R070** Incident evidence retention MUST be governed and documented.

## 26. Operating Cadence and Review *(normative)*

*Cadence catalogue (informative — a menu, not a mandate):*

| Cadence | Typical review |
|---|---|
| Continuous / event-driven | Critical alerts, publication failures, security events, threshold breaches. |
| Daily | Failed jobs, stale sources, oldest quarantines, unresolved high-impact mismatches. |
| Weekly | Quality trends, workflow backlog, mapping debt, recurring alerts, action progress. |
| Monthly | Objectives/thresholds, incident trends, customer-experience metrics, AI quality, monitoring gaps. |
| Quarterly | Dictionary and taxonomy health, conformance posture, access review, recovery readiness. |
| After material change | Regression review and post-change comparison (§21). |
| After qualifying incident | Post-incident review and action tracking (§19). |

**CDS1400-R071** The operating model MUST include, at minimum: **(a)** one recurring operational review, at a declared cadence, with recorded outcomes and tracked actions; and **(b)** a defined post-incident review path (§19). *(v0.1 mandated five governed review forums; that is enterprise practice, not a conformance floor. One honest recurring review that produces decisions beats five that produce minutes.)*

**CDS1400-R072** A recurring review that repeatedly produces no decisions, ownership or follow-up SHOULD be redesigned or retired — the same self-limiting rule that governs alerts (R027). Reviews are for decisions, not attendance.

## 27. Conformance *(normative)*

Conformance levels, test suites, outcomes and claim rules are owned by CDS-1000. A CDS-1400 conformance claim is a claim against the requirement set CDS1400-R001–R072 (with the Table 2-1 substitution where the small-team profile is declared, and the R007 upgrades where the enterprise operations profile is declared), evidenced per CDS-1000.

The recommended practices of this chapter — service objectives and error budgets (§7), separated dashboard audiences (§10), telemetry correlation and versioned reason codes (§9), canary releases (§21), the continuous-improvement loop (§22), AI calibration monitoring (§23), interaction-metric monitoring (§24) and tested runbooks (Appendix C) — are SHOULD-level and MAY be cited as supporting evidence in a claim. *(v0.1's conformance list restated several of these SHOULDs as MUSTs; this section now matches the strengths of the requirements it summarises — finding 1400-8.)* The testable operational-debt controls remain MUST: workaround expiry (R055) and visible known debt (R056).

## 28. Worked Incident Scenarios *(informative)*

### 28.1 Colour Facet Explosion

**Signal.** Colour facet cardinality rises from 12 to 87 after a supplier import (R065).
**Triage.** Canonical colour dictionary remains valid; the import bypassed alias mapping; raw supplier shades were published as facet values.
**Containment.** Pause affected collection facet publication; revert the facet projection to the last known-good dictionary version.
**Repair.** Quarantine unknown shades (they stay in the denominator — R013); map approved aliases; republish facet values; verify counts and collection filtering.
**Prevention.** Facet-cardinality regression test; alert on raw-to-facet ratio change.

### 28.2 Channel Metafield Drift (SEV-2)

**Signal.** Verification of the material field on a Shopify channel reports 430 `MISMATCH` results. Expected `Linen`, observed `Cotton`; recent change: a manual bulk edit in the channel admin. Diagnosed drift cause: `EXTERNAL_EDIT` (CDS-500 §20).

**Response.**
- Declare SEV-2: customer-visible incorrect material claims.
- Preserve the observation snapshot **before** repairing — republishing first would destroy the evidence of what was edited and when (R041).
- Confirm PIM canonical values are correct (rule out a canonical defect masquerading as drift).
- Republish a bounded cohort through the governed path; observe and verify; then repair the remainder in batches (R039, R043).

**Follow-up — with real mechanisms.** "Freeze affected channel edits" is not an operation most platforms provide; the platform cannot lock a merchant-editable metafield against admin users. The real controls are:

- **Staff instruction and training** — operators are told, specifically, which channel-admin edits will be overwritten or treated as drift (this is the CDS1300-R051 training obligation applied in run-state).
- **Permission narrowing** — restrict which staff accounts hold channel-admin roles that can edit products/metafields at all; this is coarse (role-level, not field-level) but is an enforceable platform mechanism.
- **App-owned namespaces** — move PIM-owned metafields into an app-owned namespace, which admin users cannot edit. **Trade-off:** app-owned metafields are also not visible to merchants in the admin UI, so staff lose the ability to *see* the governed values in their daily tool, which can itself cause errors and shadow spreadsheets.
- **Drift detection stays armed regardless** — enforcement may be detection-only, and that is a legitimate declared posture (CDS1300-R014(c)).

> RESOLVED — accepted as drafted (owner 2026-08-04; was D17 (resolved)): For PIM-owned channel metafields there is an unresolved tension between **app-owned namespaces** (edit-proof but invisible to merchant staff) and **merchant-visible metafields** (visible and editable, so protected only by permissions, training and drift detection). This chapter permits either posture provided it is declared per channel profile with its residual risk; the alternative — mandating app-owned namespaces for all PIM-owned fields — was rejected because operator visibility loss is itself an error source.

### 28.3 Supplier Feed Staleness

**Signal.** No successful stock-source event for 28 hours; expected cadence is daily (absence-of-expected-event alert).
**Triage.** Supplier portal changed HTML format; canonical descriptions and prices unaffected; stock values now stale.
**Containment.** Flag source freshness as stale; prevent stale stock from being represented as freshly verified; notify purchasing and channel operations.
**Repair.** Update the parser; run a bounded extraction test; replay the source load (idempotent — R045); verify quantity and publication effects.
**Prevention.** Keep the absence alert; add a parser fixture from a supplier sample.

### 28.4 AI Material Misclassification

**Signal.** Human correction rate for AI material extraction rises from 4% to 21% after a model change (segmented monitoring per R062 localises it).
**Triage.** Decline limited to homewares image-only extraction; the model confuses rattan-look resin with natural rattan.
**Containment.** Reduce autonomy to proposal-only for the affected task (containment proportional to autonomy — R064, CDS-700); require text evidence or human review.
**Repair.** Revert the model version or update evidence rules; re-evaluate unreviewed proposals.
**Prevention.** Benchmark fixtures for imitation materials; quality gate by product family and evidence class.

## 29. Architecture Decisions *(informative)*

Per CDS000-R006, ADRs live in the single global register. Decisions originating in this chapter, recorded there: monitor data correctness as an operational service; keep observation coverage separate from match rate; base severity on impact, not record count; require verification after repair; treat reference-data and AI changes like code changes; make continuous improvement evidence-driven; prescribe no universal numeric objectives (profiles may). The v0.1 record CDS-ADR-1400-003 (detailed statuses beneath traffic lights) is **subsumed by ADR-D3**, whose normative expression is CDS-500 §17–§18; v0.1 Appendix E (five-colour palette including BLUE) is superseded — see the note after Appendix D.

## Appendix A — Reference Metric Catalogue *(informative)*

| Metric | Definition | Dimensions | Type |
|---|---|---|---|
| source_freshness_age | Age since last successful authoritative source update | source, organisation | duration |
| ingestion_failure_rate | Failed eligible source records / attempted eligible source records | source, batch | rate |
| canonical_required_completeness | Populated required fields / required eligible fields | family, category | rate |
| dictionary_unmapped_rate | Unmapped reference values / distinct eligible reference values | dictionary, source | rate |
| quarantine_backlog | Records currently awaiting governed resolution | queue, owner | count and age |
| publication_lag | Canonical approval to channel acknowledgement | channel, category | duration distribution |
| publication_failure_rate | Failed publication records / attempted eligible records | channel, reason | rate |
| observation_coverage | Observed expected fields / observable expected fields | channel, field | rate |
| verification_match_rate | `MATCH` results / observed expected fields | channel, field | rate |
| unresolved_mismatch_age | Age of unresolved `MISMATCH` | channel, severity | duration distribution |
| facet_cardinality | Distinct facet values exposed | facet, collection | count |
| zero_result_combination_rate | Zero-result filter interactions / filter interactions *(conditionally observable — §24)* | facet, collection | rate |
| ai_correction_rate | Materially corrected accepted proposals / accepted proposals | task, model | rate |
| incident_mtta | Declaration time minus detection time | severity, class | duration |
| incident_mttr | Verified recovery time minus declaration time | severity, class | duration |
| incident_recurrence_rate | Recurring incidents / closed incidents | class, period | rate |

## Appendix B — Severity and Response Matrix *(informative)*

The **minimum-roles column describes the enterprise operations profile (R007)**; it is informative illustration for all other adopters — every role is a hat holdable by one person (§2).

| Severity | Response expectation | Minimum roles *(enterprise profile — informative)* | Communication | Exit condition |
|---|---|---|---|---|
| SEV-1 | Immediate (coverage per R033) | Incident commander; technical/data lead; communications; business owner; security/compliance as relevant | Continuous coordination until contained; frequent updates | Verified containment and business approval to downgrade |
| SEV-2 | Urgent | Incident commander; owning technical/data team; channel/business owner | Regular updates during active response | Material impact stopped; verified recovery plan operating |
| SEV-3 | Prompt business-hours response unless risk increases | Owning team and data/channel owner | Updates at agreed milestones | Scope corrected or controlled workaround accepted (with expiry — R055) |
| SEV-4 | Normal queue | Named owner | Status through work management | Fix, acceptance or explicit retirement |

> Informative note: profiles or organisations may define numeric acknowledgement and restoration targets. Targets should be realistic, measured and reviewed, not copied without operational capacity.

## Appendix C — Runbook Template *(informative)*

| Section | Content |
|---|---|
| Runbook identity | Name, owner, version, last tested date, applicable services. |
| Trigger | Alert conditions, reason codes, scope. |
| Safety checks | Actions not to be taken without approval; data or channel risks. |
| Triage | Queries, dashboards, record samples, recent-change checks. |
| Containment | Safe ways to stop propagation, including the R040 pause mechanisms for each stage. |
| Repair | Deterministic repair, rollback or replay procedure. |
| Verification | Expected observations, comparison strategy, exit criteria. |
| Escalation | Contacts, severity triggers, external obligations. |
| Evidence | Required snapshots, batch IDs, logs, decision records. |
| Recovery | How paused automation is restored and monitored. |
| Known limitations | Unobservable fields, manual dependencies, unsupported scenarios. |

## Appendix D — Post-Incident Review Templates *(informative)*

### D.1 Full review (SEV-1 — R050)

Incident identifier, title, severity and dates; executive summary; impact and affected populations; detection and declaration; timeline; expected controls and actual behaviour; contributing factors; containment and recovery; verification evidence; what went well; what made response difficult; corrective and preventive actions; owners, due dates and completion evidence; recurrence indicators and review date; changes to CDS profiles, runbooks, tests or training.

### D.2 Lightweight review (SEV-2 — R050)

One page or less:

```
Incident:        <id, title, SEV-2, dates>
What happened:   <two or three sentences>
Impact:          <affected products/fields/channels/customers>
Why:             <contributing conditions and the control gap, not just the trigger>
Fixed by:        <repair + verification evidence reference>
Prevent next:    <0..3 actions, each with an owner and a date>
Recurrence of:   <link to problem record, or "first occurrence">
```

---

**Appendix E of v0.1 is deleted.** Traffic-light presentation is single-homed in **CDS-500 §18** (implementing ADR-D3): GREEN/AMBER/RED plus optional GREY, whose denominator semantics are preserved there — `NOT_APPLICABLE` is never a success state and is excluded from success denominators either way (CDS500-R069). v0.1's **BLUE / INFORMATIONAL tier is dropped** from the standard; in-flight badging remains a local presentation choice with no conformance meaning (CDS-500 §18 note). The accessibility rule survives strengthened as CDS1400-R024 (colour never the only signal, in any operational view) alongside CDS500-R072.

END OF CDS-1400 v0.2 REVIEW DRAFT

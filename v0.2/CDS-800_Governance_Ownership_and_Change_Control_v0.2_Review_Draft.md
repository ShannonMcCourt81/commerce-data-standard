# Commerce Data Standard (CDS)
## CDS-800 — Governance, Ownership and Change Control

> RESOLVED (was new (resolved), owner decision 2026-08-04): retitle accepted — "Governance, Ownership and Change Control". File renamed to match.

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 |
| Date | 2026-08-04 |
| Supersedes | CDS-800 Working Draft v0.1, including its §9 conformance ladder (superseded by CDS-1000 per ADR-D1) and its exception/waiver dual vocabulary (superseded by the single Exception definition in CDS-100 §4) |
| Normative status | §1, §3–§8, §9–§30 are normative except where marked. §2 (principles), §31 (scenarios), Annexes A–C, E (templates/checklists) and Annex F (organisation example) are informative. Annex D is a normative pointer. |
| Findings addressed | 800-1 (via ADR-D1), 800-2, 800-3, 800-5, 800-6, 800-7, 800-8, 800-9, 800-10; SYS-1 (CLEANUP-PASS §C: all 86 prefix-labelled rules corrected, including the one ambiguous case), SYS-2 (requirement IDs), SYS-4 (non-testable MUSTs); ADR-D1, ADR-D24; REVIEW-003 Matrix 5 dedup |

---

## 1. Purpose and Scope *(normative)*

CDS-800 defines how a CDS implementation is governed over time: authority, ownership, decision rights, change control, quality oversight, audit evidence, security responsibility and the governance of conformance claims. Conformance **levels, tests and claim schemas** are owned by CDS-1000; this chapter governs who may claim, how claims stay honest, and how the organisation operates the standard day to day.

A technically capable PIM still fails if nobody owns the taxonomy, uncontrolled dictionary values are accepted, channel mappings change without review, or editors work around the master data layer. Governance exists to keep those failures from becoming normal operating practice.

**CDS800-R001** Every CDS implementation MUST define accountable ownership for the canonical product model, each governed data domain and each publication channel.

*Informative note:* Governance does not require a large committee. A small organisation may assign several roles to one person (see §18 and ADR-800-008), but responsibilities and decision rights remain explicit. Governance is judged by operating behaviour and its evidence trail (§16), not by the existence of a policy document.

## 2. Governance Principles *(informative)*

- **Accountability precedes automation.** A system may automate work only after authority, ownership and exception handling are defined.
- **One owner, many contributors.** Many people and systems may contribute to a field; one authority resolves conflict (CDS-200 §13).
- **Enter data where it originates.** Information is captured and corrected in its system of authority, not patched downstream. Downstream edits to upstream-owned facts are drift, not maintenance (CDS-500 §11).
- **The standard is stable; implementations evolve.** Local tools and schemas change without weakening CDS principles (CDS-P-12, Governance Over Convenience).
- **Change is deliberate.** New fields, values, namespaces and mappings follow a visible proposal and review path.
- **Exceptions are explicit.** A deviation is recorded, time-bounded and reviewed — never an undocumented permanent rule.
- **Evidence survives decisions.** Approvals, migrations, mappings and verification results remain auditable.
- **Quality is measured.** Completeness, validity, consistency, mapping coverage and channel fidelity are observable (CDS-1400).
- **Access follows responsibility.** Users receive the minimum permission needed for their role.
- **Customer impact matters.** Governance decisions consider storefront discovery, accessibility, truthfulness and usability.
- **Conformance is testable.** Requirements are capable of objective assessment wherever practical (CDS-1000).

## 3. Governance Operating Model *(normative)*

```
CDS Standard and Profiles
        -> Organisation Policies and Ownership
        -> Schemas + Taxonomies + Dictionaries + Rules
        -> Product Data Operations and Publication
        -> Verification + Metrics + Audit Evidence
        -> Review, Change and Continuous Improvement
```

**CDS800-R002** The governance model MUST cover definition, operation, monitoring and change, and MUST NOT stop after initial PIM configuration.

**CDS800-R003** An organisation SHOULD maintain one identifiable forum or accountable role capable of resolving cross-domain conflicts.

*Informative note:* The forum may be called a Data Council, Product Information Council, PIM Steering Group or any locally meaningful name. CDS governs function, not branding.

## 4. Decision Rights and Authority *(normative)*

| Decision | Required authority | Typical consultation |
|---|---|---|
| Create or retire a product family | PIM Product Owner | Schema, taxonomy, channel and operations owners |
| Add or rename a category | Taxonomy Owner | Merchandising, SEO, channel and analytics owners |
| Add a canonical dictionary value | Dictionary Owner | Merchandising and channel owners |
| Change a facet grouping | Facet and Search Owner | Dictionary, search and merchandising owners |
| Add or change a canonical attribute | Schema Owner | Domain steward, integration and channel owners |
| Introduce a semantic namespace | CDS Governance Owner | Architecture, integration and operations owners |
| Change a channel mapping | Channel Owner | Schema, dictionary and verification owners |
| Approve an AI workflow for canonical writes | AI Governance Owner and Product Data Owner | Security, product and operations owners |
| Declare CDS conformance | Conformance Declaration Executive | CDS Governance Owner and assurance functions |

**CDS800-R004** A decision right MUST identify who may approve, who must be consulted and who must be informed.

**CDS800-R005** The person requesting a material change SHOULD NOT be the only person approving it when the change can affect many products or channels.

**CDS800-R006** The organisation MUST declare, in its implementation statement (§9), the thresholds that make a change *material* (for example: product count affected, number of channels affected, breaking-change class per §11).

> RESOLVED — accepted as drafted (owner 2026-08-04; was new (resolved)): R006 converts the otherwise untestable "material change" qualifier (SYS-4) into a declared-threshold mechanism. Alternative: fix corpus-wide thresholds in CDS-1000 test conditions.

## 5. Roles and Responsibilities *(normative)*

This table is the **role register** for the CDS corpus. Other chapters and local artefacts use these role names; local titles MAY differ where the mapping is documented (§9).

| Role | Accountability |
|---|---|
| CDS Governance Owner | Local interpretation of CDS, policy hierarchy, namespace introduction and unresolved cross-domain decisions. |
| Conformance Declaration Executive | The executive or accountable system owner who approves and signs conformance declarations (§29). |
| PIM Product Owner | System capability, roadmap, operational fitness and the master product layer. |
| Product Data Owner | A business data domain and its fitness for use. |
| Data Steward | Definitions, values, quality, issue resolution and daily governance within a domain (may specialise: Taxonomy Steward, Dictionary Steward). |
| Schema Owner | Product families, attribute definitions, requiredness and validation rules. |
| Taxonomy Owner | Internal category structure, boundaries, mappings and decision log. |
| Dictionary Owner | Canonical values, aliases, facets, channel representations and value lifecycle. |
| Facet and Search Owner | Customer-facing filter behaviour, search synonyms, ranking and usability outcomes. |
| Channel Owner | Destination capability, mappings, policy requirements, publication behaviour and channel health. |
| Integration Owner | Connector behaviour, transformations, retries, technical monitoring and data lineage. |
| AI Governance Owner | AI use-case approval, risk classification, evaluation, evidence and human-review policy (controls: CDS-700). |
| Security and Compliance Owner | Access, data handling, regulated claims, retention and incident obligations. |
| Auditor / Assurance Reviewer | Independent assessment of conformance, evidence and control operation. |

**CDS800-R007** One person MAY hold multiple roles, but each responsibility MUST remain explicitly assigned.

**CDS800-R008** Role assignment MUST be reviewed when personnel, systems or operating models change.

## 6. Domain Ownership Contracts *(normative)*

A domain ownership contract states what a domain owns, consumes, enforces and commits to downstream.

```
Domain: colour
Owner: Dictionary Owner
Canonical facts: canonical shade, colour family, aliases
Consumes: supplier colour text, image evidence
Publishes: display label, search terms, channel colour values
Controls: allowed values, mappings, deprecation, facet membership
Quality measures: unmapped rate, ambiguous rate, channel mismatch rate
```

**CDS800-R009** Each governed domain SHOULD have a concise ownership contract accessible to operators and automated agents.

**CDS800-R010** A domain contract MUST distinguish canonical facts from derived display, facet and channel representations.

## 7. Policy and Document Hierarchy *(normative)*

| Level | Artefact | Function |
|---|---|---|
| 1 | CDS specification | Vendor-neutral normative requirements and terminology |
| 2 | CDS profile | Industry, platform or overlay implementation constraints |
| 3 | Organisation policy | Local authority, risk, approval and operating rules |
| 4 | Data model and registries | Schemas, taxonomies, dictionaries, mappings and namespaces |
| 5 | Procedures and runbooks | How operators execute, verify and recover work |
| 6 | Records and evidence | Approvals, releases, exceptions, audits and verification results |

**CDS800-R011** Lower-level artefacts MUST NOT silently contradict higher-level normative requirements.

**CDS800-R012** Where an implementation cannot satisfy a requirement, the deviation MUST be represented through the exception process (§14) rather than hidden in procedure.

## 8. Conformance Levels and Profiles *(normative)*

The single CDS conformance ladder is defined in CDS-1000: **Foundation → Structured → Publisher → Verified → Governed**, strictly cumulative, with **overlay profiles** (for example AI-Assured, CX, multi-tenant) claimable alongside a level. Level definitions, test suites, evidence packages and claim schemas are owned by CDS-1000 and are not restated here.

*Supersession note (ADR-D1):* the v0.1 CDS-800 §9 ladder (Foundation → Governed → Publisher → Verified → AI-Assured) is withdrawn. "CDS Governed" now names only the capstone level of the CDS-1000 ladder; "AI-Assured" is an overlay profile, not a level.

**CDS800-R013** A profile MUST identify the CDS release it depends on.

**CDS800-R014** A profile MAY add required attributes, dictionaries, rules or mappings, but MUST NOT weaken any base CDS requirement or the cumulativity of the conformance levels. *(The v0.1 exception-based escape clause is deleted — finding 800-2. Implementation-level deviations use the exception process (§14); a profile itself is never a vehicle for weakening.)*

**CDS800-R015** Organisation-specific extensions MUST use governed identifiers registered per CDS-300 and MUST NOT collide with reserved CDS namespaces.

*Informative note:* Profiles make the standard practical without turning platform-specific behaviour into universal product truth.

## 9. Organisation-Specific Implementation Statement *(normative)*

Local choices — role-name mappings, approval and materiality thresholds (R006), product families, custom attributes and dictionaries, channel enablement, risk classes and human-review thresholds, quality targets, retention and access controls, approved extension namespaces — are recorded in one controlled place.

**CDS800-R016** Local implementation choices MUST be documented in an implementation statement or equivalent controlled record.

**CDS800-R017** Local naming MAY differ from CDS examples, provided semantic intent and the mapping to CDS terms remain unambiguous.

## 10. Change Proposal Lifecycle *(normative)*

```
Propose -> Triage -> Impact Analysis -> Consult Owners
  -> Approve / Reject / Return -> Implement in Test
  -> Validate and Migrate -> Release -> Observe and Review
```

| Required proposal field | Purpose |
|---|---|
| Change identifier | Stable reference for discussion and audit |
| Problem statement | Explains the need, not only the desired solution |
| Affected domains | Schemas, products, dictionaries, channels and users |
| Proposed change | The exact model or rule alteration |
| Compatibility impact | Breaking and non-breaking effects (§11) |
| Migration plan | Data, connector and channel transition |
| Validation plan | How correctness will be tested |
| Owner and approver | Accountability |
| Target release | Connection to deployment control (§28) |
| Rollback or recovery | Response to adverse outcomes |

**CDS800-R018** Material changes (per the declared thresholds, R006) MUST be represented by a durable change proposal before production implementation.

**CDS800-R019** Emergency changes MAY use an accelerated path, but MUST be documented and reviewed retrospectively.

## 11. Versioning and Release Policy for Governed Artefacts *(normative)*

Corpus and document versioning is defined in CDS-000 §4 (ADR-D5). This section governs **local** artefacts: schemas, dictionaries, taxonomies, mappings and profiles. Semantic-versioning principles apply, adapted to the impact on consuming systems and stored data.

| Change class | Typical examples | Version effect |
|---|---|---|
| Major / breaking | Remove a field, change meaning, replace identifiers, incompatible cardinality | Major version |
| Minor / compatible | Add optional field, add dictionary value, add supported mapping | Minor version |
| Patch / corrective | Correct documentation, label or non-semantic metadata | Patch version |

**CDS800-R020** Version identifiers MUST change when a governed artefact changes semantically.

**CDS800-R021** A release record MUST identify included changes, migrations, tests, approvals and effective date.

## 12. Compatibility and Migration *(normative)*

Migration execution (baselines, cutover, rollback mechanics) is defined in CDS-1300; this section governs the change-control obligations.

**CDS800-R022** A breaking change MUST include a migration plan and a defined compatibility period, unless immediate removal is required for safety, law or severe data-integrity risk.

**CDS800-R023** Migration tooling SHOULD provide a preview of affected products and values before bulk changes are applied.

**CDS800-R024** Channel mappings and verification logic MUST be reviewed when canonical identifiers or value semantics change.

*Informative note:* Renaming a display label may be a patch. Replacing a stable canonical identifier is a breaking change.

## 13. Deprecation, Aliases and Removal *(normative)*

```
Active
  -> Deprecated (replacement announced)
  -> Migration in progress
  -> Read-only alias / compatibility period
  -> Removed from new use
  -> Retired after evidence confirms no active dependency
```

**CDS800-R025** Deprecated fields and values MUST identify a replacement or explicitly state that no replacement exists.

**CDS800-R026** Aliases MAY support ingestion and migration, but MUST resolve to one canonical identity.

**CDS800-R027** A deprecated identifier MUST NOT be reused for a different meaning.

**CDS800-R028** Removal MUST be blocked while verified active dependencies remain, unless a documented risk decision authorises otherwise.

## 14. Exceptions *(normative)*

An **Exception** is defined once, in CDS-100 §4: a time-limited, documented, approved deviation from a requirement, with an expiry and a named owner. An exception acknowledges non-conformance; it does not convert failure into conformance. The v0.1 "waiver" noun is retired (CDS-100 §8, finding 800-3); the field-level verification status `WAIVED` remains and is defined in CDS-500.

| Required field | Description |
|---|---|
| Identifier | Stable exception reference |
| Requirement | The CDS or local control being deviated from (requirement ID where applicable) |
| Scope | Products, fields, channels, teams or dates affected |
| Reason | Why conformance is not currently practical |
| Risk | Customer, operational, legal, security and data-quality effects |
| Compensating control | What reduces the risk during the exception |
| Owner and approver | Who accepts accountability |
| Expiry or review date | Prevents permanent undocumented drift |
| Resolution plan | How the organisation returns to conformance |
| Retest result | Evidence at closure that conformance was re-established |

**CDS800-R029** Every exception MUST have an owner, scope, rationale, compensating-control assessment and a review or expiry date.

**CDS800-R030** Expired exceptions MUST NOT remain silently active.

**CDS800-R031** Exception closure MUST record a retest result demonstrating that conformance was re-established, or a new approved exception continuing the deviation. *(New in v0.2 — finding 800-6.)*

## 15. Data Quality Governance *(normative)*

Data quality is assessed against fitness for use, not merely field population. The quality dimensions below are the governance vocabulary; canonical metric formulas, denominators and monitoring live in CDS-1400 (which owns Channel Health and the no-100%-for-unobserved-fields rule).

| Dimension | Meaning *(informative)* |
|---|---|
| Completeness | Required information is present |
| Validity | Values conform to definitions, types, units and rules |
| Consistency | Equivalent facts agree across products and representations |
| Uniqueness | Identifiers and records do not create unintended duplicates |
| Timeliness | Information is updated within an appropriate operating window |
| Provenance | Source and decision history are known |
| Mapping coverage | Canonical values have required facet and channel mappings |
| Publication fidelity | Observed channel state matches expected state (CDS-500) |
| Usability | Customer-facing values support clear discovery and decisions |

**CDS800-R032** Quality rules MUST identify the applicable scope, severity, owner and remediation path.

**CDS800-R033** A product SHOULD NOT be published while blocking quality rules fail.

**CDS800-R034** Each governance metric (for example exception age, change failure rate) MUST be defined with an explicit formula and denominator such that repeated calculation produces comparable results.

**CDS800-R035** Quality targets SHOULD be set by risk and business use rather than one universal threshold.

*Informative note:* A 100% score can still mislead if the wrong fields are required. Governance reviews the model as well as the metric.

## 16. Audit Evidence and Traceability *(normative)*

Evidence classes retained: current and historical schema definitions; category, dictionary, mapping and namespace versions; change requests and approvals; publication and observation records; verification outcomes and channel-health calculations; exceptions; AI evidence and workflow versions where applicable; access changes and privileged actions; migration results and rollback evidence; conformance assessments and declared scope.

**CDS800-R036** Audit evidence MUST be sufficient to reconstruct who changed what, when, under which authority and with what downstream effect.

**CDS800-R037** Retention periods MUST be declared per record class in the implementation statement and reflect legal, operational and assurance needs.

## 17. Security and Access Governance *(normative)*

**CDS800-R038** Access MUST follow least privilege and be granted according to role responsibilities.

**CDS800-R039** Privileged actions such as schema change, bulk publication, mapping replacement and canonical-value deletion SHOULD require stronger authentication and enhanced audit logging.

**CDS800-R040** Supplier credentials, channel tokens and other secrets MUST NOT be exposed through human-readable product fields or AI model inputs. *(Absolute — aligned with the CDS-700 §26 credential rule, finding 700-3; the v0.1 "approved need" escape applied only to non-secret confidential source data, which remains policy-gated under CDS-700.)*

**CDS800-R041** Production and test environments SHOULD be separated.

## 18. Segregation of Duties *(normative)*

| Activity | Recommended separation *(informative)* |
|---|---|
| Create schema change | Requester separate from final approver for material changes |
| Create channel credentials | Credential administrator separate from ordinary product editors |
| Bulk publish | Operator separate from policy owner for high-impact releases |
| Approve high-risk AI canonical writes | Reviewer separate from workflow developer (CDS-700) |
| Declare conformance | Conformance Declaration Executive supported by independent assessment |
| Close serious incident | Incident owner supported by verification or assurance review |

**CDS800-R042** Material high-risk changes SHOULD involve at least two distinct accountable participants.

*Informative note (small teams — ADR-800-008):* Where full organisational separation is impractical, small teams MAY substitute system controls, delayed approval, peer review or periodic independent review. The CDS-1300/CDS-1400 small-team profile cross-references this accommodation; roles are hats, responsibilities are not erased.

## 19. Multi-Tenant and Organisation Isolation *(normative)*

**CDS800-R043** Organisation-specific products, dictionaries, mappings, credentials, exceptions and audit records MUST be isolated from other organisations.

**CDS800-R044** A shared CDS baseline MAY provide definitions and templates, but MUST NOT expose or merge tenant-specific values without explicit authorisation.

**CDS800-R045** Imports and bulk actions MUST execute within a declared organisation context.

**CDS800-R046** Cross-tenant administrative access MUST be privileged, logged and reviewed.

*Test-coverage note (finding 800-7):* conformance tests for R043–R046 are bound to the **multi-tenant overlay profile** defined in CDS-1000; single-tenant implementations declare the profile not applicable.

## 20. Supplier and Import Governance *(normative)*

**CDS800-R047** Every supplier source MUST have an identified owner, acquisition method, field mapping, refresh policy and trust classification.

**CDS800-R048** Raw source values SHOULD be preserved separately from resolved canonical values (value model: CDS-400).

**CDS800-R049** Bulk imports MUST provide validation results and a preview of high-impact changes before commit.

Unknown-value quarantine and the prohibition on imports silently creating canonical values are defined in CDS-400 §17 and are not restated here.

## 21. Taxonomy Governance *(normative)*

Governed content per taxonomy: category name, definition and inclusion boundary; parent-child relationships and depth; primary-category assignment rules; tie-breaking decision log; inherited family or attribute rules; external taxonomy mappings; collection and navigation projections.

**CDS800-R050** Every category MUST have a recorded scope definition that distinguishes what belongs from what does not.

**CDS800-R051** A taxonomy change MUST analyse product reassignment, collection, navigation, facet, SEO and channel impacts before approval.

**CDS800-R052** Ambiguous product-type decisions SHOULD be recorded in a taxonomy decision log.

## 22. Dictionary and Reference-Data Governance *(normative)*

The value model — stable canonical identifiers, alias resolution, promotion of source values, quarantine — is owned by CDS-400. This section governs the change-control obligations around it.

**CDS800-R053** New canonical values MUST be checked for existing synonyms, aliases and facet membership before approval.

**CDS800-R054** Facet-grouping changes MUST consider customer usability, product counts, search behaviour and channel effects (facet requirements: CDS-600).

**CDS800-R055** Dictionary owners MUST monitor unknown, ambiguous and unmapped value rates.

**CDS800-R056** Channel representations MUST be reviewed when destination vocabularies change.

## 23. Attribute and Schema Governance *(normative)*

| Change question *(informative)* | Required consideration |
|---|---|
| Does the attribute describe a stable product fact? | If not, it may belong to workflow, channel or merchandising state |
| Is an existing attribute semantically equivalent? | Avoid duplicates and near-duplicates |
| What is the scope and cardinality? | Product, variant, category or channel; single or multi-value |
| Is a dictionary required? | Prefer controlled values for filterable and mapped information |
| Who owns the value? | Assign authority and stewardship |
| How is it validated? | Type, range, unit, dependency and source evidence |
| How is it displayed and filtered? | Separate canonical, display and facet behaviour |
| How is it published and verified? | Define channel mappings and comparison strategy |

**CDS800-R057** A new attribute MUST have an Attribute Definition (CDS-200 §7) before product values are created at scale.

**CDS800-R058** Attribute removal or semantic change MUST follow the compatibility and migration controls of §12.

## 24. Namespace Governance *(normative)*

The single normative prefix registry, the naming tests and the reserved-prefix rules are owned by CDS-300.

**CDS800-R059** Introduction, deprecation or retirement of a semantic namespace MUST follow the change proposal lifecycle (§10) and be recorded in the CDS-300 registry.

**CDS800-R060** Legacy prefix aliases MAY remain during migration, but new fields SHOULD use the current approved namespace.

The DF_ → CH_ transition is recorded once, in ADR-D24 (see CDS-300); it is not restated here.

## 25. Channel Governance *(normative)*

| Channel governance object | Minimum content |
|---|---|
| Capability profile | Supported fields, limits, types, observability, update semantics (content: CDS-900) |
| Mapping registry | Canonical source, transformation, destination and version |
| Ownership contract | Channel owner, integration owner and escalation path |
| Publication policy | Eligibility, scheduling, retry and approval rules (CDS-500) |
| Verification policy | Read-back coverage, comparison and health thresholds (CDS-500) |
| Override policy | Allowed local differences and expiry/review rules (CDS-500 §22) |
| Change watch | How platform schema and policy changes are detected and assessed |

**CDS800-R061** Each active channel MUST have an owner and a maintained capability profile.

**CDS800-R062** Channel changes MUST be assessed against mappings, publication, observation and verification before production rollout.

## 26. AI Governance *(normative)*

All AI controls — autonomy levels, risk classes, evidence, evaluation, provenance, human review, exception handling for AI outcomes — are owned by CDS-700 and are not restated here *(finding 800-8; the v0.1 §29 duplicates are deleted)*. This chapter contributes only the role-assignment rule:

**CDS800-R063** Every production AI workflow MUST have a named owner recorded in the workflow registry (CDS-700).

## 27. Incident, Drift and Recovery Governance *(normative)*

Incident management process, severity model and monitoring are owned by CDS-1400; drift classification and repair by CDS-500. This section governs the accountability obligations.

| Incident class *(informative)* | Expected response |
|---|---|
| Data integrity (wrong canonical values, duplicate identities) | Contain, assess scope, correct and verify |
| Publication (incorrect bulk update, partial channel writes) | Pause, reconcile, retry or roll back |
| Drift (downstream edits, platform transformations) | Classify ownership, restore or approve override (CDS-500) |
| Security (credential exposure, cross-tenant leakage) | Revoke, contain, investigate, notify as required |
| AI quality (systematic hallucination, regression) | Disable workflow, review accepted outputs (CDS-700) |
| Governance (expired exception, bypassed approval) | Record non-conformance, restore control, review cause |

**CDS800-R064** A material incident MUST have an owner, severity, affected scope, containment action and closure evidence.

**CDS800-R065** Incident closure MUST include verification that canonical and downstream states are correct.

**CDS800-R066** Repeated incidents SHOULD trigger root-cause review of schema, process, tooling or authority design.

## 28. Release and Deployment Governance *(normative)*

```
Approved Change Set -> Build / Configuration -> Test Data Validation
  -> Migration Preview -> Approval Gate -> Production Release
  -> Publication Observation -> Verification and Health Review
  -> Close or Roll Back
```

**CDS800-R067** A production release MUST identify the included change records and the versions of affected governed artefacts.

**CDS800-R068** High-impact releases SHOULD use staged rollout, limited product cohorts or channel canaries.

**CDS800-R069** A release MUST NOT be considered complete until required verification and health checks pass.

## 29. Conformance Claims Governance *(normative)*

Level definitions, test suites, evidence packages and the claim/manifest schema are owned by CDS-1000 (claim schema: CDS-1000 §23). This section governs claim integrity and authority.

**CDS800-R070** A conformance claim MUST describe the implemented scope and level honestly; an organisation MUST NOT claim conformance to capabilities it has not implemented.

**CDS800-R071** An implementation MUST pass all MUST and MUST NOT requirements applicable to its declared scope.

**CDS800-R072** SHOULD requirements MAY be unmet only where a documented rationale exists. *(Keyword corrected per the CLEANUP-PASS §C ambiguous-case ruling: the governing modal is MAY; "SHOULD requirements" is a noun reference to the requirement class.)*

**CDS800-R073** A conformance claim MUST be accompanied by a dated conformance statement conforming to CDS-1000 §23, approved by the Conformance Declaration Executive.

**CDS800-R074** An organisation MAY declare different conformance levels or overlay profiles for different channels or business units, provided each claim's scope is explicit.

**CDS800-R075** Assessment method MUST be stated using the CDS-1000 §20 vocabulary: **self-attestation**, **customer assessment** or **independent assessment** *(finding 800-5; replaces v0.1 "self-assessed / partner-reviewed / independent")*.

**CDS800-R076** A certification mark or badge MUST NOT imply independent assessment when only self-attestation occurred.

**CDS800-R077** Material scope or control changes SHOULD trigger reassessment before a previous claim is reused.

*Informative example claim (CDS-1000 naming):* CDS v0.2 · scope: apparel catalogue, AU organisation, Shopify and Google channels · level: **CDS Verified** · overlay profiles: none (AI-Assured overlay not claimed) · assessment: self-attestation, 2026-08-04 · known exceptions: EXC-014, expires 2026-10-01. Full field set: CDS-1000 §23.

## 30. Review Cadences and Forums *(normative)*

| Cadence *(informative)* | Typical review |
|---|---|
| Daily / event-driven | Import failures, publication errors, blocking quality issues, security alerts |
| Weekly | Unknown values, workflow queues, channel drift, ageing incidents |
| Monthly | Quality scorecards, mapping coverage, AI evaluation, change backlog |
| Quarterly | Taxonomy, dictionary, namespace, exception and access review |
| Per release | Schema, mapping, migration and conformance impact |
| Annually | Governance model, ownership, profiles, conformance claim, roadmap |

Minimum recurring-review requirements are owned by CDS-1400 §24; the table above is a recommended shape, not a mandate.

**CDS800-R078** Review cadence SHOULD reflect the rate and risk of change in the governed domain.

**CDS800-R079** Review outcomes SHOULD create assigned actions rather than remain informational only.

## 31. Worked Governance Scenarios *(informative)*

**31.1 Supplier introduces a new colour name.** Supplier value "Midnight Ocean" enters the source layer; dictionary matching finds no approved alias; the value is quarantined (CDS-400 §17). The Dictionary Steward reviews imagery and supplier evidence and aliases it to canonical `navy`, retaining "Midnight Ocean" as the display label; facet membership is `blue`; channel values inherit existing navy mappings. The decision and evidence are recorded; affected products are revalidated, published, and read-back verifies the expected result (CDS-500).

**31.2 Proposed category rename.** "Throw Pillows" → "Cushions": the internal category identifier remains stable; display label, navigation text and storefront collection title change; URLs require redirect review; external taxonomy mappings are unchanged; analytics dimensions need an alias/continuity plan; legacy `collection_*` tag compatibility is assessed. Approved as a minor compatible release.

**31.3 Manual downstream edit creates drift.** Expected channel title "Linen Relaxed Shirt"; observed "Summer Linen Shirt"; verification result MISMATCH. The title is PIM-owned with no active override, so this is unauthorised drift: restore the expected title on the next controlled publication, notify the editor of the ownership rule ("enter data where it originates"), retain the observed value and reconciliation evidence.

**31.4 High-risk AI workflow change.** A request to let AI write compliance claims directly into canonical fields is rejected (claims may require evidence and legal approval — CDS-700). Approved alternative: AI drafts a proposal with mandatory evidence attachment; the compliance owner reviews; the accepted value enters the canonical record with provenance; publication remains subject to channel verification.

## 32. Architecture Decision Records *(normative record; rationale informative)*

| ADR | Decision | Status | Rationale |
|---|---|---|---|
| CDS-ADR-800-001 | Governance is a conformance requirement | Accepted (scope updated) | A sound data model degrades without ownership, controlled change and measurable operation. Under ADR-D1, full governance is the **Governed capstone level**; ownership basics (R001) bind from Foundation. |
| CDS-ADR-800-002 | Conformance is scoped and levelled | **Superseded by ADR-D1** | The single ladder and overlay-profile model now live in CDS-1000. |
| CDS-ADR-800-003 | One authority per product fact | Accepted | Multiple simultaneous masters create unresolved drift and accountability gaps (CDS-200 §13). |
| CDS-ADR-800-004 | Exceptions expire or are reviewed | Accepted | Unbounded exceptions become hidden permanent architecture. |
| CDS-ADR-800-005 | Stable identifiers are governed separately from labels | Accepted | Display language evolves without breaking identity and mappings. |
| CDS-ADR-800-006 | Release completion includes verification | Accepted | Deployment success does not prove correct downstream state. |
| CDS-ADR-800-007 | Certification claims distinguish assessment type | Accepted | Self-attestation, customer assessment and independent assessment are not equivalent (vocabulary: CDS-1000 §20). |
| CDS-ADR-800-008 | Small teams may combine roles but not erase responsibilities | Accepted | Governance must remain practical while preserving accountability. Cross-referenced by the CDS-1300/CDS-1400 small-team profile. |

---

## Annex A — Recommended RACI Matrix *(informative)*

Role names are those of the §5 register.

| Governance activity | Accountable | Responsible | Consulted | Informed |
|---|---|---|---|---|
| Canonical product model | PIM Product Owner | Schema Owner | Product Data and Channel Owners | Product teams |
| Taxonomy change | Taxonomy Owner | Data Steward (taxonomy) | Merchandising, SEO, Channel Owners | Editors and analysts |
| Dictionary value approval | Dictionary Owner | Data Steward (dictionary) | Merchandising and Channel Owners | Import and content teams |
| Channel mapping release | Channel Owner | Integration Owner | Schema Owner, verification owners | Commerce operations |
| AI workflow approval | AI Governance Owner | AI workflow owner (per CDS-700 registry) | Product Data, Security and Compliance Owners | Reviewers and operators |
| Conformance statement | Conformance Declaration Executive | CDS Governance Owner | Assurance Reviewer and domain owners | Stakeholders |

## Annex B — Change Proposal Record *(informative template)*

Change ID · Title · Requester · Problem statement · Proposed change · Affected artefacts · Affected product count · Affected channels · Compatibility class · Risk and customer impact · Migration plan · Validation plan · Rollback plan · Required approvals · Target release · Outcome and evidence.

## Annex C — Exception Record *(informative template)*

Exception ID · Requirement (ID) · Scope · Reason · Risk · Compensating control · Owner · Approver · Start date · Expiry/review date · Resolution plan · **Retest result** (evidence at closure, R031) · Status.

*(The v0.1 "Exception and Waiver Record" title is retired with the waiver noun — CDS-100 §8.)*

## Annex D — Conformance Statement *(normative pointer)*

The conformance statement and claim/manifest schema are defined in CDS-1000 §23 and encoded in CDS-1100. The v0.1 Appendix D template is withdrawn *(finding 800-6)*; CDS-800 adds only the governance obligations of §29 (executive approval, honest scope, dated statement, assessment vocabulary).

## Annex E — Governance Readiness Checklist *(informative)*

- [ ] PIM and canonical authority are explicitly declared (CDS-200 §13).
- [ ] Every governed domain has an accountable owner.
- [ ] Taxonomy, dictionary, schema and namespace registries exist.
- [ ] Channel owners and capability profiles exist.
- [ ] Change, release, migration and rollback processes are documented.
- [ ] Exceptions have owners, review dates and retest evidence at closure.
- [ ] Quality metrics and review cadences are defined.
- [ ] Publication observation and verification are operational for claimed channels.
- [ ] Access and tenant isolation are reviewed.
- [ ] AI workflows have named owners and CDS-700 controls.
- [ ] Conformance statement scope is accurate and supportable with evidence (CDS-1000).

## Annex F — Organisation Example: Legacy Documentation Alignment *(informative — organisation-specific example; not part of the vendor-neutral standard)*

This annex records how one adopting organisation's pre-CDS artefacts map to this chapter *(finding 800-10: all organisation-specific material consolidated here)*. It illustrates that CDS governance can be reached bottom-up from working practice; no artefact named here is a CDS requirement.

| Existing artefact or pattern | CDS-800 interpretation |
|---|---|
| Legacy product-data workflow | Operational evidence of source separation, canonical resolution, channel output and verification responsibility |
| Legacy tag-governance workflow | A governed registry, namespace discipline, deprecation model and PIM authority over channel tags |
| Legacy implementation sequencing guide | A controlled implementation sequence in which taxonomy and governance precede product-scale publication |
| Airtable `Import_*` / `Airtable_*` / `Shopify_*` / `Match_*` layers | Clear separation of supplier intake, authority, observed state and verification evidence — a working example of §20's source/canonical separation |
| Traffic-light formulas | Human-facing control status backed by detailed reconciliation logic (now: CDS-500 §18) |
| Taxonomy decision log | A practical record for ambiguous classification decisions (R052) |
| Profile H / Profile S choice | An organisation-level implementation policy that must remain consistent or be migrated deliberately (§9) |

> RESOLVED — accepted as drafted (owner 2026-08-04; was new (resolved)): Annex placement. REVIEW-003 Matrix 5 proposes one corpus-wide legacy-alignment annex (candidate homes: CDS-1300 or standalone). This chapter's organisation-specific material is consolidated here for now; if a corpus-wide annex is created at v0.2 freeze, this annex merges into it and becomes a pointer.

*END OF CDS-800 v0.2 REVIEW DRAFT*

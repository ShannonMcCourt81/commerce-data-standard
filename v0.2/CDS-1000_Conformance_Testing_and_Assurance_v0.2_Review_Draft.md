# Commerce Data Standard (CDS)
## CDS-1000 — Conformance, Testing and Assurance

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 (single corpus release per ADR-D5) |
| Date | 2026-08-04 |
| Supersedes | CDS-1000 Working Draft v0.1; CDS-800 §9 conformance ladder and CDS-800 Appendix D claim template (both replaced by references to this chapter per ADR-D1) |
| Normative status | §§2–5, 7–19, 21–27 and Appendix B are normative. §1, §6, §20, §28 and Appendices A and C are informative. |
| Findings addressed | 1000-1, 1000-2, 1000-3, 1000-4, 1000-5, 1000-6; 800-1, 800-2, 800-5, 800-6, 800-7 (this chapter's side); CDS1100-6 (corollary); SYS-2; ADR-D1, ADR-D3, ADR-D5 |
| Dependencies | CDS-000 through CDS-900 (all published in the CDS v0.2 corpus release); machine-readable claim and manifest schemas in CDS-1100 |
| Audience | Implementers, PIM vendors, auditors, platform integrators, data owners, standards maintainers |

---

## 1. Purpose and Scope *(informative)*

CDS-1000 makes the Commerce Data Standard testable. The other chapters state what a conformant implementation does; this chapter defines how an implementation proves it: objective conformance levels, overlay profiles, test suites, evidence requirements, assurance methods and the rules for honest public claims.

This chapter is the **single normative home** for conformance levels, test suites, conformance claims and assurance (CDS-000 R005, ADR-D1). Other chapters cite it and do not restate it. In particular, the divergent five-level ladder formerly in CDS-800 §9 and the claim template formerly in CDS-800 Appendix D are superseded by this chapter.

CDS-1000 does not create a certification authority. It defines the framework that a self-assessor, customer, auditor or future certification body may use.

## 2. Conformance Philosophy *(normative)*

- **Objective.** A test yields the same conclusion when repeated against the same implementation state.
- **Version-specific.** A claim applies to a named CDS release and does not automatically transfer to a later release.
- **Profile-aware.** Platform, industry and overlay profiles add requirements; they never weaken the CDS core.
- **Evidence-based.** Every pass is supported by a retained artefact, query result, export, log or reproducible observation.
- **No compensation.** Strong performance in one area does not cancel failure of a mandatory requirement in another.
- **Honest scope.** A component, connector or workflow may claim limited conformance without implying that the entire organisation is conformant.
- **Repeatable.** The test suite is designed for automation where possible and controlled human review where necessary.

**CDS1000-R001** A conformance claim MUST identify the CDS version, test-suite version, conformance level, applicable profiles, implementation scope, assessment method and assessment date.

**CDS1000-R002** An implementation MUST NOT claim general CDS conformance when only a subset of requirements has been tested.

**CDS1000-R003** Tests MUST evaluate observable system behaviour and evidence, not marketing descriptions or intended future capability.

**CDS1000-R004** Mandatory tests MUST be pass/fail. A score or maturity percentage MUST NOT convert a failed mandatory test into a conformant result.

**CDS1000-R005** Informative quality metrics MAY accompany a conformance result but MUST be clearly separated from normative pass/fail status.

## 3. Conformance Claim Model *(normative)*

A complete claim is a structured statement with these parts: specification version, test-suite version, conformance level, implementation scope, profiles and assessment method.

```yaml
cds_claim:
  specification_version: "0.2"
  test_suite_version: "0.2"
  level: verified
  scope: Product information service and storefront connector
  profiles:
    - apparel-0.2
    - <platform-profile>-0.2
  assessment_method: independent_assessment
  assessed_at: 2026-08-04
  valid_until: 2027-08-04
```

**CDS1000-R006** A claim MUST name the product, service, component or organisational process being assessed.

**CDS1000-R007** A claim MUST list every profile — platform, industry and overlay — included in the assessment.

**CDS1000-R008** A claim MUST state its assessment method as exactly one of the three canonical methods defined in §20: self-attestation, customer assessment or independent assessment.

**CDS1000-R045** A claim and its machine-readable manifest (§26) MUST record the `test_suite_version` and `assessment_method` used, so that the result can be reproduced against the same test definitions.

## 4. Conformance Levels *(normative)*

CDS defines exactly five conformance levels, strictly cumulative:

**Foundation → Structured → Publisher → Verified → Governed**

| Level | Primary capability | Minimum proof |
|---|---|---|
| CDS Foundation | Canonical authority and semantic clarity | Canonical source, ownership, terminology and namespace evidence |
| CDS Structured | Governed classification, attributes and dictionaries | Schema, data types, dictionary controls, validation and facet separation |
| CDS Publisher | Deterministic channel projection and publication | Expected channel state, mappings, preflight and publication records |
| CDS Verified | Downstream observation and field-level reconciliation | Read-back, comparison strategies, verification results and channel health |
| CDS Governed | Sustained ownership, change control and assurance | Owners, policies, audit, incident handling, versioning and recurring review |

**CDS1000-R009** A higher-level claim MUST satisfy all mandatory tests of every preceding level. No profile — platform, industry, overlay or organisational — may exempt an implementation from this rule or weaken any core requirement. There is no exception process for level cumulativity.

**CDS1000-R010** An implementation MAY claim different levels for different components if the scope of each claim is explicit.

*Informative notes:*
- A PIM implementation might be CDS Structured while its channel connector is CDS Verified. This is preferable to an inflated claim covering both.
- Governance is deliberately the capstone: a team may prove Publisher and Verified round-trip value before formalising full change-control and audit governance (ADR-D1).
- Superseded drafts of CDS-800 defined a different ladder in which "Governed" was level 2 and permitted profiles to relax cumulativity. That ladder and its escape clause are deleted; any prior claim using it must be restated against this section.

## 5. Overlay Profiles *(normative)*

An overlay profile binds an additional test suite to a claim without being a level. Overlays are claimed alongside a level and appear in the claim's `profiles` list.

| Overlay profile | Binds test suite | Additional bound controls | Minimum level |
|---|---|---|---|
| AI-Assured | T-AI (§17) | CDS-700 normative controls for proposal status, provenance, approval and publication boundary | CDS Structured |
| CX | T-UX (§16) | CDS-600 facet and navigation requirements within the declared storefront scope | CDS Foundation |
| Multi-Tenant | T-TEN (§18) | CDS-800 §22 tenant-isolation requirements | CDS Foundation |

**CDS1000-R039** An overlay profile claim MUST name the overlay, its version and the level alongside which it is claimed, and MUST pass every mandatory test in the bound suite in addition to all mandatory tests of the claimed level.

**CDS1000-R040** The AI-Assured overlay MUST NOT be claimed below CDS Structured, because T-AI tests presuppose governed attribute definitions and dictionaries for AI output to conform to.

**CDS1000-R041** A claim that includes customer-facing facet or navigation scope MUST bind the CX overlay for that scope; T-UX tests are mandatory only under this overlay.

**CDS1000-R042** An implementation serving more than one organisation from shared infrastructure MUST bind the Multi-Tenant overlay before claiming any level for that shared deployment.

*Informative note:* AI-Assured is not a sixth level (ADR-D1). Implementations without AI enrichment simply do not claim the overlay; their level claims are unaffected.

> RESOLVED — accepted as drafted (owner 2026-08-04; was new (resolved)): The T-TEN suite (§18) is newly designed here as a minimal one-test-per-requirement mapping of CDS-800 §22; ADR-D1 assigned the overlay pattern but not the test list. Alternative: a broader penetration-style suite, deferred to a future test-suite version.

## 6. Adoption Maturity Mapping *(informative)*

CDS-1300's adoption maturity model describes organisational progress; it is not a conformance construct. It maps onto the conformance ladder as follows (ADR-D1):

| CDS-1300 maturity level | Conformance ladder equivalent |
|---|---|
| Level 0 — Fragmented | Pre-Foundation (no claim available) |
| Level 1 — Foundation (formerly "Canonical") | CDS Foundation |
| Level 2 — Structured | CDS Structured |
| Level 3 — Publisher | CDS Publisher |
| Level 4 — Verified | CDS Verified |
| Level 5 — Governed | CDS Governed |

CDS-400's cumulative dictionary capability badges — Dictionary Core, Dictionary Facet, Dictionary Channel, Dictionary Round-Trip (renamed from "Dictionary Verified") — are not levels or overlays. They are evidence descriptors carried inside the CDS Structured evidence set, defined in CDS-400.

## 7. Requirement and Test Identification *(normative)*

Every normative requirement and test case has a stable identifier. Requirement identifiers (`CDSnnn-Rmmm`) describe obligations; test identifiers describe a reproducible method for evaluating them.

```text
Requirement:   CDS500-R014
Test:          CDS1000-T-VRF-014
Profile test:  CDS1000-T-<profile>-023
Evidence:      EVID-2026-000184
```

| Prefix | Suite | Bound to |
|---|---|---|
| T-FND | Foundation tests | CDS Foundation |
| T-STR | Structured data tests | CDS Structured |
| T-PUB | Publisher tests | CDS Publisher |
| T-VRF | Verified tests | CDS Verified |
| T-GOV | Governed tests | CDS Governed |
| T-DICT | Controlled dictionary tests | CDS Structured |
| T-UX | Customer experience tests | CX overlay |
| T-AI | AI governance tests | AI-Assured overlay |
| T-TEN | Tenant isolation tests | Multi-Tenant overlay |

Each platform or industry profile in CDS-900 registers its own test prefix in its versioned profile test matrix (Appendix A).

**CDS1000-R011** Test identifiers MUST remain stable after publication. Substantive changes to test meaning require a new identifier or a new test-suite version.

**CDS1000-R012** Every mandatory requirement in the CDS corpus MUST map to at least one test case or a documented inspection procedure.

*Informative note:* the corpus-wide retrofit of `CDSnnn-Rmmm` requirement identifiers is complete in v0.2 (finding SYS-2 resolved); every chapter now carries stable IDs, so this traceability mandate is implementable across the whole standard.

## 8. Test Categories *(normative)*

| Category | Method | Typical evidence |
|---|---|---|
| Static schema | Inspect definitions and configuration | Schema export, namespace registry, dictionary definitions |
| Data sample | Evaluate representative records | Product export, variant records, mapping outputs |
| Behavioural | Trigger a workflow and observe the result | API logs, before/after states, job records |
| Round-trip | Publish, read back and compare | Expected state, observed state, comparison result |
| Negative | Provide invalid or unknown data | Validation error, quarantine record, rejected publication |
| Security and governance | Inspect permissions and approvals | Role matrix, audit history, change record |
| Human factors | Review visible labels and operational clarity | UI capture, field list, task observation |
| Performance | Measure defined operational limits | Timing log, batch result, retry behaviour |

**CDS1000-R013** A test suite SHOULD include positive, negative and boundary cases where the requirement can fail in materially different ways.

## 9. Test Artefacts and Evidence Package *(normative)*

The evidence package is the durable record supporting a claim. It must allow another qualified reviewer to reproduce or reasonably verify the assessment conclusion. Contents:

- assessment manifest and scope statement
- implementation, test-suite and profile versions
- test-run identifier and timestamps
- test environment description
- input fixtures and expected outcomes
- actual outputs and comparison results
- screenshots or exports for human-inspection tests
- logs for publication, observation and verification
- list of failed, not-tested and not-applicable tests
- exceptions and corrective-action records
- assessor identity or responsible organisation
- cryptographic hashes or checksums for retained files

**CDS1000-R014** Evidence MUST be retained for every mandatory test result included in a claim.

**CDS1000-R015** Evidence MUST identify the implementation version and configuration that was tested.

**CDS1000-R016** Sensitive evidence MAY be redacted, but the redaction MUST NOT remove information necessary to validate the result.

## 10. Foundation Test Suite (T-FND) *(normative)*

| Test ID | Objective | Pass condition |
|---|---|---|
| T-FND-001 | Canonical source exists | Product facts have a declared master and channel read-back is stored separately |
| T-FND-002 | Authority is explicit | Each tested field has exactly one declared authority |
| T-FND-003 | Channel independence | Canonical values remain valid and retrievable with any single channel disabled |
| T-FND-004 | Self-describing fields | Every sampled visible field identifier resolves to a registered namespace and Attribute Definition (CDS-300/CDS-200) with no out-of-band notes required; sample size and selection rule are declared in the assessment scope |
| T-FND-005 | Semantic namespaces | Field prefixes match the approved namespace registry |
| T-FND-006 | Product/variant boundary | SKU-producing differences are variants; descriptive facts are not misused as options |
| T-FND-007 | Classification separation | Internal category, collection and external taxonomy are distinct concepts |
| T-FND-008 | Audit identity | A change can be attributed to an actor or process |

**CDS1000-R017** CDS Foundation conformance requires every mandatory Foundation test to pass.

## 11. Structured Data Test Suite (T-STR) *(normative)*

| Test ID | Objective | Pass condition |
|---|---|---|
| T-STR-001 | Attribute definitions | Every governed attribute has type, scope, cardinality and validation |
| T-STR-002 | Controlled values | Governed enumerations use a dictionary or equivalent reference-data control |
| T-STR-003 | Canonical identity | Dictionary values use stable identifiers independent of display labels |
| T-STR-004 | Source fidelity | Original supplier values are retained when required for provenance |
| T-STR-005 | Facet separation | Facet values are stored distinctly from canonical values for every attribute with a declared facet layer |
| T-STR-006 | Conditional rules | Category- or value-dependent requirements are machine-expressible |
| T-STR-007 | Unknown-value handling | Unmapped values are rejected or quarantined rather than silently accepted |
| T-STR-008 | Units and measurements | Numeric quantities retain declared units and normalisation rules |
| T-STR-009 | Inheritance | Inherited values preserve provenance and can be distinguished from direct values |
| T-STR-010 | Dictionary lifecycle | Aliases, deprecation and replacement are governed |

**CDS1000-R018** CDS Structured conformance requires Foundation conformance plus all mandatory Structured tests, including the Controlled Dictionary Test Suite (§15).

## 12. Publisher Test Suite (T-PUB) *(normative)*

| Test ID | Objective | Pass condition |
|---|---|---|
| T-PUB-001 | Expected state generation | The system calculates an expected channel representation before publishing |
| T-PUB-002 | Mapping determinism | The same canonical input and mapping version produce the same expected output |
| T-PUB-003 | Preflight validation | Invalid or incomplete output is blocked before transport |
| T-PUB-004 | Publication record | Each attempt records product, channel, revision, status and timestamps |
| T-PUB-005 | Replace semantics safety | Full-replace operations preserve governed values and remove stale generated values |
| T-PUB-006 | Partial failure handling | Field or object failures are visible and not reported as complete success |
| T-PUB-007 | Retry safety | Retries do not create duplicate or contradictory downstream records |
| T-PUB-008 | Override governance | Channel overrides are explicit, scoped and auditable |
| T-PUB-009 | Mapping version trace | Published output identifies the transformation or mapping version |
| T-PUB-010 | Disabled publication | A disabled channel or product does not publish unintentionally |

**CDS1000-R019** CDS Publisher conformance requires Structured conformance plus all mandatory Publisher tests.

## 13. Verified Test Suite (T-VRF) *(normative)*

| Test ID | Objective | Pass condition |
|---|---|---|
| T-VRF-001 | Downstream observation | Published values are read back or otherwise observed |
| T-VRF-002 | Expected vs observed separation | Expected and observed values are stored separately |
| T-VRF-003 | Comparison strategy | Each verified field uses a declared type-aware comparison |
| T-VRF-004 | Status distinction | Missing, unobservable, pending and not-applicable verification states are distinguishable per the CDS-500 status enum |
| T-VRF-005 | Mismatch evidence | A mismatch records expected value, observed value and a machine-readable reason code (CDS-500, CDS-1100) |
| T-VRF-006 | Normalised equivalence | Equivalent case, numeric and unordered-list representations can pass correctly |
| T-VRF-007 | Drift detection | Manual or external downstream changes are detected |
| T-VRF-008 | Channel health | Health reporting is derived from detailed verification results |
| T-VRF-009 | Timestamp integrity | Last publish, last observe and last verify times are separately recorded |
| T-VRF-010 | Repair policy | Automatic repair, alert or accepted override is governed and auditable |

**CDS1000-R020** CDS Verified conformance requires Publisher conformance plus all mandatory Verified tests.

## 14. Governed Test Suite (T-GOV) *(normative)*

| Test ID | Objective | Pass condition |
|---|---|---|
| T-GOV-001 | Domain ownership | Every governed domain has an accountable owner |
| T-GOV-002 | Change control | Schema, dictionary, namespace and mapping changes follow an approved process |
| T-GOV-003 | Versioning | Breaking, additive and corrective changes are distinguishable |
| T-GOV-004 | Deprecation | Retired values and fields have aliases, replacement guidance and dates |
| T-GOV-005 | Access control | Roles follow least privilege and separate approval where required |
| T-GOV-006 | Incident response | Data-quality and publication incidents have detection, ownership and recovery procedures |
| T-GOV-007 | Review cadence | Governance reviews occur at a declared interval |
| T-GOV-008 | Exception expiry | Exceptions are scoped, justified, approved and time-limited (CDS-800 §16) |
| T-GOV-009 | Supplier governance | Supplier mappings and imports are controlled and reviewable |
| T-GOV-010 | Claim governance | Public CDS claims match current assessment scope and status |

**CDS1000-R021** CDS Governed conformance requires Verified conformance plus all mandatory Governed tests.

## 15. Controlled Dictionary Test Suite (T-DICT) *(normative)*

Dictionary tests verify both data integrity and customer-useful projection. This suite is bound to CDS Structured: it is mandatory for every claim at Structured or above.

| Test ID | Fixture | Expected result |
|---|---|---|
| T-DICT-001 | French Navy | Reference preserved; canonical Navy; facet Blue |
| T-DICT-002 | navy / NAVY / Navy | Aliases resolve to one canonical identifier |
| T-DICT-003 | Blue-Green | Ambiguous value is mapped by rule or sent to review |
| T-DICT-004 | 80% cotton, 20% polyester | Composition retained; Cotton and Synthetic facet rules applied explicitly |
| T-DICT-005 | Tasmanian Oak | Canonical Oak; facet Wood; display label may remain Tasmanian Oak |
| T-DICT-006 | Unknown supplier colour | Quarantine or review; no uncontrolled canonical creation |
| T-DICT-007 | Deprecated canonical value | Alias resolves to replacement while history remains auditable |
| T-DICT-008 | Channel vocabulary mismatch | Channel-specific representation is generated without changing canonical identity |

**CDS1000-R022** A dictionary test MUST verify identifiers and relationships, not only visible labels.

**CDS1000-R043** The Controlled Dictionary Test Suite is mandatory at CDS Structured and every higher level; a Structured claim MUST NOT omit it.

## 16. Customer Experience Test Suite (T-UX) *(normative — mandatory under the CX overlay)*

| Test ID | Objective | Pass condition |
|---|---|---|
| T-UX-001 | Facet size control | Each assessed facet exposes no more values than the maximum declared for its facet family in the assessment scope, and every exposed value is a governed facet value rather than a raw source or canonical shade |
| T-UX-002 | Colour family projection | Detailed shades group into usable colour families |
| T-UX-003 | Truthful availability | Facet counts and product cards reflect available product or variant combinations |
| T-UX-004 | No false zero results | For the filter-combination set and zero-result threshold declared in the assessment scope, misleading empty states do not exceed the threshold. If no combination set and threshold are declared, this test is a WARNING-class advisory: it MUST NOT report PASS and its result MUST NOT support the CX overlay claim |
| T-UX-005 | Progressive disclosure | Long lists collapse or search without hiding essential context |
| T-UX-006 | Accessible labels | Facet names and values remain understandable without colour alone |
| T-UX-007 | Search synonym alignment | Search terms map to the same governed concepts as facets |
| T-UX-008 | Navigation distinction | Navigation categories and filter facets do not duplicate each other unnecessarily |

**CDS1000-R023** A customer-facing facet test MUST evaluate the published experience, not only the PIM configuration.

> RESOLVED — accepted as drafted (owner 2026-08-04; was new (resolved)): T-UX-001 and T-UX-004 use declared-threshold criteria (thresholds set in the assessment scope) rather than fixed universal numbers; the alternative — standard-wide numeric limits — was rejected as arbitrary across industries. Finding 1000-2.

## 17. AI Governance Test Suite (T-AI) *(normative — mandatory under the AI-Assured overlay)*

| Test ID | Objective | Pass condition |
|---|---|---|
| T-AI-001 | Proposal status | AI output is identifiable as a proposal until accepted |
| T-AI-002 | Schema constraint | AI values conform to attribute definitions and dictionaries |
| T-AI-003 | Evidence and provenance | The source evidence, model/workflow version and confidence are retained |
| T-AI-004 | Abstention | Low-confidence or unsupported extraction returns review-required rather than invented data |
| T-AI-005 | Human approval | Required review gates cannot be bypassed accidentally |
| T-AI-006 | Publication boundary | AI does not publish to production outside declared authority |
| T-AI-007 | Regression testing | Model or prompt changes are tested against a benchmark set |
| T-AI-008 | Rights and privacy | Restricted source material and personal data controls are enforced |

**CDS1000-R024** AI tests MUST assess the complete workflow, including validation and approval, rather than only model output quality. The controls under test are defined in CDS-700.

## 18. Tenant Isolation Test Suite (T-TEN) *(normative — mandatory under the Multi-Tenant overlay)*

Each test maps to one of the four tenant-isolation requirements of CDS-800 §22 (finding 800-7 resolved).

| Test ID | Objective | Pass condition |
|---|---|---|
| T-TEN-001 | Tenant data isolation | A cross-tenant read attempt against organisation-specific products, dictionaries, mappings, credentials, exceptions or audit records is denied and the denial is evidenced |
| T-TEN-002 | Shared baseline boundary | Shared baseline definitions and templates are readable, but no tenant-specific value is exposed to or merged into another tenant without recorded explicit authorisation |
| T-TEN-003 | Organisation-scoped operations | An import or bulk action submitted without a declared organisation context is rejected; the same operation with a declared context affects only that organisation's records |
| T-TEN-004 | Cross-tenant administration | Cross-tenant administrative access requires a privileged role and produces a reviewable log entry for each access |

*CDS1000-R042 (defined in §5) applies here: shared deployments must pass all mandatory T-TEN tests before claiming any level.*

## 19. Platform and Industry Profile Test Suites *(normative)*

A platform or industry profile adds profile-specific tests to the applicable core level. It may constrain mappings, capability declarations and observation methods; it cannot weaken core requirements (CDS1000-R009, CDS000-R011).

Profile test content — including test matrices, expected platform outputs and observation methods — lives with the versioned, dated profile definitions in CDS-900 (platform) and CDS-1500 (industry), not in this chapter (see Appendix A).

**CDS1000-R025** A profile conformance claim MUST pass all mandatory core tests for the claimed level and all mandatory tests in that profile's version-pinned test matrix.

*Informative note — typical profile test areas:* commerce-platform profiles cover taxonomy mapping, variant constraints, structured metadata definitions, tag/collection safety under full-replace semantics, storefront facet exposure, API read-back and drift handling; feed-destination profiles cover taxonomy and identifier mapping, field validation, disapproval handling and observed item-state reconciliation; supplier-import profiles cover source identification, delta/full behaviour, normalisation, duplicate detection, unknown-value quarantine and provenance; apparel and homewares profiles cover colour, size, fit, composition, materials, dimensions, units and facet truthfulness.

## 20. Reference Test Vectors *(informative)*

Reference vectors are small, portable records with known expected outcomes, usable in automated tests and demonstrations. Core vectors state **canonical and facet expectations only**; platform-specific expected outputs (e.g. a channel's filter value or feed colour) live in the version-pinned profile test matrices (finding 1000-4), because they change with platform API versions while canonical expectations do not.

### 20.1 Apparel product

```yaml
input:
  product_type: shirt
  supplier_colour: French Navy
  material_text: 100% Linen
  variants:
    - { size: S, colour: French Navy }
    - { size: M, colour: French Navy }
expected:
  canonical_colour: navy
  facet_colour: blue
  canonical_material: linen
  verification_case_rule: case_insensitive
# Channel-specific expectations for this vector are defined in each
# profile's version-pinned test matrix (CDS-900 / CDS-1500).
```

### 20.2 Homewares product

```yaml
input:
  product_type: cushion
  supplier_material: Tasmanian Oak buttons and linen cover
  dimensions: 50 x 50 cm
expected:
  canonical_materials: [linen, oak]
  material_facets: [textile, wood]
  dimension_width: 50 cm
  dimension_height: 50 cm
  room_facets: determined_by_governed_rule_or_review
```

### 20.3 Verification equality

```yaml
expected: [Cotton, Linen]
observed: [linen, cotton]
comparison: unordered_list + case_insensitive + dictionary_identity
result: MATCH
```

## 21. Test Outcomes *(normative)*

A test result takes exactly one of six outcomes. Spellings are the canonical underscore forms (ADR-D3 alignment). Test outcomes are distinct from field-level verification statuses, whose single normative home is CDS-500.

| Outcome | Meaning | Effect on claim |
|---|---|---|
| PASS | Mandatory condition is satisfied with evidence | Supports conformance |
| FAIL | Mandatory condition is not satisfied | Blocks the applicable level/profile claim |
| WARNING | Non-mandatory guidance or quality concern | Does not block the claim but MUST be reported |
| NOT_APPLICABLE | Requirement genuinely does not apply to the declared scope | Allowed only with documented rationale |
| NOT_TESTED | No valid test result exists | Blocks the claim when the test is mandatory |
| INCONCLUSIVE | Evidence is insufficient or contradictory | Treated as not passed until resolved |

**CDS1000-R026** A conformance claim MUST NOT be made for a level or profile while any of its mandatory tests has a result of FAIL, NOT_TESTED or INCONCLUSIVE.

**CDS1000-R027** NOT_APPLICABLE requires a written scope-based justification and reviewer approval.

## 22. Nonconformity, Exceptions and Corrective Action *(normative)*

A nonconformity is a failed mandatory requirement. An exception (defined in CDS-100; governed by CDS-800 §16) is a time-limited, documented, approved acknowledgement that the implementation does not currently satisfy a requirement. An exception acknowledges non-conformance; it never converts failure into conformance.

An exception record contains:

- identifier and affected requirement
- description and evidence
- risk and affected records/channels
- responsible owner
- corrective action and target completion date
- temporary control
- approval and expiry date
- retest result

**CDS1000-R028** An exception MUST NOT be used to claim conformance to a level or profile whose mandatory capability is absent. This rule is absolute; no CDS release, profile or exception class relaxes it.

**CDS1000-R029** Corrected nonconformities MUST be retested using the same or a stronger test method.

## 23. Assurance Methods: Self-Attestation and Independent Assurance *(normative)*

The three assurance methods below are the canonical vocabulary for the entire standard; CDS-800's claims-governance requirements cite this section (finding 800-5 resolved).

| Method | Description | Claim wording |
|---|---|---|
| Self-attestation | The implementing organisation performs and records its own assessment | "Self-attested CDS Verified conformance" |
| Customer assessment | A customer or contracting party evaluates the implementation | "Customer-assessed against CDS Publisher" |
| Independent assessment | A qualified party independent of implementation delivery performs the assessment | "Independently assessed CDS Governed conformance" |

**CDS1000-R030** The assurance method MUST be disclosed wherever a conformance claim is presented.

**CDS1000-R031** Independent assessment MUST include evidence sampling, assessor independence and conflict-of-interest disclosure.

## 24. Certification Framework *(normative)*

CDS-1000 provides a future-ready certification structure but does not designate a certification body.

**CDS1000-R044** Any organisation offering CDS certification MUST publish its assessor-competence, impartiality, surveillance, complaint and certificate-withdrawal processes.

**CDS1000-R032** A certificate MUST identify its issuer, scope, CDS version, level, profiles, issue date, expiry date and public verification reference.

**CDS1000-R033** A certification mark MUST NOT imply endorsement of product quality beyond the assessed CDS conformance scope.

## 25. Versioning and Reassessment *(normative)*

Conformance can be invalidated by changes to the system, schema, mappings, dictionaries, channel API behaviour, governance or the CDS specification itself.

| Change | Minimum response |
|---|---|
| Patch implementation release | Risk review and targeted regression tests |
| New attribute or dictionary values | Structured-data tests for affected domains |
| Mapping change | Publisher and Verified tests for affected fields/channels |
| New platform API version | Platform profile regression and observation review |
| Major architecture change | Full reassessment of affected level and profiles |
| New CDS minor version | Gap analysis and tests for new/changed requirements |
| New CDS major version | Formal reassessment before using the new-version claim |

**CDS1000-R034** A claim MUST be reviewed after any change that could alter a mandatory test outcome.

**CDS1000-R035** A claim SHOULD include an expiry or reassessment date.

## 26. Machine-Readable Conformance Manifest *(normative)*

A machine-readable manifest enables automated reporting, procurement checks and public verification. This chapter owns the manifest's semantics; its JSON Schema is published in CDS-1100 (finding 800-6: the former CDS-800 Appendix D template is a pointer to this section). JSON or YAML may be used, provided the required semantics are preserved.

```yaml
cds_conformance:
  specification_version: "0.2"
  test_suite_version: "0.2"
  level: verified
  scope_id: product-information-service-connector
  profiles:
    - <platform-profile>-0.2
    - apparel-0.2
    - ai-assured-0.2
  assessment_method: independent_assessment
  assessed_at: 2026-08-04T09:00:00+10:00
  valid_until: 2027-08-04
  results:
    passed: 86
    failed: 0
    warnings: 4
    not_applicable: 7
    not_tested: 0
    inconclusive: 0
  evidence_package_hash: sha256:...
  public_report: https://example.invalid/cds/assessment-184
```

**CDS1000-R036** The manifest MUST NOT report a conformant level or profile when any mandatory test for that level or profile has a result of FAIL, NOT_TESTED or INCONCLUSIVE.

*(Required fields `test_suite_version` and `assessment_method`: CDS1000-R045.)*

## 27. Reporting and Public Claims *(normative)*

Reports should be understandable to both technical and non-technical readers. Detailed evidence may remain private, while the public summary states scope, result, limitations and assurance method.

```text
Conformant claim:
"Product Information Service 4.2 is independently assessed as conformant with
Commerce Data Standard v0.2 at the CDS Verified level for the Apparel v0.2
profile and the AI-Assured v0.2 overlay. Scope excludes inventory and order
management. Assessment date: 4 August 2026."

Nonconformant claim:
"CDS certified"   # invalid: no version, scope, level, profile, issuer or method
```

**CDS1000-R037** Public claims MUST be precise enough that a reader can determine what was assessed and what was excluded.

**CDS1000-R038** Expired, withdrawn or superseded claims MUST be removed or visibly marked.

## 28. Decision Records *(informative)*

Architecture decisions are held in the single global ADR register (CDS000-R006). Decisions governing this chapter: **ADR-D1** (one cumulative ladder owned by CDS-1000; governance as capstone; AI-Assured, CX and Multi-Tenant as overlay profiles; T-DICT bound to Structured; assurance vocabulary and claim/manifest ownership here), **ADR-D3** (status-enum spellings; verification statuses homed in CDS-500), **ADR-D5** (single corpus release version; casing of enum values). The chapter-local records CDS-ADR-1000-001..007 from v0.1 (cumulative levels; pass/fail mandatory tests; version- and scope-specific claims; self-attestation with disclosure; warnings separated from conformance; machine-readable manifest; no in-spec certification body) are subsumed into the global register unchanged in substance.

---

## Appendix A — Profile Test Matrices *(informative)*

Version-pinned profile test matrices — including all platform-specific expected outputs formerly embedded in this chapter's reference vectors and Shopify appendix — are published alongside each profile definition (CDS-900 for platforms, CDS-1500 for industries). Each matrix pins: the profile version, the platform API version and date verified, the registered test prefix, the mandatory test list, and the profile-specific expected outputs for the shared core reference vectors (§20). A representative matrix covers: product identity mapping, taxonomy mapping, structured metadata definitions, variant boundaries, tag/collection safety, storefront filter exposure, observation method, verification comparison and drift handling.

## Appendix B — Apparel and Homewares Reference Dataset *(normative)*

Implementations must demonstrate more than a single happy path.

**CDS1000-R046** A test dataset used to support a conformance assessment MUST include negative and non-happy-path cases, covering at minimum: an unknown supplier value requiring quarantine, a deprecated alias resolving to a current canonical value, and a deliberate downstream manual edit that must produce detected drift.

The reference dataset SHOULD additionally contain:

- an apparel product with multiple size and colour variants
- colour values French Navy, Sky Blue, Royal Blue and Teal with controlled facet grouping
- an unordered multi-material composition
- a homewares product with dimensions and explicit units
- a homewares product with multiple materials and one dominant display material
- a product whose internal category maps differently to two external taxonomies
- a product with a deliberate channel title override

## Appendix C — Example Evidence Package *(informative)*

```text
assessment-184/
  manifest.yaml
  scope.md
  environment.yaml
  results/
    T-FND-001.json
    T-STR-001.json
    T-PUB-001.json
    T-VRF-001.json
    ...
  fixtures/
    apparel-shirt.json
    homewares-cushion.json
  exports/
    attribute-definitions.json
    dictionaries.json
    namespace-registry.json
  logs/
    publication.ndjson
    observation.ndjson
    verification.ndjson
  screenshots/
    storefront-filters.png
    channel-health.png
  exceptions/
    none.md
  report.pdf
  checksums.sha256
```

---

*End of CDS-1000 v0.2 Review Draft.*

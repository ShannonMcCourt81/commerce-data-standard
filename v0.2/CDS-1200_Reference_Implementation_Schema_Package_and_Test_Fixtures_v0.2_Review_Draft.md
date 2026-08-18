# Commerce Data Standard (CDS)
## CDS-1200 — Reference Implementation, Schema Package and Test Fixtures

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 |
| Date | 2026-08-04 |
| Supersedes | CDS-1200 Working Draft v0.1 (and Reference Package v0.1.0) |
| Companion package | CDS-1200 Reference Package v0.2.1 (semver, independent of chapter prose — ADR-D5; schemas remain 0.2.0) |
| Normative status | §1–§2, §4–§16 and §18 are normative except where marked otherwise. §3, §17, §19–§21, Annex A and Appendices A–B are informative. |
| Findings addressed | CDS1200-1..13, PKG-1, PKG-2 (REVIEW-010); ADR-D5 |

A reproducible reference package that turns the CDS machine-readable contracts into executable schemas, fixtures, an executable structural and semantic test suite, and environment-annotated validation evidence.

---

## 1. Purpose and Scope *(normative)*

CDS-1200 defines the executable reference implementation that accompanies the machine-readable contracts in CDS-1100. Its purpose is to make the standard reproducible: implementers obtain the same schemas, run the same fixture suite, observe the same expected failures and produce comparable validation evidence.

The reference implementation is deliberately small enough to read in full, but complete enough to demonstrate the core CDS lifecycle from canonical product records through channel publication, observation and verification (CDS-500). It is not a production PIM, commerce connector or certification service, and it confers no conformance claim by itself (claims: CDS-1000).

**CDS1200-R001** A CDS reference package MUST contain executable schemas, positive fixtures, negative fixtures, a machine-readable expected-results catalogue, a machine-readable semantic test catalogue and a repeatable validation procedure.

**CDS1200-R002** A reference fixture MUST NOT depend on undocumented database state, a network service, the mutable current time or an external API response.

**CDS1200-R003** Where the reference package and the published specification conflict on **normative content** — contract meaning, requirement wording, enumerations, identifier and versioning rules — the specification governs and the package carries the defect. This precedence rule does NOT extend to execution evidence: test reports, result counts and environment records are informative snapshots of a recorded run (§16), never specification prose, and the specification cannot make a non-reproducing number authoritative over an actual run. *(Re-scoped per finding CDS1200-8.)*

## 2. Relationship to CDS-1100 *(normative)*

CDS-1100 specifies the logical contracts and their serialization rules; CDS-1200 packages those contracts into concrete schema files, reusable examples and automated tests. The chapters are complementary, not duplicative. Contract semantics, type rules and extension rules are homed in CDS-1100 and are not restated here.

| CDS-1100 responsibility | CDS-1200 responsibility |
|---|---|
| Define the logical document contracts | Publish executable schema files |
| Define identifier, type and extension rules | Provide conforming and non-conforming examples |
| Define validation and compatibility expectations | Run validation and produce evidence |
| Define the reference schema registry | Distribute the registry as a versioned package |
| Define document semantics | Demonstrate cross-document and lifecycle behaviour |

**CDS1200-R004** The reference package MUST identify the CDS release its contracts implement: the envelope pins `cds_version` as a per-release constant (`"0.2"` for this release), and every schema carries its own semantic version (ADR-D5; details CDS-1100).

**CDS1200-R005** A package release MUST NOT silently change the meaning of a schema without a corresponding specification change or schema version change.

## 3. Reference Implementation Principles *(informative)*

- **Executable:** every claimed schema rule is represented in a validation artefact where the schema language can express it.
- **Reproducible:** a clean environment, with the declared pinned dependencies installed, runs the suite and obtains the same expected outcomes. An environment that cannot enforce a declared assertion fails loudly instead of passing weakly (§5).
- **Deterministic:** fixture IDs, timestamps, values and expected reports are fixed.
- **Inspectable:** schemas and fixtures are readable without proprietary tooling.
- **Layered:** structural schema validation is separated from semantic cross-document tests — and both layers are executed (§12).
- **Positive and negative:** a rule is demonstrated by valid examples and by intentionally invalid counterexamples that fail for the intended reason (§11).
- **Channel-aware:** the package includes an expected publish, observed state and verification chain (§13).
- **Safe:** fixtures contain synthetic data — no real credentials, customer records or confidential supplier data.
- **Portable:** the logical test catalogues are independent of the reference Python runner.
- **Evidence-producing:** a run emits a structured, environment-annotated report rather than only console text.

## 4. Distribution Package Layout *(normative)*

```
CDS-1200_Reference_Package_v0.2/
  README.md
  CHANGELOG.md
  LICENSE.txt
  requirements.txt
  package-manifest.json
  schemas/
    common/  core/  reference/  channel/  automation/  assurance/
  fixtures/
    positive/
    negative/
  tests/
    expected-validation-results.json
    semantic-tests.json
  tools/
    validate.py
    make_manifest.py
  evidence/
    test-report.json        (generated)
```

**CDS1200-R006** A reference distribution MUST keep schemas, fixtures, test catalogues, tools and generated evidence logically separate.

**CDS1200-R007** A consumer MUST be able to identify which files are source artefacts and which are generated evidence. In the reference layout, everything under `evidence/` is generated; everything else is source.

## 5. Dependency Declaration and Environment Integrity *(normative)*

The v0.1 package shipped without a dependency declaration, and its headline evidence claim did not reproduce in a clean environment: JSON Schema Draft 2020-12 treats `format` as annotation-only by default, and the Python format checker silently skips the `date-time` assertion unless the optional `rfc3339-validator` package is installed. A clean run therefore accepted an invalid timestamp fixture (22/23 against a claimed 23/23; REVIEW-010). The v0.2 package closes both the declaration gap and the silent-weakening gap.

**CDS1200-R008** A reference package MUST declare its complete runtime dependencies with pinned versions in a machine-readable file distributed with the package.

**CDS1200-R009** The reference runner MUST verify at startup that every validation capability the suite depends on (including the `date-time` format assertion) is actually enforced in the current environment, and MUST exit non-zero with an actionable message when one is not — it MUST NOT continue with silently weakened validation.

*Informative note.* `requirements.txt` pins `jsonschema==4.26.0`, `referencing==0.37.0` and `rfc3339-validator==0.1.4`. `tools/validate.py` probes a deliberately invalid date-time against a `format: date-time` schema before loading anything; if the probe validates, the runner exits with `FATAL: the 'date-time' format assertion is not enforced in this environment` and the install command. This was proven the same way the original defect was found: in a third clean virtualenv with no dependencies installed, the v0.2 runner refuses to run at all — where the v0.1 runner reported a quietly wrong pass — and with the pinned dependencies installed the full suite reproduces (§17).

## 6. Package Manifest and Integrity *(normative)*

`package-manifest.json` inventories the distributed files with a SHA-256 digest and byte length per file, plus the schema registry inventory (§7). This supports reproducible downloads, release comparison and evidence that a run used the intended artefacts.

The manifest convention *(resolves finding CDS1200-6)*: the manifest lists every package file **except itself and `evidence/`**. The manifest cannot contain its own hash without circularity, and evidence is regenerated per run and instead embeds the manifest's hash (`manifest_sha256` in the report). The manifest's top-level `package_hash` is the SHA-256 over the sorted `"path  sha256"` lines, giving a single package-level integrity value that covers all listed files. The manifest is regenerated with `tools/make_manifest.py`, run *before* the validator so the report embeds the current manifest hash.

**CDS1200-R010** A released package MUST include a machine-readable file manifest with a cryptographic hash for each distributed file, and MUST state its self-exclusion convention.

**CDS1200-R011** The manifest MUST include a single package-level hash derived deterministically from the per-file hashes.

**CDS1200-R012** Generated evidence intended for assurance MUST embed the hash of the package manifest (or an equivalent package release identifier) so the evidence identifies the exact artefacts evaluated. *(Closes finding CDS1200-10: the v0.2 report records `manifest_sha256`.)*

**CDS1200-R013** A validator or assurance process SHOULD verify package hashes before treating results as release evidence.

## 7. Executable Schema Registry *(normative)*

The v0.2 package ships **21 schemas** implementing the registry needed to demonstrate the canonical and publication lifecycle. Each schema declares JSON Schema Draft 2020-12, a release-independent URN `$id` and its own semantic version.

| Domain | Schemas (21) |
|---|---|
| common (5) | envelope, entity-reference, localised-text, measurement, money |
| core (3) | product, variant, attribute-definition |
| reference (5) | dictionary, dictionary-value, category, taxonomy-mapping, facet-definition |
| channel (5) | channel-profile, field-mapping, publication-record, observation-record, verification-result |
| automation (1) | ai-proposal |
| assurance (2) | conformance-manifest, validation-output |

Identifier policy (ADR-D5, homed in CDS-000/CDS-1100; restated here only as it binds the package): `$id`s take the form `urn:cds:schema:<domain>:<name>` with **no release version in the URN**, so identifiers are stable across releases; each schema carries a `version` keyword with its own semver (all `0.2.0` at this release); instances pin the corpus release via the envelope `cds_version` constant. *(Resolves finding CDS1200-13: v0.1's "stable $id" wording contradicted its version-embedded `urn:cds:schema:v0.1:*` URNs.)*

**CDS1200-R014** Every reference schema MUST declare the supported schema dialect, a release-independent `$id` and a per-schema semantic version, per the identifier policy in CDS-1100.

**CDS1200-R015** The package MUST include all referenced schemas required to validate the distributed fixtures without network access, and the manifest MUST inventory the registry (id, version, path).

## 8. Shared Definitions and Composition *(normative)*

Common types are defined once and reused by `$ref`. Entity schemas compose the common document envelope with entity-specific properties, so identifiers, revisions, timestamps and source-system fields behave consistently.

```json
{
  "$id": "urn:cds:schema:core:product",
  "version": "0.2.0",
  "allOf": [
    {"$ref": "urn:cds:schema:common:envelope"},
    {"type": "object", "properties": {"document_type": {"const": "product"}}}
  ],
  "unevaluatedProperties": false
}
```

The envelope requires `cds_schema`, `cds_version`, `document_type`, `document_id`, `revision`, `status`, `created_at`, `updated_at` and `source_system`; `cds_version` is `{"const": "0.2"}` *(resolves finding CDS1200-7 — v0.1 fixtures declared `"1.0"` against an unpinning pattern)*; extension keys are constrained to dotted reverse-namespace form (extension rules: CDS-1100, CDS-300).

**CDS1200-R016** A shared definition MUST have exactly one authoritative schema file within a package release.

**CDS1200-R017** Entity schemas SHOULD close unevaluated top-level properties unless a governed extension point is explicitly provided.

**CDS1200-R018** The reference runner MUST cross-check each instance's declared `cds_schema` against the `$id` of the schema actually applied, and treat a mismatch as a validation error.

## 9. Fixture Design Model *(normative)*

A fixture is a stable document designed to demonstrate one or more contract rules, identified by path, declared schema and expected outcome. Positive fixtures model realistic commerce records; negative fixtures isolate a specific invalid condition.

| Fixture property | Rule |
|---|---|
| Synthetic | No personal, confidential or credential data |
| Minimal but meaningful | Enough business context to explain the rule |
| Stable | No current timestamps, random IDs or live taxonomy lookups |
| Single purpose | A negative case fails for one declared principal reason |
| Self-identifying | The envelope declares document type and schema |
| Traceable | The expected-results catalogue names the schema, expected outcome and, for negatives, the intended error |

**CDS1200-R019** Every fixture MUST have a declared expected validation outcome in the machine-readable catalogue.

**CDS1200-R020** A negative fixture SHOULD isolate one principal violation so that a failed test remains diagnosable.

**CDS1200-R021** Reference fixtures MUST be synthetic and MUST NOT contain live credentials, personal customer information or confidential supplier data.

## 10. Positive Fixture Suite *(normative)*

The v0.2 suite contains **16 positive structural fixtures**. Together they demonstrate the canonical product, controlled dictionary, classification, channel profile and publication assurance chain.

| Fixture group | Demonstrated behaviour |
|---|---|
| Attribute Definitions (2) | Semantic prefix syntax, scope, value type, cardinality, comparison behaviour, dictionary binding |
| Dictionaries (2) | Stable dictionary identity, canonical labels (localised-text form), aliases, facet memberships, channel representations |
| Classification (2) | Internal category path (stable-ID array) and Shopify taxonomy mapping |
| Product and variants (3) | Canonical product truth, typed attribute values, variant options, SKU and zero-preserving GTIN handling |
| Channel profile (1) | Capabilities, field mappings (source layer, write mode, comparison strategy), transformations |
| Publication chain (3) | Expected channel state, observed state, field-level verification (§13) |
| Facets (1) | Facet family definition and configured values |
| AI proposal (1) | Proposed value, evidence, confidence, review state, model and workflow version (rules: CDS-700) |
| Conformance manifest (1) | Declared level, profiles, assessment method, test summary (semantics: CDS-1000 §26) |

**CDS1200-R022** All positive fixtures MUST validate under their declared schemas, and the package MUST include at least one complete canonical product-to-verification lifecycle fixture chain.

## 11. Negative Fixture Suite *(normative)*

The package includes **13 negative fixtures**. Each fails under its declared schema, and — new in v0.2 — each catalogue entry declares the *intended* error via `expected_error_substrings`. Negative tests prove that a validator rejects invalid input for the right reason, not merely that it produced some error.

The mechanism *(resolves findings CDS1200-3 / PKG-2)*: because entity schemas compose the envelope via `allOf` and close with `unevaluatedProperties: false`, any subschema failure in Draft 2020-12 drops property annotations and triggers a blanket "Unevaluated properties are not allowed" cascade error alongside the real one. In v0.1 the runner asserted only "any error", so the suite could not detect loss of the constraint actually under test. The v0.2 runner requires at least one declared intended substring among the reported errors and **excludes the `unevaluatedProperties` cascade line from counting as evidence** — a negative case whose only surviving error is the cascade is a suite failure.

| Negative fixture | Intended principal failure |
|---|---|
| product-missing-product-id.json | Missing required `product_id` |
| envelope-missing-revision.json | Missing required envelope `revision` |
| envelope-bad-status.json | Envelope status not in the controlled enumeration |
| variant-invalid-gtin.json | Barcode contains a non-digit |
| attribute-invalid-semantic-name.json | Field identifier violates CDS semantic prefix syntax (CDS-300) |
| dictionary-value-invalid-code.json | Canonical code is not lowercase snake_case (CDS-400) |
| publication-invalid-status.json | Publication status not in the controlled enumeration (CDS-500) |
| observation-invalid-timestamp.json | Timestamp is not RFC 3339 date-time |
| timestamp-missing-offset.json | Date-time lacks a timezone offset |
| product-attribute-wrong-type.json | Attribute value violates the typed-value shape |
| verification-invalid-status.json | Presentational colour label used where a normative verification status is required (CDS-500) |
| verification-missing-reason-code.json | Non-MATCH field result lacks the required `reason_code` (CDS-500) |
| ai-confidence-out-of-range.json | Confidence exceeds 1.0 (CDS-700) |

**CDS1200-R023** A package MUST contain negative fixtures for required fields, controlled enumerations, semantic identifier syntax, numerical ranges and standard formats where those constraints are normative.

**CDS1200-R024** A validator run MUST be considered failed if a negative fixture unexpectedly validates.

**CDS1200-R025** Each negative catalogue entry MUST declare the intended error (as one or more expected error substrings or an equivalent machine-checkable assertion), and the runner MUST require the intended error to be present, excluding composition-cascade errors from counting as evidence.

## 12. Semantic and Cross-Document Tests *(normative)*

JSON Schema validates a document in isolation. CDS also requires relationships that span documents, revisions and tenant boundaries. These live in a separate machine-readable semantic catalogue (`tests/semantic-tests.json`) and — new in v0.2 — are **executed by the reference runner**, not merely documented. *(Resolves finding CDS1200-4: in v0.1 the semantic catalogue was aspirational, SEM-001 would have failed if run, and the CI narrative listed steps the runner never performed.)*

| Test | Cross-document rule |
|---|---|
| SEM-001 | Product variant references resolve to variants whose `product_id` matches the product |
| SEM-002 | Dictionary value facet membership resolves to a configured facet value |
| SEM-003 | Publication `canonical_revision` equals the product revision used to calculate expected state |
| SEM-004 | All related documents remain within the same tenant boundary |

Scope honesty: SEM-001..004 demonstrate the *mechanism* — a distinct, executed semantic layer over already-validated documents. They are four checks over a small fixture set, not a complete semantic integrity suite. Production-scale referential integrity, authority enforcement and tenancy isolation remain the implementation's obligation, tested under CDS-1000 (for example T-TEN-001 for tenant isolation).

**CDS1200-R026** An implementation MUST NOT represent cross-document or semantic integrity as established merely because each individual document passes structural schema validation. *(Applies equally to this chapter's own evidence: §17 reports structural and semantic counts separately.)*

**CDS1200-R027** A semantic test MUST identify all documents or services required to evaluate the rule.

**CDS1200-R028** The reference runner MUST execute the packaged semantic catalogue, and a run MUST be considered failed when any semantic outcome differs from its declared expectation.

## 13. Publication Assurance Test Chain *(normative)*

The reference apparel fixtures demonstrate the CDS-500 assurance lifecycle using four linked documents, separating canonical revision, expected state, downstream observation and verification evidence. Verification statuses, detailed statuses and traffic-light presentation are homed in CDS-500 and not restated here.

```
prd_shirt_100 revision 42
  -> pub_shopify_shirt_100_r42   expected title, category, material, tags
  -> obs_shopify_shirt_100_001   observed downstream representation
  -> ver_shopify_shirt_100_001   field comparison + overall MATCH
```

The observation returns the same tags in a different order; the declared comparison strategy treats tags as an unordered set, so the verified result remains MATCH.

**CDS1200-R029** A publication assurance fixture MUST preserve the identifiers linking canonical revision, publication, observation and verification result, and MUST keep canonical, observed and verification values in distinct documents.

**CDS1200-R030** A verification fixture MUST declare the comparison strategy used for each compared field.

## 14. Determinism and Reproducibility *(normative)*

A reference suite is useful only when independent implementers can reproduce its results. The package therefore fixes timestamps, revisions, IDs, source systems, channel states and expected reports:

- No fixture calls a live channel or taxonomy service.
- No fixture obtains the current time during validation.
- No test depends on random values or array iteration order.
- All schema references resolve from the local package registry.
- Generated reports use stable case ordering.
- Package and manifest hashes let evidence identify the exact artefacts used.

**CDS1200-R031** A reference fixture MUST be deterministic under the documented comparison and validation rules.

**CDS1200-R032** Where a test requires randomness or time simulation, the seed and clock MUST be explicitly controlled and recorded.

**CDS1200-R033** The packaged validation suite MUST run without network access.

## 15. Reference Validation Runner and CLI Contract *(normative)*

The package contains a small Python runner as an **informative** executable implementation (the standard is language-neutral; §18). A clean run:

1. Verifies that declared validation capabilities are enforced (§5) — else exits FATAL.
2. Loads every schema file and registers it by `$id` in a local registry.
3. Validates each positive fixture and requires no errors; validates each negative fixture, requires errors and requires the intended error substring (§11).
4. Cross-checks `cds_schema` against the applied schema (§8).
5. Executes the semantic catalogue SEM-001..004 (§12).
6. Writes the evidence report, embedding the manifest hash and environment (§16).
7. Exits 0 only when every structural and semantic case matches its expectation.

| CLI behaviour | Contract |
|---|---|
| Default run | Validate the packaged structural and semantic catalogues |
| Report output | Print a structured JSON summary; optionally write the full report to a path |
| Exit 0 | All actual outcomes equal expected outcomes |
| Non-zero exit | Any outcome differs, package loading fails, or a required validation capability is unavailable |
| Offline | All schema references resolve locally |
| Diagnostics | Include fixture, schema, expected, actual, outcome and validator errors |

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python tools/validate.py --write-report evidence/test-report.json
```

**CDS1200-R034** A reference runner MUST return a non-zero process status when any actual outcome differs from the expected outcome or the package cannot be loaded and verified.

**CDS1200-R035** An alternative implementation MAY replace the reference runner if it evaluates the same catalogues and produces equivalent outcomes.

## 16. Validation Evidence and Reporting *(normative)*

Validation evidence is a machine-readable record of the package version, environment, test cases, expected and actual outcomes, and error messages. Evidence is **informative**: it is a snapshot of a recorded run in a recorded environment, never governed prose (§1, CDS1200-R003). Evidence feeding a conformance claim is governed by CDS-1000's evidence-package rules.

| Evidence field | Purpose |
|---|---|
| package_version | Identifies the schema and fixture release |
| generated_at | When the evidence was generated |
| environment | Python version, platform, and pinned dependency versions actually resolved |
| manifest_sha256 | Hash of the package manifest — ties evidence to exact artefacts (CDS1200-R012) |
| summary | Structural and semantic case counts, passed/failed, reported separately and combined |
| fixture / schema_id | Identifies the tested document and governing contract |
| expected / actual / outcome | PASS only when actual equals expected — an intentionally invalid negative fixture passes its test by failing validation |
| detail / errors | Intended-error assertion result and preserved validator diagnostics |

**CDS1200-R036** A validation report MUST distinguish instance validity from test-case outcome.

**CDS1200-R037** Generated evidence MUST identify fixture, schema, expected result, actual result, test outcome and the execution environment (language runtime and dependency versions).

**CDS1200-R038** Structural and semantic results MUST be separately identifiable in the report and its summary.

## 17. Execution Snapshot *(informative)*

The following is the recorded outcome of executing Reference Package v0.2.1 in a clean environment with the pinned dependencies installed. It is an evidence snapshot, not a normative claim (§1); reproducing it requires the recorded environment or a compatible one.

| Metric | Result |
|---|---|
| Schemas | 21 |
| Positive fixtures | 16 |
| Negative fixtures | 13 |
| Structural cases | 29 / 29 as expected |
| Semantic cases (SEM-001..004) | 4 / 4 as expected |
| Total cases | 33 / 33, 0 unexpected outcomes |
| Manifest-listed files | 60 (manifest itself and `evidence/` excluded by convention, §6) |
| Evidence ties | `manifest_sha256` embedded in report; manifest `package_hash` present |

Recorded environment: Python 3.14.7; `jsonschema` 4.26.0, `referencing` 0.37.0, `rfc3339-validator` 0.1.4 (per `evidence/test-report.json`, generated 2026-08-17). In a clean environment *without* the pinned dependencies, the runner exits FATAL at startup rather than reporting a weakened pass (§5) — the failure mode that produced v0.1's non-reproducing 23/23 (REVIEW-010) can no longer occur silently.

## 18. Release Packaging, Versioning and Language Neutrality *(normative)*

The reference package uses semantic versioning independently of chapter prose (ADR-D5). A patch release corrects a fixture or tool without changing schema meaning; a minor release adds backward-compatible schemas or fixtures; a major release introduces incompatible contract changes.

| Change | Package version impact |
|---|---|
| Documentation typo only | Patch |
| Additional positive or negative fixture | Minor, unless it changes a prior expected outcome |
| Backward-compatible optional schema property | Minor |
| New required property | Major |
| Enumeration removal or meaning change | Major |
| Validator bug fix restoring specified behaviour | Patch, with documented evidence change |

**CDS1200-R039** Every package release MUST publish a changelog, a manifest and a test report. *(The v0.2.1 release ships all three; v0.2.0 first closed finding CDS1200-5, under which the v0.1 release failed its own rule.)*

**CDS1200-R040** A fixture outcome change between releases MUST be explained as a standard correction, a test correction or an intentional compatibility change.

**CDS1200-R041** Conformance MUST be determined by documented outcomes against the packaged catalogues, not by use of a particular programming language or library. Python is used only for the initial informative runner; any language may host an equivalent implementation (CDS1200-R035).

> RESOLVED (was D27 (resolved), owner decision 2026-08-04, research REVIEW-006A): dual licence adopted — **Apache-2.0** for machine-readable artifacts (schemas, fixtures, tests, tools, manifests; express patent grant) and **CC-BY 4.0** for specification prose, matching prevailing open-standard practice (OpenAPI, AsyncAPI, CloudEvents use Apache-2.0; W3C separates document and software licences). `LICENSE.txt` declares the split; `LICENSE-CODE.md` and `LICENSE-SPEC.md` contain the full terms; tools carry SPDX headers. The distribution blocker recorded in the original v0.2 draft was closed on 2026-08-17.

## 19. Implementation Guidance: CI, Release Discipline and Code Generation *(informative)*

The v0.1 draft stated several MUSTs regulating adopters' internal CI pipelines, release processes and generated model classes — untestable against this package and out of its scope *(finding CDS1200-9)*. They are retained here as guidance with their normative homes cross-referenced:

- **Run the suite on change.** A maintained implementation should run the reference fixture suite whenever schemas, mappings, serializers or validators change, and should not release a schema change that causes an unexplained change to a golden fixture outcome. (Release evidence obligations for the *package itself* remain normative in §18; conformance testing obligations: CDS-1000.)
- **Reference CI shape.** checkout package → verify manifest → validate schema metaschemas → run structural suite (positive + negative) → run semantic tests → compare evidence summary → publish report and artefact hashes. Unlike v0.1, every step listed here is one the reference runner actually performs, except metaschema validation and hash verification, which `make_manifest.py` and standard tooling cover.
- **Multi-tenant testing.** Production assurance suites should verify that cross-tenant references cannot resolve without an explicit governed sharing mechanism; the normative tenant-isolation test is CDS-1000 T-TEN-001, and SEM-004 demonstrates only the single-boundary fixture case.
- **Code generation.** Generated model classes should preserve unknown governed extensions and CDS scalar semantics when round-tripping documents; the governing serialization and extension rules are CDS-1100's, and round-trip assertions belong to the future suite in §20.
- **Organisation-specific fixtures.** Organisations should add fixtures for known incidents, migrations and channel failure modes; these live alongside, not inside, the reference package.

## 20. Future Work: Round-Trip, Security and Scale Suites *(informative)*

These suites are deliberately out of scope for v0.2 and are stated as future work rather than implied capability.

**Round-trip serialization.** Structural validity does not prove an implementation preserves values when reading and writing. A complete harness should parse, serialize, reparse and compare representative documents with type-aware semantics: GTIN leading zeros and exact textual form; decimal/money scale and value; measurement value/unit separation; ordered arrays vs unordered sets; null vs absent; UTF-8 stability under the declared normalization policy; language-tag association. An implementation claiming safe interchange should pass round-trip tests for every supported CDS type (interchange rules: CDS-1100).

**Security and multi-tenant fixtures.** The public package is synthetic and secret-free (CDS1200-R021). Production assurance additionally needs: cross-tenant reference rejection; quarantine of disallowed script markup; unknown extension namespaces rejected or isolated per policy; fixtures containing credentials blocked from evidence publication; oversized payloads rejected under profile limits; AI proposals unable to mutate canonical state without the required approval transition (CDS-700).

**Performance and scale.** The v0.2 package prioritises correctness. Future releases should add *generated* scale fixtures while preserving a small hand-reviewable core: bounded validation time and memory across small (100 products) to large (1M products, 8M variants) catalogues, wide products, deep taxonomies and large publication batches. Illustrative sizes are not normative performance targets; service-level expectations belong to implementation profiles (CDS-900).

## 21. Adoption by a PIM Project *(informative)*

A PIM project can adopt CDS-1200 incrementally. The package does not force internal database schemas to mirror the JSON documents; it defines stable interchange and assurance boundaries.

1. Map existing product and variant records to the CDS product and variant contracts.
2. Export a small canonical fixture set and validate it.
3. Model existing controlled lists as CDS dictionaries and values.
4. Generate expected channel state for one channel product.
5. Pull the product back into an observation record.
6. Produce a field-level verification result.
7. Add organisation-specific negative fixtures for historical failure modes.
8. Run the suite in CI before connector or schema releases.

*(Steps renumbered from the v0.1 draft's 8–15 — finding CDS1200-11.)*

## 22. Architecture Decision Records *(informative)*

Decisions are held in the single global ADR register (CDS000-R006). Governing this chapter: **ADR-D5** (single corpus release; release-independent `$id` URNs; per-schema semver; envelope `cds_version` const; changelog, pinned dependencies and informative environment-annotated evidence required of the v0.2 package). The chapter-local records CDS-ADR-1200-001..007 from v0.1 are subsumed into the global register unchanged in substance: ship executable artefacts with the prose standard; use JSON Schema Draft 2020-12; separate structural from semantic tests; require positive and negative fixtures; use deterministic synthetic fixtures; treat the Python runner as informative; record package hashes.

---

## Annex A — Organisation Example: Legacy Hosted-Table PIM *(informative)*

An organisation migrating from a hosted-table PIM (for example Airtable) can express its legacy estate directly in package terms: legacy canonical tables and merchandising-fact fields become canonical fixtures; per-channel export tables become observation fixtures; existing match/compare reports become verification fixtures. This turns a migration inventory into an executable regression suite before cutover. The governed migration pathway — including the pre-cutover downstream baseline — is defined in CDS-1300. *(Moved from the v0.1 adoption section per finding CDS1200-12.)*

## Appendix A — Schema and Fixture IDs *(informative)*

| Schema `$id` | Representative fixture |
|---|---|
| urn:cds:schema:core:product | relaxed-linen-shirt.product.json |
| urn:cds:schema:core:variant | relaxed-linen-shirt-navy-s.variant.json, relaxed-linen-shirt-navy-m.variant.json |
| urn:cds:schema:core:attribute-definition | MF_colour.json, MF_material.json |
| urn:cds:schema:reference:dictionary | colour.dictionary.json |
| urn:cds:schema:reference:dictionary-value | colour_navy.value.json |
| urn:cds:schema:reference:category | womens-shirts.category.json |
| urn:cds:schema:reference:taxonomy-mapping | womens-shirts.shopify-mapping.json |
| urn:cds:schema:reference:facet-definition | colour-family.json |
| urn:cds:schema:channel:channel-profile | shopify.channel-profile.json |
| urn:cds:schema:channel:publication-record | shopify-shirt.publication.json |
| urn:cds:schema:channel:observation-record | shopify-shirt.observation.json |
| urn:cds:schema:channel:verification-result | shopify-shirt.verification.json |
| urn:cds:schema:automation:ai-proposal | colour-mapping.ai-proposal.json |
| urn:cds:schema:assurance:conformance-manifest | reference.conformance-manifest.json |

`common/*` (envelope, entity-reference, localised-text, measurement, money), `channel/field-mapping` and `assurance/validation-output` are composed by reference and exercised through every fixture rather than by a dedicated fixture file.

## Appendix B — Reference Commands *(informative)*

```bash
# Unpack the companion package
unzip CDS-1200_Reference_Package_v0.2.zip
cd CDS-1200_Reference_Package_v0.2

# Install pinned dependencies (required; the runner exits FATAL without them)
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

# Run the structural + semantic suite and write evidence
.venv/bin/python tools/validate.py --write-report evidence/test-report.json

# Regenerate the manifest (run BEFORE the validator so evidence embeds the current hash)
.venv/bin/python tools/make_manifest.py
```

---

*End of CDS-1200 v0.2 Review Draft.*

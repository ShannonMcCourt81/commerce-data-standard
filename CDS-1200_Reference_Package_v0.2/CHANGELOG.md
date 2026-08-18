# Changelog — CDS-1200 Reference Package

## 0.2.1 (2026-08-17)

Distribution-only patch; the 21 schema versions and fixture outcomes are unchanged.

- Added the full Apache-2.0 and CC-BY-4.0 licence texts.
- Added Apache-2.0 SPDX identifiers to both Python tools.
- Regenerated the 60-file manifest and clean-environment evidence report (33/33).

## 0.2.0 (2026-08-04)

Rebuilt from 0.1.0 against the v0.2 Review Draft chapters and the accepted ADRs. Changes are keyed to review finding IDs (REVIEW-002 / REVIEW-002A / REVIEW-010).

### Identifiers and versioning (ADR-D5; CDS1100-7, CDS1200-7, CDS1200-13)
- All `$id`s rewritten to release-independent URNs `urn:cds:schema:<domain>:<name>` (version removed from the URN).
- Every schema carries its own semver in a `version` keyword (all start at `0.2.0`).
- Envelope `cds_version` is now `{"const": "0.2"}`; all fixtures pinned to `"0.2"`.
- Validator cross-checks each instance's `cds_schema` against the applied schema `$id` (CDS1100-17).

### Verification contract (ADR-D3; CDS1100-1, CDS1100-11, CDS1100-19)
- `status` enum is the 8-value core enum incl. `OVERRIDDEN`: MATCH, MISSING, MISMATCH, PENDING, UNOBSERVABLE, NOT_APPLICABLE, OVERRIDDEN, ERROR.
- Optional `detailed_status` (CDS-500 §17.2 detailed set with deterministic rollup).
- `reason_code` (`^CDS_[A-Z_]+$`) is REQUIRED on every non-MATCH field result (if/then).
- `field_path` (JSON Pointer) replaces bare `field` (CDS1100-19 / R062).
- Added optional `coverage_ratio`, `comparison_engine_version`, `repair_action`, and informative lowercase `presentation_status` (green/amber/red/grey).

### New schemas (CDS1100-10, CDS1100-1, CDS1100-4)
- `common/money.schema.json` — ISO-4217 currency + string-decimal amount (choice documented in `$comment`).
- `channel/field-mapping.schema.json` — source/target, `source_layer` (ADR-D4 layers), `transformation_version`, `write_mode`, `read_back_path`, `comparison_strategy`; channel-profile now references it.
- `assurance/validation-output.schema.json` — document_id, field_path, CDS_* reason_code, severity, message; embedded by ai-proposal `validation_results`.
- Schema registry inventory added to `package-manifest.json`.

### Closed contracts completed (closure trap; CDS1100-2/-3/-5/-6/-23)
- observation-record: `observation_method` (api_read/feed_diagnostic/scrape/manual, required), per-field `coverage` object {supported, unobservable} replacing the bare enum, `channel_entity_id`.
- publication-record: required `mapping_set_version` and `payload_hash` (`^sha256:`); `preflight_result` and `transport_status` (queued/sent/acknowledged/rejected/failed) split from `publication_status`.
- ai-proposal: `review_state` enum per CDS-700 §6 R015 (proposed/review_required/accepted/rejected/superseded/expired) replaces `proposal_status`; added `reviewer`, `accepted_revision`, `task_type`, `validation_results`.
- conformance-manifest: required `test_suite_version` and `assessment_method` (self-attestation/customer-assessment/independent-assessment); `test_summary` now counts passed/failed/not_tested/inconclusive; fixture counts match the evidence report.
- product: optional `lifecycle` (introduction_date, end_of_sale_date, approval_state) and `provenance` groups.

### Tightening (CDS1100-12/-14/-15/-16/-21)
- Envelope `extensions` keys constrained to dotted reverse-namespace (`propertyNames` pattern).
- attribute-definition: `dictionary_id` required when `value_type` is enum_reference (or enum_reference_list).
- One localised-text model everywhere: dictionary-value `canonical_label` and facet `label` are now arrays of `{language, text}`.
- category `path` is an array of stable category IDs, not display labels.
- Product `attributes` values constrained to a minimal typed-value shape (`dictionary_value_id`/`text`/`number`/`measurement`/`money`/`boolean`/`identifier`/`date_time`); `"MF_material": 42` no longer validates.
- GTIN: per-scheme exact digit lengths via if/then; positive variant fixture uses the zero-preserving GTIN-14 `09338716007824`.
- Every date-time field asserts both `format: date-time` AND a pattern requiring a timezone offset.

### Validator and tests (REVIEW-010; PKG-2, CDS1100-8/-9, CDS1200-2/-8/-10)
- Pinned `requirements.txt`; runner fails loudly at startup if the date-time format assertion is unavailable.
- Negative catalogue entries carry `expected_error_substrings`; the runner requires an intended substring in the errors, ignoring the `unevaluatedProperties` cascade line.
- Semantic runner implemented (SEM-001..004); SEM-001 fixed by adding the missing `relaxed-linen-shirt-navy-s` variant fixture.
- Dead duplicate `run_catalogue` removed.
- Report includes structural + semantic counts, environment (python + dependency versions), and the sha256 of `package-manifest.json`.

### Fixtures
- All updated to v0.2 envelopes and new URNs.
- New positive: `fixtures/positive/variants/relaxed-linen-shirt-navy-s.variant.json`.
- New negatives: envelope-bad-status, envelope-missing-revision, timestamp-missing-offset, product-attribute-wrong-type, verification-missing-reason-code. All 8 v0.1 negatives kept (updated).

### Package hygiene (CDS1200-5/-6/-8; ADR-D5)
- This CHANGELOG added; README states run instructions and the manifest self-hash convention; evidence marked informative-with-environment; LICENSE carries the `[OPEN-D27]` marker; manifest regenerated with per-file sha256 and a top-level `package_hash`.

## 0.1.0 (2026-08-03)

Initial working-draft package (18 schemas, 15 positive + 8 negative fixtures).

# CDS-1200 Reference Package v0.2

This package accompanies CDS-1200 - Reference Implementation, Schema Package and Test Fixtures (v0.2 Review Draft).

## Contents

- `schemas/` - JSON Schema Draft 2020-12 reference schemas (21). Every schema carries a release-independent `$id` (`urn:cds:schema:<domain>:<name>`) and its own semver `version` keyword (ADR-D5).
- `fixtures/positive/` - documents that MUST validate (16).
- `fixtures/negative/` - documents that MUST fail validation, each with declared `expected_error_substrings` (13).
- `tests/` - expected structural results and the semantic test catalogue (both executed by the runner).
- `tools/validate.py` - reference validation runner (structural + semantic).
- `tools/make_manifest.py` - manifest regenerator.
- `evidence/` - generated validation evidence. **Informative**, not normative: results depend on the recorded environment, which the report states (python and dependency versions).

## Run

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python tools/validate.py --write-report evidence/test-report.json
```

Dependencies are pinned in `requirements.txt`. The runner fails loudly at startup if the `date-time` format assertion is unavailable (i.e. `rfc3339-validator` missing), rather than silently passing invalid timestamps.

The runner:
- validates every catalogued fixture against its schema,
- cross-checks each instance's `cds_schema` against the `$id` of the schema actually applied,
- asserts that each negative fixture fails with its *intended* error substring (the `unevaluatedProperties` cascade line does not count as evidence),
- executes the semantic tests (SEM-001..SEM-004), and
- exits 0 only when all structural and semantic cases match expectations.

## Manifest self-hash convention

`package-manifest.json` lists the sha256 and byte size of every package file **except itself and `evidence/`**: evidence is regenerated per run and embeds the manifest hash (`manifest_sha256` in the report), so listing it would be circular. The manifest's `package_hash` is the sha256 over the sorted `"path  sha256"` lines, providing a single package-level hash. Regenerate with `tools/make_manifest.py`; run it *before* the validator so the report embeds the current manifest hash.

The reference package is informative software supporting the normative CDS chapters. The published specification remains governing where the package and prose conflict.

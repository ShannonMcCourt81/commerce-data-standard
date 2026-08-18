#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""CDS-1200 v0.2 reference validation runner.

Runs the structural fixture catalogue (tests/expected-validation-results.json)
and the semantic test catalogue (tests/semantic-tests.json). Exit 0 only when
every case matches its expected outcome.
"""
from __future__ import annotations
import argparse
import datetime
import hashlib
import importlib.metadata
import json
import platform
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_VERSION = "0.2.1"
PINNED = ("jsonschema", "referencing", "rfc3339-validator")
CASCADE_PREFIX = "Unevaluated properties are not allowed"


def assert_datetime_format_enforced() -> None:
    """Fail loudly if the environment silently skips date-time format assertion
    (REVIEW-010 finding 2: clean environments without rfc3339-validator)."""
    probe = Draft202012Validator(
        {"type": "string", "format": "date-time"}, format_checker=FormatChecker())
    if not list(probe.iter_errors("not a date-time")):
        sys.exit(
            "FATAL: the 'date-time' format assertion is not enforced in this "
            "environment. Install the pinned dependencies first:\n"
            "  pip install -r requirements.txt")


def load_schemas() -> dict:
    schemas = {}
    for path in sorted((ROOT / "schemas").rglob("*.schema.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        schemas[data["$id"]] = data
    return schemas


def validate_instance(instance: dict, schema_id: str, schemas: dict, registry) -> list[str]:
    validator = Draft202012Validator(
        schemas[schema_id], registry=registry, format_checker=FormatChecker())
    errors = [e.message for e in sorted(validator.iter_errors(instance), key=lambda e: list(e.path))]
    # CDS1100-17: the instance must declare the schema actually applied.
    declared = instance.get("cds_schema")
    if declared != schema_id:
        errors.insert(0, f"cds_schema mismatch: instance declares {declared!r} "
                         f"but was validated against {schema_id!r}")
    return errors


def run_structural(catalogue: dict, schemas: dict, registry) -> list[dict]:
    results = []
    for group in ("positive", "negative"):
        for case in catalogue[group]:
            instance = json.loads((ROOT / case["path"]).read_text(encoding="utf-8"))
            errors = validate_instance(instance, case["schema_id"], schemas, registry)
            actual = "PASS" if not errors else "FAIL"
            outcome = "PASS" if actual == case["expected"] else "FAIL"
            detail = None
            if group == "negative" and outcome == "PASS":
                # PKG-2 / CDS1100-9: the intended error must be present, and the
                # unevaluatedProperties cascade line does not count as evidence.
                meaningful = [e for e in errors if not e.startswith(CASCADE_PREFIX)]
                subs = case["expected_error_substrings"]
                if not any(s in e for s in subs for e in meaningful):
                    outcome = "FAIL"
                    detail = f"intended error not found; expected one of {subs}"
            results.append({
                "group": group, "fixture": case["path"], "schema_id": case["schema_id"],
                "expected": case["expected"], "actual": actual, "outcome": outcome,
                "reason": case.get("reason"), "detail": detail, "errors": errors})
    return results


# ---- semantic checks (plain JSON walking over already-validated fixtures) ----

def sem_variant_refs(docs):
    product = next(d for d in docs if d["document_type"] == "product")
    variants = {d["variant_id"]: d for d in docs if d["document_type"] == "variant"}
    for vid in product["variant_ids"]:
        if vid not in variants:
            return f"variant_id {vid!r} does not resolve to a variant document"
        if variants[vid]["product_id"] != product["product_id"]:
            return f"variant {vid!r} belongs to {variants[vid]['product_id']!r}"
    return None


def sem_facet_membership(docs):
    value = next(d for d in docs if d["document_type"] == "dictionary_value")
    facets = {d["facet_id"]: d for d in docs if d["document_type"] == "facet_definition"}
    for m in value["facet_memberships"]:
        facet = facets.get(m["facet_id"])
        if facet is None:
            return f"facet {m['facet_id']!r} not present"
        if m["value_id"] not in facet["value_ids"]:
            return f"value {m['value_id']!r} not configured on facet {m['facet_id']!r}"
    return None


def sem_revision_join(docs):
    product = next(d for d in docs if d["document_type"] == "product")
    publication = next(d for d in docs if d["document_type"] == "publication_record")
    if publication["canonical_revision"] != product["revision"]:
        return (f"canonical_revision {publication['canonical_revision']!r} != "
                f"product revision {product['revision']!r}")
    return None


def sem_single_tenant(docs):
    tenants = {d.get("tenant_id") for d in docs}
    return None if len(tenants) == 1 else f"documents span tenants {sorted(map(str, tenants))}"


SEMANTIC_CHECKS = {
    "SEM-001": sem_variant_refs,
    "SEM-002": sem_facet_membership,
    "SEM-003": sem_revision_join,
    "SEM-004": sem_single_tenant,
}


def run_semantic(tests: list[dict]) -> list[dict]:
    results = []
    for test in tests:
        docs = [json.loads((ROOT / p).read_text(encoding="utf-8")) for p in test["documents"]]
        check = SEMANTIC_CHECKS.get(test["test_id"])
        if check is None:
            actual, error = "FAIL", f"no check implemented for {test['test_id']}"
        else:
            error = check(docs)
            actual = "PASS" if error is None else "FAIL"
        results.append({
            "test_id": test["test_id"], "description": test["description"],
            "expected": test["expected"], "actual": actual,
            "outcome": "PASS" if actual == test["expected"] else "FAIL",
            "error": error})
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate CDS-1200 v0.2 reference fixtures")
    parser.add_argument("--catalogue", default=str(ROOT / "tests" / "expected-validation-results.json"))
    parser.add_argument("--semantic", default=str(ROOT / "tests" / "semantic-tests.json"))
    parser.add_argument("--write-report", default=None)
    args = parser.parse_args()

    assert_datetime_format_enforced()

    schemas = load_schemas()
    registry = Registry().with_resources(
        (uri, Resource.from_contents(data)) for uri, data in schemas.items())

    structural = run_structural(json.loads(Path(args.catalogue).read_text(encoding="utf-8")),
                                schemas, registry)
    semantic = run_semantic(json.loads(Path(args.semantic).read_text(encoding="utf-8")))

    manifest_path = ROOT / "package-manifest.json"
    manifest_sha256 = (hashlib.sha256(manifest_path.read_bytes()).hexdigest()
                       if manifest_path.exists() else None)

    s_failed = sum(r["outcome"] == "FAIL" for r in structural)
    m_failed = sum(r["outcome"] == "FAIL" for r in semantic)
    report = {
        "package_version": PACKAGE_VERSION,
        "generated_at": datetime.datetime.now(datetime.timezone.utc)
                        .isoformat(timespec="seconds").replace("+00:00", "Z"),
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "dependencies": {d: importlib.metadata.version(d) for d in PINNED},
        },
        "manifest_sha256": manifest_sha256,
        "summary": {
            "structural_cases": len(structural),
            "structural_passed": len(structural) - s_failed,
            "structural_failed": s_failed,
            "semantic_cases": len(semantic),
            "semantic_passed": len(semantic) - m_failed,
            "semantic_failed": m_failed,
            "total_cases": len(structural) + len(semantic),
            "passed": len(structural) + len(semantic) - s_failed - m_failed,
            "failed": s_failed + m_failed,
        },
        "results": structural,
        "semantic_results": semantic,
    }
    if args.write_report:
        out = Path(args.write_report)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))
    return 0 if report["summary"]["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

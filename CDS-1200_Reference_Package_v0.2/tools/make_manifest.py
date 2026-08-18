#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Regenerate package-manifest.json.

Convention (stated in README.md): the manifest lists the sha256 and size of
every package file EXCEPT itself and evidence/ (evidence is informative and
embeds the manifest hash, so including it would be circular). package_hash is
the sha256 over the sorted "path  sha256" lines, giving one package-level hash
that covers everything the manifest lists (CDS1200-6).
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE = {"package-manifest.json"}


def main() -> None:
    entries = []
    for path in sorted(ROOT.rglob("*")):
        rel = path.relative_to(ROOT).as_posix()
        if not path.is_file() or rel in EXCLUDE or rel.startswith("evidence/") \
                or any(part.startswith(".") or part == "__pycache__" for part in path.parts):
            continue
        data = path.read_bytes()
        entries.append({"path": rel, "sha256": hashlib.sha256(data).hexdigest(),
                        "bytes": len(data)})
    package_hash = hashlib.sha256(
        "\n".join(f"{e['path']}  {e['sha256']}" for e in entries).encode()).hexdigest()

    registry = []
    for path in sorted((ROOT / "schemas").rglob("*.schema.json")):
        schema = json.loads(path.read_text(encoding="utf-8"))
        registry.append({"id": schema["$id"], "version": schema["version"],
                         "path": path.relative_to(ROOT).as_posix()})

    manifest = {
        "package": "CDS-1200 Reference Package",
        "version": "0.2.1",
        "schema_dialect": "https://json-schema.org/draft/2020-12/schema",
        "hash_convention": "sha256 per file; manifest itself and evidence/ excluded; "
                           "package_hash = sha256 over sorted 'path  sha256' lines.",
        "package_hash": package_hash,
        "schema_registry": registry,
        "files": entries,
    }
    (ROOT / "package-manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"wrote package-manifest.json: {len(entries)} files, package_hash={package_hash[:12]}...")


if __name__ == "__main__":
    main()

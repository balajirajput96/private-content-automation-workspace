#!/usr/bin/env python3
"""Validate the repository's non-secret automation control plane.

This validator intentionally inspects only repository content. It never reads
credentials, invokes browsers, accesses social platforms, or processes media.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

VALIDATOR_VERSION = "1.0.0"

REQUIRED_FILES = {
    "daily_runbook": "daily_multiplatform_automation_runbook.md",
    "instagram_safety_notice": "instagram_account_safety_notice_2026-08-16.md",
    "local_sync_mapping": "antigravity_local_sync_mapping.md",
    "validation_contract": "docs/validation_contract.md",
    "persistence_policy": "docs/persistence_and_credentials_policy.md",
    "historical_records_index": "docs/historical_records_index.md",
    "run_record_schema": "schemas/automation_run_record.schema.json",
}

REQUIRED_PHRASES = {
    "daily_runbook": ["non-public", "Never store credentials"],
    "instagram_safety_notice": ["suspended immediately", "local-only mode"],
    "local_sync_mapping": ["No external synchronizations are performed"],
    "validation_contract": ["does not upload, publish, browse, authenticate"],
    "persistence_policy": ["official credential stores", "must never contain passwords"],
    "historical_records_index": ["raw terminal history remains local", "not copied into this repository"],
}

FORBIDDEN_TEXT = ("BEGIN " + "PRIVATE KEY", "gh" + "p_", "github" + "_pat_", "AI" + "za")


def git_revision(repo: Path) -> str:
    try:
        completed = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"
    return completed.stdout.strip()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_repository(repo: Path) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    def record(name: str, passed: bool, detail: str) -> None:
        checks.append({"name": name, "result": "pass" if passed else "fail", "detail": detail})

    resolved: dict[str, Path] = {}
    for key, relative_path in REQUIRED_FILES.items():
        path = repo / relative_path
        resolved[key] = path
        record(f"required_file:{relative_path}", path.is_file(), "present" if path.is_file() else "missing")

    for key, phrases in REQUIRED_PHRASES.items():
        path = resolved[key]
        if not path.is_file():
            continue
        text = read_text(path)
        for phrase in phrases:
            record(
                f"safety_phrase:{key}:{phrase}",
                phrase in text,
                "required safety phrase retained" if phrase in text else "required safety phrase missing",
            )

    schema_path = resolved["run_record_schema"]
    if schema_path.is_file():
        try:
            schema = json.loads(read_text(schema_path))
            required_keys = set(schema.get("required", []))
            expected_keys = {"timestamp", "repository_revision", "validator_version", "checks", "overall_result"}
            record(
                "run_record_schema:required_fields",
                expected_keys.issubset(required_keys),
                "required run-record fields present" if expected_keys.issubset(required_keys) else "required run-record fields missing",
            )
        except json.JSONDecodeError as error:
            record("run_record_schema:valid_json", False, f"invalid JSON: {error.msg}")

    for path in repo.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "run-records" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".txt", ".json", ".yml", ".yaml", ".py"}:
            continue
        text = read_text(path)
        for forbidden in FORBIDDEN_TEXT:
            record(
                f"secret_marker:{path.relative_to(repo)}:{forbidden}",
                forbidden not in text,
                "no prohibited marker found" if forbidden not in text else "prohibited marker found",
            )

    passed = all(check["result"] == "pass" for check in checks)
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "repository_revision": git_revision(repo),
        "validator_version": VALIDATOR_VERSION,
        "checks": checks,
        "overall_result": "pass" if passed else "fail",
        "blocker": None if passed else "Repository safety or structure validation failed; inspect failed checks.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, help="Optional non-secret JSON output path")
    args = parser.parse_args()

    report = check_repository(args.repo.resolve())
    rendered = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if report["overall_result"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())

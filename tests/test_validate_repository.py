from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "automation"))

from validate_repository import REQUIRED_FILES, REQUIRED_PHRASES, check_repository  # noqa: E402


class RepositoryValidatorTests(unittest.TestCase):
    def make_repo(self) -> Path:
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)
        repo = Path(temp_dir.name)
        for key, relative_path in REQUIRED_FILES.items():
            path = repo / relative_path
            path.parent.mkdir(parents=True, exist_ok=True)
            if key == "run_record_schema":
                path.write_text(
                    json.dumps(
                        {
                            "required": [
                                "timestamp",
                                "repository_revision",
                                "validator_version",
                                "checks",
                                "overall_result",
                            ]
                        }
                    ),
                    encoding="utf-8",
                )
            else:
                text = "\n".join(REQUIRED_PHRASES.get(key, ["placeholder"]))
                path.write_text(text, encoding="utf-8")
        return repo

    def test_valid_repository_passes(self) -> None:
        report = check_repository(self.make_repo())
        self.assertEqual(report["overall_result"], "pass")
        self.assertIsNone(report["blocker"])

    def test_missing_safety_notice_fails(self) -> None:
        repo = self.make_repo()
        (repo / REQUIRED_FILES["instagram_safety_notice"]).unlink()
        report = check_repository(repo)
        self.assertEqual(report["overall_result"], "fail")
        self.assertIn("required_file:instagram_account_safety_notice_2026-08-16.md", {item["name"] for item in report["checks"]})

    def test_prohibited_marker_fails(self) -> None:
        repo = self.make_repo()
        (repo / "notes.md").write_text("placeholder " + "gh" + "p_example", encoding="utf-8")
        report = check_repository(repo)
        self.assertEqual(report["overall_result"], "fail")
        self.assertTrue(any(item["name"].startswith("secret_marker:") and item["result"] == "fail" for item in report["checks"]))


if __name__ == "__main__":
    unittest.main()

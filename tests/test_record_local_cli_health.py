from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "automation"))

import record_local_cli_health as health  # noqa: E402


class LocalCliHealthTests(unittest.TestCase):
    @patch("record_local_cli_health.shutil.which", return_value=None)
    def test_missing_command_is_absent(self, _which: Mock) -> None:
        self.assertEqual(health.executable_state("not-present")["state"], "absent")

    @patch("record_local_cli_health.shutil.which", return_value="/usr/bin/example")
    def test_path_command_is_installed(self, _which: Mock) -> None:
        record = health.executable_state("example")
        self.assertEqual(record["state"], "installed")
        self.assertEqual(record["source"], "PATH")

    @patch("record_local_cli_health.shutil.which", return_value="/usr/bin/gh")
    @patch("record_local_cli_health.subprocess.run")
    def test_github_auth_success_is_nonsecret_state(self, run: Mock, _which: Mock) -> None:
        run.return_value = Mock(returncode=0)
        self.assertEqual(health.github_auth_state(), "authenticated")
        self.assertEqual(run.call_args.kwargs["stdout"], health.subprocess.DEVNULL)
        self.assertEqual(run.call_args.kwargs["stderr"], health.subprocess.DEVNULL)


if __name__ == "__main__":
    unittest.main()

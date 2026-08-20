#!/usr/bin/env python3
"""Create a non-secret local CLI-health record.

The record captures executable availability and an official GitHub CLI authentication
result only. It does not read credential stores, print command output, inspect
connector configuration, or invoke remote AI requests.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

RECORDER_VERSION = "1.0.0"


def executable_state(command: str, alternate_path: Path | None = None) -> dict[str, str]:
    if alternate_path and alternate_path.is_file() and alternate_path.stat().st_mode & 0o111:
        return {"state": "installed", "source": "known_local_path"}
    if shutil.which(command):
        return {"state": "installed", "source": "PATH"}
    return {"state": "absent", "source": "none"}


def github_auth_state() -> str:
    if not shutil.which("gh"):
        return "absent"
    result = subprocess.run(
        ["gh", "auth", "status"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return "authenticated" if result.returncode == 0 else "unauthenticated"


def collect() -> dict[str, Any]:
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "recorder_version": RECORDER_VERSION,
        "scope": "non-secret local executable and official CLI status only",
        "tools": {
            "antigravity": executable_state("agy", Path.home() / ".local" / "bin" / "agy"),
            "gemini": executable_state("gemini"),
            "jules": executable_state("jules"),
            "github": {"state": github_auth_state()},
        },
        "blocker": None,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    record = collect()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())

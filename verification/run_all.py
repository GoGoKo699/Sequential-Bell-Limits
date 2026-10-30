#!/usr/bin/env python3
"""Run the scientific verification programs without rewriting any fixture.

Each program has its own independently checked mathematical cases. This
coordinator preserves their reports, rejects malformed output, and returns
a nonzero exit status if any required check fails.
"""
from __future__ import annotations

import json
from pathlib import Path
import platform
import subprocess
import sys


PROGRAMS = (
    "verify_tons.py",
    "verify_quantum_protocol.py",
    "verify_evidence.py",
)


def main() -> int:
    directory = Path(__file__).resolve().parent
    checks = []
    for program in PROGRAMS:
        result = subprocess.run(
            [sys.executable, str(directory / program)],
            cwd=directory.parent,
            capture_output=True,
            text=True,
            check=False,
        )
        try:
            report = json.loads(result.stdout)
        except json.JSONDecodeError:
            report = {"status": "fail", "reason": "Verifier did not return JSON",
                      "stdout": result.stdout}
        passed = result.returncode == 0 and report.get("status") == "pass"
        checks.append({"program": program, "passed": passed,
                       "returncode": result.returncode, "report": report,
                       "stderr": result.stderr})
    passed = all(check["passed"] for check in checks)
    print(json.dumps({"status": "pass" if passed else "fail",
                      "python": platform.python_version(),
                      "checks": checks}, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

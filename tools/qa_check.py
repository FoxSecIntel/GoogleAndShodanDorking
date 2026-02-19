#!/usr/bin/env python3
"""Basic content QA for dork markdown files."""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DORKS = REPO / "dorks"


def check_table_shapes(path: Path) -> list[str]:
    issues: list[str] = []
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    header_cols = None

    for i, line in enumerate(lines, start=1):
        s = line.strip()
        if not s.startswith("|"):
            header_cols = None
            continue

        cols = [c.strip() for c in s.strip("|").split("|")]

        if all(re.fullmatch(r":?-{2,}:?", c or "") for c in cols):
            continue

        if header_cols is None:
            header_cols = len(cols)
            continue

        if len(cols) != header_cols:
            issues.append(f"{path.name}:{i} column mismatch ({len(cols)} vs {header_cols})")

    return issues


def check_suspicious_truncation(path: Path) -> list[str]:
    issues: list[str] = []
    for i, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), start=1):
        if line.strip().endswith(" cont") or line.strip().endswith("..."):
            issues.append(f"{path.name}:{i} suspicious truncation: {line.strip()}")
    return issues


def check_duplicates(path: Path) -> list[str]:
    issues: list[str] = []
    seen: set[str] = set()

    for i, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), start=1):
        s = line.strip()
        if not s.startswith("|"):
            continue

        cols = [c.strip() for c in s.strip("|").split("|")]
        if len(cols) < 2:
            continue

        # Skip header/separator rows
        if all(re.fullmatch(r":?-{2,}:?", c or "") for c in cols):
            continue
        if any(c.lower() in {"filter", "use case", "shodan query", "example", "description"} for c in cols):
            continue

        # Prefer likely query column names by index conventions in this repo
        # google table: Filter | Description | Example
        # shodan table: Use Case | Shodan Query | Description
        key = cols[1] if path.name == "shodan_dorks.md" else cols[-1]
        key = key.strip("`").strip()
        if not key:
            continue

        if key in seen:
            issues.append(f"{path.name}:{i} possible duplicate query: {key}")
        seen.add(key)

    return issues


def main() -> int:
    files = [DORKS / "google_dorks.md", DORKS / "shodan_dorks.md", DORKS / "use_case_templates.md"]
    all_issues: list[str] = []

    for f in files:
        if not f.exists():
            all_issues.append(f"missing file: {f}")
            continue
        all_issues += check_table_shapes(f)
        all_issues += check_suspicious_truncation(f)
        all_issues += check_duplicates(f)

    if all_issues:
        print("QA issues found:")
        for issue in all_issues:
            print(f"- {issue}")
        return 1

    print("QA checks passed: no obvious table/truncation/duplicate issues found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

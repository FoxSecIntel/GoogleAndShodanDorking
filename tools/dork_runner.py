#!/usr/bin/env python3
"""Simple CLI to search and export curated Google/Shodan dorks from markdown tables."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List


def parse_markdown_table(md_path: Path, source: str) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    if not md_path.exists():
        return rows

    lines = md_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    headers: List[str] | None = None

    for line in lines:
        s = line.strip()
        if not s.startswith("|"):
            headers = None
            continue

        parts = [p.strip() for p in s.strip("|").split("|")]
        if not parts:
            continue

        # separator row like |---|---|
        if all(re.fullmatch(r":?-{2,}:?", p or "") for p in parts):
            continue

        if headers is None:
            headers = [h.lower().replace(" ", "_") for h in parts]
            continue

        if len(parts) != len(headers):
            continue

        row = dict(zip(headers, parts))
        row["source"] = source
        rows.append(row)

    return rows


def load_dorks(repo_root: Path, source: str) -> List[Dict[str, str]]:
    dorks_dir = repo_root / "dorks"
    sources = [source] if source in {"google", "shodan"} else ["google", "shodan"]

    all_rows: List[Dict[str, str]] = []
    for src in sources:
        file_name = f"{src}_dorks.md"
        all_rows.extend(parse_markdown_table(dorks_dir / file_name, src))
    return all_rows


def render(rows: List[Dict[str, str]], output: str) -> None:
    if output == "json":
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return

    if not rows:
        print("No matching dorks found.")
        return

    for i, row in enumerate(rows, start=1):
        # Try to infer likely columns from both google/shodan styles
        query = row.get("shodan_query") or row.get("example") or ""
        title = row.get("use_case") or row.get("filter") or "(no title)"
        desc = row.get("description") or ""

        print(f"{i}. [{row.get('source', 'unknown')}] {title}")
        if query:
            print(f"   Query: {query}")
        if desc:
            print(f"   Why:   {desc}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Search curated Google/Shodan dorks from markdown files.")
    parser.add_argument("--source", choices=["google", "shodan", "all"], default="all")
    parser.add_argument("--search", default="", help="Keyword to match across title/query/description")
    parser.add_argument("--output", choices=["text", "json"], default="text")
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[1]),
        help="Path to repo root (defaults to current repo)",
    )

    args = parser.parse_args()
    repo_root = Path(args.repo_root)

    rows = load_dorks(repo_root, args.source)

    if args.search:
        needle = args.search.lower()
        rows = [
            r
            for r in rows
            if needle in json.dumps(r, ensure_ascii=False).lower()
        ]

    render(rows, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

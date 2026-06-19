#!/usr/bin/env python3
"""Validate the GitHub-based Investment Brain memory layer.

Checks:
1. Markdown files under Brain have YAML-like frontmatter.
2. final_action values are from the allowed set when present.
3. status values are from the allowed set when they are theme lifecycle statuses.
4. last_updated exists.
5. stale_after exists.
6. Index wikilinks point to existing Brain note stems.
7. No broken [[wikilink]] references.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRAIN = ROOT / "Brain"

ALLOWED_FINAL_ACTIONS = {
    "Buy Candidate",
    "Probe Candidate",
    "Watch",
    "Wait",
    "Avoid",
    "Reduce Risk",
    "",
}

ALLOWED_STATUSES = {
    "Stage 0 Plausible Idea",
    "Stage 1 Early Evidence",
    "Stage 2 Commercial Signal",
    "Stage 3 Financial Validation",
    "Existing Leader",
    "Developing Theme",
    "Early Reversal",
    "Strong Continuation",
    "Late / Overheated",
    "Weak Bounce",
    "Defensive Rotation",
    "Initial Pass",
    "Active",
    "",
}

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.startswith("  - ") or line.startswith("-"):
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def note_stems(md_files: list[Path]) -> set[str]:
    stems = {p.stem for p in md_files}
    for p in md_files:
        fm = parse_frontmatter(p.read_text(encoding="utf-8"))
        title = fm.get("title", "").strip()
        ticker = fm.get("ticker", "").strip()
        if title:
            stems.add(title)
        if ticker:
            stems.add(ticker)
    return stems


def main() -> int:
    if not BRAIN.exists():
        print("ERROR: Brain directory does not exist")
        return 1

    md_files = sorted(BRAIN.rglob("*.md"))
    if not md_files:
        print("ERROR: no Brain markdown files found")
        return 1

    known = note_stems(md_files)
    errors: list[str] = []

    for path in md_files:
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if not fm:
            errors.append(f"{rel}: missing YAML frontmatter")
            continue

        if "last_updated" not in fm:
            errors.append(f"{rel}: missing last_updated")
        if "stale_after" not in fm:
            errors.append(f"{rel}: missing stale_after")

        action = fm.get("final_action", "")
        if action not in ALLOWED_FINAL_ACTIONS:
            errors.append(f"{rel}: invalid final_action: {action}")

        status = fm.get("status", "")
        if status and status not in ALLOWED_STATUSES:
            errors.append(f"{rel}: invalid status: {status}")

        for link in WIKILINK_RE.findall(text):
            if link not in known:
                errors.append(f"{rel}: broken wikilink [[{link}]]")

    if errors:
        print("Brain validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"Validated {len(md_files)} Brain markdown files successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

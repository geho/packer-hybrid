#!/usr/bin/env python3
"""
Verify that every .codex/prompts/*.md file contains YAML front matter and an OPENSPEC guardrails block.
"""

from __future__ import annotations

import sys
from pathlib import Path


def check_prompt(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        errors.append("missing YAML front matter")
        return [f"{path}: {err}" for err in errors]

    end_idx = text.find("\n---", 3)
    if end_idx == -1:
        errors.append("front matter not terminated with ---")
        end_idx = 0
    front_matter = text[0 : end_idx + 4]

    if "description:" not in front_matter:
        errors.append("front matter missing description key")
    if "argument-hint:" not in front_matter:
        errors.append("front matter missing argument-hint key")

    if "<!-- OPENSPEC:START -->" not in text or "<!-- OPENSPEC:END -->" not in text:
        errors.append("missing OPENSPEC guardrails block")

    return [f"{path}: {err}" for err in errors]


def main() -> int:
    base = Path(".codex/prompts")
    if not base.exists():
        print("No .codex/prompts directory found", file=sys.stderr)
        return 1

    failures: list[str] = []
    for path in sorted(base.glob("*.md")):
        failures.extend(check_prompt(path))

    if failures:
        for line in failures:
            print(line, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

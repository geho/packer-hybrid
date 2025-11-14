#!/usr/bin/env python3
"""Migrate pending project notes into a change's tasks.md."""
import argparse
import sys
from pathlib import Path


def load_sections(text: str):
    if "## Pending Questions" not in text or "## Decisions" not in text:
        raise ValueError("project-notes.md must contain '## Pending Questions' and '## Decisions / Follow-ups' sections")
    before, rest = text.split("## Pending Questions", 1)
    pending_block, decisions_block = rest.split("## Decisions / Follow-ups", 1)
    return before, pending_block.strip("\n"), decisions_block.rstrip()


def write_project_notes(path: Path, header: str, pending_block: str, decisions_block: str):
    pending_text = pending_block or "- [ ] Describe the unresolved question or risk here."
    new_text = (
        f"{header}## Pending Questions\n{pending_text}\n\n"
        f"## Decisions / Follow-ups\n{decisions_block if decisions_block else '- Capture answers or follow-up actions once resolved; run `tools/migrate-notes.sh <change-id>` once a change is scaffolded so pending items move into `openspec/changes/<change-id>/tasks.md`.'}\n"
    )
    path.write_text(new_text)


def ensure_tasks_structure(text: str):
    lines = text.splitlines()
    if "## Proposal Clarifications" not in text:
        lines = ["## Proposal Clarifications", ""] + lines
    if "## Implementation Tasks" not in text:
        if lines and lines[-1] != "":
            lines.append("")
        lines.append("## Implementation Tasks")
        lines.append("")
    return lines


def insert_pending(lines, items):
    idx = 0
    while idx < len(lines):
        if lines[idx].strip() == "## Proposal Clarifications":
            idx += 1
            break
        idx += 1
    while idx < len(lines) and not (lines[idx].startswith("## ") and lines[idx].strip() != "## Proposal Clarifications"):
        idx += 1
    insert_idx = idx
    if insert_idx >= len(lines) or lines[insert_idx].strip() != "":
        lines.insert(insert_idx, "")
        insert_idx += 1
    for item in items:
        lines.insert(insert_idx, item)
        insert_idx += 1
    if insert_idx >= len(lines) or lines[insert_idx].strip() != "":
        lines.insert(insert_idx, "")
    return lines


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("change_id", help="OpenSpec change ID (folder under openspec/changes)")
    parser.add_argument("--repo-root", default=".", help="Path to repo root (defaults to current dir)")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    notes_path = repo_root / "openspec" / "project-notes.md"
    change_dir = repo_root / "openspec" / "changes" / args.change_id
    tasks_path = change_dir / "tasks.md"

    if not notes_path.exists():
        sys.exit(f"Missing project notes file: {notes_path}")
    if not change_dir.exists():
        sys.exit(f"Change folder does not exist: {change_dir}")

    notes_text = notes_path.read_text()
    try:
        header, pending_block, decisions_block = load_sections(notes_text)
    except ValueError as exc:
        sys.exit(str(exc))

    pending_lines = [line.strip() for line in pending_block.splitlines() if line.strip()]
    items_to_move = [line for line in pending_lines if line.startswith("- [") and "Describe the unresolved question" not in line]
    if not items_to_move:
        print("No pending questions to migrate.")
        return

    remaining_lines = [line for line in pending_lines if line not in items_to_move]
    write_project_notes(notes_path, header, "\n".join(remaining_lines), decisions_block)

    if tasks_path.exists():
        tasks_lines = ensure_tasks_structure(tasks_path.read_text())
    else:
        tasks_lines = ensure_tasks_structure("## Proposal Clarifications\n\n## Implementation Tasks\n\n")
    tasks_lines = insert_pending(tasks_lines, items_to_move)
    tasks_text = "\n".join(tasks_lines).rstrip() + "\n"
    tasks_path.parent.mkdir(parents=True, exist_ok=True)
    tasks_path.write_text(tasks_text)
    print(f"Migrated {len(items_to_move)} pending question(s) to {tasks_path}")

if __name__ == "__main__":
    main()

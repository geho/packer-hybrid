---
description: Prepare git changes for commit, ensuring alignment with the active OpenSpec change.
argument-hint: change-id (plus optional summary of current edits)
---

$ARGUMENTS

<!-- OPENSPEC:START -->

**Guardrails**

- Favor straightforward, minimal implementations first and add complexity only when it is requested or clearly required.
- Keep changes tightly scoped to the requested outcome.
- Review `@/AGENTS.md`, `@/agents/startup.md`, `@/openspec/AGENTS.md`, and `@/assessments/AGENTS.md` before staging so commit prep honors OpenSpec plus assessment requirements.
- Use this prompt after completing implementation chunks (post-`openspec-implement`) and especially after `openspec-archive` when the change is fully ready to commit.
- You may re-enter the prompt mid-implementation to stage incremental work, but always reconfirm scope and validation status.
- Keep commits scoped to the targeted change ID; do **not** mix unrelated fixes.
- Confirm working tree cleanliness before staging. If unrelated files are dirty, call it out and wait for direction.

**Workflow**

1. **Status Review (Re-entrant)**
   - Run `git status -sb` and list modified/untracked files, grouping them by relevance to the current change.
   - Highlight any unexpected files and ask whether to include them or revert.
2. **Validation Snapshot**
   - Ensure required checks (tests, lint, `openspec validate <id> --strict`) have passed since the last modification. Record command outputs or summarize logs.
   - Confirm documentation/diagram updates required by `openspec/project.md` or `tasks.md` are present and ready to stage alongside code/spec changes.
3. **Staging Plan**
   - Propose logical staging chunks (e.g., spec updates, implementation code, tests) tied to the change ID.
   - Stage files (`git add ...`) once the developer confirms the plan, or instruct them explicitly if manual staging is preferred.
4. **Commit Guidance**
   - Suggest a commit message template referencing the OpenSpec change ID (e.g., `feat(change-id): short summary`).
   - Confirm whether multiple commits are needed (spec vs code) and outline each message.
5. **Final Check**
   - Re-run `git status -sb` to confirm only staged files remain.
   - If anything is still unstaged or unexpected, document it and wait for clarification before proceeding.
   <!-- OPENSPEC:END -->

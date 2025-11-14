---
description: Continue implementing an approved OpenSpec change between the apply and archive phases.
argument-hint: change-id (plus optional progress summary)
---

$ARGUMENTS

<!-- OPENSPEC:START -->

**Guardrails**

- Favor straightforward, minimal implementations first and add complexity only when it is requested or clearly required.
- Keep changes tightly scoped to the requested outcome.
- Review `@/AGENTS.md`, `@/agents/startup.md`, `@/openspec/AGENTS.md`, and `@/assessments/AGENTS.md` before resuming work so coding style, assessment handovers, and OpenSpec workflow rules stay in sync.
- Confirm the change ID refers to an approved proposal (from `openspec/changes/<id>/`) and do **not** invent new scope without updating specs/proposals first.
- Keep edits tightly scoped to tasks listed in `changes/<id>/tasks.md`; if new work emerges, loop back to the proposal owner before proceeding.
- Treat this prompt as re-entrant: when you return mid-implementation, restate completed tasks, pending items, and blockers, and verify the checklist remains accurate.
- Ask clarifying questions whenever requirements, dependencies, or acceptance criteria are unclear.
- Validate frequently (`openspec validate <id> --strict`, project tests, linters) and capture results before moving on.
- Ensure `tasks.md` exists and starts with “## Proposal Clarifications” followed by “## Implementation Tasks.” If the change folder hasn’t been scaffolded, migrate outstanding notes from `openspec/project-notes.md` after creating the change (run `tools/migrate-notes.sh <change-id>`), and if headings are missing add them (with placeholder checkboxes) before categorizing work.
- If the change originated from an assessment, verify `proposal.md` cites the assessment reference and the corresponding `assessments/<folder>/summary.md` row lists this change ID/status before coding.

**Workflow**

1. **Change Verification**
   - Confirm the provided change ID exists, is approved, and not yet archived (via `openspec list`, `openspec show <id>`, or directory inspection).
   - Summarize proposal highlights (purpose, impacted capabilities) and cite any relevant specs before coding.
2. **Task Sync**
   - Read `changes/<id>/tasks.md` (migrating any remaining notes from `openspec/project-notes.md` first) and categorize each checkbox as done, in progress, or pending. If assessments triggered this change, confirm the relevant assessment `summary.md` entry has been updated to “implementation in progress.”
   - Keep “Proposal Clarifications” (spec questions) and “Implementation Tasks” separated; if an implementation blocker belongs in the clarification section, pause coding and switch to the refinement prompt.
3. **Implementation Loop**
   - Pick the next pending task, document the planned edits/files, and perform the minimal set of changes needed.
   - Run targeted validation/tests immediately after each chunk and record outcomes (pass/fail, logs, artifacts).
   - Update `tasks.md` statuses (and any related notes) only after confirming the work is finished and verified.
4. **Status Reporting**
   - After each loop, summarize progress (completed tasks, new findings, open risks) so the next session can resume smoothly.
   - Highlight unresolved issues or questions using `⚠️` plus a short explanation.
5. **Pre-Archive Readiness Check**
   - When the “Implementation Tasks” section is fully checked off, ensure `openspec validate <id> --strict` passes, specs/tests are updated, and there are no pending items in “Proposal Clarifications.”
   - If everything is green, hand off to the `openspec-archive` prompt (or equivalent instructions) to move the change into archive.

**Reference Tips**

- Use `openspec show <id> --json --deltas-only` if you need to re-check requirements while coding.
- `rg`, `ls`, or targeted file reads help you keep edits grounded in current implementation.
- Keep commit-sized changesets; note any large refactors so reviewers know what changed and why.
<!-- OPENSPEC:END -->

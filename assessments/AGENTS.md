# Assessment AGENTS

These instructions apply to AI assistants when performing assessment workflows (between or alongside OpenSpec changes).

## Purpose
- Run structured, read-only reviews to uncover discrepancies between specs, project policies, documentation, and implementation.
- Capture all findings in assessment folders (`assessments/<date-scope>/`) before converting them into OpenSpec change proposals.

## Required Reading
- `@/agents/startup.md`
- `@/openspec/AGENTS.md`
- `@/assessments/.template/README.md`

## Workflow Overview
1. **Initialization**: `/prompts:assessment-init <scope>` – create a new folder, copy templates, define plan/checklist.
2. **Specs vs Policies**: `/prompts:assessment-specs <folder>` – log findings comparing specs, `openspec/project.md`, and policies.
3. **Specs vs Documentation**: `/prompts:assessment-docs <folder>` – cross-check README/diagrams vs specs.
4. **Specs vs Implementation**: `/prompts:assessment-code <folder>` – sample code/tests to verify behavior.
5. **Summary & Handoff**: `/prompts:assessment-summary <folder>` – consolidate findings, map them to future OpenSpec change IDs.

## File Structure
Each assessment folder should include:
- `plan.md` – scope, success criteria, checklist.
- `notes.md` – running observations/tasks.
- `specs-findings.md`, `docs-findings.md`, `code-findings.md` – structured tables.
- `summary.md` – top findings, proposed changes, next steps.

## Guardrails
- Assessments are read-only: never edit specs, docs, or code directly during these prompts.
- Reference files with paths/line numbers (e.g., `specs/payments/spec.md:42`).
- If unresolved questions precede a change ID, log them in `openspec/project-notes.md` and migrate them once a change exists (`tools/migrate-notes.sh <change-id>`).
- Every assessment finding that requires remediation must be converted into one or more OpenSpec change proposals.

## Handoff to OpenSpec
- For every finding that needs remediation, add a row to `summary.md`'s “Proposed Changes” table with: finding reference, suggested change ID, and the exact slash command to run (`/prompts:openspec-proposal "..."` including the assessment reference).
- Do not mark the assessment complete until each finding row has a status (`proposal created`, `implementation in progress`, etc.) and a change folder path.
- After scaffolding a change, run `tools/migrate-notes.sh <change-id>` so pending questions leave `openspec/project-notes.md` and land in `openspec/changes/<change-id>/tasks.md` under “Proposal Clarifications.”
- Inside the new proposal (`proposal.md`, `tasks.md`), cite the assessment reference (e.g., `assessments/2025-Q1/specs-findings#3`) so refinement/implementation prompts can verify traceability.
- Update `summary.md` whenever the change advances (proposal created, implementation, archived) to maintain a bidirectional link between assessment findings and OpenSpec workflow.

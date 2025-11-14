---
description: Cross-check specs against project policies and record findings.
argument-hint: assessment folder path (e.g., assessments/2025-Q1)
---

$ARGUMENTS

<!-- OPENSPEC:START -->

**Guardrails**

- Review `@/AGENTS.md`, `@/agents/startup.md`, `@/openspec/AGENTS.md`, and `@/assessments/AGENTS.md` so you apply consistent policies and handover rules.
- Work read-only; do not edit specs/policies directly during assessment.
- Reference exact files/lines (e.g., `openspec/specs/auth/spec.md:42`) in findings tables.
- Log every finding in `specs-findings.md` and summarize in `notes.md`.

**Workflow**

1. Review `plan.md` to confirm scope.
2. Compare relevant specs with `openspec/project.md` and policies under `agents/policies/` for consistency, duplication, deviations, ambiguity, and completeness.
3. For each issue:
   - Add a row to `specs-findings.md` (severity, source spec/policy, summary, proposed action).
   - Add or update entries in `notes.md` (unchecked) referencing the finding row.
4. Highlight gaps requiring future OpenSpec changes and mark them for the summary phase.
<!-- OPENSPEC:END -->

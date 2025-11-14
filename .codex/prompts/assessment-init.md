---
description: Initialize an assessment run capturing scope and checklist.
argument-hint: short scope description (e.g., "2025-Q1 cross-check")
---

$ARGUMENTS

<!-- OPENSPEC:START -->

**Guardrails**

- Review `@/AGENTS.md`, `@/agents/startup.md`, `@/openspec/AGENTS.md`, and `@/assessments/AGENTS.md` before starting; assessments are read-only until proposals are created.
- Do not modify specs, code, or policies during this prompt—only scaffold assessment files.
- Create a unique folder under `assessments/<date-scope>/` using the provided scope argument.

**Workflow**

1. Confirm scope, timeframe, and target capabilities with the requester.
2. Copy templates from `assessments/.template/` into the new folder (`plan.md`, `notes.md`, `specs-findings.md`, `docs-findings.md`, `code-findings.md`, `summary.md`).
3. Populate `plan.md` with scope details, success criteria, and checklist items.
4. Record any immediate known issues in `notes.md` as unchecked items.
5. Share the folder path and await the next assessment prompt.
<!-- OPENSPEC:END -->

---
description: Cross-check specs against implementation artifacts.
argument-hint: assessment folder path (e.g., assessments/2025-Q1)
---

$ARGUMENTS

<!-- OPENSPEC:START -->

**Guardrails**

- Review `@/AGENTS.md`, `@/agents/startup.md`, `@/openspec/AGENTS.md`, and `@/assessments/AGENTS.md` before inspecting code so findings line up with policies and handover requirements.
- Read files/tests/services as needed but do not modify code.
- When referencing code, include file paths and line numbers.

**Workflow**

1. Review `plan.md` and targeted capabilities.
2. Sample relevant code/tests to verify behavior matches specs:
   - Look for missing scenarios, inconsistent validation, ambiguous behavior.
3. Record each discrepancy in `code-findings.md` with severity, spec reference, code reference, and a proposed action.
4. Add notes/tasks in `notes.md` pointing to potential OpenSpec changes.
<!-- OPENSPEC:END -->

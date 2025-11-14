---
description: Consolidate assessment findings and map them to OpenSpec changes.
argument-hint: assessment folder path (e.g., assessments/2025-Q1)
---

$ARGUMENTS

<!-- OPENSPEC:START -->

**Guardrails**

- Review `@/AGENTS.md`, `@/agents/startup.md`, `@/openspec/AGENTS.md`, and `@/assessments/AGENTS.md` so the handoff follows documented policy.
- Summarize findings only; do not edit specs/implementation.
- Clearly indicate which findings require formal OpenSpec proposals and capture explicit slash commands for launching them.

**Workflow**

1. Review `specs-findings.md`, `docs-findings.md`, `code-findings.md`, and `notes.md`.
2. De-duplicate and rank findings by severity; capture them in `summary.md` (Top Findings, Proposed Changes table).
3. For each finding needing remediation, populate the table with:
   - Finding reference (e.g., `specs#3`)
   - Suggested change ID or placeholder
   - Exact `/prompts:openspec-proposal "..."` command including assessment reference, plus current status.
4. Update `plan.md` and `notes.md` checklists; ensure no finding remains without an assigned change ID/command. If any are deferred, document why.
5. Hand off summary and recommended change IDs to stakeholders, noting which change folders must be created next.
<!-- OPENSPEC:END -->

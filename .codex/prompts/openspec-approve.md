---
description: Facilitate stakeholder approval for an OpenSpec proposal before implementation begins.
argument-hint: change-id (plus optional summary of outstanding concerns)
---

$ARGUMENTS

<!-- OPENSPEC:START -->

**Guardrails**

- Favor straightforward, minimal implementations first and add complexity only when it is requested or clearly required.
- Keep changes tightly scoped to the requested outcome.
- Review `@/AGENTS.md`, `@/agents/startup.md`, `@/openspec/AGENTS.md`, and `@/assessments/AGENTS.md` (plus the canonical OpenSpec prompts) so approval conversations stay within scope and respect assessment handovers.
- Confirm the change folder (`openspec/changes/<id>/`) exists, the proposal is fully drafted, and `openspec validate <id> --strict` passes before seeking approvals.
- Treat approvals as part of the spec cycle—do **not** start implementation or edit production code in this prompt.
- Capture approvals, rejections, or requested changes verbatim and note the responsible stakeholder.

**Workflow**

1. **Change Verification**
   - Ensure `proposal.md`, `tasks.md`, and spec deltas exist and summarize the intent, impacted capabilities, and validation status.
2. **Approval Matrix**
   - Identify required approvers (e.g., product owner, tech lead, security reviewer, spec owner). If unclear, ask the developer to confirm the stakeholders.
3. **Clarification Loop**
   - For each pending approver, restate the proposal summary and unresolved questions, then capture their explicit approval or requested changes.
   - If a stakeholder asks for modifications, loop back through the refine prompt to update files before re-approaching them.
4. **Decision Log**
   - Record the outcome per stakeholder (`Approved`, `Changes Requested`, `Blocked`, `Pending`) along with any notes or follow-up tasks.
5. **Hand-off**
   - Once all required approvals are marked `Approved`, instruct the user to proceed with `openspec-apply` (or `openspec-implement`) for implementation.
   - If approvals are incomplete, summarize blockers and next steps; do not advance to implementation until resolved.

**Reference Tips**

- Use `openspec show <id> --json --deltas-only` for quick summaries.
- Keep `tasks.md` in sync with any commitments made during the approval phase.
<!-- OPENSPEC:END -->

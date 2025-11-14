---
description: Clarify and refine an existing OpenSpec proposal before implementation begins.
argument-hint: change-id (plus optional summary of open questions)
---

$ARGUMENTS

<!-- OPENSPEC:START -->

**Guardrails**

- Favor straightforward, minimal implementations first and add complexity only when it is requested or clearly required.
- Keep changes tightly scoped to the requested outcome.
- Review `@/AGENTS.md`, `@/agents/startup.md`, `@/openspec/AGENTS.md`, and `@/assessments/AGENTS.md` so every clarification stays aligned with project policies, OpenSpec conventions, and assessment handovers.
- Confirm the referenced change already exists under `openspec/changes/<id>/`; if not, stop and run the proposal prompt first.
- Treat this prompt as re-entrant: on each pass, restate the current proposal status, unresolved questions, and reviewer feedback before asking for new input.
- Keep scope tied to the approved intent. If new features emerge, note them and suggest creating a separate change ID or updating the spec explicitly.
- Do **not** start implementation work; focus on clarifying requirements, refining specs, updating `proposal.md`, `tasks.md`, `design.md`, and spec deltas.
- Ask clarifying questions whenever acceptance criteria, scenarios, or impacts are unclear; document assumptions and wait for confirmation.
- Log every unresolved question or risk in `openspec/changes/<id>/tasks.md` as an unchecked item so it persists between iterations, and update the entry when resolved.
- Maintain a dedicated “Proposal Clarifications” section in `tasks.md` for refinement items so they stay separate from implementation tasks.
- If the change folder is missing (or `tasks.md` hasn’t been scaffolded yet), pause and run the proposal prompt first. Migrate any outstanding notes from `openspec/project-notes.md` into the new `tasks.md` via `tools/migrate-notes.sh <change-id>` before continuing.
- If `tasks.md` exists but is missing the “Proposal Clarifications” heading (with an empty checklist) or the “Implementation Tasks” heading, insert them before proceeding.
- When the proposal originates from an assessment, confirm `proposal.md` (and `summary.md` in the corresponding `assessments/<id>/` folder) reference the same finding ID before editing tasks/specs.

**Workflow**

1. **Change Verification**
   - Check that `openspec/changes/<id>/proposal.md` (and related files) exist.
   - Summarize the proposal’s purpose, affected capabilities, and current validation status (`openspec validate <id> --strict`).
2. **Feedback Inventory**
   - Read existing reviewer comments, TODOs inside the proposal, unresolved `tasks.md` notes (especially “Proposal Clarifications” + documentation items), and any entries in `openspec/project-notes.md` waiting to be migrated (use `tools/migrate-notes.sh <change-id>` if needed). If the proposal was triggered by an assessment, cross-check `assessments/<folder>/summary.md` to ensure the finding is marked as “proposal created” and that `proposal.md` cites the same reference.
   - Build a list of open questions grouped by topic (requirements, scenarios, design, scope) and capture them as unchecked tasks inside the “Proposal Clarifications” section of `openspec/changes/<id>/tasks.md`, moving items out of `openspec/project-notes.md` as soon as the change exists.
3. **Clarification Loop**
   - Present each open question to the developer/stakeholders, restating current understanding and asking for missing details.
   - Capture answers directly into the relevant files only after confirmation; otherwise keep them as notes.
   - For each refinement, run best-practice checks tied to the proposal’s domain (see “Domain Hints” below) and flag potential risks (`⚠️`) when conflicts arise.
4. **Spec & Task Updates**
   - Once clarifications are approved, update `proposal.md`, `design.md`, `tasks.md`, and `specs/` deltas to reflect the agreed changes.
   - Add or update tasks for documentation, diagrams, or structural adjustments to keep `README`/architecture references aligned with conventions.
   - Re-run `openspec validate <id> --strict` and ensure all warnings/errors are resolved.
5. **Ready-for-Implementation Check**
   - Confirm every item under “Proposal Clarifications” is either resolved or explicitly deferred, `tasks.md` reflects actionable implementation steps, and reviewers agree the proposal is ready.
   - Hand off to the implementation prompt (`openspec-apply` / `openspec-implement`) only after explicit approval. If implementation later surfaces new spec questions, add them back to the “Proposal Clarifications” section and switch to this prompt again.

## Domain Hints (use what applies)

- **Web/UI changes**: verify user flows, accessibility requirements, performance budgets, and state management implications.
- **Auth/Security**: double-check threat scenarios, MFA flows, audit logging, secret storage/rotation, and compliance requirements.
- **Data/Analytics**: clarify schema changes, migration strategy, SLAs, and data retention policies.
- **Automation/CLI**: specify command UX, flag options, exit codes, plugin compatibility, and cross-platform behavior.
- **Infrastructure/Platform**: call out deployment impacts, rollout strategy, observability hooks, and rollback plans.
- **API/Backend Services**: confirm endpoint contracts (REST/GraphQL/OpenAPI), versioning/backward compatibility, rate limits, idempotency rules, and error semantics.
- **DevOps/Tooling**: outline environment automation scope, infrastructure-as-code standards, secret management, rollout/rollback expectations, and observability requirements.

**Alignment & Approvals**

- Flag any inconsistencies with existing specs (use `openspec show <spec>` for reference) and request direction from stakeholders.
- Document all clarifications in the change folder; wait for final approval before moving on to implementation prompts.
<!-- OPENSPEC:END -->

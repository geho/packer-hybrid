# Proposal: Execute spec remediations across all capabilities

## Why

The latest assessment identified fresh remediation items for every capability spec (CLI, hybridcore umbrella/modules, provisioning, security, templates, governance, meta). To keep policies enforced, we must execute those remediations: turn each draft item into spec/diagram/test updates, keep Open Issues in sync, and archive the resulting changes. This proposal scopes the execution workflow so `/prompts:openspec-apply` can implement the backlog chunk by chunk.

## Scope

- Drafts: every `docs/spec-remediations/<spec>-remediations.md` file.
- Specs: cli, governance, hybridcore, hybridcore-config, hybridcore-logs, hybridcore-packer, hybridcore-provisioners, hybridcore-sources, hybridcore-state, hybridcore-templates, meta, provisioning, security, templates.

## Plan

1. Pre-flight: run `openspec list`, `openspec list --specs`, review `openspec/project.md`, and read each remediation draft to confirm pending gaps.
2. For each draft, choose a verb-led change ID (e.g., `remediate-cli-<date>`), scaffold proposal/tasks/spec deltas, and present the `/prompts:openspec-proposal …` command for the operator to run.
3. After proposals are approved, present `/prompts:openspec-apply <change-id>` when implementation is ready, ensuring spec deltas update requirements, diagrams (per governance), and tests.
4. Once a remediation change passes validation, update the corresponding spec’s `## Open Issues`, move items from Open to Closed in the draft, and present `/prompts:openspec-archive <change-id>` for execution.
5. Repeat until all drafts either move their items to Closed Topics or spawn fresh follow-up proposals.

## Deliverables

- A tracked checklist (tasks.md) covering each remediation draft.
- Spec deltas (if needed) describing cross-cutting updates, e.g., meta workflow guidance.
- `openspec validate remediate-all-specs-2025-11 --strict` succeeds.

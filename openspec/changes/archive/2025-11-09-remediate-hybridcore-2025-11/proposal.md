# Proposal: Remediate hybridcore umbrella spec

## Why

`docs/spec-remediations/hybridcore-remediations.md` still lists unresolved items: the Module Registry table is missing, readers lack a summary matrix of module Open Issues, requirements duplicate module-level detail instead of referencing sub-specs, there is no severity/escalation rubric for cross-module issues, and existing diagrams ignore the new governance/meta policies. We need to update the hybridcore umbrella spec and supporting docs so module ownership, escalation paths, and governance touchpoints are explicit.

## Scope

- Spec: `openspec/specs/hybridcore/spec.md`.
- Docs: `docs/spec-remediations/hybridcore-remediations.md`, diagrams under `openspec/specs/hybridcore/`.

## What Changes

1. Reintroduce the Module Registry table with module name, spec path, implementation status, and remediation doc link; ensure the requirement references it.
2. Add a matrix summarizing each module’s `## Open Issues` pointer, outstanding topics, and severity.
3. Replace duplicated module requirements with references into the module specs/remediation drafts.
4. Define a severity/escalation rubric (critical/high/medium) for cross-module issues and describe expected response times.
5. Update the orchestration/sequence diagrams to highlight governance/meta dependencies (diagram verification, assessment cadence).

## Deliverables

- Updated spec sections (registry requirement, new matrix requirement, escalation guidance, updated diagrams).
- `docs/spec-remediations/hybridcore-remediations.md` reflecting the closed topics.
- `openspec validate remediate-hybridcore-2025-11 --strict`.

# Proposal: Remediate hybridcore-sources spec

## Why

`docs/spec-remediations/hybridcore-sources-remediations.md` lists five open topics: override approvals alignment with governance, persistent storage of overrides/mirrors, tying metadata to security scanning diagnostics, missing resume/repair workflows, and override audit retention. The spec needs these details to uphold governance, security, and state integration guarantees.

## Scope

- Spec: `openspec/specs/hybridcore-sources/spec.md` plus new diagrams under `openspec/specs/hybridcore-sources/`.
- Docs: `docs/spec-remediations/hybridcore-sources-remediations.md`, references into security/governance/state specs, and CLI diagnostics flows.

## What Changes

1. Embed governance-approved override policy and scenarios for manual overrides.
2. Require state tracking of override approvals/mirror inventories with validation/tests.
3. Tie scanning metadata fields to the security spec and `diag` outputs.
4. Document resume/repair workflows, state markers, and test expectations.
5. Define audit/retention requirements referencing security + state specs, plus diagrams showing override lifecycle.

## Deliverables

- Updated hybridcore-sources spec requirements + diagrams.
- Remediation doc updated (open topics moved to Closed).
- `openspec validate remediate-hybridcore-sources-2025-11 --strict` and Prettier on touched Markdown.

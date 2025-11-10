# Proposal: Remediate hybridcore-packer spec

## Why

`docs/spec-remediations/hybridcore-packer-remediations.md` highlights unresolved needs: per-builder incremental hash manifests (for drift detection integrity), a documented result schema for packer orchestration (CLI/automation integration), explicit exit-code/retry mapping, and guidance on how packer logs/diagnostics feed into the security retention policy. The current spec does not cover these details, so we need to update it before implementing the backlog.

## Scope

- Spec: `openspec/specs/hybridcore-packer/spec.md` (requirements and referenced docs/tests).
- Docs: `docs/spec-remediations/hybridcore-packer-remediations.md`, artifact/hash manifest references.

## What Changes

1. Add a requirement covering incremental per-builder hash manifests with CI examples.
2. Document the structured result schema (fields, exit codes, retry classification) so CLI/automation can rely on it.
3. Add an exit-code/retry policy table clarifying when automatic retries are allowed.
4. Describe how packer logs/diagnostics feed into the security retention policy (e.g., writing summaries to `state/` for security/diag integration).

## Deliverables

- Updated spec requirements with scenarios.
- Updated remediation doc moving items to Closed.
- `openspec validate remediate-hybridcore-packer-2025-11 --strict`.

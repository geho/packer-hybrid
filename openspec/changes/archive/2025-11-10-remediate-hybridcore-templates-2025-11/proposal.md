# Proposal: Remediate hybridcore-templates spec

## Why

`docs/spec-remediations/hybridcore-templates-remediations.md` lists five open topics around variant taxonomy, checksum caches, state sync, provisioner metadata alignment, and diagram governance. Templates drift from provisioning/state without those requirements.

## Scope

- Spec: `openspec/specs/hybridcore-templates/spec.md` + new diagrams under `openspec/specs/hybridcore-templates/`.
- Docs: `docs/spec-remediations/hybridcore-templates-remediations.md`, `docs/hybridcore-architecture.md` references.

## What Changes

1. Define canonical variant naming/layout and validation scenarios.
2. Document checksum cache storage/invalidation under `state/templates/cache/` with CLI parity/CI coverage.
3. Describe builder manifest ↔ state sync contract, with sequence diagram/tests.
4. Align provisioner metadata with provisioning spec, adding drift validation.
5. Relocate onboarding diagrams into the spec directory and update docs per governance.

## Deliverables

- Spec updates + diagrams.
- Remediation doc updated (open topics closed).
- `openspec validate remediate-hybridcore-templates-2025-11 --strict` and Prettier on touched Markdown.

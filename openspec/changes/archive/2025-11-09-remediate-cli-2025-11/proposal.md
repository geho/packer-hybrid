# Proposal: Execute CLI spec remediations

## Why

The latest assessment highlighted several unresolved gaps in the CLI spec and docs: diagnostics lack clear redaction/retention rules, `status/inspect` promise machine-readable output without a canonical schema, verification gates duplicate security requirements, command sections fail to cite module Open Issues, diagrams in docs drift from the spec versions, and `clean` omits retention boundaries. We need to tighten the CLI spec and supporting docs/tests so behaviour stays aligned with governance, security, and other hybridcore modules.

## Scope

- Spec: `openspec/specs/cli/spec.md`.
- Docs/tests: `docs/spec-remediations/cli-remediations.md`, `docs/wizard-ui.md`, CLI JSON schema fixtures/tests, `security` references.

## What Changes

1. **Diagnostics redaction/retention** – Update the Diagnostics requirement with explicit redaction hooks (linking to security spec), describe retention windows, and add tests verifying bundles scrub secrets.
2. **Status/Inspect schema** – Document the JSON schema/versioning requirements in the spec, add fixtures/tests referencing it, and expose machine-readable output fields.
3. **Verification gates de-duplication** – Replace the duplicated checklist with references to `specs/security/spec.md`, detailing how CLI enforces those gates (link to tests).
4. **Command alignment with hybridcore modules** – Each command section should cite the relevant `docs/spec-remediations/<module>-remediations.md` so outstanding module work is discoverable.
5. **Diagram/doc alignment** – Require wizard/command diagrams in the spec to be the source of truth, update docs to embed them, and add a regression test ensuring docs reference the spec diagrams.
6. **Clean scope retention** – Clarify which artifacts/logs/scans must be preserved despite `clean` operations and add tests proving compliance with security retention rules.

## Out of Scope

- Implementing remediation items for other specs (handled by sibling changes in `remediate-all-specs-2025-11`).
- CLI feature work beyond the listed remediation topics.

## Validation

- Updated spec/diagrams/tests as described above.
- `openspec validate remediate-cli-2025-11 --strict` passes.

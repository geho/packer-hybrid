# Proposal: Remediate hybridcore templates gaps from 2025-11 assessment

## Why

Assessment `assessments/2025-11-14-remediation-migration/summary.md` (finding `specs-findings#11`) left five open topics in `remediations/templates-remediations.md` covering:

1. OS image variant naming/layout/validation guidance.
2. Checksum cache storage/reuse/invalidation.
3. Builder manifest integration with `hybridcore.state` + CLI validation hooks.
4. Platform-specific script directory naming conventions and lint coverage.
5. Missing template diagrams inside `openspec/specs/templates/`.

Without these updates, contributors still rely on tribal knowledge and onboarding docs drift from the spec, causing inconsistent template structures and weaker validation.

## What Changes

- Define canonical variant naming + directory/layout expectations in `openspec/specs/templates/spec.md`, add supporting tables/diagrams, and reference them from the CLI/provisioning specs as needed.
- Document checksum cache ownership (paths, retention, invalidation) plus required CI hooks/tests to ensure caches refresh on manifest changes.
- Expand state integration requirements (templates ↔ `hybridcore.state`) with clear validation commands consumed by CLI `status/publish`.
- Add script-directory naming requirements (Linux vs Windows) and specify lint/tests to enforce them.
- Move the missing template diagrams into `openspec/specs/templates/` per governance and reference them from docs/spec.

## Scope

- Primary spec: `openspec/specs/templates/spec.md` (plus diagrams under `openspec/specs/templates/*.mmd`).
- Secondary references: `openspec/specs/cli/spec.md`, `openspec/specs/hybridcore-state/spec.md`, and `docs/wizard-ui.md` (if cross-links need updates); include only if the spec changes require new references.
- Tests: CLI/spec tests ensuring new references exist and lint/tests for script naming + checksum cache validations (extend existing unit tests or add new ones under `tests/specs/`).
- Assessment linkage: cite `assessments/2025-11-14-remediation-migration/remediations/templates-remediations.md` in proposal/tasks/spec.

Out of scope: provisioning logic changes unrelated to the listed open topics or new template features not mentioned in the assessment.

## Impact

- Clear guidance for template variants/caches/scripts/state integration documented in specs and enforced via tests.
- Governance compliance (diagrams stored under specs, references updated).
- Assessment finding `specs-findings#11` moves its open topics to “Closed” once the implementation finishes.

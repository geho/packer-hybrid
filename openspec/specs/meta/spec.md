# meta Specification

## Purpose

TBD - created by archiving change add-spec-assessment-remediation. Update Purpose after archive.
## Requirements
### Requirement: Spec Assessment Workflow

Assessments SHALL explicitly cover `cli`, every `hybridcore-*` module, `provisioning`, `security`, and `templates`, recording findings in the corresponding `assessments/2025-11-14-remediation-migration/remediations/<spec>-remediations.md` files.

#### Scenario: Multi-spec assessment scope

- **WHEN** the quarterly assessment runs
- **THEN** it MUST log deviations for each capability above, update their remediation drafts, and ensure the change tasks reflect the scope before `/prompts:openspec-apply` executes.

### Requirement: Spec Remediation Execution

Add guidance that remediation execution SHALL cover every `assessments/2025-11-14-remediation-migration/remediations/*.md` file in scope, presenting `/prompts:openspec-proposal|apply|archive` commands for operators to run, and tracking status in tasks.md until all drafts are closed or rolled into follow-up work.

#### Scenario: Operator-driven execution

- **WHEN** a remediation run starts
- **THEN** the change owner MUST list each draft, present the appropriate `/prompts:openspec-*` commands for the operator, and update the change checklist only after validation/archival complete.

### Requirement: Open Issues Tracking

The meta spec SHALL expose a `## Open Issues` section linking to `assessments/2025-11-14-remediation-migration/remediations/meta-remediations.md` so assessments/remediations remain discoverable at the repository-policy level.

#### Scenario: Meta remediations

- **WHEN** assessment gaps are logged for meta workflows
- **THEN** contributors MUST update `assessments/2025-11-14-remediation-migration/remediations/meta-remediations.md` and ensure the meta spec’s `## Open Issues` section references it until the work is complete.

### Requirement: Assessment Tracking

Assessments SHALL capture remediation findings under `assessments/<scope>/remediations/<spec>.md` (current scope: `assessments/2025-11-14-remediation-migration/`) so specs reference the new SoT instead of the retired docs.

#### Scenario: Findings migrate from `docs/spec-remediations` to `assessments/`

- **GIVEN** assessments now own remediation tracking
- **WHEN** documenting open issues or remediation history
- **THEN** specs MUST reference the latest `assessments/<scope>/remediations/<spec>.md` entries (currently `assessments/2025-11-14-remediation-migration/remediations/*.md`) instead of the retired `docs/spec-remediations/*.md` files.

## Open Issues

See `assessments/2025-11-14-remediation-migration/remediations/meta-remediations.md`.

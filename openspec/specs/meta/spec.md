# meta Specification

## Purpose

TBD - created by archiving change add-spec-assessment-remediation. Update Purpose after archive.
## Requirements
### Requirement: Spec Assessment Workflow

Assessments SHALL explicitly cover `cli`, every `hybridcore-*` module, `provisioning`, `security`, and `templates`, recording findings in the corresponding `docs/spec-remediations/<spec>-remediations.md` files.

#### Scenario: Multi-spec assessment scope

- **WHEN** the quarterly assessment runs
- **THEN** it MUST log deviations for each capability above, update their remediation drafts, and ensure the change tasks reflect the scope before `/prompts:openspec-apply` executes.

### Requirement: Spec Remediation Execution

Remediation workflow MUST list diagrams/tests touched and enforce documentation of those artifacts before archiving.

#### Scenario: Diagram/test reporting

- **WHEN** `/prompts:openspec-apply <change-id>` completes
- **THEN** the change description MUST call out any diagrams/tests updated (or explicitly say "none") before archiving.

### Requirement: Open Issues Tracking

The meta spec SHALL expose a `## Open Issues` section linking to `docs/spec-remediations/meta-remediations.md` so assessments/remediations remain discoverable at the repository-policy level.

#### Scenario: Meta remediations

- **WHEN** assessment gaps are logged for meta workflows
- **THEN** contributors MUST update `docs/spec-remediations/meta-remediations.md` and ensure the meta spec’s `## Open Issues` section references it until the work is complete.

## Open Issues

See `docs/spec-remediations/meta-remediations.md`.

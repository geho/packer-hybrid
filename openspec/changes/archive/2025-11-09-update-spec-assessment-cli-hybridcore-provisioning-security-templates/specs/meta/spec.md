## MODIFIED Requirements

### Requirement: Spec Assessment Workflow

The remediation workflow SHALL reference `docs/spec-remediations/<spec>-remediations.md` (template: `docs/spec-remediations/templates-spec-remediations.md`) instead of the removed `docs/drafts` files so the new drafts remain the source of truth.

#### Scenario: Remediation drafts

- **WHEN** assessments produce deviations
- **THEN** contributors SHALL update `docs/spec-remediations/<spec>-remediations.md` and link them from specs before implementation.

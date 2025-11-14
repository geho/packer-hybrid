## MODIFIED Requirements

### Requirement: Assessment Tracking

Assessments SHALL capture remediation findings under `assessments/<scope>/remediations/<spec>.md` (current scope: `assessments/2025-11-14-remediation-migration/`) so specs reference the new SoT instead of the retired docs.

#### Scenario: Findings migrate from `docs/spec-remediations` to `assessments/`

- **GIVEN** assessments now own remediation tracking
- **WHEN** documenting open issues or remediation history
- **THEN** specs MUST reference the latest `assessments/<scope>/remediations/<spec>.md` entries (currently `assessments/2025-11-14-remediation-migration/remediations/*.md`) instead of the retired `docs/spec-remediations/*.md` files.

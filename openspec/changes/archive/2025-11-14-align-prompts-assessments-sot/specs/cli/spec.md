## MODIFIED Requirements

### Requirement: CLI references assessments

CLI documentation (commands, diagnostics, open issues) SHALL point to the active assessment folder for remediation logs instead of the old `docs/spec-remediations` directory.

#### Scenario: Diagnostics link to assessment findings

- **WHEN** CLI documentation references remediation status
- **THEN** it SHALL cite the active assessment folder (starting with `assessments/2025-11-14-remediation-migration/remediations/*.md`) instead of the retired `docs/spec-remediations/*.md` path.

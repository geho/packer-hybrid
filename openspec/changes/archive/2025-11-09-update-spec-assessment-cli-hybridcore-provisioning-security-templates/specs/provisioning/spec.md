## ADDED Requirements

### Requirement: Open Issues Tracking

The provisioning spec SHALL keep a `## Open Issues` section pointing to `docs/spec-remediations/provisioning-remediations.md`. Assessments MUST summarize outstanding gaps per dimension in that doc and cross-reference it from the spec.

#### Scenario: Remediation linkage

- **WHEN** a spec assessment uncovers deviations for the provisioning spec
- **THEN** contributors SHALL update `docs/spec-remediations/provisioning-remediations.md` and refresh the spec's `## Open Issues` pointer before merging changes.

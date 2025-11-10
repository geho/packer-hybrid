## MODIFIED Requirements

### Requirement: Cross-Module Integrations & Regression Tests

The config spec SHALL reference the templates/state Open Issues (and their remediation drafts) so drift detection contracts stay synchronized.

#### Scenario: Drift linkage

- **WHEN** templates or state Open Issues change
- **THEN** the config spec SHALL reference the updated remediation drafts so operators can trace dependencies.

### Requirement: Manifest & State Integration

Rendered configs SHALL emit provenance metadata (hashes, overlay sources, secret indirection notes) and record the data alongside state to support audits.

#### Scenario: Provenance metadata

- **WHEN** configs render `.auto.pkrvars.hcl`
- **THEN** the manifest SHALL record file hashes, source overlays, and secret references; tests must verify these fields.

### Requirement: Config Pipeline Diagram

The spec SHALL include the Mermaid diagram showing discovery → schema validate → merge/render → state update, and docs MUST link back to it instead of duplicating.

#### Scenario: Diagram availability

- **WHEN** reviewers inspect the config pipeline
- **THEN** they SHALL use the spec-hosted diagram, and `docs/` MUST reference it instead of duplicating.

### Requirement: Schema Validation Severity

Schema validation SHALL define severity/exit-code mapping for warnings vs failures so CLI callers know how to react consistently.

#### Scenario: Severity mapping

- **WHEN** validation encounters warnings
- **THEN** it SHALL exit 0 with logged warnings; fatal errors SHALL exit non-zero and tests MUST cover both paths.

### Requirement: Provisioning Input Mapping

Config SHALL reference the provisioning spec/templates for input schemas instead of duplicating fields; a mapping table MUST link each config input to its provisioning source of truth.

#### Scenario: Reference over duplication

- **WHEN** config requirements mention provisioning inputs
- **THEN** they SHALL link to provisioning spec sections/templates rather than restate fields.

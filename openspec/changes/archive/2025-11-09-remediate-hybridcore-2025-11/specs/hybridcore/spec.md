## MODIFIED Requirements

### Requirement: Module Registry & Naming

The registry SHALL include a table listing each module’s name, spec path, implementation status, and remediation draft link so onboarding stays auditable.

#### Scenario: Registry visibility

- **WHEN** a new module is proposed or updated
- **THEN** the table SHALL record its status/spec/remediation link (and PR reference) before code merges.

### Requirement: Module Spec Hierarchy

The umbrella spec SHALL provide a matrix summarizing each module’s `## Open Issues` pointer, outstanding themes, and severity so readers do not jump between files blindly.

#### Scenario: Matrix upkeep

- **WHEN** module Open Issues change
- **THEN** the matrix SHALL be updated so umbrella readers see cross-module status at a glance.

### Requirement: Cross-Module Dependency Guidelines

Umbrella requirements MUST reference the authoritative module spec/remediation draft instead of duplicating module-level behaviour; cross-module guidance SHALL link to the relevant module documents.

#### Scenario: Avoid duplication

- **WHEN** the umbrella spec mentions a module’s behaviour
- **THEN** it SHALL link to the module spec/remediation draft rather than restating the requirement.

### Requirement: Escalation & Severity

Cross-module issues SHALL be assigned a severity (critical/high/medium) with documented response times (24h/3d/1 week respectively) and MUST reference governance/meta policies.

#### Scenario: Escalation rubric

- **WHEN** a critical cross-module issue is recorded
- **THEN** the release captain SHALL respond within 24h and update the remediation draft + matrix accordingly.

### Requirement: Packer-Hybrid Integration Diagram

The orchestration and sequence diagrams SHALL highlight governance/meta touchpoints (diagram verification, assessment cadence) and docs MUST link back to the spec diagrams to avoid drift.

#### Scenario: Diagram governance linkage

- **WHEN** governance/meta policies change
- **THEN** the diagrams SHALL show the touchpoints so contributors understand compliance flows.

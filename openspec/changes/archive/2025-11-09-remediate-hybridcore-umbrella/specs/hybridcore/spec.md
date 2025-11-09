## ADDED Requirements

### Requirement: Module Registry & Naming

`hybridcore` SHALL maintain the registry table of active/planned modules plus naming guidance; new modules MUST update the table before implementation.

#### Scenario: Registry update

- **WHEN** a `metrics` module is proposed
- **THEN** the table MUST gain a `hybridcore-metrics` entry with spec path/status before code lands.

### Requirement: Cross-Module Dependency Guidelines

Consumers SHALL call modules only via published APIs, and module specs MUST document inbound/outbound dependencies + Open Issues references.

#### Scenario: Dependency adherence

- **WHEN** the CLI needs template info during `build`
- **THEN** it MUST call `hybridcore.templates` via its API rather than reaching into internals.

### Requirement: Orchestration Flow

The new orchestration diagram (`specs/hybridcore/orchestration-flow.md`) SHALL accompany the spec and remain up to date.

#### Scenario: Diagram upkeep

- **WHEN** module flows change
- **THEN** the orchestration diagram MUST be updated and referenced from the spec.

## MODIFIED Requirements

### Requirement: Module Spec Hierarchy

Module specs SHALL link back to the umbrella spec and their `## Open Issues` (tracked in `docs/spec-remediations/<spec>-remediations.md`).

#### Scenario: Linking Open Issues

- **WHEN** a module resolves a remediation item
- **THEN** its spec MUST update `## Open Issues` and the umbrella spec remains the entry point.

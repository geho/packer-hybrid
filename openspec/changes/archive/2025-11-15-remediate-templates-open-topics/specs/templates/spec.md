## MODIFIED Requirements

### Requirement: Variant Naming & Layout

Template variants SHALL follow a canonical naming table (platform + os + variant suffix) and reside in the prescribed directory hierarchy so tooling can locate configs/tests deterministically.

#### Scenario: Canonical variant table

- **WHEN** contributors add or reference template variants
- **THEN** they MUST follow the canonical naming table (platform + OS + variant suffix) and store files in the prescribed directory hierarchy so automation/tests can locate them deterministically.

### Requirement: Checksum Cache Lifecycle

The template spec SHALL define where checksum caches live, how they are reused, and which events invalidate them so CI/drift detection stays accurate.

#### Scenario: Cache invalidation

- **WHEN** manifests, template files, or packer inputs change
- **THEN** the checksum cache SHALL outline storage paths, reuse rules, and invalidation triggers, and CI MUST bust caches when manifests differ from state.

### Requirement: Templates ↔ State Integration

Builder manifests SHALL describe how data flows into `hybridcore.state` and which CLI commands verify/update that data so operators understand failure modes.

#### Scenario: Builder manifest validation

- **WHEN** the CLI runs `status`, `validate`, or `publish`
- **THEN** the templates spec SHALL describe how builder manifests write into `hybridcore.state`, which commands verify those entries, and how failures are surfaced (exit codes/logging).

### Requirement: Script Directory Naming

Platform-specific script directories and filenames SHALL follow documented conventions enforced via lint/tests to avoid drift and duplication.

#### Scenario: Platform-specific scripts

- **WHEN** new scripts are added for Linux or Windows builds
- **THEN** the spec SHALL define the naming convention (directories + filenames) and require lint/tests to catch deviations.

### Requirement: Template Diagrams

All diagrams explaining variant flows, cache lifecycle, or state integration SHALL live under `openspec/specs/templates/` with docs referencing them per governance.

#### Scenario: Diagram placement

- **WHEN** diagrams explain variant flows, cache lifecycles, or state integration
- **THEN** they MUST live under `openspec/specs/templates/` (Mermaid) with docs referencing them to satisfy governance.

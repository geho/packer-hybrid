## REMOVED Requirements

### Requirement: Incremental Hash Manifests
The duplicate text under `## ADDED Requirements` SHALL be removed so the canonical description at the top of the spec remains the single source of truth.

#### Scenario: Removal of duplicate incremental hash text

- **WHEN** contributors reference `Incremental Hash Manifests`
- **THEN** they MUST read the original requirement under the main `## Requirements` section because the duplicated text under `## ADDED Requirements` has been removed.

### Requirement: Result Schema & Exit Codes
The repeated schema requirement under `## ADDED Requirements` SHALL be removed, keeping the authoritative schema + retry table only once in the spec.

#### Scenario: Removal of duplicate result schema text

- **WHEN** automation owners need the packer result schema
- **THEN** they SHALL rely on the single requirement under `## Requirements`, ensuring they do not encounter conflicting copies.

### Requirement: Diagnostics & Retention Integration
The repeated diagnostics requirement under `## ADDED Requirements` SHALL be removed so the logging/retention rules exist exactly once.

#### Scenario: Removal of duplicate diagnostics text

- **WHEN** readers trace how diagnostics metadata is stored
- **THEN** they MUST consult the canonical requirement under `## Requirements`, avoiding the previously duplicated block.

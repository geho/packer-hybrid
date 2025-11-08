## ADDED Requirements

### Requirement: Config Inputs & Overlays

`hybridcore-config` SHALL accept template defaults, environment overlays, and CLI-provided answers, merging them deterministically. Inputs MUST be validated against a schema before rendering `.auto.pkrvars.hcl`.

#### Scenario: Overlay precedence

- **WHEN** `generate_env_config` receives defaults + `prod` overrides + CLI flags
- **THEN** the resulting vars file MUST apply overrides in that order and emit warnings for unused keys.

### Requirement: Serialization Format

Rendered configs MUST be written as HCL with stable key ordering and comments pointing to the originating spec section; secrets MUST be referenced via `env()` or external paths, never inlined.

#### Scenario: Secret reference

- **WHEN** the config requires `PROXMOX_TOKEN`
- **THEN** the output MUST contain `env("PROXMOX_TOKEN")` (or documented secret manager path) instead of the raw token.

### Requirement: Testing

`hybridcore-config` SHALL provide unit tests covering schema validation, overlay precedence, and deterministic output (e.g., hash comparisons). CI MUST run these tests before merging.

#### Scenario: Regression prevention

- **WHEN** a contributor modifies overlay logic
- **THEN** the associated unit tests MUST catch ordering regressions by comparing rendered files against golden fixtures.

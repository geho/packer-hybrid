## MODIFIED Requirements

### Requirement: Sink Extensions & Compatibility

Sink extension guidance SHALL include syslog/cloud shippers plus formatter parity expectations so operators know how to deploy additional sinks.

#### Scenario: Syslog formatter parity

- **WHEN** `register_sink("syslog")` is enabled
- **THEN** the syslog payload SHALL include the canonical fields plus extras while the console/file handlers continue emitting the original format.

### Requirement: Retention & Audit Alignment

Retention requirements SHALL include a mapping table tying CLI flags/env vars to rotation thresholds and referencing the security retention policy.

#### Scenario: Flag propagation

- **WHEN** `--log-keep=14d` is set
- **THEN** the mapping SHALL describe the retention window, env var override, and link to the security policy.

### Requirement: Diagnostics Integration

The logs spec SHALL document how log redaction integrates with `diag` bundles and require a scrub manifest before packaging.

#### Scenario: Diag log scrub

- **WHEN** `hybridcore-logs` prepares a diag bundle
- **THEN** it SHALL invoke the shared redaction hook before files are packaged and record the scrub manifest.

### Requirement: Redaction & Context

The spec SHALL define the canonical context schema (required keys, optional keys, defaults) so callers know what fields to supply.

#### Scenario: Context validation

- **WHEN** log helpers receive a context object
- **THEN** they SHALL validate required keys (env, component, command_id) and default optional ones (correlation_id, user) in a documented order.

### Requirement: Logger Interface

The spec SHALL ensure diagrams for logging bootstrap live in `specs/hybridcore-logs/` and are referenced from docs per governance.

#### Scenario: Diagram reference

- **WHEN** logging bootstrap changes
- **THEN** the spec diagrams SHALL be updated and docs MUST link back rather than embedding divergent copies.

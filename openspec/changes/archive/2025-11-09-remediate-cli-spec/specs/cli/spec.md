## ADDED Requirements

### Requirement: Command Semantics & Validation

CLI commands `publish`, `clean`, `diag`, `status`, and `wizard` SHALL document required args, validation gates, and exit codes (table added to spec) so operators know deterministic behaviours. See `specs/cli/command-module-map.md` for module interactions.

#### Scenario: Publish semantics

- **WHEN** `publish --env prod` runs
- **THEN** the CLI MUST run drift detection, refuse to continue when manifests mismatch, and exit with code 2 on validation failure.

### Requirement: Logging & Error Handling (updated)

Logging behaviour SHALL explicitly describe `--verbose`, `--quiet`, and `--json` semantics aligned with `hybridcore-logs` so operators know how to configure diagnostics.

#### Scenario: Verbose logging

- **WHEN** `build --verbose` fails because credentials are missing
- **THEN** the CLI MUST emit DEBUG logs via `hybridcore.logs` while redacting sensitive values.

### Requirement: Command → Module Mapping

The CLI spec SHALL reference `specs/cli/command-module-map.md` (new diagram) showing how commands call hybridcore modules, and contributors SHALL keep it aligned whenever commands change.

#### Scenario: Diagram upkeep

- **WHEN** a new command is added
- **THEN** the diagram MUST be updated and referenced from the CLI spec.

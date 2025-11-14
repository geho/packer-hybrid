# hybridcore-logs Specification

## Purpose

Outline the logging interface shared across CLI/tests, including formatting, rotation, and redaction, as part of the hybridcore umbrella. Reference: [specs/hybridcore/spec.md](openspec/specs/hybridcore/spec.md)
## Requirements
### Requirement: Logger Interface

`hybridcore-logs` SHALL provide `init_logging(env, component, artifact_dir)` that boots loggers for CLI, tests, and background workers before any other module runs. The initializer MUST:

- Configure a shared formatter `[timestamp] level component command_id message`.
- Install a console handler (INFO default, DEBUG via `--verbose`) and a rotating file handler under `<artifact_dir>/logs/<component>.log` with size/time rotation thresholds defined in config.
- Register a hook so `pytest` fixtures and CLI entrypoints share the same handler stack and emit identical prefixes.
- Stream file handler output to CI artifacts (attach logs directory) and gracefully close handlers on teardown.

Docs referencing logging bootstrap diagrams (e.g., `docs/hybridcore-architecture.md`) SHALL link back to the spec-hosted diagrams in `specs/hybridcore-logs/logging-bootstrap.md` per governance.

#### Scenario: CLI bootstrap

- **WHEN** `hybridcore.cli.main()` executes `init_logging("prod", "cli", artifacts)`
- **THEN** both stdout and `<artifacts>/logs/cli.log` MUST emit identical formatter strings, use rotation thresholds from config, and register for upload at the end of the run.

### Requirement: Redaction & Context

The spec SHALL define the canonical context schema (required keys, optional keys, defaults) so callers know what fields to supply.

#### Scenario: Context validation

- **WHEN** log helpers receive a context object
- **THEN** they SHALL validate required keys (env, component, command_id) and default optional ones (correlation_id, user) in a documented order.

### Requirement: Testing

Unit tests SHALL verify formatting, rotation triggers, and redaction behavior. Integration tests SHALL run sample CLI commands and assert that log files contain the expected structure without secrets.

#### Scenario: Rotation test

- **WHEN** log size exceeds the configured threshold
- **THEN** tests MUST confirm a new file is created and the old one archived per policy.

### Requirement: Observability & CI Artifacts

`hybridcore-logs` SHALL ship observability tooling: unit tests that mock concurrent writes and ensure handlers stay thread-safe, integration tests that spawn CLI commands and compare emitted lines to golden fixtures, and corruption tests that truncate log files mid-run to verify recovery + rotation. CI MUST always attach the logs directory and publish rotation summaries (active file count, newest timestamp).

Recovery states are visualized in `specs/hybridcore-logs/rotation-recovery.md`.

#### Scenario: Rotation & corruption test

- **WHEN** tests append data past the rotation threshold and then simulate a crash mid-write
- **THEN** on restart the module MUST roll to a new file, mark the corrupted file in the artifact manifest, and tests MUST diff the resulting lines against fixtures to confirm format stability.

### Requirement: Sink Extensions & Compatibility

Sink extension guidance SHALL include syslog/cloud shippers plus formatter parity expectations so operators know how to deploy additional sinks.

#### Scenario: Syslog formatter parity

- **WHEN** `register_sink("syslog")` is enabled
- **THEN** the syslog payload SHALL include the canonical fields plus extras while the console/file handlers continue emitting the original format.

### Requirement: Retention & Audit Alignment

Retention requirements SHALL include a mapping table tying CLI flags/env vars to rotation thresholds and referencing the security retention policy.

| Flag/env var | Description | Retention target | Security reference |
| --- | --- | --- | --- |
| `--log-keep=<days>` | CLI flag controlling retention window | Days before purge, default 7 | `specs/security/spec.md#requirement-retention-workflow` |
| `HYBRIDCORE_LOG_MAX_DAYS` | Env var override for retention | Days override for headless jobs | Same as above |
| `HYBRIDCORE_LOG_MAX_BYTES` | Env var controlling max log size before rotation | Bytes threshold before rotation | `specs/security/spec.md#requirement-quality-gate-checklist` |

#### Scenario: Flag propagation

- **WHEN** `--log-keep=14d` is set
- **THEN** the mapping SHALL describe the retention window, env var override, and link to the security policy.

### Requirement: Diagnostics Integration

The logs spec SHALL document how log redaction integrates with `diag` bundles and require a scrub manifest before packaging.

#### Scenario: Diag log scrub

- **WHEN** `hybridcore-logs` prepares a diag bundle
- **THEN** it SHALL invoke the shared redaction hook before files are packaged and record the scrub manifest.

### Requirement: Open Issues Tracking

The hybridcore-logs spec SHALL keep a `## Open Issues` section pointing to `assessments/2025-11-14-remediation-migration/remediations/hybridcore-logs-remediations.md`. Assessments MUST summarize outstanding gaps per dimension in that doc and cross-reference it from the spec.

#### Scenario: Remediation linkage

- **WHEN** a spec assessment uncovers deviations for the hybridcore-logs spec
- **THEN** contributors SHALL update `assessments/2025-11-14-remediation-migration/remediations/hybridcore-logs-remediations.md` and refresh the spec's `## Open Issues` pointer before merging changes.

## Open Issues

See `assessments/2025-11-14-remediation-migration/remediations/hybridcore-logs-remediations.md`.

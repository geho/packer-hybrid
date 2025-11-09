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

See `specs/hybridcore-logs/logging-bootstrap.md` for the end-to-end bootstrap flow.

#### Scenario: CLI bootstrap

- **WHEN** `hybridcore.cli.main()` executes `init_logging("prod", "cli", artifacts)`
- **THEN** both stdout and `<artifacts>/logs/cli.log` MUST emit identical formatter strings, use rotation thresholds from config, and register for upload at the end of the run.

### Requirement: Redaction & Context

Logger helpers MUST enforce structured context propagation (`env`, `component`, `command_id`, `correlation_id`, `user`) by requiring callers to pass a context object; missing fields MUST be defaulted centrally. Redaction filters SHALL run before serialization, masking values that match secret patterns or are flagged via helper APIs. Module-specific enrichers MAY add extra fields but MUST not override the canonical names.

The call + filtering sequence is illustrated in `specs/hybridcore-logs/context-flow.md`.

#### Scenario: Command context

- **WHEN** `log_command_start(ctx, command="packer build")` is invoked with `ctx.command_id="1234"`
- **THEN** every emitted line MUST include `command_id=1234` and any argument containing secrets (e.g., `--token`) MUST be replaced with `***`.

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

Additional sinks (JSON, syslog, cloud log shippers) MUST be registered via `register_sink()` that mirrors handler setup while preserving the canonical console/file formatter. JSON sinks SHALL nest the canonical fields plus extras but MUST not remove `[timestamp] level component command_id message` from console/file outputs. Upgrade paths MUST be documented so existing deployments can opt in without format drift.

#### Scenario: JSON sink opt-in

- **WHEN** `register_sink("json")` is enabled
- **THEN** the JSON payload MUST include the canonical fields plus structured context, while the console/file handlers continue emitting the original bracketed format to prevent tooling regressions.

### Requirement: Retention & Audit Alignment

Spec SHALL describe retention policy guidance and linkage to security/CLI flags with scenario(s).

#### Scenario: Retention config

- **WHEN** operators configure retention
- **THEN** they MUST follow the spec’s guidance on size/time limits and CLI flag propagation.

### Requirement: Open Issues Tracking

The hybridcore-logs spec SHALL keep a `## Open Issues` section pointing to `docs/spec-remediations/hybridcore-logs-remediations.md`. Assessments MUST summarize outstanding gaps per dimension in that doc and cross-reference it from the spec.

#### Scenario: Remediation linkage

- **WHEN** a spec assessment uncovers deviations for the hybridcore-logs spec
- **THEN** contributors SHALL update `docs/spec-remediations/hybridcore-logs-remediations.md` and refresh the spec's `## Open Issues` pointer before merging changes.

## Open Issues

See `docs/spec-remediations/hybridcore-logs-remediations.md`.

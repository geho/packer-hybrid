## ADDED Requirements

### Requirement: Logger Interface

`hybridcore-logs` SHALL expose `get_logger(name)` returning a stdlib `logging.Logger` configured with a shared format (`[timestamp] level component message`) and rotating file handlers under `logs/`.

#### Scenario: Shared format

- **WHEN** CLI and tests request a logger
- **THEN** both MUST emit the same prefix so logs are easily correlated.

### Requirement: Redaction & Context

Logger helpers MUST support redaction (masking secrets) and structured context (extra fields such as `env`, `command`). APIs SHALL provide convenience wrappers (e.g., `log_command_start/finish`).

#### Scenario: Secret redaction

- **WHEN** log messages include credential hints
- **THEN** the logger MUST replace sensitive tokens with `***`.

### Requirement: Testing

Unit tests SHALL verify formatting, rotation triggers, and redaction behavior. Integration tests SHALL run sample CLI commands and assert that log files contain the expected structure without secrets.

#### Scenario: Rotation test

- **WHEN** log size exceeds the configured threshold
- **THEN** tests MUST confirm a new file is created and the old one archived per policy.

# Packer Hybrid CLI Specification

## Requirements

### Requirement: Deterministic Command Surface

The CLI SHALL expose the following subcommands with stable semantics: `init`, `sources sync`, `config`, `validate`, `build`, `publish`, `status`/`inspect`, `clean`, `diag`, and optional `wizard`/`tui`.

#### Scenario: Deterministic execution

- **WHEN** an operator invokes any command with the same inputs
- **THEN** the CLI MUST produce identical file layout, stdout/stderr structure, and exit codes (0 on success, non-zero on failure) regardless of environment.

### Requirement: Hybridcore Integration

All commands MUST operate through the `hybridcore` package rather than reimplementing logic.

#### Scenario: Shared orchestration

- **GIVEN** hybridcore modules handle config rendering, source syncing, template composition, provisioner toggles, packer orchestration, state storage, and logging
- **WHEN** the CLI runs a subcommand
- **THEN** it MUST call the corresponding hybridcore API and surface errors/logs verbatim.

### Requirement: Validation Gate

`packer-hybrid validate` SHALL run `packer fmt -check` and `packer validate` for each targeted OS/platform tuple and fail fast on the first error.

#### Scenario: Targeted validation

- **WHEN** `--targets proxmox,vsphere,azure` is passed
- **THEN** the command MUST only evaluate those builders and report individual success/failure summaries.

### Requirement: Build & Publish Flow

`build` MUST orchestrate parallel packer builds per platform using merged configs, capture manifests, update `state/packer-hybrid.json`, and stream logs. `publish` MUST handle post-build actions (template conversion, Azure SIG replication) and refuse to run if manifests and state diverge.

#### Scenario: Manifest enforcement

- **GIVEN** the previous build manifest hash differs from the current templates
- **WHEN** `publish` is invoked
- **THEN** it MUST exit non-zero and instruct the operator to rerun `build`.

### Requirement: Interactive Wizard

The optional `wizard`/`tui` SHALL wrap non-interactive commands without diverging behaviour.

#### Scenario: Wizard parity

- **WHEN** an operator generates configs via the wizard
- **THEN** the CLI MUST emit the same files as `packer-hybrid config --env <env> --from answers.json` and log the underlying commands executed.

### Requirement: Diagnostics

`packer-hybrid diag` MUST collect recent logs, manifests, and state snapshots into an archive for troubleshooting.

#### Scenario: Diag bundle

- **WHEN** `diag` executes
- **THEN** it SHALL gather `logs/*.log`, the latest manifests in `artifacts/`, and `state/packer-hybrid.json`, store them under `artifacts/diag/<timestamp>.tar.gz`, and report the file path.

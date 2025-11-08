# hybridcore-packer Specification

## Purpose
TBD - created by archiving change add-hybridcore-module-specs. Update Purpose after archive.
## Requirements
### Requirement: Command Wrappers

`hybridcore-packer` SHALL wrap `packer fmt`, `packer validate`, and `packer build`, providing structured results (status, stdout/stderr, artifacts). It MUST stream logs to `hybridcore.logs` while capturing manifests.

#### Scenario: Build result object

- **WHEN** `build()` finishes
- **THEN** it MUST return a dict containing exit code, manifest path, artifact IDs, timestamps, and any error messages.

### Requirement: Drift Detection

Before builds, the module MUST compare current templates/config hashes with the last recorded manifest; on drift, it SHALL refuse to build until validation runs again.

#### Scenario: Drift refusal

- **WHEN** templates change after the last manifest
- **THEN** `hybridcore-packer` MUST raise a drift error instructing the user to re-run validate.

### Requirement: Testing

Unit tests SHALL mock packer subprocess calls to verify command invocation and error handling. Integration tests SHALL execute `packer fmt -check` and `packer validate` on sample templates in CI.

#### Scenario: Mocked failure

- **WHEN** `packer validate` returns exit code 1
- **THEN** the module MUST surface the stderr and unit tests MUST assert that the error is propagated with context.


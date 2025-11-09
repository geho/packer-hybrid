## Purpose

Specify how `hybridcore.packer` wraps packer commands, enforces drift detection, tracks artifacts, and validates packer integrations. Reference: [specs/hybridcore/spec.md](openspec/specs/hybridcore/spec.md)
## Requirements
### Requirement: Command Wrappers

`hybridcore-packer` SHALL provide wrapper functions `fmt(targets)`, `validate(targets, vars)`, and `build(targets, vars, provisioners)` that:

- Map CLI args/flags deterministically (e.g., `fmt --recursive`, `validate -var-file`, `build -force` when requested).
- Prepare the environment by exporting required variables (e.g., `PACKER_LOG=1`, `HYBRIDCORE_ENV`), ensuring secrets flow via `env()` references.
- Stream stdout/stderr to `hybridcore.logs` while capturing JSON manifests and raw logs per command.
- Return a structured response object `{command, exit_code, stdout, stderr, manifest_path, artifacts, started_at, finished_at, retryable}`.
- Classify failures as retryable (network/transient) vs. hard-stop (validation errors) and surface remediation hints.

See `specs/hybridcore-packer/wrapper-flow.md` for the wrapper/execution sequence.

#### Scenario: Build result object

- **WHEN** `build()` completes
- **THEN** it MUST return the structured response with manifest path, artifact metadata, timestamps, and a `retryable` flag.

### Requirement: Drift Detection

Drift detection SHALL reference templates/provisioners/state Open Issues for alignment.

#### Scenario: Drift reference

- **WHEN** drift is detected
- **THEN** the spec MUST point operators to the relevant Open Issues so they can remediate upstream modules.

### Requirement: Cache & Parallelism

Packer caches/parallelism SHALL follow the documented invalidation/limit rules.

#### Scenario: Cache invalidation

- **WHEN** templates bump ISO versions
- **THEN** caches MUST be purged per spec before concurrent builds proceed.

## ADDED Requirements

### Requirement: Artifact Tracking & Parallel Builds

`hybridcore-packer` SHALL:

- Record artifacts in JSON (`artifacts/<build>.json`) with builder ID, platform, region, image IDs, and provenance (command ID, git SHA).
- Support parallel builds by isolating manifests/logs per target and ensuring caches (e.g., ISO downloads) are shared read-only.
- Provide caching controls (`use_cache`, `cache_dir`) and document when caches are invalidated.
- Return artifact metadata to callers/CI so downstream automation can publish images.

See `specs/hybridcore-packer/artifact-registry.md` for the artifact/data flow.

#### Scenario: Artifact registry

- **WHEN** a vsphere+azure build runs in parallel
- **THEN** each produces its own manifest/artifact JSON with unique IDs while sharing read-only caches; the response object MUST include both artifact records.

### Requirement: Testing & Packer Upgrades

Testing SHALL cover:

- Mocked subprocesses verifying argument mapping, env prep, failure classifications.
- Golden manifest tests that parse stored JSON and confirm schema stability.
- Integration suites running `packer fmt -check`, `packer validate`, and representative `packer build` targets in CI.
- Packer upgrade validation playbooks (smoke builds, manifest diffs) before bumping the packer version.

#### Scenario: Upgrade validation

- **WHEN** upgrading packer from `1.14.x` to `1.15.x`
- **THEN** CI MUST run the integration suite + manifest diffs, and the spec MUST document required sign-offs before merging the upgrade.

## Open Issues

See `docs/spec-remediations/hybridcore-packer-remediations.md`.

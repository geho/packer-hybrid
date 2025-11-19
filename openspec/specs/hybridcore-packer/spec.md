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

### Requirement: Open Issues Tracking

The hybridcore-packer spec SHALL keep a `## Open Issues` section pointing to `assessments/2025-11-14-remediation-migration/remediations/hybridcore-packer-remediations.md`. Assessments MUST summarize outstanding gaps per dimension in that doc and cross-reference it from the spec.

#### Scenario: Remediation linkage

- **WHEN** a spec assessment uncovers deviations for the hybridcore-packer spec
- **THEN** contributors SHALL update `assessments/2025-11-14-remediation-migration/remediations/hybridcore-packer-remediations.md` and refresh the spec's `## Open Issues` pointer before merging changes.

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

### Requirement: Incremental Hash Manifests

`hybridcore-packer` SHALL persist per-builder incremental hash manifests (`artifacts/<builder>.hash.json`) listing inputs (templates, scripts, configs) and resulting artifact IDs so drift detection can compare hashes across builds.

#### Scenario: Incremental hash enforcement

- **WHEN** a builder reruns with modified inputs
- **THEN** the hash manifest MUST change and CI SHALL compare the new hash against the previous manifest before allowing publish.

### Requirement: Result Schema & Exit Codes

`hybridcore-packer` SHALL return a documented result schema so CLI/automation can rely on stable fields. The schema includes `command`, `exit_code`, `stderr`, `manifest_path`, `artifacts`, `started_at`, `finished_at`, and `retryable`. Exit codes SHALL map to retry policy as per the table below:

| Exit code | Classification                   | Retry policy                                     |
| --------- | -------------------------------- | ------------------------------------------------ |
| 0         | Success                          | N/A                                              |
| 1         | Packer validation/config error   | Do not retry; surface error to operator          |
| 2         | Infrastructure/transient failure | Retry once automatically, then escalate          |
| 3         | Security/retention violation     | Abort immediately and require manual remediation |

#### Scenario: Schema contract

- **WHEN** CLI parses the packer result
- **THEN** the response object MUST match the schema above and apply the retry policy based on `exit_code`.

### Requirement: Diagnostics & Retention Integration

`hybridcore-packer` SHALL write a log summary (including artifact IDs, manifest path, scrub manifest reference) into `state/packer/logs/<builder>.json` so security/diagnostics tooling can reference it when enforcing retention policies.

#### Scenario: Log summary generation

- **WHEN** a build completes
- **THEN** packer SHALL record the log summary with retention metadata and ensure `diag` bundles include/point to the summary file.

## Open Issues

See `assessments/2025-11-14-remediation-migration/remediations/hybridcore-packer-remediations.md`.

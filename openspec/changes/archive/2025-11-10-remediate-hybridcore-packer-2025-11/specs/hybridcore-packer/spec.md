## ADDED Requirements

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

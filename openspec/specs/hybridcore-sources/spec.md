# hybridcore-sources Specification

## Purpose

Define how `hybridcore.sources` manages plugin/example repositories, metadata, auditing, and tests, building on the umbrella spec. Reference: [specs/hybridcore/spec.md](openspec/specs/hybridcore/spec.md)
## Requirements
### Requirement: Repository Lifecycle & Concurrency

`hybridcore-sources` SHALL manage repositories under `sources/` with a deterministic lifecycle:

- `sync_repos()` clones missing repos, fetches remotes, checks out pinned refs, and updates pins via explicit commands.
- Only git transports `https://`, `ssh://`, or local file URLs are allowed; configureable air-gapped mirrors MUST be supported via environment variables.
- A file-based lock (`sources/.lock`) SHALL enforce single-writer concurrency; concurrent reads MAY proceed but writes must serialize.
- Dirty working trees or diverging SHAs MUST block updates; operators receive actionable errors and remediation guidance (clean/reset steps).

#### Scenario: Dirty repo

- **WHEN** `sources sync` detects uncommitted changes in `sources/packer-plugin-proxmox`
- **THEN** it MUST stop, report the path, and instruct the operator to clean/reset before retrying.

### Requirement: Metadata & Atomic Writes

Metadata SHALL include:

- `state/sources.json` containing entries `{name, repo_url, branch/tag, commit_sha, updated_at, updated_by}`.
- Optional lock files `state/sources.lock` capturing desired SHAs for reproducible builds.
- Atomic write strategy: write to `*.tmp`, fsync file + directory, and rename. Schema evolution SHALL be tracked via `schema_version`; readers MUST migrate as needed.
- Visibility surfaces (CLI commands, dashboards) MUST read metadata and display status (clean/dirty, last updated, operator).

See `specs/hybridcore-sources/metadata-flow.md`.

#### Scenario: Metadata update

- **WHEN** the Azure plugin advances to a new SHA
- **THEN** `state/sources.json` MUST record the new SHA, timestamp, and operator, and dashboards MUST reflect the change.

### Requirement: Failure Recovery & Auditing

`hybridcore-sources` SHALL:

- Detect partial clones or network failures; retry per configurable policy (exponential backoff). If retries fail, report remediation steps (e.g., manual cleanup).
- Support manual overrides (force-pin a SHA) with audit logs referencing operator, command ID, and reason.
- Integrate with security scanning (e.g., run scripts or call external scanners) and record results in metadata.

See `specs/hybridcore-sources/recovery-flow.md`.

#### Scenario: Partial clone recovery

- **WHEN** cloning aborts mid-way
- **THEN** the module MUST detect the incomplete repo, clean up, retry (per policy), and log the event.

### Requirement: Air-Gapped Workflows & Overrides

Spec SHALL describe air-gapped workflow guidance and override auditing.

#### Scenario: Air-gap doc

- **WHEN** mirrors/offline bundles are configured
- **THEN** the spec MUST describe validation and override auditing.

### Requirement: Metadata Schema Reference

Spec SHALL tie `scan_status` fields to the security spec so CLI diagnostics and diag bundles always report scanning cadence/status and warn when scans are stale.

#### Scenario: Schema reference

- **WHEN** CLI renders status output
- **THEN** it MUST include the `scan_status` fields and highlight stale or missing scans.

### Requirement: Open Issues Tracking

The hybridcore-sources spec SHALL keep a `## Open Issues` section pointing to `assessments/2025-11-14-remediation-migration/remediations/hybridcore-sources-remediations.md`. Assessments MUST summarize outstanding gaps per dimension in that doc and cross-reference it from the spec.

#### Scenario: Remediation linkage

- **WHEN** a spec assessment uncovers deviations for the hybridcore-sources spec
- **THEN** contributors SHALL update `assessments/2025-11-14-remediation-migration/remediations/hybridcore-sources-remediations.md` and refresh the spec's `## Open Issues` pointer before merging changes.

### Requirement: Override Approvals & Alignment

Overrides SHALL follow governance policy (request IDs, approvers, expiry) and the override-flow diagram; CLI commands MUST capture the approval metadata.

#### Scenario: Manual override request

- **WHEN** an operator force-pins a repo
- **THEN** the command SHALL require the governance request ID, store approver metadata, and link to the audit entry.

### Requirement: Persistent Overrides & Mirror Inventory

Override approvals and mirror inventories MUST persist in `state/sources-overrides.json` / `state/sources-mirrors.json`, and validation SHALL fail when metadata is missing.

#### Scenario: Missing override metadata

- **WHEN** an override lacks a state record
- **THEN** diagnostics SHALL fail and instruct the operator to capture the metadata.

### Requirement: Resume & Repair Workflows

`sources resume` SHALL use state markers to recover interrupted syncs, requeue pending repos, and clear markers on success; tests simulate network failures, referencing `resume-flow.md`.

#### Scenario: Interrupted sync resume

- **WHEN** a sync fails mid-run
- **THEN** resume SHALL read the marker, finish pending repos, update metadata, and log completion.

### Requirement: Override Audit & Retention

Override approvals SHALL be auditable long-term, retaining historical entries aligned with security/state specs and exposing CLI audit exports referencing governance approvals.

#### Scenario: Audit trail

- **WHEN** auditors request history
- **THEN** maintainers export overrides showing approvals, expirations, and related incidents.

## ADDED Requirements

### Requirement: Testing & Contract Coverage

Testing SHALL include:

- Mocked git invocations verifying command arguments, retries, and error propagation.
- Contract tests ensuring metadata correctness (sorted keys, required fields) and lock-file enforcement.
- Optional integration suites running shallow clones on sample repos (executed nightly or manually) to prove workflows on real git servers.

See `specs/hybridcore-sources/testing-matrix.md`.

#### Scenario: Mocked failure

- **WHEN** git returns non-zero exit code
- **THEN** unit tests MUST assert that stderr/stdout and remediation hints propagate.

## Open Issues

See `assessments/2025-11-14-remediation-migration/remediations/hybridcore-sources-remediations.md`.

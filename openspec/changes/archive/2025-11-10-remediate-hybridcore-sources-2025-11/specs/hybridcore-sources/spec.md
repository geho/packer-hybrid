## MODIFIED Requirements

### Requirement: Metadata Schema Reference

Spec SHALL tie `scan_status` fields to the security spec so CLI diagnostics and diag bundles always report scanning cadence/status and warn when scans are stale.

#### Scenario: Schema reference

- **WHEN** CLI renders status output
- **THEN** it MUST include the `scan_status` fields and highlight stale or missing scans.

## ADDED Requirements

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

## ADDED Requirements

### Requirement: State Coordination & Locking

Hybridcore state SHALL define multi-process coordination semantics using lockfiles (e.g., `state/.lock`) and atomic writes. Concurrency checks MUST describe how CLI, templates, and automation coordinate when multiple writers attempt to update `state/packer-hybrid.json`, including explicit error messages and rollback steps.

#### Scenario: Concurrent writers

- **WHEN** two processes attempt to write state simultaneously
- **THEN** only the process holding the lock SHALL proceed, the other MUST receive a `StateLockHeld` error with retry guidance, and tests SHALL cover the behaviour.

### Requirement: State Schema & Consumers

The spec SHALL define the JSON schema for `state/packer-hybrid.json`, including per-builder hashes, metadata (git SHA, template ID), and consumer expectations (CLI diagnostics, templates, provisioning). Each consumer MUST validate required fields and log if hashes are missing/stale.

#### Scenario: CLI diagnostics consumption

- **WHEN** `packer-hybrid diag state` runs
- **THEN** it SHALL read the schema-defined fields, report drift if hashes are missing, and link to remediation guidance.

### Requirement: State Schema Versioning & Migration

State files SHALL carry a `schema.version` and `created_with` metadata. The spec SHALL describe upgrade/downgrade behaviour, migration scripts, and tests that fail when the version regresses unexpectedly.

#### Scenario: Unexpected downgrade

- **WHEN** the state file version decreases compared to the CLI’s supported version
- **THEN** the CLI SHALL abort, instructing operators to run the migration tool or restore from backup.

### Requirement: Snapshot Provenance

Every snapshot SHALL record provisioning/test provenance (test suite name, timestamp, artifact links) alongside hashes. Governance SHALL require diagrams showing how provenance flows from tests into state artifacts, and diagnostics MUST surface the provenance when issues arise.

#### Scenario: Provenance audit

- **WHEN** a reviewer inspects a state snapshot
- **THEN** they SHALL see which test suite produced it, when it ran, and where artifacts live; missing provenance MUST fail validation.

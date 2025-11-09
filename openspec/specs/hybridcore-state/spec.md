# hybridcore-state Specification

## Purpose

Describe how `hybridcore.state` stores JSON metadata, handles schema evolution, and provides read/write helpers aligned to the umbrella spec. Reference: [specs/hybridcore/spec.md](openspec/specs/hybridcore/spec.md)

## Requirements

### Requirement: Storage Format

`hybridcore-state` SHALL catalog every JSON artifact under `state/`:

- `state/sources.json` – plugin/example repo pins (`name`, `url`, `branch`, `sha`, `updated_at`).
- `state/config/<env>.json` – vars hashes + provenance for each environment.
- `state/packer-manifests/<build>.json` – packer artifact metadata, builder IDs, timestamps.
- `state/index.json` – registry referencing the latest version/hash of each artifact.

Each file MUST include `schema_version`, `generated_at`, and `origin` metadata (module + command). Writes SHALL be atomic using temp files (`*.tmp`), fsync (file + directory), optional advisory locks, and rename.

See `specs/hybridcore-state/state-map.md` for the data layout.

#### Scenario: Atomic write

- **WHEN** `state/sources.json` updates
- **THEN** the module MUST write to `state/sources.json.tmp`, fsync file + directory, honor locks if configured, and rename to the final path.

### Requirement: Access APIs & Migrations

Requirement SHALL reference migration graph/audit logging details.

#### Scenario: Migration reference

- **WHEN** migrations are updated
- **THEN** the requirement MUST link to the toolkit + audit logging sections.

### Requirement: Cross-Module Integrations & Recovery

State mutations MUST be traceable across modules:

- `hybridcore.sources` writes repo pins and records the command ID triggering the update.
- `hybridcore.templates` consumes config hashes to detect drift and records checks in state.
- `hybridcore.packer` reads/writes manifest state referencing build IDs.
- `hybridcore.provisioners` reads state to decide var toggles and writes execution summaries.

Crash recovery MUST detect leftover `.tmp` files, log warnings, and attempt automated repair (finalize rename or remove corrupted temp files).

#### Scenario: Crash recovery

- **WHEN** a `.tmp` file exists on startup
- **THEN** the module MUST verify its integrity, finish the rename if complete, or delete + alert if corrupted so downstream modules resume safely.

### Requirement: Testing & CLI Surfacing

`hybridcore-state` SHALL enforce:

- Schema fixtures validated via JSON Schema/Pydantic.
- Concurrency simulations stressing atomicity in temp dirs.
- Corruption injection tests (truncate, garble JSON) verifying detection/recovery.
- CLI command `hybridcore state check` that scans for inconsistencies, version mismatches, and temp leftovers; CI MUST run it.

#### Scenario: Corruption detection

- **WHEN** `state/config/dev.json` is truncated
- **THEN** the CLI check MUST fail with remediation guidance, and automated recovery SHALL restore from the latest good backup when available.

### Requirement: Migration Toolkit & Audit Logging

Spec SHALL describe migration tooling/rollback/audit guidance.

#### Scenario: Toolkit usage

- **WHEN** operators run migrations
- **THEN** they MUST follow the documented toolkit and audit logging steps.

### Requirement: Open Issues Tracking

The hybridcore-state spec SHALL keep a `## Open Issues` section pointing to `docs/spec-remediations/hybridcore-state-remediations.md`. Assessments MUST summarize outstanding gaps per dimension in that doc and cross-reference it from the spec.

#### Scenario: Remediation linkage

- **WHEN** a spec assessment uncovers deviations for the hybridcore-state spec
- **THEN** contributors SHALL update `docs/spec-remediations/hybridcore-state-remediations.md` and refresh the spec's `## Open Issues` pointer before merging changes.

## Open Issues

See `docs/spec-remediations/hybridcore-state-remediations.md`.

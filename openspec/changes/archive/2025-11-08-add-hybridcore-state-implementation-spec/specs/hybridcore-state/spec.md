## MODIFIED Requirements

### Requirement: Storage Format

`hybridcore-state` SHALL catalog every JSON artifact under `state/`:

- `state/sources.json` – plugin/example repo pins (`name`, `url`, `branch`, `sha`, `updated_at`).
- `state/config/<env>.json` – vars hashes + provenance for each environment.
- `state/packer-manifests/*.json` – packer artifact metadata, builder IDs, timestamps.
- `state/index.json` – registry referencing the latest version/hash of each artifact.

Each file MUST record `schema_version`, `generated_at`, and `origin` (module + command). Writes SHALL be atomic using temp files (`*.tmp`), fsync, and rename; large files MAY use advisory file locks to block concurrent writes.

See `specs/hybridcore-state/state-map.md` for an overview.

#### Scenario: Atomic write

- **WHEN** `state/sources.json` updates
- **THEN** the module MUST: write to `state/sources.json.tmp`, fsync file + directory, acquire/release the lock (if configured), and rename to the final path.

### Requirement: Access APIs & Migrations

The module SHALL expose `read_state(path, schema)` and `write_state(path, payload, schema)` helpers that:

- Validate `schema_version` before read/write.
- Apply migrations via `migrate_state(data, from_version, to_version)`; migrations MUST be idempotent and logged.
- Provide backward compatibility for external consumers via `deprecated_fields` shim logic and default populators.
- Emit audit records (structured logs) for every mutation, including before/after hashes.

See `specs/hybridcore-state/state-io.md` for the atomic write flow and `specs/hybridcore-state/migration-workflow.md` for schema upgrade steps.

#### Scenario: Schema upgrade

- **WHEN** `schema_version` increments from `2` to `3`
- **THEN** `read_state()` MUST migrate older files transparently, log the upgrade, and write back only after successful validation.

## ADDED Requirements

### Requirement: Cross-Module Integrations & Recovery

State updates MUST be traceable across modules:

- `hybridcore.sources` writes repo pins and records the command ID that triggered the update.
- `hybridcore.templates` consumes config hashes to detect drift, recording checks in state.
- `hybridcore.packer` reads/writes manifest state, referencing build IDs.
- `hybridcore.provisioners` reads state to decide var toggles and writes execution summaries.

Crash recovery MUST detect partial writes (e.g., leftover `.tmp` files) on startup, log warnings, and attempt automated repair (e.g., resume from last good snapshot).

#### Scenario: Crash recovery

- **WHEN** a `.tmp` file exists during startup
- **THEN** the module MUST verify the temp content, either finalize the rename if complete or delete + alert if corrupted, so downstream commands resume safely.

### Requirement: Testing & CLI Surfacing

`hybridcore-state` SHALL enforce:

- Schema fixtures validated via JSON Schema or Pydantic.
- Concurrency simulations using temp dirs and threads to stress atomicity.
- Corruption injection tests (truncate, garble JSON) verifying detection/recovery.
- CLI command `hybridcore state check` (or equivalent) that scans for inconsistencies, missing files, version mismatches, and leftover temp files; CI MUST run it.

#### Scenario: Corruption detection

- **WHEN** `state/config/dev.json` is truncated
- **THEN** the CLI check MUST fail with actionable remediation steps, and automated recovery SHALL restore from the latest good backup when available.

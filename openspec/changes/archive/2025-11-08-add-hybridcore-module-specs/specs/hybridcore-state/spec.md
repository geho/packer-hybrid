## ADDED Requirements

### Requirement: Storage Format

`hybridcore-state` SHALL persist JSON documents under `state/` capturing plugin versions, repo SHAs, manifests, and timestamps. Keys MUST be sorted and files written atomically using temp files + rename.

#### Scenario: Atomic write

- **WHEN** state updates occur
- **THEN** the module MUST write to `state/packer-hybrid.json.tmp`, fsync, and rename to avoid corruption on crash.

### Requirement: Access APIs

The module MUST provide `read_state()` and `write_state()` helpers that validate schema versions and default missing fields, ensuring backward compatibility.

#### Scenario: Schema upgrade

- **WHEN** a new field is introduced
- **THEN** `read_state()` MUST populate defaults so older state files still load.

### Requirement: Testing

Unit tests SHALL simulate concurrent writes (using temp dirs) to confirm atomicity and schema migrations. Integration tests SHALL ensure state files pass JSON schema validation in CI.

#### Scenario: Concurrent access

- **WHEN** two writes happen back-to-back
- **THEN** tests MUST verify the last write wins without partial files remaining.

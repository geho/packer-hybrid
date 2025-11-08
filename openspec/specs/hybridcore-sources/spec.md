# hybridcore-sources Specification

## Purpose

Define how `hybridcore.sources` manages plugin/example repositories, metadata, and tests, building on the umbrella hybridcore spec. Reference: [specs/hybridcore/spec.md](openspec/specs/hybridcore/spec.md)

## Requirements

### Requirement: Repository Management

`hybridcore-sources` SHALL clone, fetch, and pin plugin/example repositories under `sources/` using only git CLI commands. Dirty working trees or diverging SHAs MUST abort the operation with actionable errors.

#### Scenario: Dirty repo

- **WHEN** `sources sync` detects uncommitted changes in `sources/packer-plugin-proxmox`
- **THEN** it MUST stop, report the path, and instruct the operator to clean/reset before retrying.

### Requirement: Metadata Tracking

For every sync, the module MUST update `state/sources.json` with repo URL, branch/tag, commit SHA, and timestamp. Writes MUST be atomic (temp file + rename).

#### Scenario: Metadata update

- **WHEN** the Azure plugin advances to a new SHA
- **THEN** `state/sources.json` MUST record the new SHA and `updated_at` so CLI commands can display current pins.

### Requirement: Testing & Tooling

Unit tests SHALL mock git commands to verify error handling, and integration tests SHALL exercise real repos via shallow clones (optional CI). A lint script MUST ensure `state/sources.json` stays formatted (sorted keys, newline).

#### Scenario: Mocked failure

- **WHEN** git returns a non-zero exit code
- **THEN** tests MUST confirm that `hybridcore-sources` surfaces the stderr/stdout to the caller with context.

# hybridcore-templates Specification

## Purpose

Capture the contracts for `hybridcore.templates`—builder inventory, composition outputs, metadata, onboarding, and testing—while referencing the umbrella hybridcore spec. Reference: [specs/hybridcore/spec.md](openspec/specs/hybridcore/spec.md)

## Requirements

### Requirement: Builder Inventory & Layout

`hybridcore-templates` SHALL organize builders under `templates/<os>/<platform>/` with canonical naming (`source.<plugin>-iso.<name>`, `build.<os>.<platform>.<variant>`). The inventory API MUST:

- Enumerate builders per OS/platform and provide file paths to `*.pkr.hcl`.
- Validate naming rules and directory layout, emitting actionable errors for deviations.
- Include metadata per builder (supported provisioners, required scripts/configs).

#### Scenario: Inventory lookup

- **WHEN** the CLI requests builders for `windows,vsphere`
- **THEN** the inventory MUST return canonical identifiers, file paths, and metadata (provisioners/scripts) for deterministic loading.

### Requirement: Composition Pipeline

Composition SHALL:

- Merge common + platform layers in deterministic order (common core → platform overlays → builder-specific HCL).
- Resolve dependencies (scripts/provisioners) and include them in outputs for `packer fmt|validate|build`.
- Generate manifests describing the composed files, provisioners, and checksums stored under `state/templates/<builder>/manifest.json`.

See `specs/hybridcore-templates/composition-flow.md`.

#### Scenario: Deterministic composition

- **WHEN** two runs compose the same builder set
- **THEN** the file ordering and manifest MUST match byte-for-byte to support caching and CI diffs.

### Requirement: Metadata & Validation Hooks

Each builder MUST include metadata (`metadata/<builder>.json`) capturing supported provisioners, required configs, scripts, and references to repo/state files. Validation hooks SHALL:

- Ensure metadata matches actual files.
- Verify references (scripts, provisioners) exist.
- Cross-check state entries for builder hashes.

See `specs/hybridcore-templates/metadata-map.md`.

#### Scenario: Missing script reference

- **WHEN** metadata lists `scripts/hardening.sh` that is missing
- **THEN** validation MUST fail with a descriptive error linking to the builder.

### Requirement: Deterministic Ordering, Manifests & Onboarding

The module SHALL define onboarding rules for new OS/platforms:

- Enforce builder naming patterns.
- Require manifests/checksums stored in `state/templates/`.
- Provide a checklist for adding new layers without breaking existing consumers.

See `specs/hybridcore-templates/onboarding-checklist.md`.

#### Scenario: New platform onboarding

- **WHEN** adding `linux/gcp`
- **THEN** the contributor MUST follow the checklist (naming, manifests, metadata) before enabling the platform.

## ADDED Requirements

### Requirement: Testing & Change Detection

Testing SHALL cover:

- Schema/naming linters for builder metadata and directories.
- Golden composition fixtures per builder set to detect drift.
- `packer fmt|validate` in CI per builder combination, including dual provisioner modes when applicable.
- Change detection rules to block partial updates (builders must update manifests, metadata, and state together).

See `specs/hybridcore-templates/testing-matrix.md`.

#### Scenario: Partial update block

- **WHEN** a builder HCL changes without updating the manifest/checksum
- **THEN** change detection MUST fail and instruct the contributor to regenerate manifests before merging.

## Open Issues

OS Image variant taxonomy, checksum cache policies, metadata schema completeness, change-detection signals, and state sync requirements remain open. See `docs/drafts/templates-spec-gaps.md`.

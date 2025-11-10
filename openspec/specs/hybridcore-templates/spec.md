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

### Requirement: Open Issues Tracking

The hybridcore-templates spec SHALL keep a `## Open Issues` section pointing to `docs/spec-remediations/hybridcore-templates-remediations.md`. Assessments MUST summarize outstanding gaps per dimension in that doc and cross-reference it from the spec.

#### Scenario: Remediation linkage

- **WHEN** a spec assessment uncovers deviations for the hybridcore-templates spec
- **THEN** contributors SHALL update `docs/spec-remediations/hybridcore-templates-remediations.md` and refresh the spec's `## Open Issues` pointer before merging changes.

### Requirement: Variant Naming & Layout

`hybridcore-templates` SHALL define the canonical variant naming and directory layout (`templates/<os>/<platform>/<variant>/`). Inventory validation MUST enforce the naming scheme, metadata map examples SHALL list every variant, and docs SHALL reference `specs/hybridcore-templates/variant-taxonomy.md`.

#### Scenario: Variant validation

- **WHEN** a contributor adds `windows/vsphere/sec-hardened`
- **THEN** validation MUST confirm directories/manifests follow the naming pattern and metadata references the variant before merge.

### Requirement: Checksum Cache & Invalidation

Checksum caches SHALL live under `state/templates/cache/<builder>/` with `{source_sha, manifest_sha, generated_at, expires_at}`. CLI commands MUST refresh caches when SHAs drift/expire, CI SHALL run cache-busting tests, and cache metadata SHALL link to `hybridcore.state` for drift detection.

#### Scenario: Cache parity

- **WHEN** a builder manifest SHA changes
- **THEN** `templates build` SHALL invalidate the cache entry, recompute checksums, and log the refresh.

### Requirement: Builder Manifest State Sync

Builder manifests SHALL sync to `state/templates/<builder>.json` with hashes, provisioners, config SHA, and provenance. A sequence diagram (`specs/hybridcore-templates/state-sync-flow.md`) SHALL illustrate the flow, and diagnostics MUST fail when manifests/state drift.

#### Scenario: State sync drift

- **WHEN** manifest hashes differ from state
- **THEN** CLI diagnostics SHALL block builds until state updates.

### Requirement: Provisioner Metadata Alignment

Templates SHALL declare provisioner requirements per builder, referencing provisioning specs. Validation MUST compare metadata against `state/provisioners/<env>/manifest.json` and fail when toggles/metadata drift.

#### Scenario: Provisioner drift

- **WHEN** a template expects Ansible but provisioning disables it
- **THEN** validation SHALL fail and instruct operators to reconcile toggles or metadata.

### Requirement: Diagram Governance

Onboarding/state-sync diagrams SHALL live under `specs/hybridcore-templates/` (variant taxonomy, state sync). Docs MUST link to them per governance.

#### Scenario: Diagram compliance

- **WHEN** onboarding flows change
- **THEN** diagrams MUST be updated in-spec and docs refreshed before merge.

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

See `docs/spec-remediations/hybridcore-templates-remediations.md` for outstanding work on variant taxonomy, checksum caching, metadata completeness, change-detection signals, and state/state sync requirements.

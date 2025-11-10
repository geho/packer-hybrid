## ADDED Requirements

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

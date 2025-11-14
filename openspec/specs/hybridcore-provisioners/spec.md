## Purpose

Document how `hybridcore.provisioners` structures Ansible/Puppet assets, enforces toggles, compatibility, artifacts, and testing expectations. Reference: [specs/hybridcore/spec.md](openspec/specs/hybridcore/spec.md)
## Requirements
### Requirement: Provisioner Layout & Toggles

`hybridcore-provisioners` SHALL define how provisioning toggles are declared (`configs/<env>/provisioners.yaml`), overridden by CLI flags (e.g., `packer-hybrid build --enable-ansible --disable-puppet`), and persisted into `state/provisioners/<env>/`. When no structured provisioner is enabled, the module SHALL fall back to the SSH script bundle (documented in the provisioning spec) only if `allow_ssh_fallback=true`; otherwise it MUST fail with a descriptive error. Validation SHALL compare requested provisioners against required assets and lint status before mutating state. The requirement SHALL reference the enable/disable diagram in `openspec/specs/hybridcore-provisioners/toggle-flow.md` and log which source (config vs CLI) selected each provisioner.

#### Scenario: Config vs CLI precedence

- **WHEN** the config disables Puppet but the CLI passes `--enable-puppet`
- **THEN** the CLI value SHALL take precedence for that run, the spec MUST require a warning noting the override, and validation SHALL still ensure Puppet assets/lint pass before writing `.pkrvars.hcl` files.

### Requirement: Compatibility & Extension Hooks

`hybridcore-provisioners` SHALL maintain a compatibility matrix mapping OS/platform targets to supported provisioners. Shared libraries (common scripts, env vars) MUST be reused across Ansible/Puppet where possible. Extension hooks SHALL allow new provisioners (e.g., Chef) to register directories, vars, and validation rules without breaking deterministic outputs.

See `specs/hybridcore-provisioners/compat-matrix.md` for the matrix format.

#### Scenario: Unsupported combination

- **WHEN** a user enables Puppet for `alpine` (unsupported)
- **THEN** the matrix MUST reject the combination with guidance on supported provisioners or extension steps.

### Requirement: Artifact Generation & Logging

Provisioner toggles SHALL produce artifacts:

- Vars files: `state/provisioners/<env>/ansible.pkrvars.hcl`, `.../puppet.pkrvars.hcl`.
- Manifests/checksums: `state/provisioners/<env>/manifest.json` containing roles/modules, git SHAs, timestamps.
- Logs MUST explain why provisioner initialization failed, referencing missing assets, lint errors, or compatibility blocks. Logs feed `hybridcore.logs` with structured fields (`provisioner`, `env`, `error_code`).

See `specs/hybridcore-provisioners/artifact-flow.md` for artifact relationships.

#### Scenario: Artifact capture

- **WHEN** Puppet is enabled for `prod`
- **THEN** the module MUST produce `puppet.pkrvars.hcl`, update `manifest.json` with module SHAs, and log success/failure with context.

### Requirement: Provisioner Modes & Fallback

The spec SHALL promote the Puppet agent mode matrix from drafts: `standalone`, `apply`, and `server`. Each mode MUST document required assets (`templates/puppet/**`), secrets (certs/tokens stored via security spec paths), connectivity expectations, and cleanup hooks. Mode metadata SHALL live in `state/provisioners/<env>/puppet.json` and be referenced by templates and config specs. SSH fallback MUST describe the minimal scripts that run when Ansible/Puppet are disabled, including how secrets are sourced and audited.

#### Scenario: Puppet server mode

- **WHEN** `puppet.mode=server`
- **THEN** the spec SHALL require certificates/tokens to live in the security-managed secret store, expect `templates/puppet/hiera/server.yaml`, and mandate validation that the configured endpoint is reachable before builds proceed.

### Requirement: Open Issues Tracking

The hybridcore-provisioners spec SHALL keep a `## Open Issues` section pointing to `assessments/2025-11-14-remediation-migration/remediations/hybridcore-provisioners-remediations.md`. Assessments MUST summarize outstanding gaps per dimension in that doc and cross-reference it from the spec.

#### Scenario: Remediation linkage

- **WHEN** a spec assessment uncovers deviations for the hybridcore-provisioners spec
- **THEN** contributors SHALL update `assessments/2025-11-14-remediation-migration/remediations/hybridcore-provisioners-remediations.md` and refresh the spec's `## Open Issues` pointer before merging changes.

### Requirement: Provisioner Secrets & Validation Pipeline

Each provisioner stack SHALL document secret inputs (vault paths, env vars), lint/unit tests, and CI steps. `enable_ansible` MUST run `ansible-lint`, `yamllint`, and optional role-level unit tests before writing vars; `enable_puppet` MUST run `puppet parser validate`, `metadata-json-lint`, and mode-specific smoke hooks. Secrets consumed by provisioners SHALL reference the security spec (`openspec/specs/security/spec.md#requirement-security-rotation-workflow`) and record provenance in `state/provisioners/<env>/manifest.json`.

#### Scenario: Validation pipeline failure

- **WHEN** `ansible-lint` fails for an enabled provisioner
- **THEN** the spec SHALL require the toggle to abort, log the failure with provisioner/context, and block packer runs until lint passes.

### Requirement: Provisioner Alignment & Drift Detection

Provisioner metadata SHALL remain aligned with config (`openspec/specs/hybridcore-config/spec.md`) and templates (`openspec/specs/hybridcore-templates/spec.md`). The spec SHALL require a drift detector that compares `state/provisioners/<env>/manifest.json` against templated vars and config overlays each time toggles change, emitting actionable guidance when mismatches occur. CLI diagnostics SHALL surface the alignment status and reference the remediation doc when drift persists.

#### Scenario: Drift between templates and provisioners

- **WHEN** a template removes an Ansible role still listed in `state/provisioners/<env>/manifest.json`
- **THEN** the detection hook SHALL fail the build, point to the config/templates specs for reconciliation, and update the remediation tracker if manual cleanup is required.

### Requirement: Provisioner Diagram Governance

All enable/disable flow diagrams and metadata propagation diagrams SHALL live under `openspec/specs/hybridcore-provisioners/` (e.g., `toggle-flow.md`, `metadata-propagation.md`). Docs and remediation drafts MUST embed or link to these spec-hosted diagrams to satisfy governance policies. Diagram updates SHALL be included whenever toggles, modes, or alignment logic change.

#### Scenario: Diagram refresh

- **WHEN** a new provisioner (Chef) is added or SSH fallback changes
- **THEN** the spec SHALL require updating the diagrams under `specs/hybridcore-provisioners/`, documenting the new branches, and rerunning diagram lint/Prettier before merging.

## ADDED Requirements

### Requirement: Provisioner Secrets & Validation Pipeline

Each provisioner stack SHALL describe its secrets, validation hooks, and CI gates:

- `enable_ansible` MUST read secrets via env vars or secret manager paths recorded in `state/provisioners/<env>/manifest.json`, run `ansible-lint`, `yamllint`, and optional role unit tests before writing vars.
- `enable_puppet` MUST record which mode is active, fetch certificates/tokens via the security spec locations, run `puppet parser validate`, `metadata-json-lint`, and mode-specific smoke hooks (e.g., `puppet agent --test` for server mode).
- Failures SHALL abort the toggle, log the provisioner/context, and block `packer-hybrid build/publish` until lint passes or the provisioner is disabled.

#### Scenario: Validation pipeline failure

- **WHEN** `ansible-lint` fails for an enabled provisioner
- **THEN** the toggle SHALL abort, the log MUST cite the failing command/output, and CI SHALL block merge until the lint job passes or the provisioner is disabled per governance.

### Requirement: Provisioner Alignment & Drift Detection

Provisioner metadata SHALL remain aligned with config (`openspec/specs/hybridcore-config/spec.md`) and templates (`openspec/specs/hybridcore-templates/spec.md`):

- Each toggle SHALL emit metadata to `state/provisioners/<env>/manifest.json` including roles/modules, SHAs, and consumed config overlays.
- A drift detector SHALL compare manifests with rendered templates/config each time toggles change or `packer-hybrid status` runs, failing the build when mismatches appear and pointing to reconciliation steps.
- CLI diagnostics MUST surface drift status and reference `assessments/2025-11-14-remediation-migration/remediations/hybridcore-provisioners-remediations.md` when manual remediation is pending.
- The metadata propagation diagram in `openspec/specs/hybridcore-provisioners/metadata-propagation.md` SHALL illustrate the required flow.

#### Scenario: Drift between templates and provisioners

- **WHEN** a template removes an Ansible role still listed in the manifest
- **THEN** the detection hook SHALL fail the run, describe the stale entry, and guide operators to sync the config/templates specs (or disable the provisioner) before re-running.

### Requirement: Provisioner Diagram Governance

All enable/disable and metadata propagation diagrams SHALL live under `openspec/specs/hybridcore-provisioners/` with docs embedding or linking to them per governance. Diagram updates SHALL accompany any change to toggle flows, modes, or metadata paths and be validated via Prettier/diagram lint.

#### Scenario: Diagram refresh

- **WHEN** a new provisioner (e.g., Chef) is added or SSH fallback logic changes
- **THEN** contributors SHALL update `toggle-flow.md` and `metadata-propagation.md`, note the change in docs/remediation trackers, and re-run the diagram lint before merging.

### Requirement: Testing & CI Matrix

Testing SHALL cover:

- Unit tests for toggle logic, asset validation, vars emission, and compatibility matrix enforcement.
- Fixture-backed `packer validate` runs with Ansible-only, Puppet-only, and dual-mode toggles.
- Provisioner-specific linting: `ansible-lint`, `yamllint` on inventories, `puppet parser validate`, `metadata-json-lint`.
- CI matrix ensuring each provisioner/OS combination runs at least lint + validate steps; packer upgrades MUST re-run the matrix.

See `specs/hybridcore-provisioners/testing-matrix.md` for required combinations.

#### Scenario: CI enforcement

- **WHEN** a change touches Puppet manifests
- **THEN** CI MUST run `puppet parser validate`, dual-mode packer validate, and record results in the testing matrix to prove both enable/disable paths.

## Open Issues

See `assessments/2025-11-14-remediation-migration/remediations/hybridcore-provisioners-remediations.md`.

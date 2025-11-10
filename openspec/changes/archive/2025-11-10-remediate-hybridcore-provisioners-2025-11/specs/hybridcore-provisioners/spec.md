## MODIFIED Requirements

### Requirement: Provisioner Layout & Toggles

`hybridcore-provisioners` SHALL define how provisioning toggles are declared (`configs/<env>/provisioners.yaml`), overridden by CLI flags (e.g., `packer-hybrid build --enable-ansible --disable-puppet`), and persisted into `state/provisioners/<env>/`. When no structured provisioner is enabled, the module SHALL fall back to the SSH script bundle (documented in the provisioning spec) only if `allow_ssh_fallback=true`; otherwise it MUST fail with a descriptive error. Validation SHALL compare requested provisioners against required assets and lint status before mutating state. The requirement SHALL reference the enable/disable diagram in `openspec/specs/hybridcore-provisioners/toggle-flow.md` and log which source (config vs CLI) selected each provisioner.

#### Scenario: Config vs CLI precedence

- **WHEN** the config disables Puppet but the CLI passes `--enable-puppet`
- **THEN** the CLI value SHALL take precedence for that run, the spec MUST require a warning noting the override, and validation SHALL still ensure Puppet assets/lint pass before writing `.pkrvars.hcl` files.

### Requirement: Provisioner Modes & Fallback

The spec SHALL promote the Puppet agent mode matrix from drafts: `standalone`, `apply`, and `server`. Each mode MUST document required assets (`templates/puppet/**`), secrets (certs/tokens stored via security spec paths), connectivity expectations, and cleanup hooks. Mode metadata SHALL live in `state/provisioners/<env>/puppet.json` and be referenced by templates and config specs. SSH fallback MUST describe the minimal scripts that run when Ansible/Puppet are disabled, including how secrets are sourced and audited.

#### Scenario: Puppet server mode

- **WHEN** `puppet.mode=server`
- **THEN** the spec SHALL require certificates/tokens to live in the security-managed secret store, expect `templates/puppet/hiera/server.yaml`, and mandate validation that the configured endpoint is reachable before builds proceed.

## ADDED Requirements

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

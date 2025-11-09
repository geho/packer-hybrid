## MODIFIED Requirements

### Requirement: Provisioner Layout & Toggles

`hybridcore-provisioners` SHALL describe Ansible and Puppet structures on disk:

- Ansible assets under `templates/ansible/{roles,playbooks,inventories,group_vars}` with mandatory `roles/common`, `inventories/<env>.ini`, and shared `library/` scripts.
- Puppet assets under `templates/puppet/{manifests,modules,hiera}` with required `manifests/site.pp` and module metadata.
- Toggle APIs (`enable_ansible(env)`, `enable_puppet(env)`) MUST verify required assets, produce descriptive errors listing missing/extra files, and emit logs referencing the failing provisioner.
- Toggles map to packer vars (`var.enable_ansible`, `var.enable_puppet`) and generate `.pkrvars.hcl` fragments under `state/provisioners/<env>/`.

#### Scenario: Missing asset

- **WHEN** Ansible is enabled but `templates/ansible/roles/common` is missing
- **THEN** the API MUST raise `ProvisionerAssetMissing` specifying the expected path and suggestions.

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

## ADDED Requirements

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

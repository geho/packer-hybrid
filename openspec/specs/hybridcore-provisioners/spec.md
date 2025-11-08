# hybridcore-provisioners Specification

## Purpose

Document how `hybridcore.provisioners` toggles Ansible/Puppet stacks, validates assets, and emits vars, anchored to the umbrella hybridcore spec. Reference: [specs/hybridcore/spec.md](openspec/specs/hybridcore/spec.md)

## Requirements

### Requirement: Provisioner Toggles

`hybridcore-provisioners` SHALL expose APIs to enable/disable Ansible and Puppet stacks, ensuring required assets exist under `templates/ansible` or `templates/puppet`. Missing assets MUST raise descriptive errors.

#### Scenario: Missing role

- **WHEN** Ansible is enabled but `templates/ansible/roles/common` is absent
- **THEN** the module MUST fail fast and list the missing path.

### Requirement: Variable Emission

The module MUST emit packer variables signaling which provisioners are active (`var.enable_ansible`, `var.enable_puppet`) and provide any necessary vars files for packer builds.

#### Scenario: Puppet opt-in

- **WHEN** Puppet is toggled on
- **THEN** the module MUST emit both baseline Ansible vars and puppet-specific vars so templates stay consistent.

### Requirement: Testing

Unit tests SHALL cover toggle logic, asset validation, and variable emission. Integration tests SHALL run packer validate with `-var enable_puppet=true/false` to confirm templates behave as expected.

#### Scenario: Dual-mode testing

- **WHEN** tests run in puppet-enabled mode
- **THEN** they MUST assert that packer validate references puppet manifests and that disabling Puppet removes those references.

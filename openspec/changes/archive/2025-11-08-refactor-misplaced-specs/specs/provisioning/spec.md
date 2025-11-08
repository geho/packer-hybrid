## ADDED Requirements

### Requirement: Ansible-First Provisioning

Ansible (remote or local) SHALL be the default provisioning mechanism for all builders.

#### Scenario: Role structure

- **WHEN** provisioning runs
- **THEN** roles under `templates/ansible/roles/{common,linux,windows,platform_*}` MUST execute idempotently and support both Linux and Windows images.

### Requirement: Windows Automation Assets

Windows unattended files, sysprep scripts, and platform helpers MUST live under `templates/scripts/windows/` and be referenced consistently across platforms.

#### Scenario: Centralized assets

- **WHEN** a Windows template references unattended files
- **THEN** the HCL MUST point to `templates/scripts/windows/...` paths so the same assets are reused across platforms.

### Requirement: Optional Puppet Support

Puppet MAY be enabled via CLI flags; when enabled, `templates/puppet/{manifests,modules}` MUST exist and the CLI MUST pass `var.enable_puppet=true` to relevant builders.

#### Scenario: Mutual exclusivity

- **WHEN** an operator enables Puppet
- **THEN** the CLI MUST still run baseline Ansible steps required for shared hardening unless explicitly disabled in config.

### Requirement: Provisioning Validation

`packer-hybrid validate` MUST ensure provisioning assets referenced in HCL exist and are linted (`ansible-lint` optional, `yamllint` optional but recommended).

#### Scenario: Asset existence

- **WHEN** validation runs
- **THEN** it MUST fail if any referenced `templates/ansible` roles, Puppet modules, or scripts are missing, surfacing the missing path in the error.

### Requirement: Shared Scripts

Scripts under `templates/scripts/{linux,windows}` SHALL be reusable across platforms; HCL files MUST reference them via `templatefile` or `file` to avoid duplication.

#### Scenario: Reused shell scripts

- **WHEN** both Proxmox and vSphere builders need the same hardening script
- **THEN** they MUST reference the common script via `templatefile("templates/scripts/linux/hardening.sh", ...)` instead of duplicating content.

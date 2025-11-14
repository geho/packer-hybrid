# provisioning Specification

## Purpose

Define provisioning expectations for the framework—Ansible-first workflows, optional Puppet support, validation, and shared scripts—so all platforms follow the same hardening model.
## Requirements
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

### Requirement: Provisioner Testing Matrix

Provisioners SHALL document lint/test expectations per provisioner/platform (Ansible/Puppet/SSH) with CI gate descriptions.

#### Scenario: Puppet gate

- **WHEN** Puppet manifests change
- **THEN** CI MUST run `puppet parser validate` + metadata lint and record the results.

### Requirement: OS Parity & Secret Distribution

The provisioning spec SHALL define OS-specific behaviors (Linux vs Windows) covering script entrypoints, WinRM/SSH requirements, and secret handoff (Vault/env/KeyVault). Templates/provisioners MUST consume secrets via indirection referencing the security spec.

#### Scenario: Windows secret delivery

- **WHEN** provisioning a Windows builder
- **THEN** secrets MUST be delivered via secure WinRM scripts referencing vault paths, not inline strings.

### Requirement: Open Issues Tracking

The provisioning spec SHALL keep a `## Open Issues` section pointing to `assessments/2025-11-14-remediation-migration/remediations/provisioning-remediations.md`. Assessments MUST summarize outstanding gaps per dimension in that doc and cross-reference it from the spec.

#### Scenario: Remediation linkage

- **WHEN** a spec assessment uncovers deviations for the provisioning spec
- **THEN** contributors SHALL update `assessments/2025-11-14-remediation-migration/remediations/provisioning-remediations.md` and refresh the spec's `## Open Issues` pointer before merging changes.

### Requirement: Provisioner Metadata Alignment

Provisioning SHALL reference hybridcore-provisioners/templates specs to keep metadata/toggles aligned; the spec must describe how metadata is consumed and how drift is detected.

#### Scenario: Metadata drift

- **WHEN** provisioning metadata diverges from templates
- **THEN** validation MUST fail and instruct operators to reconcile the specs.

### Requirement: Provisioning Flow Diagram

Provisioning SHALL include a Mermaid diagram showing config → provisioning → packer interactions; docs MUST link to the spec-hosted diagram per governance.

#### Scenario: Diagram governance

- **WHEN** provisioning flow changes
- **THEN** the diagram MUST be updated to reflect new steps before merging.

### Requirement: CLI Variable Mapping

The spec SHALL document CLI flag ↔ `hybridcore` variable ↔ provisioner asset mappings, and validation MUST keep them consistent.

#### Scenario: Mapping drift

- **WHEN** a CLI flag changes
- **THEN** the mapping table MUST be updated and tests fail until alignment is restored.

### Requirement: Security-Aligned Secret Handling

Provisioning scripts/tests MUST reference the security spec’s retention/secret handling rules, requiring indirected secrets and retention policies.

#### Scenario: Secret compliance

- **WHEN** a provisioning script references plaintext secrets
- **THEN** validation MUST fail and instruct using indirection (Vault/env) per security policy.

## Open Issues

See `assessments/2025-11-14-remediation-migration/remediations/provisioning-remediations.md`.

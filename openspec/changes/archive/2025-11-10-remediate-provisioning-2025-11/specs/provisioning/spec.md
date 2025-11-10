## MODIFIED Requirements

### Requirement: OS Parity & Secret Distribution

The provisioning spec SHALL define OS-specific behaviors (Linux vs Windows) covering script entrypoints, WinRM/SSH requirements, and secret handoff (Vault/env/KeyVault). Templates/provisioners MUST consume secrets via indirection referencing the security spec.

#### Scenario: Windows secret delivery

- **WHEN** provisioning a Windows builder
- **THEN** secrets MUST be delivered via secure WinRM scripts referencing vault paths, not inline strings.

### Requirement: Provisioner Testing Matrix

Provisioners SHALL document lint/test expectations per provisioner/platform (Ansible/Puppet/SSH) with CI gate descriptions.

#### Scenario: Puppet gate

- **WHEN** Puppet manifests change
- **THEN** CI MUST run `puppet parser validate` + metadata lint and record the results.

## ADDED Requirements

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

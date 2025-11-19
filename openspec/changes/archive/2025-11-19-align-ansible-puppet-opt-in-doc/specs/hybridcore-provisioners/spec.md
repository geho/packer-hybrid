## MODIFIED Requirements

### Requirement: Provisioner Layout & Toggles

`hybridcore-provisioners` SHALL require documentation describing SSH fallback to state explicitly that fallback only occurs when `allow_ssh_fallback=true`, aligning operator guidance with the spec. The requirement text also reiterates that validation enforces the gate.

#### Scenario: Documented fallback gate

- **WHEN** writers update guidance for disabling Ansible/Puppet
- **THEN** the docs SHALL call out the `allow_ssh_fallback` flag so operators do not assume SSH runs automatically.

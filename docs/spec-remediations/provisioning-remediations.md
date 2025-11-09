# Provisioning Spec Remediations

## Open Topics

1. **Gaps** – Windows provisioning parity, secret distribution, and cross-platform script requirements are still undefined. _Plan_: add OS-specific sections that cover user-data, WinRM/SSH expectations, and secret handoff across provisioners.
2. **Completeness** – The spec lacks explicit lint/test requirements per provisioner (Ansible/Puppet/SSH) and per platform. _Plan_: add a testing matrix plus CI gate descriptions.
3. **Alignment** – Provisioning requirements should reference `hybridcore-provisioners` drafts (opt-in + Puppet modes) and the templates spec to ensure consistent builder expectations. _Plan_: add cross-links and describe how provisioner metadata is consumed.
4. **Integrity** – No diagrams/workflows detail how provisioning steps plug into CLI/hybridcore, making it hard to review toggles. _Plan_: add a Mermaid diagram showing config → provisioners → packer interactions.
5. **Consistency** – CLI/provisioner toggle semantics are defined in different specs without an authoritative mapping. _Plan_: document the mapping table (CLI flag ↔ hybridcore variable ↔ provisioner asset) and add tests verifying the mapping stays in sync.
6. **Integrity** – Security now mandates retention policies, but provisioning scripts still store secrets inline in docs/tests. _Plan_: ensure the spec references the security remediation draft and requires tests to assert secrets are indirected.

## Closed Topics

1. **Provisioner testing matrix** – Spec now references lint/test expectations.

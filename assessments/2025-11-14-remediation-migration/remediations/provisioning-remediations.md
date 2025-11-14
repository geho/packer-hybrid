# Provisioning Spec Remediations

## Open Topics

1. _None – new gaps will be recorded during the next assessment._

## Closed Topics

1. **Provisioner testing matrix** – Spec references lint/test expectations.
2. **OS parity & secrets** – `openspec/specs/provisioning/spec.md#requirement-os-parity--secret-distribution` documents Windows parity, secret distribution, and cross-platform script requirements (`remediate-provisioning-2025-11`).
3. **Provisioner alignment** – `#requirement-provisioner-metadata-alignment` links provisioning to hybridcore-provisioners/templates specs and defines drift validation (`remediate-provisioning-2025-11`).
4. **Provisioning flow diagram** – `openspec/specs/provisioning/provisioning-flow.md` plus `#requirement-provisioning-flow-diagram` capture config → provisioners → packer interactions (`remediate-provisioning-2025-11`).
5. **CLI mapping** – `#requirement-cli-variable-mapping` documents CLI ↔ hybridcore variable ↔ provisioner asset mappings with validation requirements (`remediate-provisioning-2025-11`).
6. **Security-aligned secret handling** – `#requirement-security-aligned-secret-handling` references the security spec and enforces indirected secrets with retention rules (`remediate-provisioning-2025-11`).

## Why

`docs/spec-remediations/security-remediations.md` cites missing secrets rotation workflow, provisioning credentials guidance, incident response steps, supply-chain scanning/SBOM requirements, and duplicated verification gate language. The security spec currently enumerates quality gates but doesn’t cover rotation/IR/SSBOM.

## What Changes

- Add sections covering secrets rotation (Ansible/Puppet credentials), storage, and incident response playbook references.
- Document supply-chain scanning cadence (sources/templates) and SBOM requirements.
- Replace duplicated verification gates with references to CLI/packer specs to avoid redundancy.

## Impact

- Security spec becomes actionable for secrets rotation/IR and supply-chain scanning.
- Reduces duplication by referencing existing specs for verification gates.

# Security Spec Gaps

1. **Gaps** – Secrets rotation workflow, credentials storage for Puppet/Ansible, and incident response procedures not codified.
2. **Completeness** – No coverage of supply-chain scanning (sources, templates) or SBOM requirements.
3. **Alignment** – Security spec duplicates CLI/packer verification gates; consider referencing those specs instead of restating.

Remediation: extend security spec with secrets rotation/incident response steps, supply-chain scanning requirements, and references to avoid duplication.

# Security Spec Remediations

## Open Topics

1. **Gaps** – Secrets rotation workflow, credentials storage for Puppet/Ansible, and incident response procedures are not codified. _Plan_: add requirements for rotation cadence, storage backends, and runbooks.
2. **Completeness** – No coverage of supply-chain scanning (sources, templates) or SBOM requirements. _Plan_: document mandatory scanners, outputs, and CI gating.
3. **Alignment / Duplicates** – Security spec duplicates CLI/packer verification gates instead of referencing those specs. _Plan_: replace duplicated text with references and describe how security validates the gates.
4. **Integrity** – There is no defined severity/triage rubric tying incidents back to module Open Issues, so escalation is ad hoc. _Plan_: add severity levels, response times, and guidance on when to update module remediation docs.

## Closed Topics

1. _None yet – first remediation will populate this section._

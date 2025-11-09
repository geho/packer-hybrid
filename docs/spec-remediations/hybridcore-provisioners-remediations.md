# Hybridcore Provisioners Remediations

## Open Topics

1. **Gaps** – Puppet agent modes (`standalone`, `apply`, `server`) and Ansible/Puppet opt-in precedence live only in `docs/drafts/ansible-puppet-opt-in.md` and `docs/drafts/puppet-agent-modes.md`. _Plan_: merge the draft content into the spec, add mode selection scenarios, and document validation gates for each combination.
2. **Completeness** – There are no requirements covering SSH-only fallback, secrets handling per provisioner, or the asset validation pipeline (lint/unit tests for roles/modules). _Plan_: add a requirement per provisioner stack plus CI coverage.
3. **Alignment** – Provisioner toggles do not cross-reference config/templates Open Issues, so drift between vars/templates goes unnoticed. _Plan_: explicitly link to those specs and define how provisioner metadata is consumed.
4. **Integrity** – No diagrams or workflows show enable/disable flows, making it hard to reason about toggles. _Plan_: add a Mermaid diagram (CLI → hybridcore.provisioners → packer variables) and link it from the spec.

## Closed Topics

1. _None yet – tracked once the first remediation merges._

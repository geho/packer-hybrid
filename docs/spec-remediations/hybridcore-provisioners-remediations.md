# Hybridcore Provisioners Spec Gaps

1. **Gaps** – Puppet agent modes (`standalone`, `apply`, `server`) and Ansible/Puppet opt-in precedence are tracked in separate drafts but not integrated here. Consolidate them.
2. **Completeness** – Need rules for SSH-only fallback, secrets handling per provisioner, and asset validation pipeline details.
3. **Alignment** – Cross-reference `ansible-puppet-opt-in.md` and `puppet-agent-modes.md`; ensure packaging aligns with config/templates Open Issues.
4. **Integrity** – Document reference diagrams/workflows for enabling/disabling provisioners to reduce ambiguity.

Remediation: merge existing drafts into this spec gap doc, then update spec with toggle precedence, Puppet modes, SSH fallback, and validation workflows.

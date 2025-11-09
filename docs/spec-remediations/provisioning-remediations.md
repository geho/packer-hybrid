# Provisioning Spec Gaps

1. **Gaps** – Windows provisioning parity, secret distribution, and cross-platform script requirements not fully defined.
2. **Completeness** – Need explicit lint/test requirements per provisioner (Ansible/Puppet/SSH) and per-platform docs.
3. **Alignment** – Should reference provisioner-specific drafts (opt-in, Puppet modes) and templates spec to ensure consistent builder expectations.

Remediation: update provisioning spec with platform-specific requirements, lint/test matrices, and cross-references to toggles/Puppet modes drafts.

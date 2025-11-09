## Why

`docs/spec-remediations/provisioning-remediations.md` identifies gaps: Windows parity, secret distribution, cross-platform script requirements, explicit lint/test matrices, and cross-references to provisioner drafts/templates. The provisioning spec currently covers Ansible-first workflows but misses these details.

## What Changes

- Document Windows parity requirements (scripts, unattended files) and secret distribution guidance.
- Add lint/test matrices per provisioner (Ansible/Puppet/SSH) with per-platform expectations.
- Reference provisioner drafts (`ansible-puppet-opt-in.md`, `puppet-agent-modes.md`) and templates spec.

## Impact

- Provisioning spec becomes deterministic across OS/platforms.
- Secrets and testing expectations are clear per provisioner.
- Cross-module references keep provisioning aligned with templates/provisioners remediations.

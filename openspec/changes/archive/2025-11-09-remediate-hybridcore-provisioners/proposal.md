## Why

`docs/spec-remediations/hybridcore-provisioners-remediations.md` lists open topics: Puppet agent modes, Ansible/Puppet opt-in precedence, SSH fallback rules, secrets handling per provisioner, and missing diagrams/workflows. The current spec references toggles at a high level but lacks these details, so operators can’t confidently configure provisioners.

## What Changes

- Add requirements describing Puppet agent modes (`standalone`, `apply`, `server`) and opt-in precedence between Ansible/Puppet/SSH fallback.
- Document secrets handling per provisioner and the asset validation pipeline.
- Provide a reference diagram/workflow for enabling/disabling provisioners.
- Update the remediation draft (move completed items to “Closed Topics”) and ensure cross-links to `ansible-puppet-opt-in.md` / `puppet-agent-modes.md`.

## Impact

- Provisioner toggles become deterministic and documented (opt-in precedence, SSH fallback).
- Operators understand Puppet agent modes and secrets handling per provisioner.
- Diagrams/workflows reduce ambiguity, making the spec actionable.

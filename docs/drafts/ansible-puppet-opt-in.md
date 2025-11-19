# Draft: Ansible/Puppet Opt-In Strategy

## Context

`openspec/changes/refactor-misplaced-specs/specs/provisioning/spec.md` currently states that Puppet is optional, but it does not define _how_ operators opt in or how SSH-only provisioning should work when neither Ansible nor Puppet is selected.

## Goals

1. Specify the precedence between global configuration (e.g., `configs/<env>/defaults.yaml`) and CLI flags for provisioning toggles.
2. Document the fallback behaviour when both Ansible and Puppet are disabled (SSH command bundles only).
3. Ensure validation surfaces explicit errors when requested provisioners lack required assets.

## Proposed Behaviour

- Introduce a global `provisioners` section that enumerates `ansible`, `puppet`, and `ssh` with `enabled`, `mode`, and `asset_path` keys. CLI flags (e.g., `--enable-puppet`) override that configuration for the current run only.
- When all structured provisioners are disabled, the CLI MUST fail unless `allow_ssh_fallback=true` is present in config/CLI flags. Only when that flag is enabled SHALL the CLI emit a warning and run the minimal SSH provisioner set (e.g., shell scripts) defined under `templates/scripts/*`. Operators can opt back into Ansible or Puppet per run, but the doc MUST reference the spec rule requiring the flag to be explicit.
- Validation MUST fail if a provisioner is enabled but required assets are missing or fail linting. The error should cite the provisioner name and path.

## Open Questions

1. Should SSH fallback be enabled automatically, or require `--allow-ssh-fallback`?
2. Do we support simultaneous Ansible and Puppet, or restrict to one structured provisioner plus SSH?
3. Where should default global config live (`configs/defaults.yaml` vs `state/packer-hybrid.json`)?

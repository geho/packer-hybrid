# Proposal: align-ansible-puppet-opt-in-doc

## Why

`docs/drafts/ansible-puppet-opt-in.md` currently states that SSH fallback runs automatically whenever Ansible/Puppet are disabled. The authoritative `hybridcore-provisioners` spec requires `allow_ssh_fallback=true`; otherwise builds must fail. Docs need to match the spec so operators do not expect unsupported behaviour.

## What Changes

- Update the draft doc to explain the `allow_ssh_fallback` gate, failure path, and how CLI/config toggles interact with spec requirements.
- Clarify the validation section so it matches the spec’s description of fallback controls.

## Impact

- Keeps doc guidance aligned with the spec, preventing operators from assuming automatic fallback.
- Requires only documentation edits; no behavioural change yet.

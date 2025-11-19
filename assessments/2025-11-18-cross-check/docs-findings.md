# Findings

Status values: `open`, `wip`, `blocked`, `closed`, `archived`, `deferred`.

| #   | Severity | Source | Reference | Summary | Status | Last Updated | Change / Notes |
| --- | -------- | ------ | --------- | ------- | ------ | ------------ | -------------- |
| 1   | medium   | docs/drafts/ansible-puppet-opt-in.md vs spec | docs/drafts/ansible-puppet-opt-in.md:19; openspec/specs/hybridcore-provisioners/spec.md:8 | Draft doc states SSH fallback runs automatically when Ansible/Puppet are disabled, but the spec allows fallback only when `allow_ssh_fallback=true` else builds must fail, so doc currently promises behaviour disallowed by the spec. | open | 2025-11-18 | `/prompts:openspec-proposal align-ansible-puppet-opt-in-doc` |
| 2   | medium   | docs/drafts/puppet-agent-modes.md vs spec | docs/drafts/puppet-agent-modes.md:18; openspec/specs/hybridcore-provisioners/spec.md:73 | Draft doc says the CLI writes Puppet mode metadata into `configs/<env>/puppet.auto.pkrvars.hcl`, but the spec mandates storing mode metadata in `state/provisioners/<env>/puppet.json`; readers following the doc will write to the wrong location. | open | 2025-11-18 | `/prompts:openspec-proposal align-puppet-mode-doc` |

# Assessment Notes

Use this file to capture raw observations before categorizing them.

## Observations

- [ ] Example: Spec `specs/payments/spec.md` lacks SLA details compared to project policy.
- [ ] Confirm whether any active OpenSpec changes touch packer-hybrid builders to avoid duplicate scope.
- [ ] Inventory current repo docs describing packer-hybrid automation to compare against spec coverage.
- [x] Row #1 (`cleanup-hybridcore-packer-duplicate-requirements`): clarify which `hybridcore-packer` requirement block is authoritative for incremental hash/result schema/logging since the spec duplicates them in the ADDED section.
- [ ] Row #2 (`align-hybridcore-packer-log-path`): resolve log path disagreement between `openspec/project.md` (`logs/`) and `hybridcore-packer` spec (`state/packer/logs`).
- [ ] Docs Row #1 (`align-ansible-puppet-opt-in-doc`): `docs/drafts/ansible-puppet-opt-in.md` promises automatic SSH fallback when both structured provisioners are disabled, which conflicts with spec requirement that fallback is gated by `allow_ssh_fallback`.
- [ ] Docs Row #2 (`align-puppet-mode-doc`): `docs/drafts/puppet-agent-modes.md` instructs storing Puppet mode metadata under `configs/<env>/puppet.auto.pkrvars.hcl`, but the spec requires the metadata under `state/provisioners/<env>/puppet.json`.

## Follow-ups

- [ ] Example: Schedule meeting with product owner.
- [ ] Identify SMEs for packer workflows to schedule clarification sync if gaps are found.

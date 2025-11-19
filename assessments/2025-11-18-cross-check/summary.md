# Assessment Summary

## Top Findings

- [ ] **specs#1** – `openspec/specs/hybridcore-packer/spec.md` duplicates incremental hash/result schema/diagnostics requirements across two sections, violating OpenSpec dedupe rules and risking divergence.
- [ ] **specs#2** – `openspec/specs/hybridcore-packer/spec.md` contradicts `openspec/project.md` on log storage paths (`state/packer/logs` vs `logs/`), leaving automation unsure where diagnostics live.
- [ ] **docs#1** – `docs/drafts/ansible-puppet-opt-in.md` promises automatic SSH fallback even though the spec requires `allow_ssh_fallback=true` or the run must fail.
- [ ] **docs#2** – `docs/drafts/puppet-agent-modes.md` tells contributors to store Puppet mode metadata under `configs/<env>/puppet.auto.pkrvars.hcl`, but the spec mandates `state/provisioners/<env>/puppet.json`.

## Proposed Changes

Status values: `open`, `wip`, `blocked`, `closed`, `archived`, `deferred`. Update `Last Updated` with an ISO date whenever the row changes.

| Finding Ref | Suggested Change ID | Status | Last Updated | Notes |
| ----------- | ------------------- | ------ | ------------ | ----- |
| specs#1 | `cleanup-hybridcore-packer-duplicate-requirements` | closed | 2025-11-19 | `/prompts:openspec-proposal cleanup-hybridcore-packer-duplicate-requirements --context "assessment 2025-11-18-cross-check specs#1"` (archived 2025-11-19) |
| specs#2 | `align-hybridcore-packer-log-path` | open | 2025-11-18 | `/prompts:openspec-proposal align-hybridcore-packer-log-path --context "assessment 2025-11-18-cross-check specs#2"` |
| docs#1 | `align-ansible-puppet-opt-in-doc` | open | 2025-11-18 | `/prompts:openspec-proposal align-ansible-puppet-opt-in-doc --context "assessment 2025-11-18-cross-check docs#1"` |
| docs#2 | `align-puppet-mode-doc` | open | 2025-11-18 | `/prompts:openspec-proposal align-puppet-mode-doc --context "assessment 2025-11-18-cross-check docs#2"` |

## Next Steps

- [x] Convert findings into OpenSpec proposals (`/prompts:openspec-proposal <request>`)
- [ ] Share summary with stakeholders

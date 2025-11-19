# Findings

Status values: `open`, `wip`, `blocked`, `closed`, `archived`, `deferred`.

| #   | Severity | Source | Reference | Summary | Status | Last Updated | Change / Notes |
| --- | -------- | ------ | --------- | ------- | ------ | ------------ | -------------- |
| 1   | medium   | hybridcore-packer spec | openspec/specs/hybridcore-packer/spec.md:49 | Requirement blocks for incremental hash manifests, result schema, and diagnostics are duplicated under both the main requirements and `## ADDED Requirements`, which conflicts with OpenSpec guidance to avoid duplicated requirements and makes it unclear which block is authoritative. | closed | 2025-11-19 | Archived via `changes/archive/2025-11-19-cleanup-hybridcore-packer-duplicate-requirements`. |
| 2   | medium   | hybridcore-packer spec vs project.md | openspec/specs/hybridcore-packer/spec.md:74; openspec/project.md:44 | Spec mandates writing log summaries under `state/packer/logs/<builder>.json`, but project policy states CLI + packer logs live under the top-level `logs/` directory, so contributors receive conflicting instructions on log storage. | open | 2025-11-18 | `/prompts:openspec-proposal align-hybridcore-packer-log-path` |

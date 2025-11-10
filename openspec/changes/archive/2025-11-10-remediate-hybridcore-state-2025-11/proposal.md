# Proposal: Remediate hybridcore-state spec

## Why

`docs/spec-remediations/hybridcore-state-remediations.md` lists unresolved topics: concurrency coordination guidance, hash metadata consumers, schema versioning/back-compat, and provenance tracking for state snapshots. Without these details, CLI diagnostics and templates cannot rely on `state/packer-hybrid.json`, operators lack migration guarantees, and governance rules about diagram/test provenance remain unmet.

## Scope

- Spec: `openspec/specs/hybridcore-state/spec.md` plus diagrams under `openspec/specs/hybridcore-state/` (coordination/provenance flows).
- Docs: `docs/spec-remediations/hybridcore-state-remediations.md` and any linked drafts describing state schema/test provenance.

## What Changes

1. Document multi-process coordination + lockfile semantics, with scenarios for concurrent writers and validation/tests that enforce them.
2. Define the `state/packer-hybrid.json` schema (hash metadata, consumers) and describe how CLI diagnostics/templates consume it.
3. Introduce schema versioning/back-compat requirements plus migration steps/tests for unexpected downgrades.
4. Capture test provenance (suite name, timestamp, artifact refs) alongside each snapshot and describe how governance verifies it.

## Deliverables

- Updated spec requirements (+ diagrams) covering coordination, schema versioning, consumer alignment, and provenance.
- Remediation doc updated with closed topics.
- `openspec validate remediate-hybridcore-state-2025-11 --strict` and Prettier on touched Markdown.

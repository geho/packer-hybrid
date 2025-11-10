# Proposal: Remediate hybridcore-config spec

## Why

`docs/spec-remediations/hybridcore-config-remediations.md` lists unresolved issues: config/state cross-links aren’t explicit, provenance metadata is undocumented, there’s no diagram showing the render → state pipeline, schema validation lacks severity/exit-code guidance, and the spec duplicates provisioning schema content. To keep config aligned with templates/provisioners/security, we must address these gaps.

## Scope

- Spec: `openspec/specs/hybridcore-config/spec.md`.
- Docs/tests: `docs/spec-remediations/hybridcore-config-remediations.md`, pipeline diagrams, config provenance manifest/testing harness.

## What Changes

1. Add explicit references to templates/state Open Issues, including a short “cross-module integration” section.
2. Document provenance metadata (manifest fields, secret indirection audit trail) and add/update tests that verify hashes + provenance comments.
3. Introduce a Mermaid diagram showing config discovery → schema validate → merge/render → state update, link it from the spec, and ensure docs reference the spec diagram.
4. Define schema validation severity/exit code behaviour (warnings vs failures) and add regression tests.
5. Replace duplicated provisioning schema text with references/mapping table pointing to the provisioning spec and template source of truth.

## Deliverables

- Spec deltas covering the items above.
- Updated `docs/spec-remediations/hybridcore-config-remediations.md` (open topics moved to Closed).
- Tests/diagram artifacts as needed.
- `openspec validate remediate-hybridcore-config-2025-11 --strict`.

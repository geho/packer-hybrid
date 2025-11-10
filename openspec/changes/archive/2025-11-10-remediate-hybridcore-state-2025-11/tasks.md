# Tasks

## Prep

1. - [x] Review `openspec/specs/hybridcore-state/spec.md`, `docs/spec-remediations/hybridcore-state-remediations.md`, and any drafts covering state schema/provenance.
2. - [x] Run `openspec list`, `openspec list --specs`, and skim `openspec/project.md` to confirm dependencies.

## Implementation

3. - [x] Define coordination/lockfile semantics for concurrent writers (scenarios + tests) and update the spec.
4. - [x] Specify the `state/packer-hybrid.json` schema, including hash metadata consumers (CLI diagnostics/templates) and validation requirements.
5. - [x] Introduce schema versioning/back-compat requirements plus migration/test expectations for downgrades.
6. - [x] Capture test provenance fields (suite name, timestamp, artifact refs) and ensure governance diagrams/docs reference them.
7. - [x] Add/refresh diagrams under `specs/hybridcore-state/` (e.g., coordination + provenance flows) and ensure docs link back.
8. - [x] Update `docs/spec-remediations/hybridcore-state-remediations.md` (move closed topics, log new follow-ups).

## Wrap-up

9. - [x] Run `npx prettier --write` on touched Markdown/spec files.
10. - [x] `openspec validate remediate-hybridcore-state-2025-11 --strict`.
11. - [x] Provide `/prompts:openspec-apply remediate-hybridcore-state-2025-11` details for the implementation phase once proposal assets are ready. _Now ready for `/prompts:openspec-archive remediate-hybridcore-state-2025-11` after review._

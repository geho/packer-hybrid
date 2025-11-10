# Tasks

## Prep

1. - [x] Review `openspec/specs/hybridcore-sources/spec.md`, `specs/governance/spec.md`, `specs/security/spec.md`, `specs/hybridcore-state/spec.md`, and `docs/spec-remediations/hybridcore-sources-remediations.md`.
2. - [x] Run `openspec list`, `openspec list --specs`, and skim `openspec/project.md` to confirm dependencies.

## Implementation

3. - [x] Embed governance override approvals (policy + scenarios) into the sources spec.
4. - [x] Require persistent state tracking (overrides, mirror inventories) with validation/tests.
5. - [x] Tie metadata scanning cadence/status to security spec + CLI diagnostics.
6. - [x] Document resume/repair workflows (`sources resume`) with state markers + tests.
7. - [x] Define audit/retention guidance referencing security/state specs and add/refresh diagrams under `specs/hybridcore-sources/`.
8. - [x] Update `docs/spec-remediations/hybridcore-sources-remediations.md` (move closed topics, capture follow-ups).

## Wrap-up

9. - [x] Run `npx prettier --write` on touched Markdown/spec files.
10. - [x] `openspec validate remediate-hybridcore-sources-2025-11 --strict`.
11. - [x] Share `/prompts:openspec-apply remediate-hybridcore-sources-2025-11` details once proposal assets are ready. _Next step: `/prompts:openspec-archive remediate-hybridcore-sources-2025-11` after review._

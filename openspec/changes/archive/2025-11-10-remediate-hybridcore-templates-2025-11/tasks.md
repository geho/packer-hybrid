# Tasks

## Prep

1. - [x] Review `openspec/specs/hybridcore-templates/spec.md`, `specs/hybridcore-state/spec.md`, `specs/hybridcore-provisioners/spec.md`, and `docs/spec-remediations/hybridcore-templates-remediations.md`.
2. - [x] Run `openspec list`, `openspec list --specs`, and skim `openspec/project.md` to confirm dependencies.

## Implementation

3. - [x] Define canonical variant naming/layout + validation scenarios; update metadata-map + diagrams.
4. - [x] Document checksum cache storage/invalidation under `state/templates/cache/` with CLI parity/CI coverage.
5. - [x] Specify builder manifest ↔ state sync contract (sequence diagram, divergence tests).
6. - [x] Align provisioner metadata requirements with `docs/spec-remediations/provisioning-remediations.md` and add drift validation.
7. - [x] Move/template onboarding diagrams into `specs/hybridcore-templates/` and reference them from docs.
8. - [x] Update `docs/spec-remediations/hybridcore-templates-remediations.md` (move closed topics, note follow-ups).

## Wrap-up

9. - [x] Run `npx prettier --write` on touched Markdown/spec files.
10. - [x] `openspec validate remediate-hybridcore-templates-2025-11 --strict`.
11. - [x] Share `/prompts:openspec-apply remediate-hybridcore-templates-2025-11` details once proposal assets are ready. _Next command: `/prompts:openspec-archive remediate-hybridcore-templates-2025-11` after review._

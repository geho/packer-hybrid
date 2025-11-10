# Tasks

## Prep

1. - [x] Review `openspec/specs/hybridcore-provisioners/spec.md`, `docs/spec-remediations/hybridcore-provisioners-remediations.md`, and the drafts under `docs/drafts/` referenced by the remediation topics.
2. - [x] Run `openspec list`, `openspec list --specs`, and skim `openspec/project.md` to confirm scope + dependencies.

## Implementation

3. - [x] Define provisioning toggle precedence (config vs CLI), SSH fallback, and validation flows; update spec requirement + add scenario.
4. - [x] Promote Puppet agent mode details (standalone/apply/server) with required assets, secrets, and validation hooks.
5. - [x] Add requirements for provisioner-specific secrets handling, lint/unit tests, and CI gating for each stack.
6. - [x] Describe alignment hooks with config/templates (state metadata, drift detection) and reference the relevant specs.
7. - [x] Add Mermaid diagrams (enable/disable flow + metadata propagation) under `specs/hybridcore-provisioners/` and reference them from the spec/doc.
8. - [x] Update `docs/spec-remediations/hybridcore-provisioners-remediations.md` (move closed topics, capture any follow-ups).

## Wrap-up

9. - [x] Run `npx prettier --write` on touched Markdown/spec files.
10. - [x] `openspec validate remediate-hybridcore-provisioners-2025-11 --strict`.
11. - [x] Outline `/prompts:openspec-apply remediate-hybridcore-provisioners-2025-11` for implementation hand-off once proposal assets are ready. _Applied during this phase; next command is `/prompts:openspec-archive remediate-hybridcore-provisioners-2025-11` after review._

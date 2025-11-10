# Tasks

## Prep

1. - [x] Review `openspec/specs/hybridcore-config/spec.md`, current tests, and `docs/spec-remediations/hybridcore-config-remediations.md`.

## Implementation

2. - [x] Add cross-links to templates/state Open Issues (spec updates).
3. - [x] Document provenance metadata (manifest fields, secret indirection) + add/adjust tests.
4. - [x] Create/link the config pipeline diagram (Mermaid) and ensure docs reference it.
5. - [x] Define schema validation severity/exit codes and add regression tests.
6. - [x] Replace duplicated provisioning schema text with references/mapping table.

## Wrap-up

7. - [x] Update `docs/spec-remediations/hybridcore-config-remediations.md` (move closed topics).
8. - [x] Run `npx prettier --write` on touched Markdown.
9. - [x] Run relevant tests (`python -m unittest` or config-specific suites).
10. - [x] `openspec validate remediate-hybridcore-config-2025-11 --strict`.

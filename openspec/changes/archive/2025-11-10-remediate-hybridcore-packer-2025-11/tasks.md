# Tasks

## Prep

1. - [x] Review `openspec/specs/hybridcore-packer/spec.md`, current tests, and `docs/spec-remediations/hybridcore-packer-remediations.md`.

## Implementation

2. - [x] Add incremental hash manifest requirement + reference tests/CI.
3. - [x] Document packer result schema (fields/exit codes) and ensure CLI references it.
4. - [x] Define exit-code/retry policy table and add integration tests.
5. - [x] Describe how packer logs feed security retention/diag policies.

## Wrap-up

6. - [x] Update `docs/spec-remediations/hybridcore-packer-remediations.md` (move closed topics).
7. - [x] Run `npx prettier --write` on touched Markdown.
8. - [x] Run relevant tests (packer wrappers/result schema).
9. - [x] `openspec validate remediate-hybridcore-packer-2025-11 --strict`.

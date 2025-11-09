# Tasks

## Prep

1. - [x] Reread `openspec/specs/cli/spec.md`, `docs/spec-remediations/cli-remediations.md`, and `specs/security/spec.md`; note referenced diagrams/docs/tests.

## Implementation

2. - [x] Update Diagnostics requirement with explicit redaction + retention rules (reference security spec) and add matching unit/integration tests.
3. - [x] Define/document `status|inspect` JSON schema + versioning in the spec; add fixtures/tests ensuring CLI emits the schema.
4. - [x] Replace duplicated verification checklist with references into `security` spec and document how CLI enforces each gate.
5. - [x] Add explicit cross-links from CLI commands to the relevant module Open Issues/remediation drafts.
6. - [x] Refresh wizard/command diagrams (spec + docs) and add regression test ensuring docs embed the spec-sourced diagrams.
7. - [x] Clarify `clean` scope retention expectations, referencing security retention policy and adding tests covering preserved artifacts/logs.

## Wrap-up

8. - [x] Run `npx prettier --write` on touched Markdown.
9. - [x] Run CLI/unit/integration tests touched above.
10. - [x] `openspec validate remediate-cli-2025-11 --strict`.

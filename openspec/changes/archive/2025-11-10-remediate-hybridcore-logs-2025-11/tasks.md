# Tasks

## Prep

1. - [x] Review `openspec/specs/hybridcore-logs/spec.md`, diagrams, tests, and `docs/spec-remediations/hybridcore-logs-remediations.md`.

## Implementation

2. - [x] Expand sink extension requirement with syslog/cloud examples + formatter parity tests.
3. - [x] Add retention mapping table tying CLI flags/env vars to rotation thresholds/security policy.
4. - [x] Document diag redaction integration with `diag` bundles and add regression tests.
5. - [x] Define canonical context schema (required/optional keys/defaults) and add validation tests.
6. - [x] Ensure logging diagrams live in `specs/hybridcore-logs/` and update docs/spec references accordingly.

## Wrap-up

7. - [x] Update `docs/spec-remediations/hybridcore-logs-remediations.md` (move closed topics).
8. - [x] Run `npx prettier --write` on touched Markdown.
9. - [x] Run relevant tests (unit/integration covering sinks/context/diag).
10. - [x] `openspec validate remediate-hybridcore-logs-2025-11 --strict`.

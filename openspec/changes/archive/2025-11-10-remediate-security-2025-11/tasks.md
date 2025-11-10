# Tasks

## Prep

1. - [x] Review `openspec/specs/security/spec.md`, current tests/docs, and `docs/spec-remediations/security-remediations.md`.

## Implementation

2. - [x] Expand secrets rotation workflow requirement (cadence, storage backends, runbooks) + update docs references.
3. - [x] Document supply-chain scanning/SBOM cadence and outputs.
4. - [x] Replace duplicated verification gate text with references to CLI/packer specs and describe security validation.
5. - [x] Add incident severity/triage rubric tied to response targets and Open Issues handling.
6. - [x] Ensure security diagrams live in `specs/security/` and update docs/spec references per governance.

## Wrap-up

7. - [x] Update `docs/spec-remediations/security-remediations.md` (move closed topics).
8. - [x] Run `npx prettier --write` on touched Markdown.
9. - [x] Run relevant tests (if any tooling/scripts are adjusted). _N/A (docs/spec-only change)._
10. - [x] `openspec validate remediate-security-2025-11 --strict`.

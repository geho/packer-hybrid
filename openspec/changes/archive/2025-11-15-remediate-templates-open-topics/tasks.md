# Tasks

## Proposal Clarifications

1. - [x] Confirm whether the new variant naming table requires updates to onboarding docs (`docs/wizard-ui.md` or others) beyond the spec reference.
2. - [x] Decide on the location/filenames for the required template diagrams (e.g., `openspec/specs/templates/variant-flow.mmd`, `cache-lifecycle.mmd`) and whether simplified versions are needed in docs. _Decision: diagram files live under `openspec/specs/templates/`; simplified doc versions are optional summaries only if needed._
3. - [x] Identify existing tests or linters that can be extended for script directory enforcement vs. writing new tooling. _Decision: extend existing tests/linters to cover the new rules._

## Implementation Tasks

4. - [x] Update `openspec/specs/templates/spec.md` with variant naming/layout guidance, checksum cache lifecycle, state integration scenarios, script directory requirements, and diagram references (including new Mermaid files under `openspec/specs/templates/`).
5. - [x] Update related specs (`cli`, `hybridcore-state`, `provisioning`) if they must reference the new requirements/diagrams.
6. - [x] Add or update tests/tooling to enforce script directory naming, checksum cache invalidation, and CLI status/publish validation hooks.
7. - [x] Move or add the missing template diagrams under `openspec/specs/templates/` and ensure docs link to them per governance.
8. - [x] Update `assessments/2025-11-14-remediation-migration/remediations/templates-remediations.md` (and `summary.md`) to move the addressed topics to “Closed Topics”.
9. - [ ] Run `openspec validate remediate-templates-open-topics --strict` and fix any issues.

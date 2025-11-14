# Tasks

## Proposal Clarifications

1. - [x] Confirm whether any docs under `docs/proposals/` must remain as historical references after migration (e.g., README pointers) or can be deleted entirely.
2. - [x] Decide the target assessment scope/folder name for importing the existing `assessments/2025-11-14-remediation-migration/remediations/*.md` content.
3. - [x] Identify all automation scripts (prompt metadata checkers, schema validators) that need path updates and document them here. _Inventory:_
   - Tests referencing `docs/spec-remediations`: `tests/specs/test_hybridcore_config_spec.py`, `tests/cli/test_spec_integrations.py`.
   - CLI schema JSON referencing remediation docs: `docs/cli-status-schema.json`.
   - Outstanding change `openspec/changes/remediate-all-specs-2025-11` plus archived tasks referencing `assessments/2025-11-14-remediation-migration/remediations/*.md`.
   - No prompt metadata checker currently exists under `tools/`; need to design one targeting `.codex/prompts/*.md` (proposal needed).

## Implementation Tasks

4. - [x] Inventory every former `docs/proposals/*.md` file, capture required history, and update governance/project specs to cite `.codex/prompts/*.md` as the SoT (docs directory removed; history retained in git).
5. - [x] Update `openspec/project.md` sections (coding style, testing, git workflow, prompt usage) to reference `agents/startup.md` and `agents/policies/*.md`.
6. - [x] Update `openspec/specs/governance/spec.md`, `openspec/specs/meta/spec.md`, `openspec/specs/cli/spec.md`, and any other affected specs to remove duplicated policy text and point to the new workflows.
7. - [x] Scaffold assessment folders from the template, migrate the contents of each `assessments/2025-11-14-remediation-migration/remediations/*.md`, and update specs/docs/tests (including CLI schema JSON) to reference the assessments.
8. - [x] Refresh `openspec/changes/remediate-all-specs-2025-11` so it consumes the assessment workflow and new prompts.
9. - [x] Update tooling/tests (prompt metadata scripts, spec references, CLI integration tests) to operate on `.codex/prompts/` and `assessments/`.
10. - [x] Run `openspec validate align-prompts-assessments-sot --strict` and address all issues.

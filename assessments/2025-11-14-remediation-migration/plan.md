# Assessment Plan

- Scope: migrate the remediation backlog from `docs/spec-remediations/` into the assessment SoT and ensure specs/tests reference the new location.
- Timeframe: 2025-11-14 migration window.
- Target Specs/Capabilities: CLI, governance, meta, security, templates, provisioning, and every `hybridcore-*` module.
- Success Criteria:
  - All previous remediation docs relocated under this assessment (including template references).
  - Specs/tests/docs updated to reference `assessments/2025-11-14-remediation-migration/`.
  - Summary captures next steps for future assessments.
- Checklist:
  - [x] Cross-check specs vs project policies (mapping old remediation docs to this assessment).
  - [x] Cross-check specs vs documentation (update references away from `docs/spec-remediations/`).
  - [x] Cross-check specs vs implementation artifacts (tests/automation referencing remediation docs).

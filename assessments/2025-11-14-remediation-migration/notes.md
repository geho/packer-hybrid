# Assessment Notes

## Observations
- [x] Legacy remediation docs lived under `docs/spec-remediations/`; moved them into `assessments/2025-11-14-remediation-migration/remediations/`.
- [x] Specs/tests/docs referenced the old path (e.g., CLI spec, meta spec, CLI integration tests, `docs/cli-status-schema.json`).
- [x] Active OpenSpec change `remediate-all-specs-2025-11` still points to the retired directory.

## Follow-ups
- [x] Update every spec reference to the new assessment path.
- [x] Update automation/tests referencing the retired directory.
- [ ] Schedule the next assessment to refresh findings once new gaps appear after this migration.

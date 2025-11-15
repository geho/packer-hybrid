# Assessment Summary

## Top Findings
- [x] Remediation tracking must now live inside this assessment folder; specs/tests/docs referencing `docs/spec-remediations/` need updates.
- [x] Templates spec still has multiple open topics (variant naming, caches, diagrams) and needs follow-on OpenSpec proposals.

## Proposed Changes
| Finding | Suggested Change ID | Notes |
|---------|---------------------|-------|
| specs-findings#11 | align-prompts-assessments-sot | Completed – migrated SoT references and spawned downstream remediation work. |
| specs-findings#11 | remediate-templates-open-topics | Implementation in progress – covers variant naming, checksum caches, state integration, scripts, and diagrams. |

## Next Steps
- [x] Convert migration findings into this OpenSpec change (`align-prompts-assessments-sot`).
- [x] Launch remediation change (`remediate-templates-open-topics`) for the template-specific gaps.
- [ ] After remediation archives, schedule `/prompts:assessment-init` for the next scope to triage any new gaps.

# Assessment Summary

## Top Findings
- [x] Remediation tracking must now live inside this assessment folder; specs/tests/docs referencing `docs/spec-remediations/` need updates.
- [x] Templates spec still has multiple open topics (variant naming, caches, diagrams) and needs follow-on OpenSpec proposals.

## Proposed Changes
| Finding | Suggested Change ID | Notes |
|---------|---------------------|-------|
| specs-findings#11 | align-prompts-assessments-sot | Current change migrates references and establishes this assessment as the source of truth. |
| specs-findings#11 | follow-up change TBD (e.g., `remediate-templates-variant-naming`) | Split templates open topics into dedicated future changes once migration is complete. |

## Next Steps
- [x] Convert migration findings into this OpenSpec change (`align-prompts-assessments-sot`).
- [ ] After migration merges, schedule `/prompts:assessment-init` for the next scope to triage remaining templates gaps.

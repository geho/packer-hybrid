## Tasks

1. - [x] Confirm scope (`cli`, `hybridcore`, `hybridcore-*`, `provisioning`, `security`, `templates`) and document the assessment plan per dimension (gaps, completeness, ambiguities, consistency, alignment, integrity, duplicates, redundancies).
2. - [x] Execute the full assessment for each scope item (record deviations + remediation proposals).
3. - [x] Cross-check `docs/spec-remediations/`; update or create `docs/spec-remediations/<spec>-remediations.md` entries (follow `docs/spec-remediations/templates-spec-remediations.md`).
4. - [x] Ensure each affected spec has a `## Open Issues` section referencing the relevant remediation draft(s) (pattern: `openspec/specs/hybridcore-templates/spec.md`).
5. - [x] Summarize assessment results and identify follow-on OpenSpec remediations; run `openspec validate add-spec-assessment-remediation --strict`.

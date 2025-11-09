## Why

Large swaths of the project specs (scope: `cli`, `hybridcore`, all `hybridcore-*`, `provisioning`, `security`, `templates`) have grown organically. We need a reusable, policy-aligned assessment pass that checks every spec for gaps, completeness, ambiguities, consistency, alignment, integrity, duplicates, and redundancies. The process must also capture open issues via `docs/drafts/<spec>-spec-gaps.md` and ensure affected specs include `### Open Issues` references so the gaps remain visible until resolved.

## What Changes

- Assess each target spec per the dimensions above, reporting deviations and proposed remediation (spec updates, diagrams, tests, workflow changes).
- Cross-check `docs/spec-remediations/` for existing remediation drafts; update or create `docs/spec-remediations/<spec>-remediations.md` entries following `docs/spec-remediations/templates-spec-remediations.md`.
- Update each affected spec with a `### Open Issues` section (if missing) referencing the relevant draft(s), matching the pattern in `openspec/specs/hybridcore-templates/spec.md`.
- Prepare follow-on spec updates/diagrams/tests as required and keep the OpenSpec workflow compliant.

## Impact

- Provides a systematic, repeatable approach to spec maintenance.
- Makes outstanding issues explicit via drafts + Open Issues sections.
- Keeps the OpenSpec workflow aligned with project policies, reducing drift across capabilities.

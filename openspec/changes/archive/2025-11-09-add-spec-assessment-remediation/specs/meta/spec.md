## ADDED Requirements

### Requirement: Spec Assessment Workflow

The project SHALL maintain a reusable assessment workflow covering scopes `cli`, `hybridcore`, all `hybridcore-*`, `provisioning`, `security`, and `templates`. Each assessment cycle MUST:

- Evaluate the specs across the dimensions: gaps, completeness, ambiguities, consistency, alignment, integrity, duplicates, and redundancies.
- Report every deviation with proposed remediation (spec updates, diagrams, tests, workflow changes).
- Create or update `docs/drafts/<spec>-spec-gaps.md` (template: `docs/drafts/templates-spec-gaps.md`) and add `### Open Issues` sections in affected specs referencing those drafts.
- Ensure drafts, specs, and OpenSpec artifacts remain synchronized (proposal/tasks/spec deltas) and `openspec validate --strict` passes.

#### Scenario: Re-entrant assessment

- **WHEN** the team invokes the assessment prompt for a given scope
- **THEN** the workflow MUST produce updated drafts, `Open Issues` sections, and remediation-ready OpenSpec artifacts while keeping validation green.

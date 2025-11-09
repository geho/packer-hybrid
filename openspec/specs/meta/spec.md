# meta Specification

## Purpose
TBD - created by archiving change add-spec-assessment-remediation. Update Purpose after archive.
## Requirements
### Requirement: Spec Assessment Workflow

The project SHALL maintain a reusable assessment workflow covering scopes `cli`, `hybridcore`, all `hybridcore-*`, `provisioning`, `security`, and `templates`. Each assessment cycle MUST:

- Evaluate the specs across the dimensions: gaps, completeness, ambiguities, consistency, alignment, integrity, duplicates, and redundancies.
- Report every deviation with proposed remediation (spec updates, diagrams, tests, workflow changes).
- Create or update `docs/drafts/<spec>-spec-gaps.md` (template: `docs/drafts/templates-spec-gaps.md`) and add `### Open Issues` sections in affected specs referencing those drafts.
- Ensure drafts, specs, and OpenSpec artifacts remain synchronized (proposal/tasks/spec deltas) and `openspec validate --strict` passes.

#### Scenario: Re-entrant assessment

- **WHEN** the team invokes the assessment prompt for a given scope
- **THEN** the workflow MUST produce updated drafts, `Open Issues` sections, and remediation-ready OpenSpec artifacts while keeping validation green.

### Requirement: Spec Remediation Execution

The project SHALL maintain a reuseable remediation workflow that, given a scope of `docs/spec-remediations/<spec>-remediations.md` files, performs the following for each draft:

- Spawn an OpenSpec change (proposal → apply → archive) covering the required spec updates/diagrams/tests.
- Update the corresponding spec’s `## Open Issues` section when remediation completes.
- Move resolved topics from “Open Topics” to “Closed Topics” within the draft, keeping a record of what changed and when.
- Repeat until all drafts in scope are either closed or represented by fresh follow-up changes.

#### Scenario: Remediation loop

- **WHEN** the remediation workflow is triggered for a given scope
- **THEN** every draft MUST be processed through an OpenSpec change, its spec updated, the draft’s closed section populated, and the change archived.


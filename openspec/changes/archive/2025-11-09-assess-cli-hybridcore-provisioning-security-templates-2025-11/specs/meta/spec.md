## MODIFIED Requirements

### Requirement: Spec Assessment Workflow

Assessments SHALL explicitly cover `cli`, every `hybridcore-*` module, `provisioning`, `security`, and `templates`, recording findings in the corresponding `docs/spec-remediations/<spec>-remediations.md` files.

#### Scenario: Multi-spec assessment scope

- **WHEN** the quarterly assessment runs
- **THEN** it MUST log deviations for each capability above, update their remediation drafts, and ensure the change tasks reflect the scope before `/prompts:openspec-apply` executes.

/prompts:openspec-proposal Spec assessment & remediation (scope: <edit-me>):

- Identify the target specs (`<scope>` list), describe the assessment plan for each dimension, and ensure the execution is recorded in the change tasks (so `/prompts:openspec-apply` performs the full assessment):
  - Gaps: missing behaviours, scenarios, or references.
  - Completeness: requirements present but lacking detail/coverage.
  - Ambiguities: unclear wording, undefined terms, or conflicting instructions.
  - Consistency: contradictions across specs or against umbrella policies.
  - Alignment: divergence from current implementation, workflow policies, or related specs.
  - Integrity: missing diagrams/drafts, stale references, or broken OpenSpec workflow elements.
  - Duplicates: overlapping specs or repeated requirements that should be consolidated.
  - Redundancies: excess requirements or diagrams that add no value and should be removed or referenced.
- For every deviation found, propose remediation: outline the spec update, diagrams, tests, or workflow changes required.
- Cross-check `docs/spec-remediations/` for existing remediation drafts; note whether they address the remediation or require updates.
- Create or update `docs/spec-remediations/<specname>-remediations.md` (use `docs/spec-remediations/templates-spec-remediations.md` as the template) summarizing the deviations and remediation plan per spec.
- Add to each affected spec a new `### Open Issues` section (if not present) referencing the relevant draft(s), following the pattern in `openspec/specs/hybridcore-templates/spec.md`.
- Prepare the OpenSpec change files (proposal/tasks/spec deltas) needed to implement the remediation and run `openspec validate --strict`.

References:

- Scope placeholder `<scope>` (edit before use) – e.g., `hybridcore-templates`, `hybridcore-packer`.
- Draft template: [docs/spec-remediations/templates-spec-remediations.md](docs/spec-remediations/templates-spec-remediations.md)
- Open Issues example: [openspec/specs/hybridcore-templates/spec.md](openspec/specs/hybridcore-templates/spec.md)

/prompts:openspec-proposal Spec assessment & remediation (scope: <edit-me>):

- Identify the target specs (`<scope>` list) and describe the assessment plan for each dimension:
  - Gaps: missing behaviours, scenarios, or references.
  - Completeness: requirements present but lacking detail/coverage.
  - Ambiguities: unclear wording, undefined terms, or conflicting instructions.
  - Consistency: contradictions across specs or against umbrella policies.
  - Alignment: divergence from current implementation, workflow policies, or related specs.
  - Integrity: missing diagrams/drafts, stale references, or broken OpenSpec workflow elements.
  - Duplicates: overlapping specs or repeated requirements that should be consolidated.
  - Redundancies: excess requirements or diagrams that add no value and should be removed or referenced.
- For every deviation found, propose remediation: outline the spec update, diagrams, tests, or workflow changes required.
- Cross-check `docs/drafts/` for existing gap drafts; note whether they address the remediation or require updates.
- Create or update `docs/drafts/<specname>-spec-gaps.md` (use `docs/drafts/templates-spec-gaps.md` as the template) summarizing the deviations and remediation plan per spec.
- Add to each affected spec a new `### Open Issues` section (if not present) referencing the relevant draft(s), following the pattern in `openspec/specs/hybridcore-templates/spec.md`.
- Prepare the OpenSpec change files (proposal/tasks/spec deltas) needed to implement the remediation and run `openspec validate --strict`.

References:
- Scope placeholder `<scope>` (edit before use) – e.g., `hybridcore-templates`, `hybridcore-packer`.
- Draft template: [docs/drafts/templates-spec-gaps.md](docs/drafts/templates-spec-gaps.md)
- Open Issues example: [openspec/specs/hybridcore-templates/spec.md](openspec/specs/hybridcore-templates/spec.md)

## ADDED Requirements

### Requirement: Canonical Reference Format

Markdown references in prompts, docs, and specs SHALL use the format `Reference: [label](relative/path#optional-anchor)` (relative to repo root) so links remain clickable both locally and on Git hosts.

#### Scenario: Prompt reference

- **WHEN** a reusable prompt cites a spec
- **THEN** it MUST include `Reference: [specs/governance/spec.md#requirement-docstring-coverage](openspec/specs/governance/spec.md#requirement-docstring-coverage)` or equivalent relative link with anchor instead of plain text or HTML comments.

### Requirement: Placement & Labeling Rules

References MUST appear at the end of the sentence/paragraph they justify, use singular `Reference:` (or `References:` for multiple links), and anchors SHALL match the slugified requirement header. Specs referencing code or docs MUST use the same convention in callouts or text.

#### Scenario: Multiple references

- **WHEN** a doc needs to cite both CLI and governance specs
- **THEN** it MUST append `References: [specs/cli/spec.md](openspec/specs/cli/spec.md), [specs/governance/spec.md#requirement-canonical-reference-format](openspec/specs/governance/spec.md#requirement-canonical-reference-format)` immediately after the statement.

### Requirement: Enforcement Hooks

Projects SHALL run a Markdown/link checker (e.g., `npx markdown-link-check`, `mdbook-linkcheck`, or custom script) in CI and pre-commit hooks to verify references are clickable and targets exist.

#### Scenario: CI enforcement

- **WHEN** `npm run lint-docs` executes
- **THEN** it MUST fail if any `Reference:` link points to a missing file/anchor or uses an absolute URL outside policy.

### Requirement: Legacy Migration Guidance

When editing files with legacy reference styles (HTML comments, bare text), contributors MUST convert them to the canonical format and note the change in the PR description; newly created files MAY NOT use the legacy styles.

#### Scenario: Updating legacy prompts

- **WHEN** a prompt still contains `<!-- Spec: openspec/specs/... -->`
- **THEN** the change MUST replace it with the canonical `Reference:` link before the PR can merge.

## ADDED Requirements

### Requirement: Specs ↔ Docs Cross-Check

Every spec change SHALL identify the docs that reference it (e.g., README sections, guides) and ensure those docs cite the updated spec section. Conversely, doc updates MUST confirm the underlying spec still matches the described behaviour.

#### Scenario: Mutual references

- **WHEN** `specs/cli/spec.md#command-catalogue` changes
- **THEN** the corresponding docs (e.g., `docs/cli.md`) MUST link back to the updated spec section, and the PR description MUST state that the doc/spec alignment was verified.

### Requirement: Specs ↔ Code Cross-Check

Implementation commits SHALL reference the relevant spec IDs (in headers, commit messages) and confirm code behaviour matches the spec; any intentional deviation MUST include a temporary flag (`Deviation:`) in the commit body plus an issue to resolve it.

#### Scenario: Deviation recording

- **WHEN** code temporarily diverges from a spec to hotfix a production issue
- **THEN** the commit body MUST include `Deviation: specs/templates/spec.md#requirement-data-driven-workflow (tracked in issue #123)` so reviewers know to reconcile later.

### Requirement: Docs ↔ Code Cross-Check

Doc updates that describe behaviour SHALL either link to the code module or the spec that governs it, and CI MUST verify that referenced files/anchors exist (e.g., using `markdown-link-check` + a custom script validating code references).

#### Scenario: Link validation

- **WHEN** `docs/hybridcore-architecture.md` references `hybridcore/templates.py`
- **THEN** the cross-check script MUST confirm the file exists and fail the build if it doesn’t.

### Requirement: Cross-Check Checklist

Pull request templates SHALL include a checklist:

- `[ ] Specs ↔ Docs verified (list files)`
- `[ ] Specs ↔ Code verified (list modules/tests)`
- `[ ] Docs ↔ Code verified (link validation run)`
- `[ ] Deviations recorded (if any)`

PRs MUST fill this checklist before approval; reviewers SHALL reject submissions with unchecked boxes.

#### Scenario: Checklist enforcement

- **WHEN** a PR touches templates and documentation
- **THEN** the author MUST tick the relevant boxes and cite the files checked; absence of this information blocks approval.

### Requirement: Tooling Expectations

CI SHALL run scripts that (a) confirm spec/doc link reciprocity, (b) ensure code headers reference existing spec IDs, and (c) validate docs referencing code paths. Failures MUST block merges until cross-checks pass or documented deviations exist.

#### Scenario: CI script

- **WHEN** `make cross-check` runs
- **THEN** it MUST parse specs/docs/code, verify mutual references, confirm anchors exist, and ensure deviations are flagged; any mismatch causes a non-zero exit.

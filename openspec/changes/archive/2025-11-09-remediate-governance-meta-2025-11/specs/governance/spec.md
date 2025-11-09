## ADDED Requirements

### Requirement: Diagram Verification Workflow

Governance SHALL require a checklist + CI hook ensuring every spec diagram update also refreshes linked docs; CI MUST fail when diagram sources change without doc references.

#### Scenario: Diagram linkage review

- **WHEN** a PR edits a Mermaid file under `specs/`
- **THEN** the checklist and CI hook MUST confirm docs reference the updated diagram before merge.

## MODIFIED Requirements

### Requirement: Prompt Traceability

Prompts MUST cite both the governing spec and the relevant `docs/spec-remediations/<spec>-remediations.md` entry when communicating assessment/remediation work.

#### Scenario: Prompt + remediation linkage

- **WHEN** a contributor authors a spec-remediation prompt
- **THEN** it MUST link to the canonical spec and the active remediation draft before sharing.

### Requirement: Docstring Coverage

Missing spec references in public docstrings SHALL be treated as high severity: lint/CI MUST fail and reviewers MUST block merging (or record a deviation) until docstrings comply.

#### Scenario: Docstring severity enforcement

- **WHEN** CI detects a public docstring without a spec link
- **THEN** the build MUST fail and reviewers require either a fix or a documented deviation.

## MODIFIED Requirements

### Purpose

Replace the placeholder Purpose with a statement describing the assessment/remediation charter referencing governance policies.

### Requirement: Spec Assessment Workflow

Assessments SHALL run at least quarterly under the release captain, record ownership, and continue to use `docs/spec-remediations/` drafts.

#### Scenario: Quarterly assessment cadence

- **WHEN** a quarter ends (or a major release begins)
- **THEN** the release captain MUST run the assessment workflow, record owners in the remediation drafts, and link them from affected specs.

### Requirement: Spec Remediation Execution

Remediation workflow MUST list diagrams/tests touched and enforce documentation of those artifacts before archiving.

#### Scenario: Diagram/test reporting

- **WHEN** `/prompts:openspec-apply <change-id>` completes
- **THEN** the change description MUST call out any diagrams/tests updated (or explicitly say "none") before archiving.

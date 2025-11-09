## MODIFIED Requirements

### Requirement: Spec Remediation Execution

Add guidance that remediation execution SHALL cover every `docs/spec-remediations/*.md` file in scope, presenting `/prompts:openspec-proposal|apply|archive` commands for operators to run, and tracking status in tasks.md until all drafts are closed or rolled into follow-up work.

#### Scenario: Operator-driven execution

- **WHEN** a remediation run starts
- **THEN** the change owner MUST list each draft, present the appropriate `/prompts:openspec-*` commands for the operator, and update the change checklist only after validation/archival complete.

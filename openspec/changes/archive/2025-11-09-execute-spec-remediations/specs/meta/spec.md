## ADDED Requirements

### Requirement: Spec Remediation Execution

The project SHALL maintain a reuseable remediation workflow that, given a scope of `docs/spec-remediations/<spec>-remediations.md` files, performs the following for each draft:

- Spawn an OpenSpec change (proposal → apply → archive) covering the required spec updates/diagrams/tests.
- Update the corresponding spec’s `## Open Issues` section when remediation completes.
- Move resolved topics from “Open Topics” to “Closed Topics” within the draft, keeping a record of what changed and when.
- Repeat until all drafts in scope are either closed or represented by fresh follow-up changes.

#### Scenario: Remediation loop

- **WHEN** the remediation workflow is triggered for a given scope
- **THEN** every draft MUST be processed through an OpenSpec change, its spec updated, the draft’s closed section populated, and the change archived.

## ADDED Requirements

### Requirement: Diagram Source of Truth

Detailed Mermaid diagrams SHALL live inside the relevant spec directories, while supporting docs MUST reference those diagrams and MAY include simplified ASCII/context summaries before linking.

#### Scenario: Diagram updates

- **WHEN** a feature changes control flow or architecture
- **THEN** contributors MUST update the spec-hosted Mermaid diagram, refresh the simplified doc snippet (e.g., `docs/wizard-ui.md`), and link back to the spec so readers know where the canonical version resides.

### Requirement: Documentation Lifecycle

Temporary drafts MUST be promoted or removed once the corresponding spec merges; `project.md` SHALL reference the authoritative spec instead of duplicating content.

#### Scenario: Draft promotion

- **WHEN** a draft in `docs/drafts/` becomes an approved requirement
- **THEN** the draft MUST be deleted (or marked superseded), and `project.md` updated to link to the spec section rather than restating the details.

### Requirement: Prompt Traceability

Reusable prompts under `docs/proposals/` MUST link to the latest approved spec that justifies their guidance.

#### Scenario: Prompt reuse

- **WHEN** a contributor copies a prompt for a new proposal
- **THEN** the prompt MUST already contain a link to the canonical spec, ensuring reviewers can verify the prompt reflects current requirements.

### Requirement: Version-Control Boundaries

Git-tracked content SHALL include templates, scripts, specs, diagrams, and wizard assets; generated outputs (`configs/<env>/*.auto.pkrvars.hcl`, `artifacts/`, `logs/`, `state/`, rendered cloud-init files) MUST remain untracked via `.gitignore`.

#### Scenario: Local overrides

- **WHEN** an operator adds environment-specific overrides or build artifacts
- **THEN** those files MUST stay outside version control so the repository remains portable and free from secrets.

## ADDED Requirements

### Requirement: Commit Message Structure

All commits SHALL follow `<scope>: <summary>` (max 72 characters) where `scope` identifies the primary area (`openspec`, `docs`, `tools`, `templates`, etc.) and `summary` states the action. The summary MUST be written in present tense (“add”, “update”).

#### Scenario: Structured subject

- **WHEN** a contributor lands a change touching specs
- **THEN** they MUST use a subject like `openspec: add commit message policy` rather than a free-form sentence.

### Requirement: Commit Body Content

Commit bodies SHALL include:

1. `Specs:` followed by bullet list of spec IDs/anchors (e.g., `- specs/governance/spec.md#requirement-commit-message-structure`).
2. `Tests:` with bullet list of verification commands run (`packer fmt -check`, `python -m unittest`, etc.).
3. `Docs:` noting any documentation files updated or `Docs: none` if unchanged.

Example:

```
Specs:
- specs/governance/spec.md#requirement-commit-message-structure

Tests:
- npx prettier --check docs
- openspec validate --specs --strict

Docs:
- README.md
```

#### Scenario: Missing fields

- **WHEN** a commit message lacks the `Tests:` section
- **THEN** the lint hook MUST reject it until the contributor lists the verification steps (even if it's “Tests: not run (doc-only)”).

### Requirement: Commit Message Enforcement

Repositories SHALL provide a hook or CI job (e.g., `scripts/check-commit-msg.sh`) that validates the subject format and mandatory body sections before allowing commits to merge.

#### Scenario: Hook enforcement

- **WHEN** a developer commits locally
- **THEN** the Git hook MUST parse the message; if it doesn’t match the format, it exits non-zero with guidance.

# governance Specification

## Purpose

Provide repository-wide policies—documentation lifecycle, references, prompts, changelog, commit messages, diagram standards, and enforcement tooling—so every capability follows the same guardrails.
## Requirements
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

Prompts MUST cite both the governing spec and the relevant `docs/spec-remediations/<spec>-remediations.md` entry when communicating assessment/remediation work.

#### Scenario: Prompt + remediation linkage

- **WHEN** a contributor authors a spec-remediation prompt
- **THEN** it MUST link to the canonical spec and the active remediation draft before sharing.

### Requirement: Version-Control Boundaries

Git-tracked content SHALL include templates, scripts, specs, diagrams, and wizard assets; generated outputs (`configs/<env>/*.auto.pkrvars.hcl`, `artifacts/`, `logs/`, `state/`, rendered cloud-init files) MUST remain untracked via `.gitignore`.

#### Scenario: Local overrides

- **WHEN** an operator adds environment-specific overrides or build artifacts
- **THEN** those files MUST stay outside version control so the repository remains portable and free from secrets.

### Requirement: Docstring Coverage

Missing spec references in public docstrings SHALL be treated as high severity: lint/CI MUST fail and reviewers MUST block merging (or record a deviation) until docstrings comply.

#### Scenario: Docstring severity enforcement

- **WHEN** CI detects a public docstring without a spec link
- **THEN** the build MUST fail and reviewers require either a fix or a documented deviation.

### Requirement: Inline Comment Discipline

Inline comments SHOULD explain _why_ complex logic exists and MUST avoid restating obvious code; every comment SHALL reference the variable or flow it clarifies.

#### Scenario: Explaining non-obvious logic

- **WHEN** a provisioner helper adds a retry loop for transient SSH failures
- **THEN** an inline comment such as `# Retry SSH once to tolerate Azure quota delays` MUST precede the block; conversely, `# increment i` MUST NOT appear because it adds no context.

### Requirement: Section Headers & Module Layout

Modules SHALL organize content with ASCII section headers in the order: imports, constants/config, mixins, core classes, helper functions, CLI entry points/tests. Headers MUST match the pattern `# === Section Name ===`.

#### Scenario: Organized module skeleton

- **WHEN** a developer creates `hybridcore/templates.py`
- **THEN** they MUST group content as:

```python
# === Imports ===

# === Constants ===

# === Mixins ===

# === Core Classes ===

# === Helper Functions ===
```

so reviewers can navigate quickly.

### Requirement: Helper & Mixin Placement

Shared helpers and mixins SHALL live in their own blocks within a module (or dedicated modules) and include docstrings describing expected overrides and extension points.

#### Scenario: Mixin expectations

- **WHEN** a new `StateFileMixin` is defined
- **THEN** it MUST sit under the `# === Mixins ===` header with a docstring outlining required attributes/methods the consumer must supply.

### Requirement: Documentation Linting

CI and local workflows MUST run at least `python -m compileall` plus a docstring/comment linter (`python -m pydocstyle` or `ruff check --select D,COM`) for files touched in a PR; failures MUST block merges.

#### Scenario: Pre-submit enforcement

- **WHEN** a contributor runs `make lint`
- **THEN** the script MUST execute the docstring linter and fail if docstrings are missing, badly formatted, or references (spec IDs) are absent for public APIs.

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

### Requirement: License Header Template

Executable Python files SHALL begin with the following template (no blank lines between items):

```
#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) <YEAR> <Org/Author>
# Generated: <UTC-ISO8601 Timestamp>
# Spec: <relative/path#requirement-slug>
# Diagram: <relative/path>
```

#### Scenario: Applying the header

- **WHEN** a contributor adds `tools/packer-hybrid/sync`
- **THEN** the file MUST start with the template above, substituting the current year/author, `Generated` timestamp in `YYYY-MM-DDTHH:MM:SSZ` format, and spec/diagram references relevant to the command.

### Requirement: Header Scope & Ordering

The header MUST appear on all tracked Python executables (files in `tools/`, `hybridcore/`, `scripts/` without `.py`, and test entrypoints) before any imports/comments; helper modules MAY omit the hashbang but MUST still include the SPDX block at the top.

#### Scenario: Helper module

- **WHEN** `hybridcore/logs.py` (imported module) is updated
- **THEN** it MAY omit the hashbang but MUST keep the SPDX + metadata block as the first comment block in the file.

### Requirement: Header Enforcement

Repos SHALL provide an automated check (e.g., `python tools/check_license_headers.py` or `ruff check --select CPY`) executed via pre-commit and CI; missing or malformed headers MUST fail the build.

#### Scenario: CI gate

- **WHEN** `npm run lint-docs` or `make lint` runs in CI
- **THEN** the job MUST run the header checker and block merges if files lack the template or contain stale timestamps/spec references.

### Requirement: Prompt Metadata Block

Every file under `docs/proposals/` SHALL include a metadata block immediately after the prompt line with the following fields:

```
<!--
Prompt-Source: docs/proposals/<file>.md
Reference: [specs/<capability>/spec.md#requirement-slug](openspec/specs/<capability>/spec.md#requirement-slug)
Change-Start: <change-id> <ISO8601 timestamp>
Change-Archived: <change-id> <ISO8601 timestamp> | PENDING
-->
```

`Change-Start` records when the proposal change was opened; `Change-Archived` records when it was archived (or `PENDING` if ongoing).

#### Scenario: Prompt metadata example

- **WHEN** `docs/proposals/license-headers-proposal-prompt.md` is updated for change `add-license-header-policy`
- **THEN** it MUST include:

```
<!--
Prompt-Source: docs/proposals/license-headers-proposal-prompt.md
Reference: [specs/governance/spec.md#requirement-license-header-template](openspec/specs/governance/spec.md#requirement-license-header-template)
Change-Start: add-license-header-policy 2025-11-08T10:05:00Z
Change-Archived: add-license-header-policy 2025-11-08T11:15:00Z
-->
```

### Requirement: Metadata Placement & Updates

The metadata block SHALL sit immediately after the `/prompts:openspec-proposal …` line. When opening a new change, contributors MUST add or update `Change-Start`; once archived, they MUST replace `Change-Archived: … PENDING` with the final change ID + timestamp.

#### Scenario: Ongoing proposal

- **WHEN** a new change `add-cross-check-governance` starts
- **THEN** the prompt file MUST set `Change-Start: add-cross-check-governance <timestamp>` and `Change-Archived: PENDING` until the change archives.

### Requirement: Prompt Metadata Enforcement

CI and pre-commit hooks SHALL run a script (e.g., `python tools/check_prompt_metadata.py`) that ensures each prompt contains the metadata block, ISO timestamps, and matching change IDs. Missing or malformed metadata MUST fail the build.

#### Scenario: CI enforcement

- **WHEN** `make lint` runs
- **THEN** it MUST parse each prompt file, confirm the reference link matches the canonical spec, ensure timestamps are ISO8601 UTC, and verify `Change-Archived` is `PENDING` or a valid timestamp; failures block merging.

### Requirement: Changelog Format

The repository SHALL maintain `CHANGELOG.md` (Markdown) following the “Keep a Changelog” layout with sections: `## [Unreleased]`, followed by dated release headers (`## [YYYY-MM-DD] - <version>`). Each entry MUST use bullet points grouped under `### Added`, `### Changed`, `### Fixed`, etc.

#### Scenario: File naming

- **WHEN** a contributor adds a release entry
- **THEN** it MUST be placed in `CHANGELOG.md` under the appropriate heading; the legacy `CHANGELOG` filename MUST NOT be used going forward.

### Requirement: Changelog Entries & Commit Alignment

Every user-facing commit SHALL add (or update) an entry under `## [Unreleased]` that mirrors the commit subject, cites the relevant spec, and, when applicable, links to the short SHA. Entries MUST move from `Unreleased` to the dated section during release cuts.

#### Scenario: Entry content

- **WHEN** the commit `openspec: add commit message policy` lands
- **THEN** `CHANGELOG.md` MUST gain an `### Added` bullet such as `- Define commit message structure (specs/governance/spec.md#requirement-commit-message-structure)` under `Unreleased`.

### Requirement: Changelog Enforcement

CI or pre-commit hooks SHALL verify that any PR touching user-visible code/specs/docs also updates `CHANGELOG.md` (unless explicitly labeled `Changelog: skip`). The hook MUST ensure Markdown headings remain in order and that the `Unreleased` section exists.

#### Scenario: CI gate

- **WHEN** `make lint-changelog` runs
- **THEN** it MUST fail if a qualifying change lacks an entry, if the file is missing, or if headings are out of order.

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

### Requirement: Spec Purpose & Cross-Link Policy

Every capability spec under `openspec/specs/` SHALL include a meaningful Purpose section (no placeholders) and reference related specs/modules when applicable. When sub-specs exist (e.g., hybridcore modules), they MUST link back to the umbrella spec, and the umbrella spec MUST list them.

#### Scenario: Placeholder removal

- **WHEN** a new spec is archived
- **THEN** its Purpose section MUST describe scope in plain language and cite related specs; placeholders like “TBD … Update Purpose” are not permitted.

#### Scenario: Hybridcore cross-links

- **WHEN** a hybridcore module spec is updated or a new module is added
- **THEN** the module spec MUST link to `specs/hybridcore/spec.md`, and the umbrella spec MUST reference the module so tooling and readers can trace the hierarchy.

### Requirement: Open Issues Tracking

The governance spec SHALL expose a `## Open Issues` section that links to `docs/spec-remediations/governance-remediations.md` so repository-wide policies carry explicit remediation visibility.

#### Scenario: Governance remediations

- **WHEN** an assessment surfaces a governance policy gap
- **THEN** the governance spec MUST point readers to `docs/spec-remediations/governance-remediations.md` until the remediation is implemented.

### Requirement: Diagram Verification Workflow

Governance SHALL require a checklist + CI hook ensuring every spec diagram update also refreshes linked docs; CI MUST fail when diagram sources change without doc references.

#### Scenario: Diagram linkage review

- **WHEN** a PR edits a Mermaid file under `specs/`
- **THEN** the checklist and CI hook MUST confirm docs reference the updated diagram before merge.

## Open Issues

See `docs/spec-remediations/governance-remediations.md`.

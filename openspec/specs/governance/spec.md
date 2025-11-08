# governance Specification

## Purpose
TBD - created by archiving change refactor-misplaced-specs. Update Purpose after archive.
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

Reusable prompts under `docs/proposals/` MUST link to the latest approved spec that justifies their guidance.

#### Scenario: Prompt reuse

- **WHEN** a contributor copies a prompt for a new proposal
- **THEN** the prompt MUST already contain a link to the canonical spec, ensuring reviewers can verify the prompt reflects current requirements.

### Requirement: Version-Control Boundaries

Git-tracked content SHALL include templates, scripts, specs, diagrams, and wizard assets; generated outputs (`configs/<env>/*.auto.pkrvars.hcl`, `artifacts/`, `logs/`, `state/`, rendered cloud-init files) MUST remain untracked via `.gitignore`.

#### Scenario: Local overrides

- **WHEN** an operator adds environment-specific overrides or build artifacts
- **THEN** those files MUST stay outside version control so the repository remains portable and free from secrets.

### Requirement: Docstring Coverage

All Python modules, classes, and public functions SHALL include docstrings that: (a) cite the driving spec/diagram IDs, (b) summarize behaviour, inputs, and outputs, and (c) describe side effects or external resources.

#### Scenario: Module/class/function docstrings

- **WHEN** a contributor adds `tools/packer-hybrid/sync.py`
- **THEN** the module-level docstring MUST list the governing spec (e.g., `specs/cli/spec.md#requirement-deterministic-command-surface`), each class docstring MUST cover responsibilities/mixins used, and function docstrings MUST describe parameters + return values, as illustrated:

```python
"""Sync subcommands (spec: specs/cli/spec.md#deterministic)."""

class SourceSyncCommand(CommandMixin):
    """Drive sources sync per specs/hybridcore/spec.md#requirement-source-management."""

    def run(self, args: argparse.Namespace) -> None:
        """Fetch plugins and exit non-zero on drift."""
```

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


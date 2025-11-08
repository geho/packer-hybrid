## ADDED Requirements

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

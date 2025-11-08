## Why

Prompt files in `docs/proposals/` now link to their governing specs, but they do not record when the prompt was first processed or when the associated change was archived. Without timestamps/change IDs, there is no easy provenance trail for when a prompt was last used or whether it is still relevant. Reviewers also lack automation to ensure prompts are updated whenever a change starts or finishes.

## What Changes

- Extend the governance spec with requirements that every prompt includes metadata fields for `Reference`, `Change Start`, and `Change Archived`, capturing ISO timestamps and change IDs.
- Define the canonical metadata block format and how tools verify it.
- Describe compliance checks (linters or scripts) so prompts missing metadata cannot merge.

## Impact

- Creates traceability for every proposal prompt.
- Enables automation to detect stale prompts and cross-check prompt usage with archived changes.
- Policy change only; no runtime code impact.

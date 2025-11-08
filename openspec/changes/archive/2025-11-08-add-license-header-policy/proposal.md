## Why

Executables already “should” include SPDX headers (per project.md), but the repo lacks an enforceable spec describing the exact template, ordering, timestamp format, or how to cite specs/diagrams. Reviews end up nitpicking header consistency, and automation cannot verify compliance.

## What Changes

- Define the canonical license header template (hashbang, SPDX line(s), copyright, timestamp format, spec/diagram references).
- Specify which files require the header (Python executables, mixins reused as scripts, tests as applicable).
- Document automation requirements (linters/hooks/tests) to enforce the header and reject deviations.

## Impact

- Provides a single source of truth for contributors and tooling.
- Enables pre-commit/CI scripts to validate headers automatically, reducing review churn.
- Policy-only change; no runtime behaviour shifts.

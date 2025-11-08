## ADDED Requirements

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

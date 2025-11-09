## Why

`docs/spec-remediations/templates-remediations.md` lists open items (metadata completeness, change detection). Templates spec lacks explicit metadata/change detection guidance. This change adds that requirement.

## What Changes

- Add a requirement describing template metadata fields and change detection rules.
- Update the remediation draft accordingly.

## Impact

- Templates remain deterministic; partial updates are blocked until metadata is complete.

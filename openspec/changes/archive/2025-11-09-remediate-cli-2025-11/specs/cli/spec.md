## MODIFIED Requirements

### Requirement: Diagnostics

`diag` SHALL run the shared redaction hook before bundling, record retention metadata (per the security spec), and emit a manifest listing every scrubbing action.

#### Scenario: Redacted bundle

- **WHEN** `diag` packages logs/manifests/state
- **THEN** it MUST scrub secrets via the shared redaction hook, note retention expiry (per security spec), and include a manifest of redacted files.

### Requirement: Command Catalogue & Arguments

`status|inspect` SHALL emit machine-readable JSON matching a documented schema/version, including field definitions, error codes, and backward-compatibility guidance.

#### Scenario: Status schema enforcement

- **WHEN** `status --format json` runs
- **THEN** it MUST emit the documented schema version and fail if fields are missing or renamed.

### Requirement: Verification & Testing Gates

Verification gates SHALL reference the governing `specs/security/spec.md` sections instead of duplicating rules, and CLI MUST log which gate (by spec ID) it enforced.

#### Scenario: Security gate linkage

- **WHEN** CLI runs `build/publish`
- **THEN** it MUST invoke the security-verified gate and log the spec section ID instead of re-describing the checklist.

### Requirement: Command → Module Mapping

Each command description SHALL cite the corresponding module remediation draft/Open Issues so outstanding dependencies remain visible.

#### Scenario: Cross-link Open Issues

- **WHEN** the CLI spec describes `build`
- **THEN** it MUST cite the relevant `docs/spec-remediations/hybridcore-*` draft so readers can trace dependencies.

### Requirement: Wizard Template Consistency

Wizard/command diagrams SHALL live in the spec and docs MUST embed those diagrams; CI/test tooling MUST fail when docs drift from the spec sources.

#### Scenario: Diagram enforcement

- **WHEN** wizard/command diagrams change in the spec
- **THEN** docs MUST embed the updated diagrams, and CI MUST fail if they fall out of sync.

### Requirement: Clean Scope Retention

`clean --scope ...` SHALL describe which artifacts/logs are preserved for compliance (per the security retention policy) and MUST refuse to delete evidence outside the caller’s scope.

#### Scenario: Preserving compliance evidence

- **WHEN** `clean --scope artifacts` runs
- **THEN** it MUST leave security-required evidence (latest manifests, audit logs) untouched and log what was preserved.

# Proposal: Remediate hybridcore-logs spec

## Why

`docs/spec-remediations/hybridcore-logs-remediations.md` lists five outstanding gaps: sink extension guidance lacks concrete requirements/examples, retention/CLI flag mapping is incomplete, diag bundles don’t describe how log redaction integrates with `diag`, the context schema is ambiguous, and diagrams live only in docs (out of alignment with governance). We need to update the hybridcore-logs spec + tests to address these issues so logging/diags remain compliant with security/governance expectations.

## Scope

- Spec: `openspec/specs/hybridcore-logs/spec.md` and referenced diagrams.
- Docs/tests: `docs/spec-remediations/hybridcore-logs-remediations.md`, `specs/hybridcore-logs/logging-bootstrap.md` (if diagrams need relocation), CLI diag tests.

## What Changes

1. Extend Sink Extensions requirement with explicit guidance/examples for syslog/cloud shippers plus tests ensuring formatter parity.
2. Add retention mapping table tying CLI flags/env vars to rotation thresholds and referencing security retention rules.
3. Document the diag redaction hook integration (logs → diag bundle) and add regression tests verifying redaction occurs before bundling.
4. Define the canonical context schema (required/optional keys, defaults) and add tests enforcing context validation.
5. Move/confirm log bootstrap diagrams live under `specs/hybridcore-logs/`, reference them from the spec, and ensure docs point back per governance.

## Deliverables

- Updated spec sections/diagrams.
- Tests covering sink formatter parity, retention flag mapping, diag redaction integration, and context schema validation.
- Updated remediation doc moving completed items to Closed.
- `openspec validate remediate-hybridcore-logs-2025-11 --strict`.

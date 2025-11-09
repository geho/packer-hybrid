## Why

`docs/spec-remediations/hybridcore-state-remediations.md` calls out missing migration tooling guidance, audit logging, and explicit cross-module references. We need to update the state spec so migrations/rollback/audit behaviour are deterministic and referenced from module remediations.

## What Changes

- Document migration toolkit (version graph, rollback strategy) and audit logging requirements.
- Reference module remediations (templates/sources) in the state spec.
- Update the remediation draft and run validation.

## Impact

- State migrations become auditable and predictable.
- Cross-module alignment improves (templates/sources know which state files they touch).

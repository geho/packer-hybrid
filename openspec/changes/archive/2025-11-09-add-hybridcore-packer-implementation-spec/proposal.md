## Why

`specs/hybridcore-packer/spec.md` captures command wrappers and drift detection but lacks implementation-ready detail on argument mapping, environment prep, manifest capture, drift remediation, artifact tracking, caching/parallel builds, and testing expectations. Contributors need explicit guidance to keep wrappers consistent, ensure drift detection feeds state/logs, and avoid regressions when packer upgrades land.

## What Changes

- Enumerate the behavior for each wrapper (`fmt`, `validate`, `build`): argument/flag mapping, environment setup, log streaming, manifest parsing, and failure escalation semantics.
- Expand drift detection to describe hash computation, manifest comparison, remediation steps, and how results update `hybridcore.state`/`hybridcore.logs`.
- Document artifact tracking (IDs, platforms, metadata JSON), caching, parallel-build rules, and the response contract returned to callers/CI.
- Add exhaustive testing guidance: mocked subprocess coverage, golden manifest tests, integration suites on representative templates, and packer upgrade validation.

## Impact

- Keeps CLI and automation behavior consistent with well-defined wrapper contracts.
- Strengthens drift enforcement and artifact tracking so downstream modules (state/logs) have reliable data.
- Improves CI confidence when packer upgrades occur by requiring thorough testing and manifest validation.

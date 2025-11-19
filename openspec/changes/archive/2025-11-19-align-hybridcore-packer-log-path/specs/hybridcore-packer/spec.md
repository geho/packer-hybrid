## MODIFIED Requirements

### Requirement: Diagnostics & Retention Integration

`hybridcore-packer` SHALL write a log summary (including artifact IDs, manifest path, scrub manifest reference) into `logs/packer/<builder>.json` so security/diagnostics tooling can reference the canonical directory defined in `openspec/project.md`, replacing prior references to `state/packer/logs/<builder>.json`. The requirement SHALL document that `diag` bundles and security tooling read from `logs/`.

#### Scenario: Log summary generation

- **WHEN** a build completes
- **THEN** packer SHALL record the log summary at `logs/packer/<builder>.json` with retention metadata and ensure `diag` bundles include/point to the summary file in that directory.

# Proposal: align-hybridcore-packer-log-path

## Why

`openspec/specs/hybridcore-packer/spec.md` instructs contributors to store diagnostics summaries under `state/packer/logs/<builder>.json`, while `openspec/project.md` establishes `logs/` as the canonical home for CLI + packer logs. This mismatch causes confusion about retention policies and automated tooling paths.

## What Changes

- Update the `hybridcore-packer` spec requirement to point at the project-wide `logs/` structure (e.g., `logs/packer/<builder>.json`).
- Document how retention bundles and `diag` tooling should reference the unified log location.
- Ensure any referenced remediation/open-issue docs stay in sync with the new path.

## Impact

- Aligns spec guidance with the canonical logging policy in `project.md`.
- Unblocks future automation/tests expecting log bundles under `logs/`.
- No behavioural change yet; implementation will follow once proposal is approved.

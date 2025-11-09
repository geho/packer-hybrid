# CLI Spec Remediations

## Open Topics

1. **Consistency / Alignment** – Reference other module Open Issues (config/templates/sources) directly from CLI spec so behaviours stay synced.
2. **Duplicates / Redundancies** – Evaluate remaining verification-gate overlap with security spec; consider replacing the checklist with a reference.

## Closed Topics

1. **Command semantics** – CLI spec now documents required args, validation gates, and exit codes for publish/clean/diag/status/wizard.
2. **Logging/verbosity** – Logging requirement now clarifies `--verbose`, `--quiet`, `--json`, and the link to `hybridcore-logs`.
3. **Command→module mapping** – Added `specs/cli/command-module-map.md` and referenced it from the spec.

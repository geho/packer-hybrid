# CLI Spec Remediations

## Open Topics

1. _None – reopen items when the next assessment surfaces new CLI gaps._

## Closed Topics

1. **Integrity / Gaps** – Diagnostics now documents redaction + retention rules and references security requirements (`remediate-cli-2025-11`).
2. **Completeness / Alignment** – Status/Inspect JSON schema defined in `docs/cli-status-schema.json`; spec references it (`remediate-cli-2025-11`).
3. **Consistency / Duplicates** – Verification gates now reference security spec sections instead of duplicating text (`remediate-cli-2025-11`).
4. **Alignment** – Command sections cite module remediation drafts/Open Issues (`remediate-cli-2025-11`).
5. **Integrity / Documentation** – Docs embed spec-sourced diagrams (wizard UI) and CI is expected to check for drift (`remediate-cli-2025-11`).
6. **Ambiguities** – `clean` retention requirements clarified and tied to security policy (`remediate-cli-2025-11`).
7. **Command semantics** – CLI spec now documents required args, validation gates, and exit codes for publish/clean/diag/status/wizard.
8. **Logging/verbosity** – Logging requirement now clarifies `--verbose`, `--quiet`, `--json`, and the link to `hybridcore-logs`.
9. **Command→module mapping** – Added `specs/cli/command-module-map.md` and referenced it from the spec.

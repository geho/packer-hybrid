# CLI Spec Gaps

Open items (per assessment dimensions):

1. **Gaps / Completeness** – The spec lists commands but omits required arguments/flags, exit codes, and verification gates for `publish`, `clean`, `diag`, `status`, wizard/TUI. Need sub-sections detailing each command’s inputs, expected outputs, and packer validations.
2. **Ambiguities** – Logging/verbosity semantics (`--verbose`, `--json`, `--quiet`) are undefined; wizard/TUI flows are referenced but not specified (screens, validation order, error handling). Clarify these pieces.
3. **Consistency / Alignment** – CLI spec does not cross-reference hybridcore module Open Issues (config, templates, sources). Add references to keep CLI behaviours aligned with backend modules.
4. **Integrity** – No diagrams/table showing command→module interactions; add one to keep workflow clear. Capture CLI-specific Open Issues content (currently pointer only).
5. **Duplicates / Redundancies** – Verification gate text overlaps with the security spec. Consolidate or reference rather than duplicating.

Proposed remediation:

- Extend the CLI spec with per-command tables (inputs, validation, outputs) and wizard/TUI flows.
- Document logging/verbosity matrix and relation to `hybridcore-logs`.
- Reference module Open Issues so CLI stays aligned.
- Create a command-to-module diagram and de-duplicate verification language by referencing the security spec.

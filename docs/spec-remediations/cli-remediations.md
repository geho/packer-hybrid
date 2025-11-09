# CLI Spec Remediations

## Open Topics

1. **Integrity / Gaps** – `diag` only states which files to bundle; it never defines redaction rules, retention/expiration, or how archives are scrubbed before upload. _Plan_: extend the Diagnostics requirement with redaction + retention guidance and add CI tests that assert sensitive tokens are removed from the bundle.
2. **Completeness / Alignment** – `status/inspect` promises machine-readable output but the spec does not define the JSON schema, versioning, or how CLI/CI consumers detect breaking changes. _Plan_: add a schema table covering fields, error codes, and sample payloads plus unit tests that validate the schema contract.
3. **Consistency / Duplicates** – Verification gates in CLI still restate large portions of the security spec. _Plan_: replace the duplicated checklist with references into `specs/security/spec.md` and document how CLI enforces those gates rather than redefining them.
4. **Alignment** – CLI requirements reference hybridcore modules broadly but do not cite the specific `## Open Issues` for config/templates/sources when behaviour overlaps. _Plan_: add explicit cross-links per command so future readers can trace outstanding work in those modules.
5. **Integrity / Documentation** – The spec’s wizard + command diagrams are the canonical source, yet `docs/wizard-ui.md` and other operator docs still embed outdated ASCII renderings. _Plan_: update the docs to embed the Mermaid sources, link back to the spec, and add a regression test that fails if the diagrams drift.

## Closed Topics

1. **Command semantics** – CLI spec now documents required args, validation gates, and exit codes for publish/clean/diag/status/wizard.
2. **Logging/verbosity** – Logging requirement now clarifies `--verbose`, `--quiet`, `--json`, and the link to `hybridcore-logs`.
3. **Command→module mapping** – Added `specs/cli/command-module-map.md` and referenced it from the spec.

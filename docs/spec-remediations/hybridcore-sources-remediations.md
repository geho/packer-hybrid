# Hybridcore Sources Remediations

## Open Topics

1. _None – new gaps will be recorded during the next assessment._

## Closed Topics

1. **Alignment** – Governance override policy is embedded in `openspec/specs/hybridcore-sources/spec.md#requirement-override-approvals--alignment` and backed by the override-flow diagram (`openspec/specs/hybridcore-sources/override-flow.md`) (`remediate-hybridcore-sources-2025-11`).
2. **Integrity (persistence)** – Overrides/mirror inventories persist in state per `#requirement-persistent-overrides--mirror-inventory`, which blocks workflows when metadata is missing and references hybridcore-state requirements (`remediate-hybridcore-sources-2025-11`).
3. **Consistency (security scanning)** – `#requirement-metadata-schema-reference` ties `scan_status` to the security spec and CLI diagnostics so diag bundles always include scanning status (`remediate-hybridcore-sources-2025-11`).
4. **Completeness (resume/repair)** – `#requirement-resume--repair-workflows` defines `sources resume`, state markers, tests, and the resume-flow diagram (`openspec/specs/hybridcore-sources/resume-flow.md`) (`remediate-hybridcore-sources-2025-11`).
5. **Integrity (audit/retention)** – `#requirement-override-audit--retention` sets retention/audit export requirements aligned with security/state specs (`remediate-hybridcore-sources-2025-11`).
6. **Air-gapped workflows** – Spec now documents mirrors/offline bundles and override auditing.
7. **Security scanning** – Scanning cadence recorded in metadata (`scan_status`).
8. **Metadata schema** – Added schema example reference for CLI visibility.

# Hybridcore Sources Remediations

## Open Topics

1. **Alignment** – add future references to governance docs for override approval once defined. _Plan_: pull the policy from `specs/governance/spec.md` into this spec and add a scenario for manual overrides.
2. **Integrity** – Override approvals and mirror inventories are not persisted anywhere. _Plan_: require `hybridcore.state` to record overrides plus include validation/tests that fail when metadata is missing.
3. **Consistency** – Security scanning cadence is recorded in metadata but not tied to the security spec or CLI diagnostics. _Plan_: document how scan status is surfaced to CLI and ensure `diag` bundles include the metadata snapshot.

## Closed Topics

1. **Air-gapped workflows** – Spec now documents mirrors/offline bundles and override auditing.
2. **Security scanning** – Scanning cadence recorded in metadata (`scan_status`).
3. **Metadata schema** – Added schema example reference for CLI visibility.

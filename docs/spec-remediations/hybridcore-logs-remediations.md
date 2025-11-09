# Hybridcore Logs Remediations

## Open Topics

1. **Integrity** – Document remaining enhancements (e.g., future cloud log collectors) once requirements solidify. _Plan_: extend the Sink Extensions requirement with examples for syslog/cloud shippers plus tests that verify formatter parity.
2. **Completeness / Alignment** – Retention guidance mentions policy hooks but never states how CLI flags propagate to rotation thresholds or security retention mandates. _Plan_: add a table mapping CLI flags/env vars to rotation settings and cross-link to the security spec.
3. **Consistency** – Diagnostics bundles rely on logs, yet the spec does not describe how log redaction integrates with `diag` archives. _Plan_: add a scenario covering log scrub hooks triggered before diag packaging and document the required tests.

## Closed Topics

1. **Log shipping & flags** – Spec now covers sink extensions and CLI flag interplay.
2. **Retention guidance** – Added retention/audit alignment requirement.

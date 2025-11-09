# Hybridcore Logs Remediations

## Open Topics

1. **Integrity** – Document remaining enhancements (e.g., future cloud log collectors) once requirements solidify. _Plan_: extend the Sink Extensions requirement with examples for syslog/cloud shippers plus tests that verify formatter parity.
2. **Completeness / Alignment** – Retention guidance mentions policy hooks but never states how CLI flags propagate to rotation thresholds or security retention mandates. _Plan_: add a table mapping CLI flags/env vars to rotation settings and cross-link to the security spec.
3. **Consistency** – Diagnostics bundles rely on logs, yet the spec does not describe how log redaction integrates with `diag` archives. _Plan_: add a scenario covering log scrub hooks triggered before diag packaging and document the required tests.
4. **Ambiguities** – Context propagation lists example fields but never defines the canonical schema for `ctx`. _Plan_: document the required/optional context keys, defaulting behaviour, and add tests that fail if callers omit mandatory fields.
5. **Alignment** – Governance now mandates diagram verification, but the log bootstrap diagrams still live only in docs and are not referenced from the spec. _Plan_: move/update the diagrams under `specs/hybridcore-logs/` and link them both ways.

## Closed Topics

1. **Log shipping & flags** – Spec now covers sink extensions and CLI flag interplay.
2. **Retention guidance** – Added retention/audit alignment requirement.

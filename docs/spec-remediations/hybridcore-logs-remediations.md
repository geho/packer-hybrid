# Hybridcore Logs Spec Gaps

1. **Gaps** – Missing coverage for log shipping integrations (cloud sinks, syslog), and CLI flag interplay (`--verbose`, `--json`).
2. **Completeness** – No retention/rotation policy guidance beyond size/time thresholds; specify retention config and artifact retention expectations.
3. **Alignment** – Should reference security/CLI specs for audit logging, but doesn’t.
4. **Integrity** – Need Open Issues content beyond pointer (list pending enhancements) and cross-reference diagrams for new sinks.

Remediation: add sections covering log shipping, retention policies, CLI flag interactions, and audit logging alignment.

# Hybridcore State Spec Gaps

1. **Gaps** – State spec lacks detailed schema migration tooling guidance (version graph, rollback strategy) and concurrent writer coordination beyond `atomic write` statements.
2. **Completeness** – No mention of audit logging for state changes or integration with security/compliance requirements.
3. **Alignment** – Cross-module references (e.g., templates and sources) should specify which state files they update; currently implied but not explicit.

Remediation: add migration workflow details, audit requirements, and explicit references to per-module state interactions.

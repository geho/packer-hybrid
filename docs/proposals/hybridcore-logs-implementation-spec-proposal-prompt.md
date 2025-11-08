/prompts:openspec-proposal Hybridcore Logs implementation-ready spec:

- Capture the logging stack end-to-end: initialization hooks in CLI/tests, formatter/handler configuration, rotation policies, redaction filters, and how log shipping integrates with CI artifacts.
- Specify context propagation (env, component, command IDs), structured logging fields, masking rules, and the boundary between shared helpers vs. module-specific enrichers.
- Detail observability tests (unit + integration) covering concurrency, rotation, log corruption recovery, and contract tests that diff emitted lines to fixtures.
- Include guidance for extending log sinks (e.g., JSON, syslog) without breaking the canonical `[timestamp] level component message` format, plus upgrade paths for backward compatibility.
  - Reference diagrams: [logging bootstrap](openspec/specs/hybridcore-logs/logging-bootstrap.md), [context propagation](openspec/specs/hybridcore-logs/context-flow.md), [rotation recovery](openspec/specs/hybridcore-logs/rotation-recovery.md).
    References: [openspec/specs/hybridcore-logs/spec.md](openspec/specs/hybridcore-logs/spec.md), [openspec/specs/hybridcore/spec.md](openspec/specs/hybridcore/spec.md)

<!--
Prompt-Source: docs/proposals/hybridcore-logs-implementation-spec-proposal-prompt.md
Reference: [openspec/specs/hybridcore-logs/spec.md](openspec/specs/hybridcore-logs/spec.md)
Change-Start: add-hybridcore-logs-implementation-spec 2025-11-08T21:00:00Z
Change-Archived: add-hybridcore-logs-implementation-spec 2025-11-08T21:46:40Z
-->

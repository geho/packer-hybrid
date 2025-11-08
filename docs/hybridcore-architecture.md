# Hybridcore Architecture Overview

Two detailed diagrams live inside the governance-backed spec. References: [specs/hybridcore/spec.md#requirement-hybridcore-component-diagram](openspec/specs/hybridcore/spec.md#requirement-hybridcore-component-diagram), [specs/hybridcore/spec.md#requirement-packer-hybrid-integration-diagram](openspec/specs/hybridcore/spec.md#requirement-packer-hybrid-integration-diagram).

1. **Hybridcore Component Relationships** – shows how `packer-hybrid` CLI calls each module.
2. **Packer-Hybrid ↔ Hybridcore Dependencies** – captures invocation order and shared assets.

Simplified view:

```
CLI -> hybridcore.config -> hybridcore.templates -> hybridcore.provisioners
CLI -> hybridcore.sources -> hybridcore.packer -> hybridcore.state/logs
```

Consult the spec for full Mermaid diagrams and scenarios. Reference: [specs/hybridcore/spec.md](openspec/specs/hybridcore/spec.md).

## Logging Bootstrap Flow

For troubleshooting log initialization, see the dedicated diagram in [specs/hybridcore-logs/logging-bootstrap.md](openspec/specs/hybridcore-logs/logging-bootstrap.md). It illustrates how `init_logging` loads thresholds, attaches console/file handlers, registers CLI/pytest hooks, and streams artifacts to CI.

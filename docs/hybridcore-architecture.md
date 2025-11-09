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

## Config Pipeline Overview

The end-to-end configuration pipeline (input discovery → schema validation → deterministic merge → render → state manifest updates) is captured in [specs/hybridcore-config/config-pipeline.md](openspec/specs/hybridcore-config/config-pipeline.md). Use this when debugging overlay precedence, unused key warnings, or manifest drift.

## State Artifact Map

To understand how JSON artifacts under `state/` relate (sources pins, config hashes, packer manifests, index), see [specs/hybridcore-state/state-map.md](openspec/specs/hybridcore-state/state-map.md). Reference it when debugging drift detection or state corruption.

## Packer Wrapper Flow

For the execution pipeline (env prep → packer CLI → manifest capture → state/log updates), reference [specs/hybridcore-packer/wrapper-flow.md](openspec/specs/hybridcore-packer/wrapper-flow.md). Use it when reasoning about new flags or automation entrypoints.

## Provisioner Compatibility Matrix

Before toggling provisioners for a platform, consult [specs/hybridcore-provisioners/compat-matrix.md](openspec/specs/hybridcore-provisioners/compat-matrix.md). It shows supported combinations and extension hooks for future tools.

## Template Composition Flow

Template composition (inventory → common/platform layers → manifests) is illustrated in [specs/hybridcore-templates/composition-flow.md](openspec/specs/hybridcore-templates/composition-flow.md). Use it when onboarding new builders or debugging packer inputs.

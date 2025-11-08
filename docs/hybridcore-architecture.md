# Hybridcore Architecture Overview

Two detailed diagrams live inside `openspec/changes/refactor-misplaced-specs/specs/hybridcore/spec.md`:

1. **Hybridcore Component Relationships** – shows how `packer-hybrid` CLI calls each module.
2. **Packer-Hybrid ↔ Hybridcore Dependencies** – captures invocation order and shared assets.

Simplified view:

```
CLI -> hybridcore.config -> hybridcore.templates -> hybridcore.provisioners
CLI -> hybridcore.sources -> hybridcore.packer -> hybridcore.state/logs
```

Consult the spec for full Mermaid diagrams and scenarios.

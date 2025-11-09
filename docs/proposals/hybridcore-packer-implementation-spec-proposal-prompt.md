/prompts:openspec-proposal Hybridcore Packer implementation-ready spec:

- Enumerate every wrapper around `packer fmt|validate|build`, argument/flag mapping, environment preparation, manifest capture, and failure escalation semantics (retryable vs hard stop).
- Define drift-detection mechanics (hash inputs, manifest comparison, required remediation steps) and how results feed into `hybridcore.state`, `hybridcore.logs`, and downstream automation.
- Document artifact tracking (IDs, platforms, metadata JSON), caching, parallel builds, and the precise data contract returned to callers/CI.
- Require exhaustive testing guidance: mocked subprocess coverage, golden manifest tests, integration suites that run on representative templates, and how packer upgrades are validated.
  - Reference diagrams: [wrapper flow](openspec/specs/hybridcore-packer/wrapper-flow.md), [drift flow](openspec/specs/hybridcore-packer/drift-flow.md), [artifact registry](openspec/specs/hybridcore-packer/artifact-registry.md).
    References: [openspec/specs/hybridcore-packer/spec.md](openspec/specs/hybridcore-packer/spec.md), [openspec/specs/hybridcore/spec.md](openspec/specs/hybridcore/spec.md)

<!--
Prompt-Source: docs/proposals/hybridcore-packer-implementation-spec-proposal-prompt.md
Reference: [openspec/specs/hybridcore-packer/spec.md](openspec/specs/hybridcore-packer/spec.md)
Change-Start: add-hybridcore-packer-implementation-spec 2025-11-09T12:00:00Z
Change-Archived: add-hybridcore-packer-implementation-spec 2025-11-09T12:39:38Z
-->

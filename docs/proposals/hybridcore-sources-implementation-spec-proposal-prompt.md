/prompts:openspec-proposal Hybridcore Sources implementation-ready spec:

- Detail the lifecycle of managed repositories (clone, fetch, checkout, pin) including concurrency rules, air-gapped workflows, allowed transports, and enforcement of clean working trees before updates.
- Specify required metadata structures (`state/sources.json`, lock files), atomic write strategies, schema evolution, and visibility surfaces (CLI commands, status dashboards).
- Cover failure recovery (partially cloned repos, network retries, manual overrides), auditing (who changed which SHA), and integration with security scanning of source repos.
- Mandate test strategies: mocked git invocations, contract tests ensuring metadata correctness, and optional integration suites that operate on real sample repos with shallow clones.
  - Reference diagrams: [metadata flow](openspec/specs/hybridcore-sources/metadata-flow.md), [recovery flow](openspec/specs/hybridcore-sources/recovery-flow.md), [testing matrix](openspec/specs/hybridcore-sources/testing-matrix.md).
    References: [openspec/specs/hybridcore-sources/spec.md](openspec/specs/hybridcore-sources/spec.md), [openspec/specs/hybridcore/spec.md](openspec/specs/hybridcore/spec.md)

<!--
Prompt-Source: docs/proposals/hybridcore-sources-implementation-spec-proposal-prompt.md
Reference: [openspec/specs/hybridcore-sources/spec.md](openspec/specs/hybridcore-sources/spec.md)
Change-Start: add-hybridcore-sources-implementation-spec 2025-11-09T14:00:00Z
Change-Archived: add-hybridcore-sources-implementation-spec 2025-11-09T14:40:45Z
-->

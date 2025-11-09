# Packer Upgrade Playbook

Use [specs/hybridcore-packer/artifact-registry.md](openspec/specs/hybridcore-packer/artifact-registry.md) and [specs/hybridcore-packer/drift-flow.md](openspec/specs/hybridcore-packer/drift-flow.md) when planning packer upgrades. Ensure wrappers, drift checks, and artifact registries remain stable across versions.

Checklist:

1. Run the mocked + integration suites against new packer version.
2. Compare manifests/artifacts to golden fixtures.
3. Update docs/spec references if new flags or behaviors arise.
4. Communicate upgrade steps to automation consumers.

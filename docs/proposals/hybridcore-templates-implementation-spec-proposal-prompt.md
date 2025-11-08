/prompts:openspec-proposal Hybridcore Templates implementation-ready spec:

- Map template composition end-to-end: builder inventory, directory layout, naming rules, dependency resolution between common/platform layers, and how outputs feed `packer fmt|validate|build`.
- Define deterministic ordering guarantees, manifest generation, checksum caching, and how new OS/platform combinations are introduced without breaking consumers.
- Specify metadata that must accompany each builder (supported provisioners, required configs, scripts), plus validation hooks ensuring references stay in sync with repos and state files.
- Describe rigorous testing: schema/naming linters, golden composition fixtures, packer fmt/validate in CI per builder set, and change-detection rules to block partial updates.
  References: [openspec/specs/hybridcore-templates/spec.md](openspec/specs/hybridcore-templates/spec.md), [openspec/specs/hybridcore/spec.md](openspec/specs/hybridcore/spec.md)

<!--
Prompt-Source: docs/proposals/hybridcore-templates-implementation-spec-proposal-prompt.md
Reference: [openspec/specs/hybridcore-templates/spec.md](openspec/specs/hybridcore-templates/spec.md)
Change-Start: PENDING
Change-Archived: PENDING
-->

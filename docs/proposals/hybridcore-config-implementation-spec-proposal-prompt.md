/prompts:openspec-proposal Hybridcore Config implementation-ready spec:

- Map every stage from input discovery (defaults, env overlays, CLI answers) through schema validation and `.auto.pkrvars.hcl` rendering, including failure modes, warnings, and how unused keys are surfaced.
- Describe the exact file/dir layout, naming, and hashing rules for generated vars plus how secrets use indirection (`env()`, vault paths) without ever writing cleartext.
- Define cross-module integrations (state snapshots, templates, packer, provisioners) and the regression-testing surface: golden fixtures, hash comparisons, and negative coverage for overlay conflicts.
- Provide implementation-ready checklists for new inputs (schema patching, docs, automated tests) and outline extendability rules for future environments/platforms.
  References: [openspec/specs/hybridcore-config/spec.md](openspec/specs/hybridcore-config/spec.md), [openspec/specs/hybridcore/spec.md](openspec/specs/hybridcore/spec.md)

<!--
Prompt-Source: docs/proposals/hybridcore-config-implementation-spec-proposal-prompt.md
Reference: [openspec/specs/hybridcore-config/spec.md](openspec/specs/hybridcore-config/spec.md)
Change-Start: PENDING
Change-Archived: PENDING
-->

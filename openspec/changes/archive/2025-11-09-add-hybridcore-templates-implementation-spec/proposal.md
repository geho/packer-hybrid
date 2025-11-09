## Why

`specs/hybridcore-templates/spec.md` captures builder inventory, composition outputs, and testing, but doesn't provide implementation-ready detail on directory layout, naming rules, dependency resolution, deterministic ordering, manifest/checksum handling, metadata per builder, or rigorous testing/linting requirements. Contributors need prescriptive guidance to avoid regressions when composing templates across OS/platform combinations and when adding new builders.

## What Changes

- Map template composition end-to-end: builder inventory, directory structure, naming conventions, dependency resolution across common/platform layers, and how outputs feed `packer fmt|validate|build`.
- Define deterministic ordering guarantees, manifest generation, checksum caching, and onboarding rules for new OS/platform combinations.
- Specify metadata required per builder (supported provisioners, required configs/scripts), plus validation hooks ensuring references stay in sync with repos/state files.
- Describe rigorous testing: schema/naming linters, golden composition fixtures, packer fmt/validate coverage per builder set, and change-detection rules to block partial updates.

## Impact

- Keeps template composition predictable and debuggable across all target platforms.
- Prevents drift between builder metadata, provisioner dependencies, and state references.
- Strengthens CI by requiring comprehensive linters, fixtures, and packer validation per builder set.

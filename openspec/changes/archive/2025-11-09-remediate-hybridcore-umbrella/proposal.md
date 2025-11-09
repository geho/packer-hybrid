## Why

`docs/spec-remediations/hybridcore-remediations.md` lists open topics for the umbrella spec: missing module registry, unclear cross-module dependencies, absent orchestration diagram, no references to module Open Issues, and duplicated module-level requirements. We need to remediate the umbrella spec so it defines module criteria, dependency rules, and references, keeping it aligned with module-level specs.

## What Changes

- Add a module registry table describing existing and planned `hybridcore-*` capabilities (including naming guidance for new modules like metrics/eventing).
- Define dependency/interaction guidelines between modules and consumers (CLI/automation).
- Reference each module’s `## Open Issues` draft so umbrella readers can find outstanding work.
- Introduce an orchestration diagram showing config → templates → packer → state flows.
- Trim duplicated per-module requirements in favour of concise pointers.

## Impact

- Umbrella spec becomes the authoritative overview for modules, dependencies, and future extensions.
- Readers can jump from umbrella spec to module Open Issues, ensuring alignment.
- Reduces duplication and clarifies the onboarding path for new modules.

## Why

The existing `specs/hybridcore/spec.md` covers module boundaries and diagrams but doesn’t document the detailed contracts (inputs/outputs, serialization formats, dependency boundaries, testing requirements) for each sub-module. Contributors need module-level specs to avoid bloating the umbrella file and to match the repo’s modular code structure.

## What Changes

- Keep `specs/hybridcore/spec.md` as the umbrella spec and add sibling capabilities per module: `hybridcore-config`, `hybridcore-sources`, `hybridcore-templates`, `hybridcore-provisioners`, `hybridcore-packer`, `hybridcore-state`, and `hybridcore-logs`.
- Update the umbrella spec to reference each sub-spec, define naming conventions, and explain when to add new module specs.
- Each module spec will document data contracts, serialization formats, dependency boundaries, and testing expectations.

## Impact

- Provides clear, modular specs aligned with the codebase hierarchy.
- Keeps each spec focused and easier to maintain.
- Enables CLI/Django consumers to rely on the same documented interfaces.

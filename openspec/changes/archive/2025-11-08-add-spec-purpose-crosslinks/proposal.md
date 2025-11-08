## Why

Most specs still contain the placeholder “TBD – created by archiving change … Update Purpose after archive,” and the hybridcore module specs don’t explicitly cross-link to the umbrella spec despite the new module hierarchy policy. Without real purpose statements and mutual links, readers struggle to understand scope, and we risk future drift.

## What Changes

- Replace the placeholder Purpose sections across every spec under `openspec/specs/` with concise descriptions of each capability.
- Update the hybridcore umbrella spec to reiterate the module hierarchy guidance and ensure each module spec links back to the umbrella (and is referenced by it).
- Make sure documentation about the hierarchy (in governance or hybridcore spec) clarifies when to add new module specs.

## Impact

- Improves clarity for contributors and aligns with OpenSpec’s requirements for meaningful Purpose statements.
- Reinforces the cross-linking policy, making it easier to maintain the hybridcore package as it grows.
- Documentation-only change; no runtime code impact.

## Why

`docs/spec-remediations/hybridcore-packer-remediations.md` lists missing cache policies, parallel build guidance, cross-module references, and drift detection/upgrade gating details. The packer spec currently focuses on wrappers/drift detection but doesn’t describe cache invalidation, resource limits, or references to templates/provisioners Open Issues.

## What Changes

- Add cache/parallel build requirements (resource limits, cache invalidation rules, examples for iso/artifact caches).
- Reference templates/provisioners/state remediations so packer changes stay aligned.
- Document drift detection enhancements (e.g., incremental hashing) and upgrade gating expectations.

## Impact

- Packer spec becomes deterministic for caching/parallelism, reducing wasted builds.
- Cross-module references keep packer aligned with templates/provisioners/state.
- Upgrade gating instructions ensure packer version bumps run the required validation suite.

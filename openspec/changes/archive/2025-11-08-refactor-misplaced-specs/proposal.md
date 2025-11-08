## Summary

The repository currently contains fully fleshed CLI, hybridcore, template, provisioning, and security specifications directly under `openspec/specs/` without any associated OpenSpec change. This breaks the required workflow, leaves the specs without traceability, and prevents reviewers from understanding when and why these foundational requirements were introduced.

This change wraps those existing requirements in a formal proposal so they can be reviewed, validated, and eventually archived through the standard OpenSpec process.

## Motivation

- Restore provenance for the initial platform specifications so future updates can reference an approved change ID.
- Keep the `openspec/specs/` directory reserved for archived/approved specs only.
- Ensure every capability (CLI command surface, hybridcore modules, multi-cloud template structure, provisioning stacks, and security posture) is captured as an `ADDED` delta with scenarios, ready for reviewers to accept or iterate on.

## Impact

- No runtime code impact; this is documentation/spec hygiene.
- Provides a baseline change ID that future work (implementations or follow-up specs) can cite.
- Enables the repository to re-align with enforcement automation that expects specs to originate from `openspec/changes/<id>/`.

# Proposal: cleanup-hybridcore-packer-duplicate-requirements

## Why

The `hybridcore-packer` spec currently repeats several requirements (incremental hash manifests, result schema/exit codes, diagnostics & retention) under both the main Requirements section and the `## ADDED Requirements` block. This violates OpenSpec guidance against duplicated requirements, creates ambiguity about which block is authoritative, and risks future edits drifting between the two copies.

## What Changes

- Consolidate the duplicated requirement text into a single authoritative section.
- Update cross-references so scenarios remain under the surviving block and ensure numbering/table context stays intact.
- Add clarification text (if needed) to explain the original ADDED block intent once duplication is resolved.

## Impact

- Clearer spec structure for `hybridcore-packer` contributors.
- Reduces risk of inconsistent future edits between duplicated sections.
- No behavioural change yet; implementation will follow existing requirement semantics.

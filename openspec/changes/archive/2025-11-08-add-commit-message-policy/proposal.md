## Why

Commit messages currently follow ad-hoc conventions; some include scope prefixes while others do not cite specs or tests. Without an enforced structure, it’s harder to trace changes back to specs or confirm that verification steps ran. A formal policy will align every commit with the spec-first workflow.

## What Changes

- Define a canonical commit message format (`<scope>: <summary>`) plus required body sections referencing spec IDs, diagrams, and verification checklists.
- Describe acceptable scopes (directories, `openspec`, `docs`, etc.) and how to cite multiple specs.
- Require automation (lint hooks) that rejects commits lacking the format.

## Impact

- Improves traceability between specs and implementation.
- Makes reviews faster because required information (tests run, doc/spec references) is always present.
- Policy-only change within the governance spec.

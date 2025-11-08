## Why

`specs/hybridcore-config/spec.md` documents the high-level merge rules, serialization format, and testing expectations, but implementers lack deeper guidance on how inputs flow from discovery through schema validation to `.auto.pkrvars.hcl` rendering. Secrets handling, file layout, hashing strategy, cross-module integrations (state/templates/packer/provisioners), and onboarding checklists for new environments are undocumented, leading to drift and inconsistent regression coverage.

## What Changes

- Expand the config inputs/overlays requirement to describe the full pipeline (discovery → schema validation → merge → render), failure/warning semantics, and how unused keys are surfaced.
- Enhance the serialization requirement with explicit file/directory layouts, naming conventions, hashing rules, and indirection requirements for secrets.
- Add new requirements covering cross-module integrations (state snapshots, templates, packer, provisioners) plus mandatory regression tests (golden fixtures, hash comparisons, negative overlay cases).
- Add an extendability checklist for introducing new inputs or environments (schema patches, docs, automated tests, compatibility gates).

## Impact

- Contributors receive implementation-ready instructions, reducing guesswork for overlay logic and artifacts.
- Strengthens CI by specifying hashing, fixtures, and negative tests to prevent regressions before packer builds.
- Keeps secrets and cross-module state consistent by mandating indirection and documented integration points.

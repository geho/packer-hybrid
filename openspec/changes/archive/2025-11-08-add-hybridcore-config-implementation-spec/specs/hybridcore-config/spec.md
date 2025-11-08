## MODIFIED Requirements

### Requirement: Config Inputs & Overlays

`hybridcore-config` SHALL orchestrate the full pipeline:

1. **Discovery** – load template defaults, environment overlays, `.auto.pkrvars.hcl` seeds, and CLI answers. Each source MUST provide provenance metadata (file path, env, timestamp).
2. **Schema validation** – validate the merged candidate against the canonical schema (`schema/config.schema.json`). Failures MUST block rendering and emit actionable errors listing the offending keys + source metadata.
3. **Merge** – apply precedence `defaults -> env -> CLI` while tracking unused keys; unused entries SHALL produce warnings and appear in the rendered comments.
4. **Render** – emit `.auto.pkrvars.hcl` with deterministic ordering plus provenance comments.

Failures MUST stop at the earliest stage, while warnings SHALL accumulate and be surfaced in both console output and generated comments.

See `specs/hybridcore-config/config-pipeline.md` for the end-to-end flow.

#### Scenario: Overlay conflict

- **WHEN** `prod.hcl` sets `image="v1"` and CLI overrides `image="v2"` without schema approval
- **THEN** the merge stage MUST reject the change, citing both sources and recommending a schema update before re-run.

### Requirement: Serialization Format

Rendered vars MUST follow this structure:

- Files live under `templates/<env>/.auto.pkrvars.hcl` (one per target env), plus hashed copies under `state/config/<env>.json` capturing sha256 of the rendered file.
- Keys are ordered alphabetically within logical groups (builders, provisioners, secrets) and include inline comments referencing the source spec section.
- Secrets MUST always use indirection (`env("TOKEN")`, vault path placeholders) and reference the associated secret definition doc.
- Each render MUST update a manifest entry (`state/config/index.json`) containing file paths, hashes, and timestamps.

#### Scenario: Secret reference

- **WHEN** `PROXMOX_TOKEN` is required
- **THEN** the vars file MUST contain `env("PROXMOX_TOKEN")`, reference the secret doc in a comment, and the manifest MUST record the hash without storing cleartext.

## ADDED Requirements

### Requirement: Cross-Module Integrations & Regression Tests

`hybridcore-config` SHALL write state snapshots (hash + provenance) that `hybridcore.state`, `hybridcore.templates`, `hybridcore.packer`, and `hybridcore.provisioners` consume to detect drift. CI MUST run:

- Golden fixture comparisons for representative envs/platforms.
- Hash regression checks comparing new renders vs. stored hashes.
- Negative overlay tests (missing overrides, conflicting keys) ensuring descriptive errors.

#### Scenario: Drift detection

- **WHEN** template changes alter a vars file hash
- **THEN** the state snapshot MUST record the new hash, and downstream modules MUST detect drift before packer builds continue.

Data flow between modules is illustrated in `specs/hybridcore-config/config-integrations.md`.

### Requirement: Extendability Checklist

Adding new inputs or environments SHALL follow this checklist:

1. Update the schema with defaults + validation rules.
2. Document the input (README + spec cross-reference).
3. Add golden fixtures + regression tests covering positive/negative overlays.
4. Update onboarding docs so operators know how to provide the new values.

#### Scenario: New environment onboarding

- **WHEN** a `qa` environment is added
- **THEN** the contributor MUST patch the schema, add `templates/qa/.auto.pkrvars.hcl` fixtures, document the input expectations, and ensure CI includes `qa` in regression suites.

The contributor workflow is summarized in `specs/hybridcore-config/config-extendability.md`.

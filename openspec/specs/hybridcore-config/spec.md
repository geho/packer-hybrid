# hybridcore-config Specification

## Purpose

Detail the data contracts, inputs/overlays, and testing expectations for `hybridcore.config`, extending the umbrella hybridcore spec. Reference: [specs/hybridcore/spec.md](openspec/specs/hybridcore/spec.md)
## Requirements
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

Rendered vars MUST follow this structure and include provenance metadata recorded alongside `state/config/<env>.json`:

- Files live under `templates/<env>/.auto.pkrvars.hcl` (one per target env), plus hashed copies under `state/config/<env>.json` capturing sha256 of the rendered file and provenance metadata (source overlay, timestamp, secret indirection notes).
- Keys are ordered alphabetically within logical groups (builders, provisioners, secrets) and include inline comments referencing the source spec section.
- Secrets MUST always use indirection (`env("TOKEN")`, vault path placeholders) and reference the associated secret definition doc.
- Each render MUST update a manifest entry (`state/config/index.json`) containing file paths, hashes, timestamps, and provenance metadata linking back to source files and remediation drafts.
- Each render MUST update a manifest entry (`state/config/index.json`) containing file paths, hashes, timestamps, overlay sources, referenced remediation drafts, and secret indirection notes so provenance reviews remain auditable.

#### Scenario: Secret reference

- **WHEN** `PROXMOX_TOKEN` is required
- **THEN** the vars file MUST contain `env("PROXMOX_TOKEN")`, reference the secret doc in a comment, and the manifest MUST record the hash without storing cleartext.

### Requirement: Testing

`hybridcore-config` SHALL provide unit tests covering schema validation, overlay precedence, deterministic output (e.g., hash comparisons), and severity mapping (warnings vs failures). CI MUST run these tests before merging.

#### Scenario: Regression prevention

- **WHEN** a contributor modifies overlay logic
- **THEN** the associated unit tests MUST catch ordering regressions by comparing rendered files against golden fixtures.

### Requirement: Schema Validation Severity

Schema validation SHALL define severity/exit-code mapping for warnings vs failures so CLI callers know how to react consistently.

#### Scenario: Severity mapping

- **WHEN** validation encounters warnings
- **THEN** it SHALL exit 0 with logged warnings; fatal errors SHALL exit non-zero and tests MUST cover both paths.

### Requirement: Cross-Module Integrations & Regression Tests

The config spec SHALL reference the templates/state Open Issues (and their remediation drafts) so drift detection contracts stay synchronized.

#### Scenario: Drift linkage

- **WHEN** templates or state Open Issues change
- **THEN** the config spec SHALL reference the updated remediation drafts so operators can trace dependencies.

### Requirement: Config Pipeline Diagram

The spec SHALL include the Mermaid diagram showing discovery → schema validate → merge/render → state update, and docs MUST link back to it instead of duplicating.

#### Scenario: Diagram availability

- **WHEN** reviewers inspect the config pipeline
- **THEN** they SHALL use the spec-hosted diagram, and `docs/` MUST reference it instead of duplicating.

### Requirement: Extendability Checklist

Adding new inputs or environments SHALL follow this checklist:

1. Update the schema with defaults + validation rules.
2. Document the input (README + spec cross-reference).
3. Add golden fixtures + regression tests covering positive/negative overlays and update the config→provisioning mapping table so inputs reference the provisioning spec/templates rather than duplicate schema snippets.
4. Update onboarding docs so operators know how to provide the new values.

#### Scenario: New environment onboarding

- **WHEN** a `qa` environment is added
- **THEN** the contributor MUST patch the schema, add `templates/qa/.auto.pkrvars.hcl` fixtures, document the input expectations, and ensure CI includes `qa` in regression suites.

The contributor workflow is summarized in `specs/hybridcore-config/config-extendability.md`.

### Requirement: Provisioning Input Mapping

Config SHALL reference the provisioning spec/templates for input schemas instead of duplicating fields; a mapping table MUST link each config input to its provisioning source of truth.

#### Scenario: Reference over duplication

- **WHEN** config requirements mention provisioning inputs
- **THEN** they SHALL link to provisioning spec sections/templates rather than restate fields.

### Requirement: Extendability & Secrets

Spec SHALL describe secret handling requirements in the extendability checklist.

#### Scenario: Secret onboarding

- **WHEN** a new secret is introduced
- **THEN** docs/tests MUST reference env/secret manager usage without storing cleartext.

### Requirement: OS Platform & Variant Overlays

Spec SHALL document platform/variant overlay precedence with examples.

#### Scenario: Variant precedence

- **WHEN** Azure variant overrides secrets
- **THEN** precedence MUST follow defaults → platform → variant → CLI answers.

### Requirement: Manifest & State Integration

Rendered configs SHALL emit provenance metadata (hashes, overlay sources, secret indirection notes) and record the data alongside state to support audits.

#### Scenario: Provenance metadata

- **WHEN** configs render `.auto.pkrvars.hcl`
- **THEN** the manifest SHALL record file hashes, source overlays, and secret references; tests must verify these fields.

### Requirement: Open Issues Tracking

The hybridcore-config spec SHALL keep a `## Open Issues` section pointing to `docs/spec-remediations/hybridcore-config-remediations.md`. Assessments MUST summarize outstanding gaps per dimension in that doc and cross-reference it from the spec.

#### Scenario: Remediation linkage

- **WHEN** a spec assessment uncovers deviations for the hybridcore-config spec
- **THEN** contributors SHALL update `docs/spec-remediations/hybridcore-config-remediations.md` and refresh the spec's `## Open Issues` pointer before merging changes.

## Open Issues

See `docs/spec-remediations/hybridcore-config-remediations.md`.

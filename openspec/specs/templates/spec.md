# templates Specification

## Purpose

Define the multi-cloud template layout (common/platform HCL, vars, scripts, configs, artifacts, state) plus validation/drift rules so Proxmox, vSphere, and Azure builds stay aligned.

## Requirements

### Requirement: Repository Layout

The repository SHALL follow a multi-cloud layout containing `templates/`, `configs/`, `sources/`, `artifacts/`, `logs/`, and `state/`.

#### Scenario: Templates tree

- **WHEN** `init` scaffolds the repo
- **THEN** it MUST create:
  - `templates/common.pkr.hcl`
  - `templates/platforms/{proxmox,vsphere,azure}.pkr.hcl`
  - `templates/vars/{linux,windows}/{common,<platform>}.pkrvars.hcl`
  - `templates/scripts/{linux,windows}`
  - `templates/ansible` (and optional `templates/puppet`)

### Requirement: Composition Model

Common builders SHALL live in `common.pkr.hcl`; platform-specific sources live in per-cloud files and share the naming convention `source.<plugin>-iso.<image>` or `source.azure-arm.<image>`.

#### Scenario: Source references

- **WHEN** `packer build` runs
- **THEN** the combined HCL MUST reference sources using the standardized names so the CLI can dynamically select targets.

### Requirement: Environment Configs

`configs/<env>/` MUST store generated `.auto.pkrvars.hcl` files per platform/OS, created via the CLI and never edited manually.

#### Scenario: Config generation

- **WHEN** `packer-hybrid config --env prod --targets vsphere,azure` runs
- **THEN** only those platform var files are written/updated, leaving others untouched.

### Requirement: Artifacts and Logs

`artifacts/` SHALL retain packer manifests and optional export bundles. `logs/` SHALL store CLI + packer logs with timestamps. `state/packer-hybrid.json` SHALL track build metadata and drift indicators.

#### Scenario: Traceable outputs

- **WHEN** a build completes
- **THEN** manifests MUST be written under `artifacts/`, logs under `logs/`, and metadata under `state/packer-hybrid.json` so future publishes can verify drift.

### Requirement: Data-Driven Workflow

Commands MUST NOT edit packer templates in-place; all changes MUST flow through templates plus configs merging to ensure reproducibility.

#### Scenario: Template protection

- **WHEN** the CLI needs to adjust variables or sources for a build
- **THEN** it MUST do so by updating config overlays or generated vars, never by mutating tracked template files at runtime.

### Requirement: HCL2 as Canonical Format

All templates MUST use HCL2 (`*.pkr.hcl`) files instead of JSON templates to maximize readability and reuse.

#### Scenario: Template authoring

- **WHEN** a contributor adds a new builder or provisioner file
- **THEN** it MUST be written in HCL2; JSON templates are rejected during review.

### Requirement: Cloud-Init Support

Templates SHALL support optional cloud-init data injection stored under `templates/cloudinit/`, allowing Azure and other supported platforms to consume user-data.

#### Scenario: Injecting user-data

- **WHEN** `packer-hybrid config --cloudinit path/to/userdata.yaml` is provided
- **THEN** rendered configs MUST merge the referenced cloud-init snippets and ensure they are passed to builders that support them.

### Requirement: OS Image Variants

Each OS family SHALL expose at least one base variant and MAY add additional variants (disk layouts, packages, preconfiguration) using dedicated directories under `templates/vars/<os>/<variant>` and matching overlays in `templates/scripts`.

#### Scenario: Selecting variants

- **WHEN** an operator targets `linux/base-hardened`
- **THEN** the CLI MUST include the `base-hardened` vars and scripts while leaving other variants untouched.

### Requirement: Build Output Location

The repository SHALL continue to use `artifacts/` (not `builds/`) for build outputs to stay aligned with upstream examples; additional transient packer directories MUST be ignored via `.gitignore`.

#### Scenario: Folder expectation

- **WHEN** operators look for manifests analogous to upstream `builds/`
- **THEN** documentation MUST direct them to `artifacts/` instead, avoiding duplicate folder structures.

#### Scenario: Drift prevention

- **WHEN** the CLI detects uncommitted template changes or state drift
- **THEN** it MUST refuse to run `build`/`publish` until resolved.

### Requirement: Template Metadata & Change Detection

Templates SHALL maintain metadata fields (provisioners, configs, scripts, dependencies, variant info) and change-detection rules linking manifests/HCL diffs to state updates so partial updates are blocked.

#### Scenario: Metadata completeness

- **WHEN** builder metadata lacks provisioner information
- **THEN** change detection MUST refuse to proceed until the metadata schema includes those fields.

### Requirement: Template Metadata & Change Detection

Templates SHALL maintain metadata (provisioners, configs, scripts, dependencies, variant info) and change-detection rules tying manifests/HCL diffs to state updates so partial updates are blocked.

#### Scenario: Metadata completeness

- **WHEN** a builder metadata entry is missing provisioner references
- **THEN** the spec MUST require metadata schemas to include those fields and refuse change detection until completed.

## Open Issues

See `docs/spec-remediations/templates-remediations.md`.

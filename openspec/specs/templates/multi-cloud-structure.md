# Multi-Cloud Template Structure Specification

## Requirements

### Requirement: Repository Layout

The repository SHALL follow a multi-cloud layout: `templates/`, `configs/`, `sources/`, `artifacts/`, `logs/`, and `state/`.

#### Scenario: Templates tree

- **WHEN** `init` scaffolds the repo
- **THEN** it MUST create:
  - `templates/common.pkr.hcl`
  - `templates/platforms/{proxmox,vsphere,azure}.pkr.hcl`
  - `templates/vars/{linux,windows}/{common,<platform>}.pkrvars.hcl`
  - `templates/scripts/{linux,windows}`
  - `templates/ansible` (and optional `templates/puppet`)

### Requirement: Composition Model

Common builders SHALL live in `common.pkr.hcl`; platform-specific sources live in per-cloud files and share naming convention `source.<plugin>-iso.<image>` or `source.azure-arm.<image>`.

#### Scenario: Source references

- **WHEN** `packer build` runs
- **THEN** the combined HCL MUST reference sources using the standardized names so CLI can dynamically select targets.

### Requirement: Environment Configs

`configs/<env>/` MUST store generated `.auto.pkrvars.hcl` files per platform/OS, created via CLI, never edited manually.

#### Scenario: Config generation

- **WHEN** `packer-hybrid config --env prod --targets vsphere,azure` runs
- **THEN** only those platform var files are written/updated, leaving others untouched.

### Requirement: Artifacts and Logs

- `artifacts/` SHALL retain packer manifests and optional export bundles.
- `logs/` SHALL store CLI + packer logs with timestamps.
- `state/packer-hybrid.json` SHALL track build metadata and drift indicators.

### Requirement: Data-Driven Workflow

No command MAY edit packer templates in-place; all changes flow through templates + configs merging, ensuring reproducibility.

#### Scenario: Drift prevention

- **WHEN** CLI detects uncommitted template changes or state drift
- **THEN** it MUST refuse to run `build/publish` until resolved.

# Hybridcore Package Specification

## Requirements

### Requirement: Module Boundaries

`hybridcore` SHALL provide distinct stdlib-only modules for `config`, `sources`, `templates`, `provisioners`, `packer`, `state`, and `logs`.

#### Scenario: Dependency-free imports

- **WHEN** the CLI imports any hybridcore module
- **THEN** only Python standard library modules are loaded, ensuring zero third-party dependencies.

### Requirement: Config Rendering

`hybridcore.config` MUST render `.pkrvars.hcl` files from templates, merge environment overlays, and validate schemas before writing to `configs/<env>/`.

#### Scenario: Deterministic configs

- **WHEN** the same inputs are provided
- **THEN** `generate_env_config` MUST output identical files and raise descriptive errors for missing variables.

### Requirement: Source Management

`hybridcore.sources` SHALL clone/update plugin and example repositories under `sources/`, record SHAs, and refuse to proceed if the working tree is dirty.

#### Scenario: Pinned versions

- **WHEN** `sources sync` runs
- **THEN** it MUST update `state/packer-hybrid.json` with repo URLs and commit SHAs for reproducibility.

### Requirement: Template Composition

`hybridcore.templates` MUST list builders per OS/platform, enforce naming conventions (`source.<plugin>-iso.<name>` etc.), and assemble packer file lists for CLI commands.

### Requirement: Provisioner Coordination

`hybridcore.provisioners` SHALL expose toggles for Ansible (default) and Puppet (optional) stacks, verify required assets exist under `templates/ansible` or `templates/puppet`, and emit packer variables enabling/disabling each stack.

### Requirement: Packer Orchestration

`hybridcore.packer` MUST wrap `packer fmt/validate/build`, stream logs, parse manifests, and surface structured results (status, artifact IDs, timestamps).

### Requirement: State Management

`hybridcore.state` SHALL persist structured JSON containing plugin versions, repo SHAs, manifest hashes, and last-run metadata; updates MUST be atomic (write temp file, rename).

### Requirement: Logging

`hybridcore.logs` MUST provide a shared logger format (timestamp, level, command) used by CLI, tests, and future Django services, and support log file rotation under `logs/`.

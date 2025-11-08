# hybridcore-templates Specification

## Purpose

Capture the contracts for `hybridcore.templates`—builder inventory, composition outputs, and tests—while referencing the umbrella hybridcore spec. Reference: [specs/hybridcore/spec.md](openspec/specs/hybridcore/spec.md)

## Requirements

### Requirement: Builder Inventory

`hybridcore-templates` SHALL expose APIs to list builders per OS/platform, validate naming conventions (`source.<plugin>-iso.<name>`, `source.azure-arm.<name>`), and map builders to their HCL files.

#### Scenario: Inventory lookup

- **WHEN** the CLI requests builders for `windows,vsphere`
- **THEN** the module MUST return the canonical identifiers and file paths so downstream commands can load the correct HCL.

### Requirement: Composition Outputs

The module MUST return ordered lists of HCL files (common + platform-specific) plus script/provisioner paths, ensuring deterministic ordering for fmt/validate/build.

#### Scenario: Deterministic composition

- **WHEN** two runs request the same targets
- **THEN** the resulting file lists MUST be byte-identical (to support caching and tests).

### Requirement: Testing

Unit tests SHALL cover builder validation, naming enforcement, and composition results. Integration tests SHALL run `packer fmt -check` against the composed files in CI to detect structural regressions.

#### Scenario: Invalid name

- **WHEN** a builder is named `source.azurearm.bad`
- **THEN** `hybridcore-templates` MUST raise a validation error and tests MUST assert the failure message references the naming rule.

## ADDED Requirements

### Requirement: Provisioner Testing Matrix

Spec SHALL document lint/test expectations per provisioner/platform.

#### Scenario: Matrix enforcement

- **WHEN** Puppet assets change
- **THEN** the lint/test matrix MUST specify required checks (parser validate, metadata lint, packer validate).

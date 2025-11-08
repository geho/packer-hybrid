# security Specification

## Purpose
TBD - created by archiving change refactor-misplaced-specs. Update Purpose after archive.
## Requirements
### Requirement: Quality Gate Checklist

Every change SHALL run `prettier --write` (or `--check`), `python -m compileall`/unit tests, and `packer fmt -check` plus `packer validate` for affected builders. Drift detection via `packer-hybrid status` MUST precede `build`/`publish`.

#### Scenario: Enforcement

- **WHEN** a contributor submits a change touching templates or provisioning
- **THEN** they MUST list the verification commands run in the PR description and ensure CI replicates them.

### Requirement: Secrets Handling

Credentials MUST never be committed to git; sensitive values flow via env vars, secret managers, or encrypted `.auto.pkrvars.hcl` files stored outside VCS.

#### Scenario: CLI guardrails

- **WHEN** the CLI detects plaintext secrets in tracked files
- **THEN** it MUST abort and point to remediation guidance.

### Requirement: Access Scopes

Each platform MUST document minimal IAM scope:

- Proxmox token limited to template build/storage actions.
- vSphere service account scoped to target datacenter/cluster/datastore.
- Azure service principal scoped to build plus image resource groups.

#### Scenario: Documented permissions

- **WHEN** onboarding a new operator
- **THEN** the documentation MUST list the constrained IAM scopes above so credentials are provisioned with least privilege.


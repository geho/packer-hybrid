# Verification, Security, and Documentation Specification

## Requirements

### Requirement: Quality Gate Checklist

Every change SHALL run `prettier --write` (or `--check`), `python -m compileall`/unit tests, and `packer fmt -check` + `packer validate` for affected builders. Drift detection via `packer-hybrid status` MUST precede `build/publish`.

#### Scenario: Enforcement

- **WHEN** a contributor submits a change touching templates or provisioning
- **THEN** they MUST list the verification commands run in the PR description and ensure CI replicates them.

### Requirement: Secrets Handling

Credentials MUST never be committed to git; sensitive values flow via env vars, secret managers, or encrypted `.auto.pkrvars.hcl` files stored outside VCS.

#### Scenario: CLI guardrails

- **WHEN** CLI detects plaintext secrets in tracked files
- **THEN** it MUST abort and point to remediation guidance.

### Requirement: Access Scopes

Each platform MUST document minimal IAM scope:

- Proxmox token limited to template build/storage actions.
- vSphere service account scoped to target datacenter/cluster/datastore.
- Azure service principal scoped to build + image resource groups.

### Requirement: Documentation Expectations

Temporary research notes (e.g., `docs/drafts/...`) MUST be removed once their content lives in approved specs; contributors MUST update `project.md` references and spec links in prompts when behaviour changes.

### Requirement: Proposal Prompt Governance

Each reusable prompt under `docs/proposals/` MUST include a link to the associated spec once the spec is approved.

## ADDED Requirements

### Requirement: Credential Storage Conventions

Sensitive values SHALL be sourced from environment variables, secret manager paths (documented in `docs/secrets/`), or encrypted blobs outside git; repository configs MUST only reference these external locations (e.g., `var.proxmox_token = env("PROXMOX_TOKEN")`). `.env` files remain ignored, and `.env.example` MAY only contain placeholder keys. A helper script (e.g., `scripts/setup-secrets.sh`) MUST describe how to fetch dummy or production creds without revealing plaintext.

#### Scenario: Referencing secrets

- **WHEN** `packer-hybrid config` generates `.auto.pkrvars.hcl`
- **THEN** it MUST point to environment variables or secret manager paths rather than embedding values inline; operators MUST document the source, owner, and rotation notes in `docs/secrets/<platform>.md`.

### Requirement: Runtime Secret Consumption

CLI commands SHALL read secrets via `env()` or short-lived files fetched from the secret manager at runtime; logs MUST only confirm presence/absence of a secret and redact values. CI jobs MUST obtain credentials dynamically (OIDC → Vault, cloud secrets) and drop them after the run.

#### Scenario: Local development

- **WHEN** a developer runs `packer-hybrid status --use-dummy-secrets`
- **THEN** the CLI MUST load sanitized fixtures from `tests/fixtures/secrets/` instead of real credentials, enabling local testing without production data.

### Requirement: IAM Scope Details & Rotation

Each platform MUST document required IAM permissions, rotation cadence, and dummy/testing credentials. Proxmox tokens SHALL limit actions to template lifecycle; vSphere accounts MUST scope to datacenter/cluster/datastore; Azure service principals MUST target build/image resource groups.

#### Scenario: Rotation workflow

- **WHEN** credentials rotate
- **THEN** operators MUST update the secret manager entry, record the timestamp in `state/secrets.json`, run `packer-hybrid status` to confirm the new scopes work, and keep the previous secret for at most 24 hours for rollback.

### Requirement: Rotation & Validation Workflow

A documented rotation playbook SHALL exist per platform, including: scheduled cadence, smoke-test commands, and incident contacts. Rotation scripts MUST update `state/secrets.json` and create a note in `docs/secrets/rotations/<date>.md`.

#### Scenario: Scheduled rotation

- **WHEN** the monthly Azure rotation occurs
- **THEN** the operator runs `scripts/rotate-azure.sh`, updates `state/secrets.json`, stores the rotation log under `docs/secrets/rotations/`, and executes `packer-hybrid status --targets azure` to validate the new service principal.

### Requirement: Secret Leak Detection & Dummy Data

CI SHALL run secret scanners (e.g., `gitleaks`, `trufflehog`) on every PR; local workflows MUST provide sanitized dummy vars (e.g., `*_DUMMY` files) so developers can test without real secrets. Any detected secret MUST trigger immediate revocation and incident documentation.

#### Scenario: CI gate

- **WHEN** `pre-commit` or CI runs
- **THEN** it MUST execute the configured secret scanner and fail if matches appear, instructing the contributor to rotate the secret, document remediation, and re-run tests with dummy data.

### Requirement: Incident Documentation

Any confirmed or suspected leak SHALL be documented under `docs/secrets/incidents/<date>.md` with details (secret name, detection method, remediation, follow-up tasks). Incidents MUST trigger forced rotation and retrospective review.

#### Scenario: Leak response

- **WHEN** gitleaks flags a credential
- **THEN** the owner MUST revoke it in the secret manager, add an incident entry, ensure dummy data replaces the leaked value for tests, and link the incident to any affected PR or issue.

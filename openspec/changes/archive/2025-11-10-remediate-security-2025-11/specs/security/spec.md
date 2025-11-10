## MODIFIED Requirements

### Requirement: Security Rotation Workflow

Security SHALL document rotation cadence, storage backend, and runbook guidance per platform.

#### Scenario: Rotation runbook

- **WHEN** a platform rotates secrets
- **THEN** operators SHALL follow the runbook, update `state/secrets.json`, log the rotation in `docs/secrets/rotations/`, and run smoke tests.

### Requirement: Supply Chain Scanning & SBOM

Security SHALL document scanning cadence covering sources/templates, SBOM outputs, and CI gating.

#### Scenario: Scheduled scanning

- **WHEN** weekly scans run
- **THEN** `scripts/scan-supply-chain.sh` SHALL execute, attach SBOM artifacts, and record results.

### Requirement: Quality Gate Checklist

Security SHALL replace duplicated verification gate text with references into CLI/packer specs, describing how security validates the gates.

#### Scenario: Gate linkage

- **WHEN** security reviews a change
- **THEN** they SHALL confirm CLI/packer gates ran by referencing the spec sections instead of duplicating requirements.

### Requirement: Incident Severity & Open Issues Tracking

Security SHALL define severity levels (critical/high/medium) with response targets tied to Open Issues updates.

#### Scenario: Severity escalation

- **WHEN** a critical incident occurs
- **THEN** security SHALL respond within 24h, update the severity rubric, and refresh `docs/spec-remediations/security-remediations.md`.

### Requirement: Security Diagrams

Security SHALL ensure diagrams live under `specs/security/` and docs link back per governance.

#### Scenario: Diagram governance

- **WHEN** security processes change
- **THEN** the spec diagrams MUST be updated and docs SHALL reference the spec-hosted version.

## ADDED Requirements

### Requirement: Supply Chain Scanning & SBOM

Security spec SHALL document scanning cadence and SBOM requirements.

#### Scenario: Weekly scanning

- **WHEN** the scheduled scan runs
- **THEN** `scripts/scan-supply-chain.sh` MUST execute, attach the SBOM, and record results.

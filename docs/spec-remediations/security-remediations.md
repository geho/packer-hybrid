# Security Spec Remediations

## Open Topics

1. _None – new gaps will be recorded during the next assessment._

## Closed Topics

1. **Security rotation workflow** – `openspec/specs/security/spec.md#requirement-security-rotation-workflow` now references per-platform runbooks, storage backends, and the [rotation workflow diagram](openspec/specs/security/rotation-workflow.md) (`remediate-security-2025-11`).
2. **Supply-chain scanning & SBOM** – Weekly/pre-release scans plus SPDX outputs are defined in `openspec/specs/security/spec.md#requirement-supply-chain-scanning--sbom`, and artifacts live under `artifacts/security/sbom/<timestamp>.json` (`remediate-security-2025-11`).
3. **Verification duplicates** – The Quality Gate checklist only references the CLI and hybridcore-packer specs (`openspec/specs/security/spec.md#requirement-quality-gate-checklist`) and records evidence rather than repeating commands (`remediate-security-2025-11`).
4. **Severity rubric** – The severity table + response targets are codified in `openspec/specs/security/spec.md#requirement-incident-severity--open-issues-tracking`, keeping this file as the Open Issues pointer (`remediate-security-2025-11`).
5. **Diagram alignment** – `openspec/specs/security/spec.md#requirement-security-diagrams` requires diagrams to live under `openspec/specs/security/` (e.g., [rotation workflow](openspec/specs/security/rotation-workflow.md)) and docs now link back per governance (`remediate-security-2025-11`).

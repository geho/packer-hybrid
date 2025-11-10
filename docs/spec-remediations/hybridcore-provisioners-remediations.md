# Hybridcore Provisioners Remediations

## Open Topics

1. _None – new gaps will be recorded during the next assessment._

## Closed Topics

1. **Gaps** – `openspec/specs/hybridcore-provisioners/spec.md#requirement-provisioner-layout--toggles` now defines config vs CLI precedence, SSH fallback, and references the toggle-flow diagram; Puppet modes moved from drafts into `#requirement-provisioner-modes--fallback` with concrete scenarios (`remediate-hybridcore-provisioners-2025-11`).
2. **Completeness** – Provisioner-specific secrets and validation pipelines are captured in `#requirement-provisioner-secrets--validation-pipeline`, tying lint/unit tests plus security spec references to each toggle (`remediate-hybridcore-provisioners-2025-11`).
3. **Alignment** – Drift detection against config/templates is enforced via `#requirement-provisioner-alignment--drift-detection` and the new metadata propagation diagram, ensuring manifests stay in sync (`remediate-hybridcore-provisioners-2025-11`).
4. **Integrity / Diagrams** – Spec-hosted diagrams (`toggle-flow.md`, `metadata-propagation.md`) live under `openspec/specs/hybridcore-provisioners/` and docs link back per governance (`remediate-hybridcore-provisioners-2025-11`).
5. **Consistency** – The spec references provisioning/security requirements instead of duplicating onboarding steps, and the remediation doc remains the authoritative Open Issues pointer (`remediate-hybridcore-provisioners-2025-11`).

# Hybridcore State Remediations

## Closed Topics

1. **Migrations/Audit** – Spec now documents migration toolkit + audit logging.
2. **Cross-module references** – Added references back to templates remediations.

## Open Topics

1. _None – new gaps will be recorded during the next assessment._

## Closed Topics

1. **Concurrency / Integrity** – `openspec/specs/hybridcore-state/spec.md#requirement-state-coordination--locking` documents lockfile semantics, owner metadata, and references the coordination diagram (`specs/hybridcore-state/coordination-flow.md`), with scenarios/tests for concurrent writers (`remediate-hybridcore-state-2025-11`).
2. **Alignment** – The state schema + consumer requirements in `#requirement-state-schema--consumers` describe `state/packer-hybrid.json`, CLI diagnostics, and template/provisioner expectations, referencing the provenance diagram (`remediate-hybridcore-state-2025-11`).
3. **Schema Versioning** – `#requirement-state-schema-versioning--migration` covers version fields, migration tooling, downgrade protection, and audit logging (`remediate-hybridcore-state-2025-11`).
4. **Provenance** – `#requirement-snapshot-provenance` mandates suite/timestamp/artifact fields and diagrams how tests feed state (`specs/hybridcore-state/provenance-flow.md`), satisfying governance (`remediate-hybridcore-state-2025-11`).

# Hybridcore State Remediations

## Closed Topics

1. **Migrations/Audit** – Spec now documents migration toolkit + audit logging.
2. **Cross-module references** – Added references back to templates remediations.

## Open Topics

1. **Integrity** – Concurrent coordination guidance is still pending; the spec only mentions atomic renames. _Plan_: add scenarios covering multi-process writers and define lockfile semantics/tests.
2. **Alignment** – State snapshots do not outline how CLI diagnostics or templates should consume hash metadata. _Plan_: document the schema for `state/packer-hybrid.json`, describe the consumers, and add tests checking for required fields per module.

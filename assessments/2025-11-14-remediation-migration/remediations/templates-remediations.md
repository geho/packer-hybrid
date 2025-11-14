# Hybridcore Templates Spec Gaps

Open items to revisit after in-flight changes merge:

## Open Topics

1. **Gaps / Completeness** – Define OS image variant naming, directory layout, manifests, and validation/testing expectations. _Plan_: add a canonical naming table, update onboarding docs, and create tests covering variant selection.
2. **Integrity** – Clarify checksum cache storage, reuse, invalidation triggers, and how caches interact with drift detection. _Plan_: document cache folder layout and add CI that busts caches when manifests change.
3. **Consistency / Alignment** – Detail integration between builder manifests and `hybridcore.state`, including validation commands consumed by CLI/publish workflows. _Plan_: add a scenario plus sequence diagram hooking templates ↔ state.
4. **Ambiguities** – Platform-specific script directories (Linux vs Windows) lack naming guidance, so contributors guess file names and duplicate logic. _Plan_: add a naming table plus lint/tests ensuring new scripts follow the convention.
5. **Integrity** – Template diagrams referenced by onboarding docs are missing from the spec directory, violating governance. _Plan_: relocate the diagrams under `specs/templates/` and ensure docs link to them.

## Closed Topics

1. **Metadata schema completeness** – Covered by Template Metadata & Change Detection requirement.

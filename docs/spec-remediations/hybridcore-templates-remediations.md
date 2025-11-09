# Hybridcore Templates Remediations

## Open Topics

1. **Gaps / Completeness** – The spec references OS image variant taxonomy but never defines the canonical naming scheme, directory layout, or validation scenarios for multi-variant builders. _Plan_: add a dedicated requirement plus scenario covering variant naming (`<os>/<platform>/<variant>`), update `specs/hybridcore-templates/metadata-map.md`, and extend tests that verify variant manifests.
2. **Integrity / Alignment** – Checksum caching and invalidation rules are only implied via manifests; there is no guidance on where caches live, how they are refreshed, or how CLI/build commands ensure parity with `hybridcore.state`. _Plan_: document cache storage under `state/templates/cache/`, add drift scenarios tying into `hybridcore.state`, and add CI coverage that exercises cache busting.
3. **Consistency / State Sync** – Builder manifests reference `hybridcore.state`, but the spec does not describe the contract for syncing manifest metadata back to state or how CLI callers consume it. _Plan_: add a requirement tying manifest writes to `state/templates/<builder>.json`, include a sequence diagram, and define tests that fail when state/manifests diverge.
4. **Alignment** – The spec still treats provisioner metadata as optional even though provisioning and templates must evolve together. _Plan_: document per-builder provisioner requirements, reference `docs/spec-remediations/provisioning-remediations.md`, and add validation that fails when metadata drifts from provisioner toggles.
5. **Integrity** – Governance’s diagram checklist requires doc links, but template onboarding diagrams live only in `docs/` today. _Plan_: move them into `specs/hybridcore-templates/` and reference them from docs.

## Closed Topics

1. **Metadata schema completeness** – Addressed via the Template Metadata & Change Detection requirement.

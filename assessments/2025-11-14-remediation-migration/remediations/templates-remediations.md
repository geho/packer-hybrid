# Hybridcore Templates Spec Gaps

Open items to revisit after in-flight changes merge:

## Open Topics

1. _None – resolved by change `remediate-templates-open-topics`; reopen when future assessments surface new template gaps._

## Closed Topics

1. **Metadata schema completeness** – Covered by Template Metadata & Change Detection requirement.
2. **Variant naming/layout** – Canonical table + wizard summary added, spec links to `openspec/specs/templates/variant-flow.mmd` (`remediate-templates-open-topics`).
3. **Checksum cache lifecycle** – Cache paths/invalidation rules described with `cache-lifecycle.mmd`, CLI hooks reference the requirement (`remediate-templates-open-topics`).
4. **Templates ↔ state integration** – Manifest/state flow documented plus CLI status/publish references (`remediate-templates-open-topics`).
5. **Script directory naming** – Spec + provisioning requirements now enforce lowercase kebab-case and tests lint the structure (`remediate-templates-open-topics`).
6. **Template diagrams governance** – Mermaid sources moved under `openspec/specs/templates/` with doc references (`remediate-templates-open-topics`).

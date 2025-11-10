# Proposal: Remediate provisioning spec

## Why

`docs/spec-remediations/provisioning-remediations.md` lists open topics: Windows parity/secret distribution, provisioner lint/test coverage, alignment with hybridcore-provisioners/templates metadata, missing diagrams/mappings, and security-aligned secret handling. The provisioning spec lacks these, so toggles/tests drift.

## Scope

- Spec: `openspec/specs/provisioning/spec.md` plus diagrams in `openspec/specs/provisioning/`.
- Docs: `docs/spec-remediations/provisioning-remediations.md` (close topics).
- Related specs: hybridcore-provisioners, hybridcore-templates, security.

## What Changes

1. Add OS-specific sections covering Windows parity, secret distribution, cross-platform script requirements.
2. Define provisioner/platform lint/test expectations via a testing matrix and CI gate descriptions.
3. Reference hybridcore-provisioners/templates specs to keep metadata/toggles consistent, documenting the contract for provisioner metadata.
4. Add a Mermaid diagram showing config → provisioners → packer interactions and a CLI ↔ hybridcore variable ↔ provisioner asset mapping.
5. Align secret handling with the security spec, requiring indirected secrets + retention rules.

## Deliverables

- Spec updates + diagrams mapping provisioning flows and CLI mappings.
- Remediation doc updated (open topics moved to Closed).
- `openspec validate remediate-provisioning-2025-11 --strict` and Prettier on touched Markdown.

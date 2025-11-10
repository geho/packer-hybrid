# Proposal: Remediate hybridcore-provisioners spec

## Why

`docs/spec-remediations/hybridcore-provisioners-remediations.md` lists six open topics covering provisioner opt-in flows, Puppet mode coverage, SSH fallback, secrets handling, drift/alignment with config/templates, duplicated onboarding text, and missing diagrams. The spec lacks detail on how toggles map to config/CLI precedence, the validation gates for each provisioner, and how diagrams reference governance requirements.

## Scope

- Spec: `openspec/specs/hybridcore-provisioners/spec.md` plus new diagrams under `openspec/specs/hybridcore-provisioners/`.
- Docs: `docs/spec-remediations/hybridcore-provisioners-remediations.md`, references to drafts for Ansible/Puppet opt-in and Puppet agent modes.
- Workflow: ensure provisioning, config, and templates specs stay aligned via explicit references and Open Issues updates.

## What Changes

1. Describe provisioning toggle precedence (global config vs CLI), SSH fallback, and validation errors for missing assets.
2. Promote Puppet agent mode guidance from drafts into the spec, detailing required assets, secrets locations, and validation per mode.
3. Add requirements for provisioner-specific secrets handling, asset lint/unit test expectations, and CI matrix coverage.
4. Define alignment requirements so provisioner metadata stays in sync with config/templates specs and drift detection hooks run.
5. Introduce spec-hosted Mermaid diagrams for enable/disable flows, referenced from docs.
6. Update the remediation tracker (Closed topics) and ensure the spec’s `## Open Issues` section continues pointing at it.

## Deliverables

- Updated spec requirements + diagrams and cross-spec references.
- Refreshed remediation doc capturing closed topics.
- `openspec validate remediate-hybridcore-provisioners-2025-11 --strict` and Prettier on touched Markdown.

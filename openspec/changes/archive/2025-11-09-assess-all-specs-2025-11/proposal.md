# Proposal: Assess all specs & refresh remediation backlog

## Why

The previous assessment change covered only the hybridcore family; governance/meta lacked remediation drafts, several specs still reference outdated diagrams, and many Open Issues do not describe ambiguous behaviours uncovered during recent reviews. The project charter now requires periodic full-spectrum assessments, so we need a change that records fresh deviations across every spec and ensures governance/meta participate in the remediation workflow.

## Scope

- Specs: cli, governance, hybridcore, hybridcore-config, hybridcore-logs, hybridcore-packer, hybridcore-provisioners, hybridcore-sources, hybridcore-state, hybridcore-templates, meta, provisioning, security, templates.
- Artifacts: remediation drafts under `docs/spec-remediations/`, new drafts for governance/meta, Open Issues sections in governance/meta specs, proposal/tasks/spec deltas for this change.

## What Changes

1. Run the mandated pre-flight (openspec list/specs, project.md review) and enumerate every spec in scope.
2. Update or create `docs/spec-remediations/<spec>-remediations.md` entries so each spec records the newly observed gaps across the required dimensions (gaps, completeness, ambiguities, consistency, alignment, integrity, duplicates, redundancies) with concrete remediation plans.
3. Add missing `## Open Issues` sections to governance/meta specs referencing their remediation drafts so downstream work can discover outstanding topics.
4. Package all findings into this OpenSpec change with updated proposal/tasks/spec deltas and validate via `openspec validate assess-all-specs-2025-11 --strict`.

## Findings Summary

- **Governance** – Missing remediation draft + Open Issues reference; diagram enforcement + prompt traceability rules still point to old workflows.
- **Meta** – Purpose still `TBD`; assessment/remediation requirements lack cadence/SLA guidance and no Open Issues pointer.
- **CLI** – Diagram/document parity gaps; schema output for `status/inspect` remains undefined.
- **Hybridcore (umbrella)** – Module registry lacks severity/response metadata.
- **Hybridcore-config** – No severity mapping for schema failures; provenance flow diagram missing.
- **Hybridcore-logs** – Context schema undefined; retention/alignment gaps.
- **Hybridcore-packer** – Exit-code/retry policies unspecified.
- **Hybridcore-provisioners** – Duplicates provisioning-spec onboarding steps; toggles lack shared references.
- **Hybridcore-sources** – Resume/repair workflow undocumented; override persistence gaps.
- **Hybridcore-state** – Schema versioning unclear; consumers of hash metadata unspecified.
- **Hybridcore-templates** – Provisioner metadata sync undefined; variant taxonomy gaps persist.
- **Provisioning** – CLI/provisioner toggle mapping missing; diagrams absent.
- **Security** – Incident severity/triage rubric absent; duplication with CLI gates.
- **Templates** – Platform-specific script naming not defined; checksum caches ambiguous.

## Impact

- Governance/meta specs gain the same Open Issues visibility as other modules.
- Remediation drafts provide a single source of truth for outstanding work across all specs, enabling follow-up `/prompts:openspec-apply` changes to focus on implementation.

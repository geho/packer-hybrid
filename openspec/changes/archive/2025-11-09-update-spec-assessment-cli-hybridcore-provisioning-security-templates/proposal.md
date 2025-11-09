# Proposal: Spec assessment & remediation for CLI + hybridcore scopes + provisioning/security/templates

## Why

The last assessment (archive `add-spec-assessment-remediation`) created remediation docs but several specs regressed:

- `openspec/specs/meta/spec.md` still pointed to `docs/drafts`, so contributors were not using `docs/spec-remediations/`.
- Only a subset of specs carried `### Open Issues` references, and `hybridcore-templates` still pointed at a deleted draft.
- Remediation docs drifted, e.g., CLI no longer mentions diag redaction gaps, hybridcore lacks its module registry table, and provisioner drafts remain unmerged.

## Scope

Assessment + remediation planning for `cli`, `hybridcore`, all `hybridcore-*` modules, `provisioning`, `security`, and `templates`.

## Assessment & Remediation Approach

1. Evaluate each dimension (gaps, completeness, ambiguities, consistency, alignment, integrity, duplicates, redundancies) per spec.
2. Record deviations in `docs/spec-remediations/<spec>-remediations.md` (template now tracked in repo) with remediation plans covering spec updates, diagrams, and tests.
3. Ensure every spec exposes a `### Open Issues` block pointing to its remediation doc so downstream changes stay discoverable.
4. Capture the future work as spec deltas (this change) so `/prompts:openspec-apply` can implement the fixes.

## Key Deviations (per spec)

- **cli** – Missing diag redaction/retention guidance, no documented JSON schema for `status/inspect`, and duplicated verification gates that should point to `security`.
- **hybridcore (umbrella)** – No module registry table despite the requirement, and no summary tying module `### Open Issues` back to the umbrella spec.
- **hybridcore-config** – Lacks provenance/secret manifest schema, still missing cross-links to templates/state open issues, and has no diagram for the config → state pipeline.
- **hybridcore-logs** – Remote sink extensibility and diag bundle redaction rules remain undefined; retention guidance does not explain CLI flag propagation.
- **hybridcore-packer** – Incremental hashing/drift detection roadmap absent and result schema is unspecified, so CLI integrations guess field names.
- **hybridcore-provisioners** – Puppet modes + opt-in precedence live only in drafts, SSH fallback + secret handling lack requirements, and there is no enable/disable diagram.
- **hybridcore-sources** – Override approvals are not linked to governance rules, override metadata is not persisted, and scan cadence is not tied to security outputs.
- **hybridcore-state** – Needs concurrency/locking guidance and better alignment with CLI diagnostics/templates consumers.
- **hybridcore-templates** – Variant taxonomy, checksum caching, and state sync contracts remain unspecified.
- **provisioning** – Windows parity, per-provisioner validation, and cross-links to provisioner drafts/templates remain undocumented.
- **security** – Secrets rotation/incident response workflows, supply-chain scanning, and references to CLI/packer gates remain missing.
- **templates** – Variant naming, checksum cache handling, and templates↔state validation flows still lack detail.

## Deliverables

- Updated remediation docs (including a reusable template and a new entry for `hybridcore-templates`).
- Updated specs with `### Open Issues` references and refreshed wording to point at the remediation docs.
- Spec deltas capturing the new remediation-tracking requirement per capability plus the meta-spec fix.
- `openspec validate --strict` green.

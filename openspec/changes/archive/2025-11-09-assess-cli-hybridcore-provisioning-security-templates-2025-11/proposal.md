# Proposal: Assess CLI, hybridcore*, provisioning, security, templates specs

## Why

Recent governance/meta remediations tightened policy guardrails, but the feature-level specs (CLI, all hybridcore modules, provisioning, security, templates) still reference outdated behaviours, incomplete diagrams, and stale remediation drafts. We need a fresh assessment to catalog deviations across the required dimensions (gaps, completeness, ambiguities, consistency, alignment, integrity, duplicates, redundancies) so follow-up apply changes can implement fixes without rediscovering scope.

## Scope

- Specs: `cli`, `hybridcore`, `hybridcore-config`, `hybridcore-logs`, `hybridcore-packer`, `hybridcore-provisioners`, `hybridcore-sources`, `hybridcore-state`, `hybridcore-templates`, `provisioning`, `security`, `templates`.
- Drafts: `docs/spec-remediations/<spec>-remediations.md` entries for each spec listed above.

## What Changes

1. Run the mandated pre-flight (openspec list/specs, project.md review) and read each in-scope spec + remediation draft.
2. Record newly observed gaps per dimension inside the relevant `docs/spec-remediations/<spec>-remediations.md` (using the template) so each spec has an up-to-date backlog.
3. Verify every spec already exposes a `## Open Issues` pointer; add one if missing (following `openspec/specs/hybridcore-templates/spec.md`).
4. Capture the assessment plan + outstanding work in this change’s proposal/tasks/spec delta folders.
5. Validate with `openspec validate assess-cli-hybridcore-provisioning-security-templates-2025-11 --strict`.

## Impact

- Centralized, current remediation drafts for all user-facing specs.
- Downstream `/prompts:openspec-apply` executions can focus on implementation rather than rediscovery.
- Aligns feature specs with the latest governance/meta expectations (diagram verification, remediation references, cadence).

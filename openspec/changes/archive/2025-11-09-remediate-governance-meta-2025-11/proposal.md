# Proposal: Remediate governance + meta specs

## Why

The new assessment identified policy gaps in the governance and meta specs: governance still references the old draft workflow, lacks enforcement for diagram/doc updates, and leaves docstring severity undefined. The meta spec retains a placeholder purpose and omits cadence/ownership for assessments/remediations. We need to tighten these specs so future prompts and tooling have clear guidance.

## Scope

- Specs: `openspec/specs/governance/spec.md`, `openspec/specs/meta/spec.md`.
- Docs: `docs/spec-remediations/governance-remediations.md`, `docs/spec-remediations/meta-remediations.md`.

## What Changes

1. Update the governance spec with:
   - A diagram verification checklist/CI hook requirement.
   - Prompt traceability text aligned with remediation drafts.
   - Docstring enforcement severity guidance.
2. Refresh `docs/spec-remediations/governance-remediations.md`, moving addressed items to Closed Topics.
3. Update the meta spec to:
   - Provide a real Purpose statement.
   - Describe assessment cadence/ownership and refine remediation expectations (including diagrams/tests).
4. Update `docs/spec-remediations/meta-remediations.md` to reflect the closed topics.
5. Validate via `openspec validate remediate-governance-meta-2025-11 --strict`.

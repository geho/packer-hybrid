# Proposal: Align prompt & assessment workflows with the new SoT

## Why

- `.codex/prompts/*.md` and `agents/*.md` are the new canonical workflow/policy references, but `openspec/project.md`, `openspec/specs/governance/spec.md`, and multiple archived change checklists still cite `docs/proposals/*.md` as the source of truth for reusable prompts and metadata.
- Specs (cli, meta, hybridcore modules) plus tests and tooling continue to reference `assessments/2025-11-14-remediation-migration/remediations/*.md`, even though the new assessment workflow requires findings/remediations to live under `assessments/<scope>/`.
- Without migrating these references, contributors are forced to reconcile conflicting instructions, automation cannot enforce the right files, and assessments cannot hand off cleanly into OpenSpec changes.

## Scope

1. **Prompt SoT migration**
   - Deprecate `docs/proposals/*.md` as live prompt sources; ensure `.codex/prompts/*.md` remains the only maintained location.
   - Update governance/project specs (and any other references) to describe prompt metadata/usage in terms of `.codex/prompts/*.md`.
2. **Policy consolidation**
   - Replace duplicated coding/testing/git guidance in `openspec/project.md` with references to `agents/startup.md` and the policies inside `agents/policies/`.
   - Ensure governance/meta/cli specs cite the SoT instead of repeating policy text where feasible.
3. **Assessment-backed remediation tracking**
   - Move open/closed remediation topics from `assessments/2025-11-14-remediation-migration/remediations/*.md` into assessment folders generated via `/prompts:assessment-*`.
   - Update specs, docs, tests, and tooling (including the outstanding remediation execution change) to reference assessment outputs.
4. **Automation & validation updates**
   - Adjust prompt-metadata checks, CLI schema references, and spec tests so they operate on `.codex/prompts/` and `assessments/`.

Out of scope: implementing the actual remediation content or new assessment findings (handled by follow-on changes once the workflow is aligned).

## Impact

- Governance, meta, and cli specs (others as needed) will gain new requirements describing the SoT references.
- `openspec/project.md` will lean on `agents/policies/*.md` instead of duplicating guidance.
- `docs/proposals/` and `assessments/2025-11-14-remediation-migration/remediations/` will either be archived or reduced to historical notes, with all active workflows handled via `.codex/prompts/` and `assessments/`.
- Tests/automation referencing old paths must be updated to keep CI passing.

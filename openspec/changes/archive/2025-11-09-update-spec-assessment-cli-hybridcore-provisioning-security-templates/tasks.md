# Tasks

## Prep

1. - [x] `openspec list --specs` + read `openspec/project.md` for current conventions.
2. - [x] Re-read each target spec plus its remediation doc to capture the latest state.

## Assessment & Remediation Recording

3. - [x] For every spec in scope (cli, hybridcore, hybridcore-{config,logs,packer,provisioners,sources,state,templates}, provisioning, security, templates) evaluate gaps/completeness/ambiguities/consistency/alignment/integrity/duplicates/redundancies; capture findings + remediation plan bullets inside `docs/spec-remediations/<spec>-remediations.md` (use the template when creating new files).
4. - [x] Add or refresh the spec’s `### Open Issues` section so it points to the remediation doc (pattern: `openspec/specs/hybridcore-templates/spec.md`).
5. - [x] Update `openspec/specs/meta/spec.md` (or successor policies) whenever remediation workflows change (e.g., switch from `docs/drafts` to `docs/spec-remediations`).

## Implementation Hooks

6. - [x] For each spec touched, add a spec delta under this change capturing the remediation tracking requirement (so `/prompts:openspec-apply` can implement the fixes without guessing files).
7. - [x] When drafts already exist (e.g., `docs/drafts/ansible-puppet-opt-in.md`, `docs/drafts/puppet-agent-modes.md`), call out whether they still apply or need consolidation inside the remediation doc.

## Validation

8. - [x] Run `npx prettier --write` on touched Markdown.
9. - [x] Run `openspec validate update-spec-assessment-cli-hybridcore-provisioning-security-templates --strict` and fix any reported issues.

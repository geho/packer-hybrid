/prompts:openspec-proposal Spec remediation execution (scope: <edit-me|all spec remediations>):

- Before scoping the remediation pass, run `openspec list`, `openspec list --specs`, and review `openspec/project.md` plus the affected specs/remediation drafts so the required OpenSpec pre-flight checklist is satisfied.

- Identify the remediation drafts in scope (default: every file under `docs/spec-remediations/`, formatted using `docs/spec-remediations/templates-spec-remediations.md`).
- For each remediation draft:
  - Read its "Open Topics" (and any existing "Closed Topics") to understand pending gaps.
  - Choose a unique verb-led `<change-id>` (confirm with `openspec list`) and scaffold the change (`proposal.md`, `tasks.md`, optional `design.md`, spec deltas) before drafting. Present the `/prompts:openspec-proposal …` command that should be run and wait for the operator to execute it.
  - When it is time to implement, share the `/prompts:openspec-apply <change-id>` command (with the ready change ID) and ask the operator to run it; ensure the apply phase covers spec deltas, diagram updates (per governance), and tests.
  - Once approved/implemented, update the corresponding spec’s `## Open Issues` section to reflect the new status.
  - Run `openspec validate <change-id> --strict` before seeking approval/archiving to ensure the change passes validation.
  - Move resolved items in `docs/spec-remediations/<spec>-remediations.md` from "Open Topics" to "Closed Topics" (add the section if missing).
  - After validation passes, present the `/prompts:openspec-archive <change-id>` command and request that the operator execute it.
- Repeat for every remediation draft in scope until all open topics are either closed or converted into fresh follow-up changes.

References:

- Remediation drafts: `docs/spec-remediations/<spec>-remediations.md`
- Open Issues example: `openspec/specs/hybridcore-templates/spec.md`
- Follow OpenSpec workflow (proposal → apply → archive) for each remediation change.

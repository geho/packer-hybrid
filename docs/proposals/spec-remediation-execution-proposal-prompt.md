/prompts:openspec-proposal Spec remediation execution (scope: <edit-me|all spec remediations>):

- Before scoping the remediation pass, run `openspec list`, `openspec list --specs`, and review `openspec/project.md` plus the affected specs/remediation drafts so the required OpenSpec pre-flight checklist is satisfied.

- Identify the remediation drafts in scope (default: every file under `docs/spec-remediations/`, formatted using `docs/spec-remediations/templates-spec-remediations.md`).
- For each remediation draft:
  - Read its "Open Topics" (and any existing "Closed Topics") to understand pending gaps.
  - Choose a unique verb-led `<change-id>` (confirm with `openspec list`) and scaffold the change (`proposal.md`, `tasks.md`, optional `design.md`, spec deltas) before drafting. Open the proposal via `/prompts:openspec-proposal …` to capture the required spec updates/diagrams/tests.
  - Process the change through `/prompts:openspec-apply <change-id>` (implement spec deltas, diagrams, tests) following the OpenSpec workflow, including any Mermaid diagram updates required by governance (store sources in `specs/`, quote labels, link from docs).
  - Once approved/implemented, update the corresponding spec’s `## Open Issues` section to reflect the new status.
  - Run `openspec validate <change-id> --strict` before seeking approval/archiving to ensure the change passes validation.
  - Move resolved items in `docs/spec-remediations/<spec>-remediations.md` from "Open Topics" to "Closed Topics" (add the section if missing).
  - Archive the change via `/prompts:openspec-archive <change-id>` once validation passes.
- Repeat for every remediation draft in scope until all open topics are either closed or converted into fresh follow-up changes.

References:

- Remediation drafts: `docs/spec-remediations/<spec>-remediations.md`
- Open Issues example: `openspec/specs/hybridcore-templates/spec.md`
- Follow OpenSpec workflow (proposal → apply → archive) for each remediation change.

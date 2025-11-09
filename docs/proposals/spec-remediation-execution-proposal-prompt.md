/prompts:openspec-proposal Spec remediation execution (scope: <edit-me|all spec remediations>):

- Identify the remediation drafts in scope (default: every file under `docs/spec-remediations/`).
- For each remediation draft:
  - Read its "Open Topics" (and any existing "Closed Topics") to understand pending gaps.
  - Open an OpenSpec change proposal via `/prompts:openspec-proposal …` that captures the required spec updates/diagrams/tests.
  - Process the change through `/prompts:openspec-apply <change-id>` (implement spec deltas, diagrams, tests) following the OpenSpec workflow.
  - Once approved/implemented, update the corresponding spec’s `## Open Issues` section to reflect the new status.
  - Move resolved items in `docs/spec-remediations/<spec>-remediations.md` from "Open Topics" to "Closed Topics" (add the section if missing).
  - Archive the change via `/prompts:openspec-archive <change-id>`.
- Repeat for every remediation draft in scope until all open topics are either closed or converted into fresh follow-up changes.

References:

- Remediation drafts: `docs/spec-remediations/<spec>-remediations.md`
- Open Issues example: `openspec/specs/hybridcore-templates/spec.md`
- Follow OpenSpec workflow (proposal → apply → archive) for each remediation change.

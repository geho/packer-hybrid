## Tasks

1. - [ ] Enumerate remediation drafts in scope (`docs/spec-remediations/*.md` by default) and prioritize order of execution.
2. - [ ] For each draft, open a dedicated OpenSpec change (`/prompts:openspec-proposal …`) capturing the required spec updates/diagrams/tests.
3. - [ ] `/prompts:openspec-apply <change-id>` – implement, validate, and, once approved, update the corresponding spec’s `## Open Issues`.
4. - [ ] Move resolved items in `docs/spec-remediations/<spec>-remediations.md` from “Open Topics” to “Closed Topics”; add the section if missing.
5. - [ ] `/prompts:openspec-archive <change-id>` – archive each remediation change; repeat until all drafts are processed or converted into follow-up work.

---
description: Commit staged OpenSpec-related changes with consistent messages and validations.
argument-hint: change-id (plus optional summary of what’s staged)
---

$ARGUMENTS

<!-- OPENSPEC:START -->

**Guardrails**

- Favor straightforward, minimal implementations first and add complexity only when it is requested or clearly required.
- Keep changes tightly scoped to the requested outcome.
- Review `@/AGENTS.md`, `@/agents/startup.md`, `@/openspec/AGENTS.md`, and `@/assessments/AGENTS.md` so commits reflect both OpenSpec and assessment handover expectations.
- Prefer running this prompt immediately after `openspec-archive` so specs, proposals, and implementation files are finalized.
- If the prompt is invoked earlier, first complete the relevant implementation steps and run the `git-stage` prompt to organize files.
- Keep each commit scoped to a single OpenSpec change ID; split work into multiple commits only when the developer approves (e.g., separate spec vs code).
- Ensure required validations (`openspec validate <id> --strict`, tests, linters) have passed since the last modification.

**Workflow**

1. **Staging Confirmation**
   - If `git diff --cached` is empty, re-run the `git-stage` prompt before proceeding.
   - List staged files grouped by category (spec updates, implementation, docs/tests) and confirm they match the intended change.
2. **Validation Snapshot**
   - Summarize the most recent validation/test runs relevant to the staged files. If they haven’t run since staging, prompt the user to rerun now.
3. **Commit Message Planning**
   - Suggest a commit message format referencing the change ID (e.g., `feat(<change-id>): concise summary`) and confirm it matches the conventions documented in `openspec/project.md`.
   - When multiple commits are necessary, outline each message and its file grouping.
4. **Execute Commit**
   - Provide the exact `git commit -m "..."` command(s) (or instruct the user to run them) once the developer confirms the plan.
   - After committing, run `git status -sb` to ensure the working tree is clean.
5. **Next Steps**
   - Remind the developer to push the branch and link the OpenSpec change ID in the PR description or changelog.
   - If additional work remains, note what should happen before the next commit (e.g., rerun `git-stage`, revisit approval).

**Reference Tips**

- Use `git show --stat HEAD` to review the final commit summary before handing off.
- Keep notes on any staged-but-uncommitted files if the developer chooses to defer them.
<!-- OPENSPEC:END -->

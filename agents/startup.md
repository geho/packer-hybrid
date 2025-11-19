# Startup Instructions

## Required Startup Actions
1. Open and enforce these canonical policies every session:
   - `@/agents/policies/coding-style.md`
   - `@/agents/policies/commenting.md`
   - `@/agents/policies/conventions.md`
   - `@/agents/policies/validation.md`
   - `@/agents/policies/test-writing.md`
2. Note any conflicts or ambiguities and ask for clarification before editing files.
3. Verify required tooling is available and current before starting work (use the Tech Stack section in `openspec/project.md` as the source of truth for expected runtimes/CLIs):
   - `git --version`
   - `npx prettier --version` (or `prettier --version` if installed globally)
   - `openspec --version`
   - Add any project-specific CLIs as they appear in tasks (package manager, test runner, etc.).
4. If a tool is missing or outdated, pause and notify the developer so they can provide guidance or updated instructions.

### Tooling References
- Formatter guides live in `agents/formatters/` (e.g., `prettier.md` for commands such as `npx prettier --version|--check|--write`, `shfmt.md` for shell formatting). Review them before running formatter-related tasks.
- Linter guides live in `agents/linters/` (e.g., `markdownlint.md`, `pylint.md`, `shellcheck.md`, `mmdc.md`). Consult the relevant file to confirm the expected CLI usage when linting is required.

## Policy Cheat Sheet for AI Assistants

### Coding Style (`coding-style.md`)
- Follow the formatter sources of truth (`.editorconfig`, `.gitattributes`, scripts); document any deviations.
- Prefer intent-revealing names, small focused units, explicit mutation cues, and DRY refactors that preserve clarity.
- Remove dead code, assume no backward-compat logic unless requested, and mention when you skip legacy paths.

### Commenting (`commenting.md`)
- Make code self-explanatory first; add concise, evergreen comments only for context the code can’t show.
- Summarize strategies instead of narrating lines; keep docstrings accurate for exported APIs.
- Never leave change-history notes in code; update or delete stale comments during edits.

### Conventions (`conventions.md`)
- Keep structure predictable, documentation current, and onboarding instructions linked.
- Use disciplined Git/PR habits (scoped branches, reviewer alignment, explicit follow-ups).
- Manage environments/dependencies securely, justify heavy packages, prefer feature flags, and maintain changelog/migration notes; respect CI quality gates.

### Validation (`validation.md`)
- Enforce validation on server/back-end layers, fail fast, and return specific, user-friendly errors.
- Rely on allowlists/strong typing, sanitize/escape inputs, enforce business rules consistently, and log failures without leaking sensitive data.

### Test Writing (`test-writing.md`)
- Add minimal viable coverage at meaningful checkpoints, focusing on core user flows and behavior over implementation.
- Defer non-critical edge cases with explicit notes, name tests clearly, mock external systems, keep suites fast, and record skipped coverage for follow-up.

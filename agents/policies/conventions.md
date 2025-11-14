## General Development Conventions

### Structure & Documentation

- Keep directories predictable (`src/`, `packages/`, `apps/`, etc.) so new contributors can infer where code lives.
- README and onboarding docs must include setup, scripts, architecture overview, and links to specs/design docs. Update them whenever behavior changes.
- When diagrams help explain architecture or workflows, follow the Diagram Standards below so Mermaid/Markdown renders consistently.

### Git & Review Hygiene

- Use descriptive feature branches (`feat/`, `fix/`, `spec/`) and conventional commit summaries referencing change IDs when relevant.
- Keep PRs scoped to a single concern; call out follow-up work explicitly.
- Require at least one knowledgeable reviewer or spec owner before merging significant changes.

### Environment & Dependencies

- Configure behavior via environment variables/config files; never commit secrets or credentials. If a secret is required locally, document how to obtain it securely.
- Pin dependency versions where determinism matters, keep transitive updates minimal, and justify heavyweight dependencies in the PR/README.

### Release & Change Management

- Prefer feature flags or config toggles over long-lived branches for incomplete work.
- Maintain a changelog or release notes capturing user-impacting changes and spec updates.
- Document migration steps (DB, config, infra) within the change when they exist.

### Testing & Quality Gates

- Align with the “Test Writing” policy: focus on core flows and minimal test suites unless specs demand more.
- Ensure CI runs lint, tests, and validation scripts before merging; do not skip failing checks without approval.

### Diagram Standards

- Wrap Mermaid node and edge labels in quotes (e.g., `"Some State"`) to avoid parser errors across renderers.
- Escape placeholders with HTML entities (`&lt;change-id&gt;`) and only include raw tags when they are valid HTML like `<br>`.
- When annotating commands/prompts, include expected arguments (e.g., `/prompts:openspec-implement &lt;change-id&gt;`) so readers know required inputs.
- Represent re-entrant phases with self-loops and label them (quoted) to highlight iterative behavior.
- Keep diagram syntax ASCII-only (no Unicode box-drawing or emoji) except inside quoted labels, so all renderers and tooling handle the files consistently.

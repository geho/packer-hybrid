# Assessment Workflow

Slash commands load prompt definitions from `${CODEX_HOME:-~/.codex}/prompts/`. Edit the project-owned sources under `agents/prompts/` and run `tools/update-codex-prompts.sh` to sync them into the active Codex home before invoking `/prompts:...` commands.

## Phase Diagram

```mermaid
flowchart TD
    A["Initialize Assessment<br>(assessment-init)<br>files: assessments/&lt;id&gt;/{plan,notes,specs-findings,docs-findings,code-findings,summary}<br><b><code>prompt: /prompts:assessment-init &lt;scope&gt;</code></b>"] --> B["Specs vs Policies<br>(assessment-specs)<br>files: .../specs-findings.md + notes.md<br><b><code>prompt: /prompts:assessment-specs &lt;folder&gt;</code></b>"]
    B -->|"<repeat per scope>"| B
    B --> C["Docs vs Specs<br>(assessment-docs)<br>files: .../docs-findings.md + notes.md<br><b><code>prompt: /prompts:assessment-docs &lt;folder&gt;</code></b>"]
    C -->|"<repeat per scope>"| C
    C --> D["Code vs Specs<br>(assessment-code)<br>files: .../code-findings.md + notes.md<br><b><code>prompt: /prompts:assessment-code &lt;folder&gt;</code></b>"]
    D -->|"<repeat per scope>"| D
    D --> E["Summary & Mapping<br>(assessment-summary)<br>files: .../summary.md + plan.md<br><b><code>prompt: /prompts:assessment-summary &lt;folder&gt;</code></b>"]
    E --> F["OpenSpec Proposals<br>(openspec-proposal SoT)<br>files: openspec/changes/&lt;change-id&gt;/{proposal,tasks,specs}<br><b><code>prompt: /prompts:openspec-proposal &lt;request&gt;</code></b>"]
    F --> G["Refine & Implement<br>(openspec-refine / openspec-implement)"]
```

## State Diagram

```mermaid
stateDiagram-v2
    [*] --> Planning : /assessment-init
    Planning --> SpecsReview : /assessment-specs
    SpecsReview --> SpecsReview : "loop per capability"
    SpecsReview --> DocsReview : /assessment-docs
    DocsReview --> DocsReview : "loop per doc"
    DocsReview --> CodeReview : /assessment-code
    CodeReview --> CodeReview : "loop per area"
    CodeReview --> Summarizing : /assessment-summary
    Summarizing --> ProposalQueued : "slash command recorded"
    ProposalQueued --> OpenSpecChange : /openspec-proposal (SoT)
    OpenSpecChange --> Refinement : /openspec-refine
    Refinement --> Implementation : /openspec-implement
    Implementation --> [*] : "archive + commit"
```

## Notes

- Use `assessments/.template` to scaffold folders.
- `summary.md` must include a "Proposed Changes" table with finding ref, suggested change ID, exact `/prompts:openspec-proposal "..."` command, and status.
- After each proposal is created, update `summary.md` status (e.g., `proposal created`, `implementation in progress`).
- Run `tools/migrate-notes.sh &lt;change-id&gt;` immediately after scaffolding a change to move pending questions from `openspec/project-notes.md` into the change’s `tasks.md` under “Proposal Clarifications.”
- Reference assessment findings inside `proposal.md` so OpenSpec prompts can verify traceability.

---
description: Gather the info needed to fully populate openspec/project.md before editing the file.
argument-hint: summary of missing context or request details
---

## Prompt

$ARGUMENTS

<!-- OPENSPEC:START -->

**Guardrails**

- Favor straightforward, minimal implementations first and add complexity only when it is requested or clearly required.
- Keep changes tightly scoped to the requested outcome.
- Review `@/AGENTS.md`, `@/agents/startup.md`, `@/openspec/AGENTS.md`, and `@/assessments/AGENTS.md` so every suggestion respects existing policies, OpenSpec rules, and assessment handover expectations.
- Treat this prompt as a planning aid only—do **not** edit `openspec/project.md` (or related specs) until the developer explicitly approves the collected content.
- Surface uncertainties immediately: ask clarifying questions whenever requirements, constraints, or ownership are unclear.
- Call out conflicts with current policies/specs using a visible warning (e.g., `⚠️ Possible conflict with validation policy`) and explain the mismatch.
- Share research notes (commands run, files inspected) before proposing any changes so reviewers can trace your reasoning.
- The prompt is re-entrant: when re-invoked, review earlier answers, compare them against the full checklists, and only re-ask for the sections that remain incomplete or need confirmation.
- During each interview cycle, restate your current understanding per section and ask the developer to confirm or correct it before recording updates (“alignment check”).
- If a change has already been scaffolded, record unresolved questions or risks inside `openspec/changes/<change-id>/tasks.md` (under “Proposal Clarifications”). Otherwise log them in `openspec/project-notes.md` and migrate them into the change’s `tasks.md` as soon as it exists (run `tools/migrate-notes.sh <change-id>` right after scaffolding to automate the move).
- When `tasks.md` is present, ensure it contains the headings `## Proposal Clarifications` and `## Implementation Tasks`; add them (with placeholder lists) if missing so later prompts can separate workstreams automatically.

**Workflow**

1. Inspect the current `openspec/project.md` plus relevant specs/policies to establish the baseline.
2. **Re-entry Sync (if applicable)**
   - Scan the conversation (or stored notes) for previously recorded answers per section.
   - Compare that record with the “Core” and selected “Domain” questions. Mark each question as **answered**, **needs clarification**, or **missing**.
   - Highlight any drift since the prior run (e.g., policies changed, specs updated) and call it out before continuing.
   - If a change already exists, verify that `openspec/changes/<change-id>/tasks.md` begins with `## Proposal Clarifications` followed by `## Implementation Tasks`; insert headings when missing. If no change exists yet, log unresolved items in `openspec/project-notes.md` until a change is scaffolded, then migrate them.

3. **Domain Selection**
   - Ask which domain(s) best describe the project (examples: web application, automation/CLI framework, data pipeline).
   - If unclear, list the available modules and request confirmation; multiple selections are allowed.
4. **Core Questionnaire**
   - Regardless of domain, capture the common sections listed below (Purpose, Tech Stack Overview, Testing Strategy, etc.).
   - On re-entry, only ask follow-ups for items marked “needs clarification” or “missing,” but summarize the existing answers for confirmation.
5. **Domain-Specific Modules**
   - For each selected domain, run the tailored checklist of best-practice questions (examples provided below). Skip modules that do not apply.
   - When re-running, identify which domain questions still lack detail and interview the developer specifically on those points.
6. Record unresolved questions, risks, or potential policy/spec conflicts under “Proposal Clarifications” in `openspec/changes/<change-id>/tasks.md` when a change exists; otherwise capture them in `openspec/project-notes.md` and migrate them immediately after the change folder is created. Flag them explicitly in your summary (use `⚠️` when needed).
7. Summarize the gathered information, confirm that no files were edited, and wait for explicit approval before modifying `openspec/project.md` or running `openspec validate`.

## Core Section Checklist (always run)

### Purpose

- What goals or outcomes define project success?
- Are there known KPIs or user problems this project addresses?

### Tech Stack Overview

- Which primary runtimes/frameworks/package managers define the project?
- Are there minimum/maximum supported versions or platform caveats?

### Code Style

- Which formatting or linting tools enforce the rules?
- Are there notable deviations from the default policies in `@/agents/policies/coding-style.md`?
- What naming conventions apply to modules, components, tests, and other artifacts?
- Are there formatting expectations not already enforced by the canonical tooling/policies (e.g., max line length, comment style, import ordering)?

### Architecture Patterns

- What high-level structure (monolith, modular packages, services) is expected?
- When should new capabilities be created vs extending existing ones?
- Are there documented architectural decisions or patterns (ADR references, layering rules, shared libraries) that contributors must follow?

### Testing Strategy

- Which test layers (unit, integration, e2e) are required before merge?
- What constitutes “minimal happy-path coverage” for this project?
- Are there documented testing approaches, tooling expectations, or quality gates contributors must follow?

### Git Workflow

- What branch naming, commit message, and review practices should contributors follow?
- How do OpenSpec change IDs map to branches or commits?
- Are there additional branching strategies, rebasing rules, or release tagging conventions that contributors must observe?
- Do commit messages follow a specific format (e.g., `type(change-id): summary` plus body/footer requirements)?

### Domain Context

- What business domain knowledge (personas, workflows, terminology) is essential?
- Are there linked specs or knowledge bases to reference?
- Which historical decisions or stakeholder priorities provide critical context for how features should be scoped (reference constraint details in “Important Constraints”)?

### Important Constraints

- Which performance, security, regulatory, or business constraints must never be violated?
- How are these constraints enforced or validated?

### External Dependencies

- What third-party services, APIs, or shared systems does the project rely on?
- Are there sandbox credentials, contact points, or failure modes to note?
- Which dependencies are mission critical or have explicit SLAs that contributors should document for quick reference?

## Domain Modules (run only when relevant)

Select the modules that match the project domain(s). Use these as examples and extend the library as new domains appear.

### Web Application Module

#### Framework & Runtime

- Primary application framework, runtime/language, and package manager?

#### Frontend _(optional for backend-only or CLI projects)_

- JS framework, CSS framework, UI component library?

#### Database & Storage _(optional for frontend-only or static sites)_

- Database(s), ORM/query builder, caching tiers?

#### Testing & Quality

- Test frameworks, linting/formatting stack?

#### Deployment & Infrastructure

- Hosting platforms, CI/CD tooling, runtime environments?

#### Third-Party Services

- Auth providers, email services, analytics/monitoring stacks?

### Automation / CLI / Infrastructure Module

#### CLI Runtime & Packaging

- Language/runtime versions, distribution format (pipx, Go binary, npm global), cross-platform notes?

#### Plugin or Extension System

- How plugins integrate, API stability guarantees, versioning expectations?

#### Infrastructure SDKs & Providers

- Core SDKs or target platforms (Terraform CDK, AWS SDK, cloud CLIs) plus authentication patterns?

#### Execution Environment

- Expected execution surfaces (local, CI runners, containers, VMs) and prerequisite system packages?

#### State & Artifact Management

- Where state files, caches, or build artifacts live and how they are cleaned up?

#### Concurrency & Scheduling

- Job orchestration model (threads, async queue, workers) and resource limits/retry guidelines?

#### Security & Credential Flow

- How secrets/credentials are supplied, rotated, and audited?

#### Observability & Interoperability

- Logging/telemetry standards for CLI runs; machine-readable outputs (JSON, APIs) for automation hooks?

**Warnings & Approvals**

- Always warn when suggested content would conflict with `openspec/specs` or active change proposals.
- Wait for explicit developer approval before running `openspec validate` or editing any files based on the gathered information.
<!-- OPENSPEC:END -->

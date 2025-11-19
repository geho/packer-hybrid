# Assessment AGENTS

These instructions govern every assessment lifecycle from folder creation to archival.
Assessments are read-only investigations; all remediation must flow through OpenSpec
changes.

## Purpose & Scope

- Run structured inspections across specs, documentation, and implementation
  without modifying production files directly.
- Capture every finding inside `assessments/<date-scope>/` so there is a single
  source of truth before changes move into `openspec/changes/`.
- Archive completed folders under `assessments/archive/<date-scope>/` using
  `/prompts:assessment-close` once every finding is closed or deferred.

## Required Reading

- `@/agents/startup.md`
- `@/openspec/AGENTS.md`
- `@/assessments/.template/README.md`

## File Handling Rules

- **plan.md** (assessor). Update scope, success criteria, checklist, and
  timestamps as the assessment evolves. Keep a “Last Updated” stamp so reviewers
  know when objectives changed.
- **notes.md** (assessor). Append observations/tasks chronologically, never
  deleting history. Move TODOs into change folders once a change ID exists.
- **specs-findings.md / docs-findings.md / code-findings.md** (assessor). Append
  new rows, set `Status` + `Last Updated`, and record change IDs. Never delete or
  rewrite rows; rely on status transitions to show progress.
- **summary.md** (assessor). Maintain “Top Findings” and “Proposed Changes”
  tables with status + change links. Each row must cite an OpenSpec change ID
  (or TODO location) plus a current status.
- **remediations/** (assessor). Use as a scratch pad, then copy actionable
  content into change folders. Reset `templates-*.md` to `_None` entries before
  the assessment closes.

## Status Lifecycle

- Valid `Status` values: `open`, `wip`, `blocked`, `closed`, `archived`,
  `deferred`.
- `open`: finding recorded, no proposal yet. Update `Last Updated` when first
  logged.
- `wip`: corresponding change exists but is not archived. Include the change ID
  and keep `Last Updated` current when progress occurs.
- `blocked`: waiting on prerequisite. Explain the blocker in the Notes column.
- `closed`: implementing change archived and verified. Update `Last Updated` to
  the archive date.
- `archived`: set only after `/prompts:assessment-close` confirms the folder
  moved under `assessments/archive/<date-scope>/`.
- `deferred`: work logged elsewhere (e.g., `openspec/project-notes.md`). Provide
  a link/reference so the trail is auditable.
- Every change to `Status` or Notes must update the `Last Updated` column with
  an ISO date (optionally `YYYY-MM-DDTHH:MMZ`).

## Prompt Workflow (read-only unless approved)

1. **Initialization** – `/prompts:assessment-init <scope>`: create
   `assessments/<date-scope>/`, copy templates, fill out `plan.md` plus the
   initial checklist.
1. **Specs vs Policies** – `/prompts:assessment-specs <folder>`: analyze specs
   and policies; append rows to `specs-findings.md`, update `notes.md`.
1. **Docs vs Specs** – `/prompts:assessment-docs <folder>`: verify
   docs/diagrams; update `docs-findings.md` and `notes.md`.
1. **Code vs Specs** – `/prompts:assessment-code <folder>`: inspect
   implementation/tests; update `code-findings.md` and `notes.md`.
1. **Summary & Handoff** – `/prompts:assessment-summary <folder>`: consolidate
   `summary.md`, create “Proposed Changes” rows with change IDs and
   `/prompts:openspec-proposal` commands. Keep statuses current.
1. **Close & Archive** – `/prompts:assessment-close <folder>`: run the
   verification checklist (see below), confirm every finding is `closed` or
   `deferred`, clean `remediations/`, then move the folder to
   `assessments/archive/<date-scope>/`.

## Guardrails

- Never modify specs, code, or docs during assessments; only log findings with
  file references (e.g., `openspec/specs/payments/spec.md:42`).
- When a finding needs action, create a “Proposed Changes” row with the exact
  `/prompts:openspec-proposal <request>` command, then scaffold the change
  before editing repo files.
- Use `tools/migrate-notes.sh <change-id>` as soon as a change folder exists.
  This keeps outstanding questions out of `openspec/project-notes.md` and inside
  the change’s `tasks.md` (“Proposal Clarifications”).
- Summaries must stay synchronized: whenever a change advances (proposal
  created → refine → approve → archive), update the corresponding `Status` and
  `Last Updated` in both the findings table and `summary.md`.

## Close & Archive Checklist

Run `/prompts:assessment-close <folder>` only when every change ID linked to
the assessment is archived or explicitly deferred. The prompt should enforce
this sequence:

1. **Verification sweep** – Re-open `plan.md`, `notes.md`, all `*-findings.md`,
   `summary.md`, and `remediations/`. Ensure each row has `Status`,
   `Last Updated`, and a change reference. Highlight any rows still
   `open/wip/blocked`.
1. **Cross-link confirmation** – Check that `summary.md` lists every finding
   with a `Closed via <change-id>` (or `Deferred to <reference>`) note.
   Pause closure until all referenced changes finish archiving.
1. **Template hygiene** – Confirm `remediations/templates-*.md` contain only
   placeholder content. Move lingering items into change folders or
   `openspec/project-notes.md` before proceeding.
1. **Archive note** – Append a short section to `summary.md` (e.g., “Archived on
   2025-11-17 after closing changes XYZ, ABC”).
1. **Folder move** – Move the folder with:

   ```shell
   git mv assessments/<date-scope> assessments/archive/<date-scope>
   ```

   Keep active and archived assessments in sync and commit with a message such
   as `chore: archive assessment <date-scope>`.

1. **Final validation** – Re-run `/prompts:assessment-close <folder>`
   (pointing to the new archive path) if needed to confirm the folder is clean
   and marked `archived`.

Fail the close-out if any requirement above is unmet; capture follow-up
instructions in `notes.md` and the corresponding findings rows before retrying.

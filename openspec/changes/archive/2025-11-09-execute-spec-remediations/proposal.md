## Why

The assessment change logged open issues across every spec via `docs/spec-remediations/<spec>-remediations.md` and spec-level `## Open Issues` sections. We now need to execute those remediations: read each draft, spawn the necessary OpenSpec changes, implement/validate them, and update drafts/specs to reflect closed topics.

## What Changes

- Iterate through every remediation draft under `docs/spec-remediations/`.
- For each draft, open and process an OpenSpec change (proposal → apply → archive) covering the required spec updates/diagrams/tests.
- Update the associated spec’s `## Open Issues` section when work is complete and move resolved entries from “Open Topics” to “Closed Topics” in the draft.
- Repeat until every draft has either closed topics or new follow-up changes logged.

## Impact

- Ensures every recorded gap is actually remediated, keeping specs accurate and aligned.
- Keeps Open Issues up to date so future assessments don’t revisit already-closed work.
- Reinforces OpenSpec workflow discipline (proposal/apply/archive) for every remediation pass.

# Governance Spec Remediations

## Open Topics

1. **Completeness / Integrity** – Diagram SoT rules define where Mermaid sources live but never specify verification cadence (e.g., who confirms new diagrams are linked in docs). _Plan_: add a review checklist plus CI hook that ensures every spec diagram has a matching link in the relevant doc before merging.
2. **Alignment** – Prompt traceability requirements still reference the old drafts workflow instead of the new remediation docs. _Plan_: update the prompt-traceability section to reference `docs/spec-remediations/` artifacts and describe how prompts must cite the latest remediation draft.
3. **Ambiguities** – Docstring coverage rules require citing spec IDs but do not define severity or blocking criteria for missing references. _Plan_: add enforcement guidance (e.g., fail build vs warn) and map it to `pydocstyle`/`ruff` checks.

## Closed Topics

1. _None yet – first governance remediation will populate this section._

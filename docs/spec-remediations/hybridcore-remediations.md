# Hybridcore Umbrella Spec Gaps

## Open Topics

1. **Completeness / Integrity** – The "Module Registry & Naming" requirement references a table that never materialized. _Plan_: add the registry table with module name, spec path, implementation status, and remediation draft link so onboarding changes remain auditable.
2. **Alignment** – The umbrella spec does not summarize which module `## Open Issues` are outstanding, so readers must jump between files manually. _Plan_: add a matrix mapping each module to its remediation doc and highlight cross-cutting issues (e.g., config ↔ templates drift).
3. **Duplicates / Redundancies** – Review remaining module-specific requirements in the umbrella spec and convert any lingering duplication into links rather than re-describing module behaviour.
4. **Integrity** – There is no severity or escalation rubric for cross-module issues, so high-impact items can languish. _Plan_: add guidance (e.g., critical/high/medium) plus expected response times and reference it from each module’s Open Issues section.
5. **Consistency** – The umbrella spec’s diagrams do not mention governance/meta dependencies even though they now drive cadence/diagram verification. _Plan_: update the diagrams + surrounding text to highlight the governance/meta touchpoints so future readers understand the policy feedback loop.

## Closed Topics

1. **Module registry** – Added registry table (with planned modules) plus naming guidance.
2. **Dependency rules** – Documented cross-module dependency guidelines and referencing module Open Issues.
3. **Orchestration diagram** – Added `specs/hybridcore/orchestration-flow.md` and referenced it.
4. **Consistency** – Umbrella spec now references module specs and their remediations/Open Issues.

# Hybridcore Umbrella Spec Gaps

Open items:

1. **Module registry gaps** – Umbrella spec does not list upcoming modules (metrics/eventing) or criteria for adding new ones. Add a registry table and naming guidance.
2. **Ambiguities** – Cross-module dependency rules (who can call `hybridcore.templates`, etc.) are vague. Document APIs/data contracts between modules and CLI/automation.
3. **Consistency / Alignment** – Umbrella spec should reference each module’s Open Issues to keep alignment visible; currently absent.
4. **Integrity** – Missing orchestration diagrams showing config→templates→packer→state flow; add or reference existing diagrams to reduce confusion.
5. **Duplicates / Redundancies** – Some module-specific requirements are duplicated here; convert them into high-level summaries with links to avoid drift.

Remediation: update the umbrella spec with module registry, dependency guidelines, orchestration diagrams, and cross-references to each module’s draft.

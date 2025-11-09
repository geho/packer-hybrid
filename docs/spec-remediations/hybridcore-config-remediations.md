# Hybridcore Config Remediations

## Open Topics

1. **Alignment** – Add explicit cross-links to templates/state `## Open Issues` so drift detection contracts stay synchronized. _Plan_: update the spec’s Cross-Module Integrations section with pointers to the relevant remediation docs.
2. **Completeness / Gaps** – The spec never explains how provenance metadata is stored alongside rendered files or how operators audit secret indirection. _Plan_: add tables describing the manifest schema, extend scenarios that cover secret onboarding, and include regression tests for provenance hashes.
3. **Integrity** – There is no pipeline diagram showing how config renders update `hybridcore.state`, leading to ambiguity during reviews. _Plan_: add a Mermaid diagram (config discovery → schema validate → render → state update) and link it from the spec.
4. **Ambiguities** – Schema validation describes “warnings vs failures” but never defines the exit codes or severity levels, so CLI callers cannot distinguish recoverable issues. _Plan_: add a table mapping validation outcomes to exit codes/log levels and unit tests that enforce the mapping.
5. **Duplicates** – The spec restates portions of the provisioning input schema instead of referencing the source of truth (`templates/vars/*`). _Plan_: replace the duplicated text with references plus a mapping table to avoid drift between config and provisioning docs.

## Closed Topics

1. **Variants/Overlays** – OS image variant + platform overlay precedence documented.
2. **Secrets** – Extendability checklist now covers secret redaction/tests.
3. **Manifest/State** – Config spec now describes manifest/checksum integration with state and drift detection.

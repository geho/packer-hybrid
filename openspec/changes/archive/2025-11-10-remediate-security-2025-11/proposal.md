# Proposal: Remediate security spec

## Why

`docs/spec-remediations/security-remediations.md` lists five open topics: secrets rotation workflows/runbooks, supply-chain scanning + SBOM coverage, duplication of CLI/packer verification gates, incident severity/triage rubric gaps, and diagrams that live only in docs (governance wants spec-sourced diagrams). We need to update the security spec to address these gaps before implementation.

## Scope

- Spec: `openspec/specs/security/spec.md` (requirements + diagrams).
- Docs: `docs/spec-remediations/security-remediations.md`, `docs/secrets/*` references.

## What Changes

1. Add/expand the secrets rotation workflow requirement (cadence, storage backends, runbooks, incident response).
2. Document supply-chain scanning cadence/SBOM outputs (sources/templates dependencies) with scenario/tests.
3. Replace duplicated CLI/packer gate details with references to the relevant specs while clarifying how security validates them.
4. Introduce an incident severity/triage rubric tied to response targets and propagate it to Open Issues handling.
5. Ensure security diagrams live under `specs/security/` and docs link back per governance.

## Deliverables

- Updated security spec sections/diagrams.
- Updated remediation doc (open topics moved to Closed).
- `openspec validate remediate-security-2025-11 --strict`.

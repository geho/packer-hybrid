## Tasks

1. - [x] Enumerate state files (schemas, versioning, atomic write rules) within the `hybridcore-state` spec.
2. - [x] Document read/write helper APIs, validation hooks, migration workflow, and backward compatibility guarantees.
3. - [x] Capture cross-module integrations (sources, packer, templates, provisioners) ensuring traceable state mutations and recovery expectations.
4. - [x] Define exhaustive testing/linting (schema fixtures, concurrency simulations, corruption injection, CLI surfacing).
5. - [x] Link `specs/hybridcore-state/state-map.md` from the architecture docs so maintainers can visualize state artifacts.
6. - [x] Update the proposal prompt (docs/proposals/…) to reference the new state diagrams.
7. - [x] Reference `specs/hybridcore-state/state-io.md` in README/ops docs describing atomic writes and recovery.
8. - [x] Reference `specs/hybridcore-state/migration-workflow.md` in onboarding/runbook material for schema upgrades.
9. - [x] Run `openspec validate add-hybridcore-state-implementation-spec --strict`.

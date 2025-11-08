## Tasks

1. - [x] Document logging bootstrap, formatter/handler configuration, rotation policies, and CI artifact expectations in the `hybridcore-logs` spec.
2. - [x] Define structured context propagation, masking boundaries, and helper extension rules within the spec requirements.
3. - [x] Add observability/testing + sink-extension requirements (fixture diffs, concurrency tests, backward-compatible sink upgrades).
4. - [x] Link `specs/hybridcore-logs/logging-bootstrap.md` from the architecture doc (`docs/hybridcore-architecture.md`) in the logging section.
5. - [x] Update `docs/proposals/hybridcore-logs-implementation-spec-proposal-prompt.md` to mention the bootstrap/context/rotation diagrams as required references.
6. - [x] Link `specs/hybridcore-logs/rotation-recovery.md` from an ops/runbook (e.g., `docs/drafts/*` or equivalent incident-response doc).
7. - [x] Reference `specs/hybridcore-logs/context-flow.md` in README or ops guidance where new sinks/enrichers are described.
8. - [x] Run `openspec validate add-hybridcore-logs-implementation-spec --strict`.

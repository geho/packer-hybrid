## Why

`specs/hybridcore-sources/spec.md` documents cloning/pinning and metadata tracking, but an implementation-ready spec needs deeper detail: repo lifecycle (clone/fetch/checkout/pin) with concurrency rules, air-gapped workflows, allowed transports, clean working-tree enforcement; metadata schemas for `state/sources.json` and lock files, atomic writes, schema evolution, visibility surfaces; failure recovery (partial clones, retries, manual overrides), auditing (who changed SHAs), security scanning integrations; and testing strategies (mocked git, contract tests, optional integration suites). Without this guidance, source management remains fragile and inconsistent.

## What Changes

- Describe the full repo lifecycle (clone, fetch, checkout, pin) including concurrency policies, air-gapped workflows, allowed transports, and clean working-tree enforcement.
- Specify metadata structures (`state/sources.json`, lock files), atomic write strategies, schema evolution, and status surfaces (CLI commands, dashboards).
- Cover failure recovery, auditing (who changed which SHA), manual overrides, and integration with security scanning of source repos.
- Mandate testing strategies: mocked git invocations, contract tests ensuring metadata correctness, and integration suites on sample repos via shallow clones.

## Impact

- Makes source synchronization deterministic and auditable across environments.
- Ensures metadata and state files remain consistent, even under failure or manual override scenarios.
- Strengthens CI/testing by codifying how to mock git operations and when to run real repo tests.

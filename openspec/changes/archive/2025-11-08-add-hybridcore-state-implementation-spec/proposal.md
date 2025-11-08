## Why

`specs/hybridcore-state/spec.md` outlines atomic writes and schema helpers but lacks implementation-ready detail about each JSON document, versioning strategy, cross-module integrations, and exhaustive testing. Contributors need prescriptive guidance on state files, read/write APIs, migration workflows, drift detection hooks, and corruption recovery to avoid inconsistent or fragile state handling.

## What Changes

- Enumerate every JSON artifact under `state/` (sources, config, manifests, packer outputs, etc.), describe schemas, versioning, atomic write guarantees, and locking strategy.
- Expand access API requirements with validation hooks, schema migration workflow, and backward compatibility promises for external consumers.
- Add requirements covering module integrations (sources, packer, templates, provisioners) to ensure state mutations are traceable, auditable, and recoverable after crashes.
- Define comprehensive testing/linting: schema fixtures, concurrency simulations, corruption injection tests, CLI commands that surface inconsistencies.

## Impact

- Creates a single source of truth for state files, preventing regressions across modules relying on shared metadata.
- Ensures atomic writes, migrations, and recovery procedures are consistent and auditable.
- Improves CI confidence via explicit tests and CLI sanity checks for state drift/corruption.

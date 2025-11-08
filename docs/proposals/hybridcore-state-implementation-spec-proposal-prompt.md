/prompts:openspec-proposal Hybridcore State implementation-ready spec:

- Enumerate every JSON document under `state/`, their schemas, versioning strategy, and atomic write guarantees (temp files, fsync, rename, locking where needed).
- Describe read/write helper APIs, validation hooks, schema migration workflow, and backward compatibility promises for consumers outside this repo.
- Capture integration points with other modules (sources, packer, templates, provisioners) so state mutations are traceable, auditable, and recoverable after crashes.
- Provide exhaustive testing/linting requirements: schema fixtures, concurrency simulations, corruption injection tests, and CLI commands that surface state inconsistencies.
  References: [openspec/specs/hybridcore-state/spec.md](openspec/specs/hybridcore-state/spec.md), [openspec/specs/hybridcore/spec.md](openspec/specs/hybridcore/spec.md)

<!--
Prompt-Source: docs/proposals/hybridcore-state-implementation-spec-proposal-prompt.md
Reference: [openspec/specs/hybridcore-state/spec.md](openspec/specs/hybridcore-state/spec.md)
Change-Start: PENDING
Change-Archived: PENDING
-->

## Why

`docs/spec-remediations/cli-remediations.md` lists multiple open topics: missing per-command semantics, undefined logging verbosity behaviour, lack of command→module mapping, and duplicated verification language. The CLI spec currently enumerates commands at a high level but leaves operators guessing about required inputs/validation. We need a remediation change that documents the command surface in detail, clarifies logging flags, adds a diagram, and references other specs instead of duplicating requirements.

## What Changes

- Add a formal requirement covering command semantics (arguments, exit codes, validation gates) with a table/list for `publish`, `clean`, `diag`, `status`, and wizard/TUI.
- Define logging/verbosity behaviour and reference `hybridcore-logs`.
- Add a command→module mapping diagram describing which hybridcore modules each command invokes.
- Update `docs/spec-remediations/cli-remediations.md` to move the addressed topics into “Closed Topics” and note remaining work (if any).

## Impact

- Operators get deterministic guidance for every CLI command and logging flag.
- Specs stay aligned (CLI references security/Logs specs rather than duplicating content).
- The remediation draft documents what was closed and keeps future work visible.

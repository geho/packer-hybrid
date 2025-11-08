## Why

The CLI spec currently lists top-level commands but lacks detailed expectations for arguments, logging, error handling, TUI/wizard UX, and the required verification gates (formatter, lint/tests, drift checks). Without these details, contributors interpret behaviours differently, and implementations risk diverging from the intended workflow captured in `openspec/project.md`.

## What Changes

- Document each CLI command’s responsibilities, required arguments/flags, and logging/error semantics.
- Define the wizard/TUI experience, including sample flows and how outputs map to non-interactive commands.
- Capture verification requirements (packer fmt/validate, lint/tests, drift detection) and testing expectations per command.

## Impact

- Provides a single source of truth for CLI behaviour, aligning implementations and tests.
- Enables reviewers and future UI layers (wizard/Django) to rely on consistent command semantics.
- No runtime code change yet; this is a spec update for the CLI capability.

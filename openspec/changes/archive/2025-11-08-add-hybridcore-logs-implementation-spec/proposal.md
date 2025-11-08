## Why

`specs/hybridcore-logs/spec.md` captures the high-level interface but lacks implementation-ready details: how CLI/tests bootstrap logging, which handlers/formats are mandatory, how rotation/redaction is configured, and what regression tests enforce these behaviors. Without this depth, contributors add ad-hoc log helpers, drift from the canonical `[timestamp] level component message` format, and ship inconsistent CI artifacts.

## What Changes

- Expand the `hybridcore-logs` spec with implementation-ready requirements detailing initialization hooks, formatter/handler configuration, rotation policies, redaction filters, and CI artifact integration.
- Define structured context propagation (env, component, command IDs), masking rules, and boundaries between shared helpers and module-specific enrichers.
- Add requirements covering observability/testing obligations (unit, integration, fixture-based contract tests) plus guidance for extending log sinks (JSON/syslog) while preserving backward compatibility.

## Impact

- Provides deterministic logging behavior across CLI, tests, and automation, simplifying troubleshooting.
- Ensures new contributors have prescriptive guidance for extending the logging stack without regressions.
- Improves CI signals by mandating artifact parity and rotation/corruption safeguards.

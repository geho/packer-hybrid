## Why

`docs/spec-remediations/hybridcore-logs-remediations.md` notes missing log shipping coverage (cloud sinks/syslog), logging flag interplay with CLI, retention policies, and references to security/audit logging. We need to update the logs spec to cover these behaviours and make Open Issues actionable.

## What Changes

- Add a requirement covering optional log sinks (`json`, syslog, cloud collectors) with configuration examples.
- Document CLI logging flag behaviour (`--verbose`, `--quiet`, `--json`) and align it with hybridcore-logs API.
- Specify retention/rotation policy guidance (retention period, artifact expectations) and reference security/audit logging requirements.
- Update the remediation draft (move completed items to “Closed Topics”).

## Impact

- Operators know how to configure log sinks and retention policies.
- CLI/logs specs stay aligned, reducing ambiguity.
- Security/audit logging references ensure compliance.

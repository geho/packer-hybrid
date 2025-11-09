# packer-hybrid

## Logging & Sink Extensions

See [specs/hybridcore-logs/context-flow.md](openspec/specs/hybridcore-logs/context-flow.md) for how structured context and redaction flow through console/file handlers and optional JSON/syslog sinks. Follow that diagram whenever adding new enrichers so all outputs keep the canonical `[timestamp] level component command_id message` format.

## Config Integrations

Configuration outputs feed multiple modules. Review [specs/hybridcore-config/config-integrations.md](openspec/specs/hybridcore-config/config-integrations.md) before changing vars or manifests so you understand how hashes drive `state`, `templates`, `packer`, and `provisioners`.

## State Atomic Writes

State helpers rely on strict atomic write semantics. See [specs/hybridcore-state/state-io.md](openspec/specs/hybridcore-state/state-io.md) for the temp-file/fsync/rename flow and audit logging requirements before modifying persistence code or recovery logic.

## Packer Drift & Artifacts

When touching packer automation, review [specs/hybridcore-packer/drift-flow.md](openspec/specs/hybridcore-packer/drift-flow.md) to understand hash comparison/remediation and [specs/hybridcore-packer/artifact-registry.md](openspec/specs/hybridcore-packer/artifact-registry.md) for how manifests/artifacts feed `hybridcore.state` and CI.

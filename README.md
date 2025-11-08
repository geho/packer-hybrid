# packer-hybrid

## Logging & Sink Extensions

See [specs/hybridcore-logs/context-flow.md](openspec/specs/hybridcore-logs/context-flow.md) for how structured context and redaction flow through console/file handlers and optional JSON/syslog sinks. Follow that diagram whenever adding new enrichers so all outputs keep the canonical `[timestamp] level component command_id message` format.

## Config Integrations

Configuration outputs feed multiple modules. Review [specs/hybridcore-config/config-integrations.md](openspec/specs/hybridcore-config/config-integrations.md) before changing vars or manifests so you understand how hashes drive `state`, `templates`, `packer`, and `provisioners`.

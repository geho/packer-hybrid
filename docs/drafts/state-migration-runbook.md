# State Schema Upgrade Runbook

Consult [specs/hybridcore-state/migration-workflow.md](openspec/specs/hybridcore-state/migration-workflow.md) when bumping `schema_version` for any state document. It outlines detection, migrate-per-version steps, validation, logging, and fallback/rollback expectations.

1. Inspect existing files and capture backups.
2. Implement `migrate_state()` steps per version.
3. Run local CLI checks and corruption tests before landing.
4. Announce schema bumps to downstream consumers.

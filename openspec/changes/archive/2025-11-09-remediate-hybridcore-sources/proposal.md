## Why

`docs/spec-remediations/hybridcore-sources-remediations.md` highlights missing air-gapped workflow coverage, security scanning/auditing requirements, manual override governance, and explicit metadata schema examples. The sources spec currently covers repo lifecycle and metadata at a high level but lacks these details.

## What Changes

- Add a requirement describing air-gapped workflows (mirrors, offline bundles) and validation steps.
- Document security scanning/auditing cadence and manual override policies (force-pin SHAs).
- Provide explicit metadata schema/sample references so CLI visibility is deterministic.

## Impact

- Operators get deterministic guidance for air-gapped environments and security scanning.
- Manual overrides become auditable and aligned with security/governance specs.
- Metadata schema samples ensure CLI visibility commands show accurate data.

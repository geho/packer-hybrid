## ADDED Requirements

### Requirement: Spec Purpose & Cross-Link Policy

Every capability spec under `openspec/specs/` SHALL include a meaningful Purpose section (no placeholders) and reference related specs/modules when applicable. When sub-specs exist (e.g., hybridcore modules), they MUST link back to the umbrella spec, and the umbrella spec MUST list them.

#### Scenario: Placeholder removal

- **WHEN** a new spec is archived
- **THEN** its Purpose section MUST describe scope in plain language and cite related specs; placeholders like “TBD … Update Purpose” are not permitted.

#### Scenario: Hybridcore cross-links

- **WHEN** a hybridcore module spec is updated or a new module is added
- **THEN** the module spec MUST link to `specs/hybridcore/spec.md`, and the umbrella spec MUST reference the module so tooling and readers can trace the hierarchy.

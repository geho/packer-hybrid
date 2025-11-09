## ADDED Requirements

### Requirement: Template Metadata & Change Detection

Templates spec SHALL document metadata fields/change detection.

#### Scenario: Metadata completeness

- **WHEN** metadata lacks provisioner info
- **THEN** change detection MUST refuse to proceed until schema is complete.

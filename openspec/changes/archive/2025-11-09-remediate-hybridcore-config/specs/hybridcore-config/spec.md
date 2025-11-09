## ADDED Requirements

### Requirement: Extendability & Secrets

Spec SHALL describe secret handling requirements in the extendability checklist.

#### Scenario: Secret onboarding

- **WHEN** a new secret is introduced
- **THEN** docs/tests MUST reference env/secret manager usage without storing cleartext.

### Requirement: OS Platform & Variant Overlays

Spec SHALL document platform/variant overlay precedence with examples.

#### Scenario: Variant precedence

- **WHEN** Azure variant overrides secrets
- **THEN** precedence MUST follow defaults → platform → variant → CLI answers.

### Requirement: Manifest & State Integration

Spec SHALL describe manifest/checksum updates in `state/config/<env>.json` and change detection.

#### Scenario: Config drift

- **WHEN** configs change
- **THEN** state hashes MUST be updated so downstream modules detect drift.

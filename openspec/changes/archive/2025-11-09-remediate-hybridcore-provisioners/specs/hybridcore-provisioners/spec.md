## ADDED Requirements

### Requirement: Provisioner Modes & Fallback

Spec SHALL document Puppet agent modes, opt-in precedence, and SSH fallback behaviour.

#### Scenario: Puppet mode selection

- **WHEN** operators choose `puppet.mode=server`
- **THEN** the spec MUST describe required assets/secrets and fallback rules.

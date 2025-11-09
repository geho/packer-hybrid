## MODIFIED Requirements

### Requirement: Drift Detection

Drift detection SHALL reference templates/provisioners/state Open Issues for alignment.

#### Scenario: Drift reference

- **WHEN** drift is detected
- **THEN** the spec MUST point operators to the relevant Open Issues so they can remediate upstream modules.

## ADDED Requirements

### Requirement: Cache & Parallelism

Packer caches/parallelism SHALL follow the documented invalidation/limit rules.

#### Scenario: Cache invalidation

- **WHEN** templates bump ISO versions
- **THEN** caches MUST be purged per spec before concurrent builds proceed.

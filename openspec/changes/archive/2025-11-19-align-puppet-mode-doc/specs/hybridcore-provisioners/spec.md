## MODIFIED Requirements

### Requirement: Provisioner Layout & Toggles

`hybridcore-provisioners` SHALL state that Puppet mode metadata lives in `state/provisioners/<env>/puppet.json`, and any operator documentation describing Puppet modes MUST reference that canonical file rather than `configs/<env>/puppet.auto.pkrvars.hcl`.

#### Scenario: Mode metadata guidance

- **WHEN** docs or helpers describe how to declare Puppet modes
- **THEN** they SHALL point to `state/provisioners/<env>/puppet.json` so implementations do not write metadata into `configs/…`.

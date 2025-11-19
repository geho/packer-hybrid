# Proposal: align-puppet-mode-doc

## Why

`docs/drafts/puppet-agent-modes.md` instructs contributors to persist Puppet mode metadata into `configs/<env>/puppet.auto.pkrvars.hcl`, while the published `hybridcore-provisioners` spec mandates storing that metadata in `state/provisioners/<env>/puppet.json`. This misleads operators and testers.

## What Changes

- Update the draft doc to reference the `state/provisioners/<env>/puppet.json` location and describe how templates consume the metadata.
- Cross-link the relevant spec sections so the doc stays anchored to the canonical requirements.

## Impact

- Aligns documentation with the spec to avoid incorrect storage paths.
- No behavioural change; implementation already targets the state path.

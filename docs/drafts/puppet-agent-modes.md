# Draft: Puppet Agent Modes

## Context

The provisioning spec references optional Puppet support but never states whether builds rely on standalone agents or integrate with a Puppet Server. Operators need explicit guidance to standardize image hardening flows.

## Goals

1. Define the supported Puppet agent modes (local standalone, master/client, remote apply).
2. Describe how operators declare the mode (global config vs CLI) and what assets (`templates/puppet/*`) are required.
3. Call out validation hooks so misconfigured Puppet modes fail fast.

## Proposed Behaviour

- Introduce a `puppet.mode` enum with `standalone`, `apply`, and `server`. Each mode specifies the expected manifests, hiera data, and connectivity requirements.
- `standalone` mode runs Puppet locally with manifests baked into the image; `server` mode bootstraps an agent that points to a configured Puppet Server endpoint; `apply` mode uploads manifests and runs `puppet apply` without long-lived agents.
- The CLI writes mode metadata into `configs/<env>/puppet.auto.pkrvars.hcl` so templates can conditionally include the right provisioner blocks.

## Open Questions

1. Where do we store Puppet certificates or tokens when `server` mode is selected?
2. Should `standalone` mode allow optional post-build hooks to strip Puppet packages?
3. Do we need per-platform deviations (e.g., Windows vs Linux paths) in the spec or leave that to implementation docs?

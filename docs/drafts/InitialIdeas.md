# Draft: Initial Hybrid Framework Ideas

## Packer Plugins Overview

### Common Configuration Themes

- Authentication: API token/service principal, username/password, subscription IDs.
- Compute shape: CPU, memory, disk, networking.
- Artifact output: templates/images per platform.
- Provisioning channels: SSH/WinRM, HTTP seed server, floppy/CD injection.

### Platform Highlights

- Proxmox: `proxmox-iso` and `proxmox-clone`, required `boot_iso`, node/storage options, template conversion automatic.
- vSphere: `vsphere-iso` and `vsphere-clone`, datacenter/cluster/datastore selectors, optional `vsphere-template` post-processor.
- Azure: `azure-arm`, managed image vs SIG output, service principal auth, tags, communicator selection.

## Example Framework Takeaways

### Directory Layout Parity

- `builds/` for packer HCL per OS.
- `config/` generated `.pkrvars.hcl` via `config.sh`.
- `scripts/`, `ansible/`, `manifests/` shared between repos.
- vSphere adds `artifacts/`, `terraform/`, `docs/` vs Proxmox’s leaner tree.

### Workflow Alignment

1. Clone repo, run `config.sh` to scaffold config files (supports env suffixes).
2. Run `build.sh` with optional env filter; builds run per OS/platform.
3. Use `validate.sh` or `build-ci` pipeline to run `packer fmt/validate`.
4. Provisioning stacks rely on Ansible roles + platform scripts; Windows automation uses unattended files + sysprep scripts.

### Multi-Cloud Unification Ideas

- Shared `common.pkr.hcl` plus per-platform HCL files.
- Common provisioning scripts invoked across Proxmox/vSphere, extendable to Azure.
- Parameterized variables for ISO location, storage pools, networks, credentials.
- Simultaneous builds per OS create templates/images on all targets with identical provisioning.

## Validation & CI Patterns

- Run `packer fmt`/`validate` before builds.
- Track manifests under `manifests/` and parse for artifact metadata.
- GitLab CI example for vSphere (matrix builds per OS).
- Manual scripts for Proxmox but same logic can feed CI with self-hosted runners.

## Next Steps

- Translate these ideas into permanent openspec entries as implementation progresses.
- Remove temporary research chapters once specs + this draft cover the required knowledge.

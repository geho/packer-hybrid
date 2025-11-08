/prompts:openspec-proposal Hybridcore Provisioners implementation-ready spec:

- Lay out how Ansible and Puppet stacks are structured on disk (roles, inventories, manifests), how toggles map to packer vars, and the validation pipeline for missing/extra assets.
- Define compatibility matrices (OS/platform vs. provisioner support), shared libraries between provisioners, and extension hooks for future tools while keeping deterministic outputs.
- Describe artifact generation (vars files, manifests, checksums), error messaging, and logging expectations so operators immediately see why a provisioner failed to initialize.
- Call for deep testing guidance: unit coverage over toggle logic, fixture-backed packer validate runs, provisioner-specific linting (ansible-lint/puppet parser validate), and how CI proves both enable/disable paths.
  References: [openspec/specs/hybridcore-provisioners/spec.md](openspec/specs/hybridcore-provisioners/spec.md), [openspec/specs/hybridcore/spec.md](openspec/specs/hybridcore/spec.md)

<!--
Prompt-Source: docs/proposals/hybridcore-provisioners-implementation-spec-proposal-prompt.md
Reference: [openspec/specs/hybridcore-provisioners/spec.md](openspec/specs/hybridcore-provisioners/spec.md)
Change-Start: PENDING
Change-Archived: PENDING
-->

# Provisioner CI Playbook

Use [specs/hybridcore-provisioners/testing-matrix.md](openspec/specs/hybridcore-provisioners/testing-matrix.md) to select lint + validate jobs when toggles or manifests change. Run the matrix before merging provisioner updates or packer upgrades.

Checklist:

1. Run ansible-lint + yamllint for Ansible paths.
2. Run puppet parser validate + metadata lint for Puppet paths.
3. Execute packer validate for Ansible-only, Puppet-only, and dual-mode combinations.
4. Record results and link to the change.

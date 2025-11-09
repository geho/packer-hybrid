## Why

`specs/hybridcore-provisioners/spec.md` defines high-level toggles, vars emission, and testing expectations but lacks implementation-ready detail on disk layout (roles, inventories, manifests), compatibility matrices between OS/platforms and provisioners, artifact generation (vars/manifests/checksums), error/logging expectations, and deep testing guidance (fixture-backed packer validates, provisioner-specific linting, CI matrix coverage). Contributors need prescriptive guidance to avoid drift between Ansible/Puppet stacks, ensure deterministic outputs, and prove both enable/disable paths in CI.

## What Changes

- Document the directory structure for Ansible/Puppet stacks, how toggles map to packer vars/files, and the validation pipeline for missing/extra assets.
- Define compatibility matrices (OS/platform vs provisioner support), shared libraries, extension hooks, and deterministic output rules.
- Describe artifact generation (vars files, manifests, checksums), error messages, and logging expectations when provisioners fail to initialize.
- Add exhaustive testing guidance: unit coverage for toggle logic, fixture-backed packer validate runs, provisioner-specific linting (ansible-lint, puppet parser validate), and CI matrices proving enable/disable paths.

## Impact

- Ensures provisioner tooling remains deterministic and well-documented, reducing onboarding time.
- Provides clear diagnostics/logging when provisioners fail, improving operator experience.
- Strengthens CI by requiring targeted linting/fixture tests for each provisioner/states combination.

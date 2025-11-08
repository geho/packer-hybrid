## Tasks

1. - [x] Convert the existing CLI specification into an `ADDED` delta with scenarios under `specs/cli/spec.md`.
2. - [x] Capture the hybridcore module requirements as `ADDED` deltas under `specs/hybridcore/spec.md`.
3. - [x] Document the multi-cloud template structure requirements under `specs/templates/spec.md`.
4. - [x] Describe provisioning (Ansible-first with optional Puppet) expectations under `specs/provisioning/spec.md`.
5. - [x] Capture verification, secrets, and documentation governance under `specs/security/spec.md`.
6. - [x] Run `openspec validate refactor-misplaced-specs --strict` and clean up `openspec/specs/` so only approved specs live there.
7. - [x] Update `.gitignore` so generated assets (`configs/<env>/*.auto.pkrvars.hcl`, `artifacts/`, `logs/`, `state/`, rendered cloud-init outputs) stay untracked per the governance spec.

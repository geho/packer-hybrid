# Tasks

## Prep

1. - [x] Review `openspec/specs/provisioning/spec.md`, `specs/hybridcore-provisioners/spec.md`, `specs/hybridcore-templates/spec.md`, `specs/security/spec.md`, and `docs/spec-remediations/provisioning-remediations.md`.
2. - [x] Run `openspec list`, `openspec list --specs`, and skim `openspec/project.md` to confirm dependencies.

## Implementation

3. - [x] Add OS-specific sections covering Windows parity, secret distribution, and cross-platform script requirements.
4. - [x] Define provisioner/platform lint/test expectations (testing matrix + CI gates).
5. - [x] Align provisioning metadata with hybridcore-provisioners/templates specs and document drift detection.
6. - [x] Add a governance-compliant diagram for config → provisioners → packer interactions and a CLI variable mapping table.
7. - [x] Require security-aligned secret handling (indirection, retention) with tests/reference to the security spec.
8. - [x] Update `docs/spec-remediations/provisioning-remediations.md` (move closed topics, note follow-ups).

## Wrap-up

9. - [x] Run `npx prettier --write` on touched Markdown/spec files.
10. - [x] `openspec validate remediate-provisioning-2025-11 --strict`.
11. - [x] Share `/prompts:openspec-apply remediate-provisioning-2025-11` details once proposal assets are ready. _Next command: `/prompts:openspec-archive remediate-provisioning-2025-11` after review._

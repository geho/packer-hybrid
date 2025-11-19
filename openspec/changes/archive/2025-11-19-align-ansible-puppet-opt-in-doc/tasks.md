# Tasks

## Proposal Clarifications

- [x] Plan to remove `docs/drafts/ansible-puppet-opt-in.md` once the opt-in behaviour is fully represented in specs/production docs (defer actual deletion to a follow-up change after verification).

## Implementation Tasks

- [x] Confirm no other proposals already touch the opt-in doc or fallback requirement.
- [x] Update `docs/drafts/ansible-puppet-opt-in.md` with the spec-accurate fallback description.
- [x] Run `openspec validate align-ansible-puppet-opt-in-doc --strict` (after spec/doc deltas) and fix issues.
- [x] Circulate with provisioning spec owner for review.

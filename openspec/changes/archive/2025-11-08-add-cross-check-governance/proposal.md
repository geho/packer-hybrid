## Why

We now have policies for references, prompts, and changelog updates, but there is no explicit requirement that specs, docs, and code cross-check one another during reviews. As a result, drift between specs↔docs↔code can slip through, and automation can’t enforce alignment. A dedicated governance rule is needed so every change verifies the relevant artifacts stay in sync.

## What Changes

- Define cross-check expectations (specs↔docs, specs↔code, docs↔code) and the verification steps reviewers must follow.
- Require tooling (lint scripts/checklists) to ensure references are mutual, links valid, and deviations reported.
- Document how to record exceptions when intentional drift is approved.

## Impact

- Reduces divergence between specs, documentation, and implementation.
- Makes reviews consistent by providing a checklist and automation hooks.
- Policy-only change; no runtime behaviour impact.

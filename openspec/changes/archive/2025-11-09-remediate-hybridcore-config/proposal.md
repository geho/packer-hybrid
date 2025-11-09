## Why

`docs/spec-remediations/hybridcore-config-remediations.md` highlights missing content in the config spec: OS image variant handling, platform-specific overlays/secret guidance, missing cross-links to templates/state Open Issues, and manifest/checksum integration details. We must remediate the spec so new inputs/platforms follow deterministic rules and secrets remain safe.

## What Changes

- Add a requirement describing OS image variants/platform overlays (precedence rules, examples).
- Extend the extendability checklist with secret handling/redaction requirements and references to docs/tests.
- Reference templates/state remediations so config changes stay aligned with downstream modules.
- Document manifest/checksum integration with `state/config/<env>.json` and change-detection expectations.

## Impact

- Contributors understand how to add new variants/platforms without breaking security or drift detection.
- Config spec explicitly references templates/state, reducing misalignment.
- Secret handling guidance keeps redaction consistent across config workflows.

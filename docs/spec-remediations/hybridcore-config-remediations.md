# Hybridcore Config Spec Gaps

1. **Gaps** – No guidance on OS image variants and platform-specific overlays (e.g., Azure vs Proxmox secrets). Need explicit precedence rules and examples.
2. **Completeness** – Secret handling/redaction for new inputs isn’t covered in extendability checklist; add required doc/test updates.
3. **Alignment** – Config spec doesn’t reference CLI logging, templates Open Issues, or state hash expectations; add cross-links.
4. **Integrity** – Need manifest/checksum integration details with `state/config/<env>.json` and Change Detection rules.

Remediation: extend spec/drafts with variant overlay rules, secret-handling requirements, cross-module references, and hashing guidance.

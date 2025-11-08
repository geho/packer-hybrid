## Why

Project contributors only have a brief sentence in `project.md` about commenting, which leaves docstrings, inline comments, module headers, and helper organization up to individual interpretation. This causes inconsistent documentation quality and increases review time because reviewers must enforce unwritten rules.

## What Changes

- Define enforcement-ready requirements under the governance spec for:
  - Docstring expectations at the module/class/function level, including structure and references to specs/diagrams.
  - Inline comment usage so code stays readable without redundant narration.
  - Section headers and module organization conventions (mixins, helper functions, nested classes).
  - Examples illustrating the expected layout, plus lint/test hooks to keep the guidance verifiable.
- Keep `project.md` focused on high-level rationale by pointing to the governance spec for the detailed rules.

## Impact

- Improves readability and onboarding by documenting a single source of truth for in-code documentation.
- Gives reviewers concrete acceptance criteria that lint/test automation can enforce.
- No runtime code impact; this is a policy-only change scoped to the governance capability.

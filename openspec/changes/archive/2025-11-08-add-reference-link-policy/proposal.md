## Why

Governance currently requires prompts and docs to “link” to specs, but it never defines a canonical Markdown format, anchor syntax, or placement rules. As a result, prompts mix HTML comments, plain-text references, and sometimes omit clickable links altogether, which slows reviews and makes automated validation difficult.

## What Changes

- Add governance requirements that standardize Markdown reference formatting (relative links, allowed labels, anchor usage) for prompts, docs, and specs.
- Define enforcement guidance (linters/hooks) so CI can detect missing/invalid links.
- Outline migration expectations for existing references so contributors know how to update legacy files.

## Impact

- Creates a single source of truth for how references must look, improving readability and automation.
- No runtime code change; affects documentation and governance policy only.

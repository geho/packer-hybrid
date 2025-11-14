## Coding Style Playbook

- **Single Source of Truth**: Obey `.editorconfig`, `.gitattributes`, and project formatter scripts. If the formatter is unavailable, mirror its rules manually and call out any drift in your summary.
- **Naming Signals Intent**: Prefer descriptive names for files, modules, and identifiers. Use common abbreviations only when they are well known in the domain; otherwise expand them.
- **Small, Focused Units**: Keep functions/classes narrowly scoped. If a function exceeds ~30 lines or mixes concerns, propose a split before adding more logic.
- **Consistent Indentation & Layout**: Match the repository’s indentation style everywhere (spaces vs tabs, 2 vs 4 spaces). When copying code, reformat it rather than preserving inconsistent whitespace.
- **Side-Effect Awareness**: Default to pure/immutable helpers. When mutation is required, make it obvious via naming (`mut`, `builder`, etc.) or comments.
- **Dead Code Removal**: Delete unused imports, variables, and commented-out blocks as part of each change unless the user explicitly asks to keep them.
- **DRY with Context**: Extract shared logic when duplication exceeds two occurrences or risks divergence. If deduplication would obscure intent, document the decision to keep copies.
- **Backward Compatibility**: Assume new work targets the current spec only. Mention explicitly if you are skipping legacy paths or compatibility shims so reviewers can confirm.
- **Deviations Require Notes**: Whenever you must break these conventions (expedient fix, generated code), explain it in the PR summary or code comment so future contributors understand the trade-off.

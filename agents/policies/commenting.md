## Commenting Guidelines

- **Prefer Self-Documenting Code**: First try to clarify intent via naming, function extraction, or small helper utilities before falling back to comments.
- **Comment When Context Exceeds Code**: Use short, evergreen comments to capture non-obvious decisions (protocol quirks, performance trade-offs, security concerns). Avoid narrating line-by-line behavior.
- **Summaries Over Narratives**: For large blocks (algorithms, math, regex), add a short paragraph explaining the strategy, not each statement.
- **No Change Logs in Code**: Never describe “why” a change was made historically (“Fix for issue #123”). If future readers need that context, add it to commit/PR summaries instead.
- **Update or Remove Stale Comments**: When modifying code, edit adjacent comments or delete them if they are no longer accurate.
- **Docstrings Where Consumers Benefit**: Provide function/module docstrings when the API is reused broadly or exported publicly; focus on behavior, inputs/outputs, and side effects.

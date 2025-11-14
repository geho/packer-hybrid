## MODIFIED Requirements

### Requirement: Prompt Definition SoT

Reusable prompts SHALL live exclusively in `.codex/prompts/*.md`. Each file MUST begin with YAML front matter containing `description:` and `argument-hint:` keys, and the body MUST include the guardrails block delimited by `<!-- OPENSPEC:START -->` / `<!-- OPENSPEC:END -->`.

#### Scenario: `.codex/prompts` metadata

- **GIVEN** governance now treats `.codex/prompts/*.md` as the canonical prompt repository
- **WHEN** maintainers edit a prompt file
- **THEN** the file MUST keep YAML front matter (`description`, `argument-hint`) and the guardrails block bounded by `<!-- OPENSPEC:START -->` / `<!-- OPENSPEC:END -->`.

### Requirement: Prompt Metadata Enforcement

CI and pre-commit hooks SHALL run `python tools/check_codex_prompts.py` (or equivalent) to ensure every `.codex/prompts/*.md` file contains valid front matter and guardrails before changes land.

#### Scenario: Automated checks

- **WHEN** CI or pre-commit runs
- **THEN** it MUST execute `python tools/check_codex_prompts.py` (or equivalent) so any prompt missing front matter or guardrails fails fast.

### Requirement: Policy Reference SoT

Repository-wide policy references MUST defer to `agents/startup.md` and the linked `agents/policies/*.md` docs instead of repeating prose inside governance/spec chapters.

#### Scenario: Agents policies as primary reference

- **WHEN** governance cites coding style, commenting, validation, or testing rules
- **THEN** it SHALL link to `agents/startup.md` (and the downstream `agents/policies/*.md`) instead of duplicating the text inside the spec.

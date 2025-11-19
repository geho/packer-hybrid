# linter: markdownlint

## commands

### version

```shell
mdl --version
```

### help

```shell
mdl --help
```

### list rules

```shell
mdl --list-rules
```

### linting

```shell
mdl [options] [FILE.md|DIR ...]
```

**Prompt files:** `.mdlrc` excludes `agents/prompts/*.md` entirely (they’re intentionally non-standard). Run `mdl agents/prompts/...` without `--config` only if you need a raw lint report.

## options (useful)

- `--config <file>` – point to a project-specific `.mdlrc`/`.mdlrc.rb` (use `.mdlrc` in this repo to suppress prompt-specific rules).
- `--rules <list>` – limit checks to particular rules (comma-separated).
- `--warnings` – emit warnings in addition to errors (default suppresses them).
- `--ignore-front-matter` – skip YAML front matter blocks when linting docs/blog posts.
- `--json` – machine-readable output for CI or editor integrations.

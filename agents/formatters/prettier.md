# formatter: prettier

## commands

### version

```shell
npx prettier --version
```

### help

```shell
npx prettier --help
```

### format check

```shell
npx prettier --check [options] [file/dir/glob ...]
```

### format apply

```shell
npx prettier --write [options] [file/dir/glob ...]
```

## options (useful)

- `--config <path>` – point to a specific `.prettierrc` when running from subdirectories.
- `--ignore-path <file>` – honor custom ignore lists (defaults to `.prettierignore`).
- `--cache` – speed up repeated runs by caching file hashes (respect `--cache-location` when set).
- `--loglevel warn|error` – reduce noisy output in CI.

## globs (examples)

- `*.md` # Markdown file
- `*.mkdn` # Markdown file
- `*.mmd` # Mermaid Diagram in Markdown file format

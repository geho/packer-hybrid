# linter: mmdc (Mermaid CLI)

## commands

### version

```shell
mmdc --version
```

### help

```shell
mmdc --help
```

### render (lint via render check)

```shell
mmdc -i path/to/diagram.mmd -o /tmp/diagram.svg
```

Rendering acts as linting—syntax errors cause the command to exit non-zero with the offending line/column.

## options (common)

- `-t <theme>` – set theme (default, dark, forest, neutral).
- `-b transparent|white|#RRGGBB` – control background color during rendering.
- `-w <width>` / `-H <height>` – override output size to catch layout issues deterministically.

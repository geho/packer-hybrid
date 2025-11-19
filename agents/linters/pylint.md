# linter: pylint

## commands

### version

```shell
pylint --version
```

### help

```shell
pylint --help
```

### list rules

```shell
pylint --list-msgs-enabled
```

### linting

```shell
pylint [options]
```

## options (useful)

- `--rcfile <path>` – force pylint to use the repo’s configuration file.
- `--disable <msg-id>[,<msg-id>...]` / `--enable <msg-id>` – tweak rule selection per run.
- `--exit-zero` – keep CI pipelines green while collecting reports (use sparingly).
- `-j <N>` – run checks in parallel (set to number of CPU cores for speed).

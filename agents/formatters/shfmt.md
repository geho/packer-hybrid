# formatter: shfmt

## commands

### version

```shell
shfmt --version
```

### help

```shell
shfmt --help
```

### format check (diff mode)

```shell
shfmt -d [files...]
```

### format apply (in-place)

```shell
shfmt -w [files...]
```

## options (useful)

- `-i <N>` – set indentation width (default 0 = tabs). Use `-i 2` or `-i 4` to match project style.
- `-ci` – indent switch cases.
- `-sr` – simplify redirects (`<<EOF` placement, etc.).
- `-kp` – keep column alignment for comments and heredoc bodies.

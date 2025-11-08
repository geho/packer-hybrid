## ADDED Requirements

### Requirement: Docstring Coverage

All Python modules, classes, and public functions SHALL include docstrings that: (a) cite the driving spec/diagram IDs, (b) summarize behaviour, inputs, and outputs, and (c) describe side effects or external resources.

#### Scenario: Module/class/function docstrings

- **WHEN** a contributor adds `tools/packer-hybrid/sync.py`
- **THEN** the module-level docstring MUST list the governing spec (e.g., `specs/cli/spec.md#requirement-deterministic-command-surface`), each class docstring MUST cover responsibilities/mixins used, and function docstrings MUST describe parameters + return values, as illustrated:

```python
"""Sync subcommands (spec: specs/cli/spec.md#deterministic)."""

class SourceSyncCommand(CommandMixin):
    """Drive sources sync per specs/hybridcore/spec.md#requirement-source-management."""

    def run(self, args: argparse.Namespace) -> None:
        """Fetch plugins and exit non-zero on drift."""
```

### Requirement: Inline Comment Discipline

Inline comments SHOULD explain _why_ complex logic exists and MUST avoid restating obvious code; every comment SHALL reference the variable or flow it clarifies.

#### Scenario: Explaining non-obvious logic

- **WHEN** a provisioner helper adds a retry loop for transient SSH failures
- **THEN** an inline comment such as `# Retry SSH once to tolerate Azure quota delays` MUST precede the block; conversely, `# increment i` MUST NOT appear because it adds no context.

### Requirement: Section Headers & Module Layout

Modules SHALL organize content with ASCII section headers in the order: imports, constants/config, mixins, core classes, helper functions, CLI entry points/tests. Headers MUST match the pattern `# === Section Name ===`.

#### Scenario: Organized module skeleton

- **WHEN** a developer creates `hybridcore/templates.py`
- **THEN** they MUST group content as:

```python
# === Imports ===

# === Constants ===

# === Mixins ===

# === Core Classes ===

# === Helper Functions ===
```

so reviewers can navigate quickly.

### Requirement: Helper & Mixin Placement

Shared helpers and mixins SHALL live in their own blocks within a module (or dedicated modules) and include docstrings describing expected overrides and extension points.

#### Scenario: Mixin expectations

- **WHEN** a new `StateFileMixin` is defined
- **THEN** it MUST sit under the `# === Mixins ===` header with a docstring outlining required attributes/methods the consumer must supply.

### Requirement: Documentation Linting

CI and local workflows MUST run at least `python -m compileall` plus a docstring/comment linter (`python -m pydocstyle` or `ruff check --select D,COM`) for files touched in a PR; failures MUST block merges.

#### Scenario: Pre-submit enforcement

- **WHEN** a contributor runs `make lint`
- **THEN** the script MUST execute the docstring linter and fail if docstrings are missing, badly formatted, or references (spec IDs) are absent for public APIs.

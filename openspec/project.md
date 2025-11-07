# Project Context

## Purpose

- Deliver and maintain the **packer-hybrid** framework that produces identical “golden” images for Proxmox VE, VMware vSphere, and Microsoft Azure from a single Packer codebase (see docs/drafts/InitialIdeas.md#multi-cloud-unification-ideas).
- Provide the `tools/packer-hybrid` CLI (Python 3, stdlib only) to manage plugin sources under `sources/`, scaffold/update templates, execute `packer build/validate`, and publish artifacts to Proxmox templates, vSphere content libraries, and Azure managed images.
- Merge the lessons learned from both public example frameworks (summarized in docs/drafts/InitialIdeas.md#example-framework-takeaways) into a unified multi-cloud structure with standardized variables, scripts, and CI hooks.
- Keep the framework spec-first: every feature references an openspec entry/diagram, and the CLI enforces drift detection against specs/templates.

## Tech Stack

- **HashiCorp Packer (HCL2)** with the official plugins:
  - Proxmox plugin (sources/packer-plugin-proxmox; pin >=1.2.3 per docs/drafts/InitialIdeas.md#platform-highlights).
  - VMware vSphere plugin (sources/packer-plugin-vsphere; pin >=1.4.0 per docs/drafts/InitialIdeas.md#platform-highlights).
  - Azure ARM plugin (sources/packer-plugin-azure; pin >=2.5.0 per docs/drafts/InitialIdeas.md#platform-highlights).
- **Python 3 (stdlib only)** for CLI/tooling (argparse, dataclasses, logging, pathlib, subprocess, unittest).
- **Bash** glue scripts (when unavoidable) constrained to repo root tooling.
- **Prettier** for Markdown/docs formatting as enforced in AGENTS.md.

## Project Conventions

### Code Style

- All Python sources (including executables in `tools/` without `.py` extension) start with `#!/usr/bin/env python3`, include SPDX license header, UTC timestamp, and references to the driving spec + diagram assets.
- Favour class-based CLI commands with mixins for shared concerns (logging, filesystem IO, spec lookups). Use `argparse` sub-parsers to expose verbs such as `sync`, `validate`, `build`, `publish`.
- Standard library only; prefer `pathlib`, `subprocess.run(check=True)`, `dataclasses.dataclass`, `typing.Protocol` to keep code self-documenting. Avoid implicit globals; inject dependencies via constructors/mixins.
- Tests are written first (`unittest.TestCase`) and live next to the code (e.g., `tools/tests/test_packer_hybrid.py`). Use fixtures + tempdirs to isolate filesystem effects.

### Architecture Patterns _(Spec Migration: templates/multi-cloud-structure.md)_

- Treat the repository as a **multi-cloud mono-repo** with explicit boundaries:
  - `tools/packer-hybrid`: orchestrates plugin sync, template generation, packer commands, artifact publication, metadata export, and exposes reusable mixins for filesystem + process orchestration.
  - `templates/` fans out into:
    - `templates/common.pkr.hcl` for shared builders/provisioners and `templates/platforms/{proxmox,vsphere,azure}.pkr.hcl` for platform-specific sources.
    - `templates/vars/{linux,windows}/{common,<platform>}.pkrvars.hcl` plus overlays for OS families/versions.
    - `templates/scripts/{linux,windows}` and `templates/ansible` (and optional `templates/puppet`) for provisioning assets.
  - `configs/<env>/` holds generated `*.auto.pkrvars.hcl` snapshots (one per platform, optional per OS) produced by the CLI’s config commands.
  - `sources/` mirrors upstream git repositories (plugins + example frameworks) with pinned SHAs/tags tracked by metadata.
  - `artifacts/` retains packer manifests, exported metadata, and optional post-build payloads; `logs/` stores CLI + packer logs; `state/packer-hybrid.json` records timestamps, plugin versions, template digests, and build history for drift detection.
- Packer templates follow a **composition approach**:
  - Common builders and provisioners live in `common.pkr.hcl`; platform-specific builders live in the per-cloud files referenced above (see docs/drafts/InitialIdeas.md#multi-cloud-unification-ideas).
  - Naming convention: `source.<plugin>-iso.<image_name>` or `source.azure-arm.<image_name>` so builds can reference `source.*.*` lists without string duplication.
- Workflow is **data-driven**: all commands operate by merging `templates/**/*.pkr.hcl`, environment vars, and generated configs, never editing packer files in-place. The CLI refuses to run builds if `state/` shows drift against manifests or if `sources/` has uncommitted changes.

### CLI Workflow & Interfaces _(Spec Migration: cli/packer-hybrid-cli.md)_

- Deterministic subcommands back every operation (all stdlib, no interactive prompts unless explicitly requested):
  - `packer-hybrid init` – bootstrap directories, ensure `sources/` repos exist, seed `templates/` skeletons, create default env configs.
  - `packer-hybrid sources sync` – fetch/tag required plugin/example repos and update metadata.
  - `packer-hybrid config --env <name> [--from answers.json]` – render/update env-specific `.pkrvars.hcl` files; supports non-interactive inputs for CI and a `wizard` flag for guided prompts.
  - `packer-hybrid validate --env <name> --os <id> --targets proxmox,vsphere,azure` – run `packer fmt -check` and `packer validate` across requested builders, failing fast on drift.
  - `packer-hybrid build ...` – orchestrate multi-cloud builds (parallel where possible), stream logs, capture manifests, update `state/`.
  - `packer-hybrid publish` – run post-build steps (template conversion, Azure SIG replication, metadata export).
  - `packer-hybrid status|inspect` – summarize plugin versions, repo SHAs, manifest history, pending drift.
  - `packer-hybrid clean --scope {work,artifacts,state}` – purge temp dirs/manifests/logs without touching templates unless explicitly asked.
  - `packer-hybrid diag` – bundle logs/manifests for troubleshooting.
- Optional **text UI** (`packer-hybrid tui` or `wizard`) provides a menu-driven experience (curses-based) for new operators. It still shells out to the same subcommands so scripted and interactive flows stay consistent.

### Shared Python Core _(Spec Migration: core/hybridcore-package.md)_

- Business logic lives in a reusable stdlib-only package (working name `hybridcore`) so the CLI, tests, and future Django services import the same modules:
  - `hybridcore/config` – renders `.pkrvars.hcl` from templates, merges env overlays, validates schemas, and exposes helpers like `generate_env_config`.
  - `hybridcore/sources` – clones/syncs plugin + example repos, pins SHAs, updates metadata in `state/`.
  - `hybridcore/templates` – enumerates build targets, builds the list of packer files per platform/OS, enforces naming rules, and inspects provisioning assets.
  - `hybridcore/provisioners` – describes Ansible/Puppet stacks, verifies required roles/modules, emits packer variable switches, and becomes the seam for the follow-up Puppet spec.
  - `hybridcore/packer` – wraps `packer fmt/validate/build`, handles log streaming, parses manifests, and normalizes exit codes for higher layers.
  - `hybridcore/state` – persists `state/packer-hybrid.json`, tracks plugin versions, manifests, drift indicators, and exposes transactional update helpers.
  - `hybridcore/logs` – centralizes logging format/rotation so CLI and web tasks emit consistent records.
- `tools/packer-hybrid` becomes a thin argparse shim over `hybridcore`, and any Django/worker process can reuse the same APIs without duplicating orchestration logic.

### Provisioning Tooling _(Spec Migration: provisioning/ansible-and-puppet.md)_

- **Ansible-first**: provisioners default to `ansible`/`ansible-local` roles located in `templates/ansible/roles/{common,linux,windows,platform_*}`, ensuring identical hardening across clouds (see docs/drafts/InitialIdeas.md#workflow-alignment).
- **Optional Puppet**: teams can opt into masterless Puppet by populating `templates/puppet/{manifests,modules}`. Builders gate Puppet provisioners behind `var.enable_puppet` flags so a single template can switch between Ansible and Puppet. CLI helpers (`packer-hybrid config --provisioner puppet`) generate the necessary `puppet.conf`/Hiera stubs and ensure modules sync before builds.
- Both provisioner stacks share supporting assets (cloud-init seeds, sysprep scripts) kept under `templates/scripts/`, and the CLI verifies required tools exist before invoking Packer.

### Testing Strategy

- **Unit tests**: Python `unittest` suites for CLI command parsing, mixin behaviour, filesystem interactions (use `tempfile.TemporaryDirectory`), and subprocess wrappers (mocked).
- **Template tests**: `packer fmt -check` + `packer validate` run per platform/OS combination. CLI exposes `packer-hybrid validate --platform {proxmox,vsphere,azure}` to run targeted checks (docs/OverviewPlugins/09_ValidationAndPluginManagement.md).
- **Integration smoke tests**: optionally run nightly builds on PR merges using lightweight “dry-run” configs (e.g., minimal Ubuntu) to ensure multi-cloud compatibility like in docs/OverviewPlugins/07_MultiCloudTemplateExample.md.
- **CI** gates: lint (ruff optional when allowed, else `python -m compileall`), unit tests, and `packer validate`. Test data sits under `tests/fixtures/`.

### Git Workflow

- Trunk-based with short-lived `feature/<scope>` branches feeding PRs. Each PR:
  - References its openspec change or adds one when behaviour shifts.
  - Updates relevant research/doc chapters (docs/OverviewPlugins/_, docs/OverviewExampleRepos/_) when new findings exist.
  - Runs `prettier --write` on touched Markdown and `packer-hybrid validate`.
- Keep `sources/` synced via explicit commits (avoid detached HEAD). Use `git submodule` or a dedicated metadata file to track upstream revisions so CI can reproduce builds.

## Domain Context

- **Common configuration surface**: IPMI/SSH credentials, storage pools, networks, ISO locations, and artifact metadata align across all three plugins (docs/OverviewPlugins/02_CommonConfiguration.md). This enables a unified variable schema consumed by the CLI.
- **Platform specifics**:
  - Proxmox requires node IDs, storage pools, and HTTP autoinstall endpoints (docs/OverviewPlugins/03_ProxmoxPlugin.md).
  - vSphere needs datacenter/cluster/folder targeting plus post-build template conversion (docs/OverviewPlugins/04_vSpherePlugin.md).
  - Azure outputs managed images/shared image gallery objects and mandates service principal auth (docs/OverviewPlugins/05_AzurePlugin.md).
- **Example frameworks insight**: both public repos share config/init scripts, environment-aware vars, and provisioning stacks (see docs/drafts/InitialIdeas.md#example-framework-takeaways). These notes are treated as hints; durable learnings must migrate into openspec entries or a curated `docs/knowledge-base.md`.
- **Unified framework goal**: adopt the simultaneous-build flow described in docs/drafts/InitialIdeas.md#multi-cloud-unification-ideas—single command builds identical images per platform, with consistent provisioning + artifact tagging.

## Verification & Quality Gates

- Always run (and keep green):
  - `prettier --write` on affected docs/specs.
  - `python -m compileall` or equivalent lint suite plus `unittest` for touched modules.
  - `packer fmt -check` + `packer validate` for all impacted OS/platform targets (CLI subcommands wire into these checks).
  - Drift detection via `packer-hybrid status` to ensure manifests/state align before/after changes.
- Changes touching provisioning, templates, or hybridcore modules must include unit tests and, where feasible, a smoke test plan (documented in PR description) referencing the corresponding spec section.

## Security & Secrets Handling

- Never commit credentials or cloud-specific secrets. All sensitive values flow via environment variables, secret managers, or `.auto.pkrvars.hcl` placeholders encrypted/stored outside git.
- CLI commands must refuse to run if obvious secret leaks are detected (e.g., `.pkrvars.hcl` residing outside `configs/<env>/` with plaintext secrets).
- Access policies per platform:
  - Proxmox: token with minimal required privileges (template builds + storage upload).
  - vSphere: service account scoped to specific datacenter/cluster/datastore.
  - Azure: service principal limited to build/image resource groups.
- Document any new secret or IAM requirement in the relevant spec before implementation.

## Documentation Expectations

- Temporary research (`docs/drafts/InitialIdeas.md`) informs early decisions but is not SoT. Any durable rule must appear in `openspec/` or stable docs before merging.
- When specs change, update `project.md` references and, if needed, add short summaries to `docs/drafts/InitialIdeas.md` until the dedicated spec is live.
- Pull requests must list which specs/docs were updated (or why none needed) to keep alignment explicit.

## Spec Lifecycle Guidance

- Use `project.md` for project-wide norms. Author dedicated specs under `openspec/specs/` when:
  - Introducing/altering CLI commands or UX.
  - Modifying hybridcore modules or provisioning stacks.
  - Changing template layout, CI requirements, or security posture.
- Each spec/change request should include:
  - Problem statement, proposed solution, testing/rollout plan, and back-compat considerations.
  - Cross-links back to `project.md` and other specs it supersedes or complements.
- Before coding, ensure an approved spec exists (or confirm the change is covered by existing specs). If not, file a `/prompts:openspec-proposal …` request first.
- Store reusable proposal prompts in `docs/proposals/<topic>-proposal-prompt.md` so future assistants can copy/paste the approved wording without digging through history. When a prompt is used and the spec merges, note the spec link inside the prompt file for traceability.

## Future Extensions

- **Django web frontend**: long-term, expose the same orchestration logic via a Django app (forms to edit configs, trigger builds, view manifests). Core functionality lives in shared Python modules imported by both the CLI and the web app, ensuring no duplicated business logic. Web-triggered builds execute via queued tasks that invoke the CLI routines and stream logs/artifacts into the UI.
- **UI parity**: the text UI (`packer-hybrid wizard`) and any future web frontend consume the same command layer and state formats, so operators can move between interfaces without behavioural drift.

## Important Constraints

- Python tooling uses **only the standard library** (no venv/pip). Executables in `tools/` have no `.py` suffix, include headers (license, timestamp, spec & diagram references), and are marked executable.
- Specs/diagrams live under `openspec/` (Mermaid diagrams in `openspec/specs/` with quoted labels per AGENTS.md). Every implementation cites the relevant spec + diagram IDs in its header.
- Prettier formatting after any Markdown edit is mandatory; `.editorconfig`/`.gitattributes` govern line endings and must be honored.
- The CLI must keep `sources/` clean (no untracked changes) before kicking off builds, detect missing plugins, and refuse to run builds without validated configs.
- Builds must be data-driven: no hard-coded secrets, all credentials sourced from `.pkrvars.hcl` or environment variables managed via the CLI’s config commands.

## External Dependencies

- HashiCorp Packer binary (>=1.10) and official plugins (pulled from sources listed below).
- Git repositories cloned under `sources/`:
  - https://github.com/hashicorp/packer-plugin-proxmox.git
  - https://github.com/hashicorp/packer-plugin-vsphere.git
  - https://github.com/hashicorp/packer-plugin-azure.git
  - https://github.com/vmware/packer-examples-for-vsphere
  - https://github.com/ajschroeder/proxmox-packer-examples
- Infrastructure targets: Proxmox VE cluster (API + storage pools), VMware vCenter/ESXi estate, Azure subscription/resource groups capable of hosting build + image resource groups.

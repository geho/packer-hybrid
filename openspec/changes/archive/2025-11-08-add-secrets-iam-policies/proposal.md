## Why

The security spec outlines high-level expectations (no secrets in git, minimal IAM scopes), but it lacks concrete guidance on how credentials are stored (env vars vs secret managers), how to detect leaked secrets, and what workflows exist for rotation or dummy/testing data. Contributors need an explicit policy so they know which files stay untracked, how to document secret locations, and how to verify that IAM scopes match the supported platforms.

## What Changes

- Add detailed requirements to the security spec covering:
  - Storage conventions for secrets (environment variables, secret manager paths, encrypted files) and how they are referenced from configs.
  - IAM scope definitions per platform (Proxmox, vSphere, Azure) with rotation/testing guidance.
  - Secret-leak detection expectations (tools, CI gates) and developer workflows for rotating or testing with dummy data.

## Impact

- Provides actionable guidance for operators and contributors handling credentials.
- Enables automation (lint/CI) to verify secret policies are followed.
- No runtime code changes—policy/spec update only.

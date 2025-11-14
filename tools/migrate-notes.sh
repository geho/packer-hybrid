#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd -- "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"
if [[ $# -ne 1 ]]; then
  echo "Usage: tools/migrate-notes.sh <change-id>" >&2
  exit 1
fi
exec "$SCRIPT_DIR/migrate_notes.py" "$1" --repo-root "$REPO_ROOT"

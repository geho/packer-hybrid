# source this file

export CODEX_HOME="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )/.codex"
[ -d "${CODEX_HOME}/prompts" ] || mkdir -p "${CODEX_HOME}/prompts"
[ -f "${CODEX_HOME}/auth.json" ] || ln -s ~/.codex/auth.json "${CODEX_HOME}/auth.json"
[ -f "${CODEX_HOME}/config.toml" ] || ln -s ~/.codex/config.toml "${CODEX_HOME}/config.toml"
[ -f "${CODEX_HOME}/history.jsonl" ] || ln -s ~/.codex/history.jsonl "${CODEX_HOME}/history.jsonl"
[ -f "${CODEX_HOME}/internal_storage.json" ] || ln -s ~/.codex/internal_storage.json "${CODEX_HOME}/internal_storage.json"
[ -d "${CODEX_HOME}/log/" ] || ln -s ~/.codex/log "${CODEX_HOME}/log"
[ -d "${CODEX_HOME}/sessions/" ] || ln -s ~/.codex/sessions "${CODEX_HOME}/sessions"
[ -f "${CODEX_HOME}/version.json" ] || ln -s ~/.codex/version.json "${CODEX_HOME}/version.json"

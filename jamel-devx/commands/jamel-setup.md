---
description: Apply the JAMEL team Claude Code setup (shared settings, statusline, RTK, marketplaces, optional ClickUp/codex)
---

# /jamel-setup — JAMEL DevX bootstrap

You are applying the JAMEL agency's shared Claude Code configuration. These are the things a plugin
cannot ship declaratively (a plugin's own `settings.json` only honors `agent` + `subagentStatusLine`),
so they must be written into the user's settings. **Be careful, idempotent, and ask for confirmation
before writing.**

## Rules
- **Never** read, print, or modify any secrets/tokens (`.credentials.json`, OAuth caches). Only touch
  the keys listed below.
- Read `~/.claude/settings.json` first. Compute a merged result. **Show the user a concise diff of what
  will change and ask for confirmation before writing.** Skip keys the user already has set to a
  different value unless they agree to override.
- Idempotent: running twice changes nothing the second time.
- The bundled statusline lives at `${CLAUDE_PLUGIN_ROOT}/assets/jamel-statusline.sh`. Do NOT point
  settings at `${CLAUDE_PLUGIN_ROOT}` (it changes on every plugin update) — copy it to a stable path.

## Steps

### 1. Shared settings (merge into `~/.claude/settings.json`)
Add/ensure these keys (do not remove unrelated user keys):
```json
{
  "env": { "DISABLE_NON_ESSENTIAL_MODEL_CALLS": "1", "DISABLE_COST_WARNINGS": "1" },
  "effortLevel": "xhigh",
  "tui": "fullscreen",
  "editorMode": "normal",
  "spinnerTipsEnabled": false,
  "agentPushNotifEnabled": true,
  "remoteControlAtStartup": true
}
```
Note: do **not** force `skipAutoPermissionPrompt` — mention it as an optional opt-in the user can add
themselves (it reduces permission friction but lowers a safety gate).

### 2. Statusline
- Copy `${CLAUDE_PLUGIN_ROOT}/assets/jamel-statusline.sh` to `~/.claude/jamel-statusline.sh` and
  `chmod +x` it.
- Set in `~/.claude/settings.json`:
  ```json
  { "statusLine": { "type": "command", "command": "~/.claude/jamel-statusline.sh" } }
  ```
- Requires `jq` (the script uses it). If `jq` is missing, run `brew install jq` (with confirmation).

### 3. RTK (token compression)
- `jamel-devx` already ships the `PreToolUse`/Bash hook that runs `rtk hook claude` (guarded: it
  no-ops when `rtk` is absent). You only need the binary.
- If `command -v rtk` fails: run `brew install rtk` (it is in homebrew-core; confirm first).
- **De-duplicate:** if the user's `~/.claude/settings.json` already has a global `PreToolUse` hook
  running `rtk hook claude`, offer to remove it — the plugin now provides it, and keeping both runs RTK
  twice per Bash call.

### 4. Marketplaces + curated plugins
- The 4 curated plugins (superpowers, frontend-design, code-review, context7) are hard dependencies of
  `jamel-devx` and are auto-installed/enabled from `claude-plugins-official` when this plugin is enabled.
  Confirm with `claude plugin list` that they are enabled; if `claude-plugins-official` is not a known
  marketplace, add it: `claude plugin marketplace add anthropics/claude-plugins-official`.
- **Optional: OpenAI Codex** (`/codex:review`, delegation — needs an OpenAI API key). Offer to install:
  ```
  claude plugin marketplace add openai/codex-plugin-cc
  claude plugin install codex@openai-codex
  ```
  Then tell the user to run `/codex:setup`.

### 5. ClickUp MCP
- `jamel-devx` ships the ClickUp MCP server config (`https://mcp.clickup.com/mcp`, HTTP + OAuth).
- Tell the user to run `/mcp` and authenticate with their own ClickUp account (their own OAuth — no
  secrets are stored in the repo). Note: ClickUp allowlists vetted MCP client redirect URIs; if the
  OAuth flow is rejected, they may need to use ClickUp's claude.ai integration instead.

### 6. Team conventions (CLAUDE.md)
- The canonical conventions live at `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` (Python/venv rules, RTK usage,
  general agency conventions), wrapped in `<!-- JAMEL-DEVX:BEGIN -->` / `<!-- JAMEL-DEVX:END -->` markers.
- Offer to merge that marked block into `~/.claude/CLAUDE.md` (a plugin's CLAUDE.md is not auto-loaded).
  If the markers already exist there, replace the block between them (idempotent); otherwise append it.
  Confirm before writing and never disturb the user's other CLAUDE.md content.

### 7. Finish
- Summarize exactly what changed.
- Tell the user to run `/reload-plugins` (to pick up hooks/MCP) and, if statusline didn't appear,
  restart Claude Code.
- Run `claude plugin list` and `/doctor` mentally — flag any `dependency-*` errors.

Optional argument (extra preferences or "skip clickup"/"with codex"): $ARGUMENTS

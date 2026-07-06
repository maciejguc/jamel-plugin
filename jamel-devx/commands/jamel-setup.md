---
description: Apply the JAMEL team Claude Code setup (shared settings, statusline, RTK + caveman, marketplaces, optional ClickUp/codex)
---

# /jamel-setup — JAMEL DevX bootstrap

You are applying the JAMEL agency's shared Claude Code configuration. These are the things a plugin
cannot ship declaratively (a plugin's own `settings.json` only honors `agent` + `subagentStatusLine`),
so they must be written into the user's settings, or installed via a package manager. **Be careful,
idempotent, cross-platform, and ask for confirmation before writing or installing.**

## Rules
- **Resolve the config directory FIRST and use it for every path below.** Claude Code honors
  `CLAUDE_CONFIG_DIR` (sandbox/multi-profile testing); the config dir is:
  `CFG="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"`. Run `echo "${CLAUDE_CONFIG_DIR:-$HOME/.claude}"` once and
  target **that** directory. **Never hard-code `~/.claude`** — otherwise sandbox testing silently writes
  to the real profile. Below, `$CFG` means the resolved directory.
- **Never** read, print, or modify any secrets/tokens (`.credentials.json`, OAuth caches).
- **Only** touch the settings keys listed in step 1. **Do NOT copy or add any MCP server config or
  `permissions` into `$CFG/settings.json`** — in particular leave the user's personal `pencil` MCP and
  `mcp__pencil` permission untouched. The plugin ships its own MCP (ClickUp) separately.
- Read `$CFG/settings.json` first. Compute a merged result. **Show a concise diff and ask for
  confirmation before writing.** Skip keys the user already set differently unless they agree to override.
- Idempotent: running twice changes nothing the second time.
- **Package manager: Homebrew everywhere.** JAMEL standardizes on `brew` for all installable deps
  (macOS, Linux, and Windows **via WSL** — Homebrew has no native Windows support). On Windows, Claude
  Code and this setup are expected to run inside a WSL shell. The only thing not from brew is caveman
  (a GitHub npm package), installed via `npx`.

## Steps

### 1. Shared settings (merge into `$CFG/settings.json`)
Add/ensure exactly these keys (do not remove unrelated user keys, do not add MCP/permissions):
```json
{
  "env": { "DISABLE_NON_ESSENTIAL_MODEL_CALLS": "1", "DISABLE_COST_WARNINGS": "1" },
  "effortLevel": "high",
  "tui": "fullscreen",
  "editorMode": "normal",
  "spinnerTipsEnabled": false,
  "agentPushNotifEnabled": false,
  "remoteControlAtStartup": false
}
```
Note: do **not** set `skipAutoPermissionPrompt` here. It is undocumented and lowers a permission/
confirmation gate, so it must stay an individual, conscious opt-in — never a team default. If a user
asks, explain it and let them add it to their own settings themselves.

### 2. Statusline
- Copy `${CLAUDE_PLUGIN_ROOT}/assets/jamel-statusline.sh` to `$CFG/jamel-statusline.sh` and make it
  executable. Do NOT point settings at `${CLAUDE_PLUGIN_ROOT}` (it changes on every plugin update).
- Set `statusLine.command` to the **absolute** resolved path of `$CFG/jamel-statusline.sh` (e.g.
  `/Users/you/.claude/jamel-statusline.sh`, or the sandbox path under `CLAUDE_CONFIG_DIR`):
  `{ "statusLine": { "type": "command", "command": "<abs path to $CFG/jamel-statusline.sh>" } }`.
- The script needs `jq`: `brew install jq` if missing (confirm first). On Windows this runs in WSL, so
  the same `brew install jq` applies and the bash statusline works as on macOS/Linux.

### 3. RTK (compress Bash command output, 60–90% fewer tokens)
RTK is `rtk-ai/rtk`. Install the binary via brew, then run its own integration installer (it writes the
Claude Code hook itself — we deliberately do **not** ship a raw shell hook in the plugin).
1. If `rtk` is missing: `brew install rtk` (confirm first). Fallback if Rust is present but brew can't
   provide it: `cargo install --git https://github.com/rtk-ai/rtk`.
2. Run `rtk init -g` (installs/refreshes RTK's Claude Code hook globally; idempotent).
3. Verify: `rtk --version` and `rtk gain`. Confirm it's the Token Killer (not "Rust Type Kit").
4. **De-duplicate:** if `$CFG/settings.json` already has a manual `PreToolUse` hook running
   `rtk hook claude` AND `rtk init -g` added its own, offer to remove the manual one so RTK doesn't run
   twice per Bash call.
   Note: `rtk init -g` writes to the real `~/.claude` by default. When testing under `CLAUDE_CONFIG_DIR`,
   tell the user RTK's own integration may target `~/.claude` regardless — verify where it wrote and, in
   a sandbox, prefer inspecting rather than relying on it landing in `$CFG`.

### 4. Caveman (compress model output + tool descriptions — complementary to RTK, no conflict)
Caveman shrinks Claude's *responses* and MCP tool descriptions; RTK shrinks *Bash output*. Different
layers, safe together. Not a Claude Code plugin, and not in Homebrew, so install via npm (needs Node ≥18):
- Ensure Node: `brew install node` if `node` is missing (confirm).
- `npx -y github:JuliusBrussee/caveman` (confirm).
- After install, mention the commands: `/caveman [lite|full|ultra]`, `/caveman-commit`, `/caveman-review`,
  `/caveman-stats`, `/caveman-compress <file>`.

### 5. Homebrew bootstrap (if `brew` is missing)
Everything above assumes `brew`. If it is missing:
- **macOS / Linux / WSL**: offer to install Homebrew via the official installer (the one place a `curl`
  bootstrap is justified — there is no package manager to install the package manager):
  `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`.
  Confirm first; afterwards remind the user to add brew to PATH if the installer asks.
- **Native Windows (no WSL)**: Homebrew is not supported. Tell the user to set up WSL (Ubuntu) and run
  Claude Code + `/jamel-setup` from inside WSL. Do not fall back to other managers — JAMEL standardizes
  on brew-via-WSL for a single, consistent toolchain.

### 6. Marketplaces + curated plugins
- The 4 curated plugins (superpowers, frontend-design, code-review, context7) are hard dependencies of
  `jamel-devx`, auto-installed/enabled from `claude-plugins-official`. Confirm with `claude plugin list`;
  if `claude-plugins-official` is missing, add it: `claude plugin marketplace add anthropics/claude-plugins-official`.
- **Optional: OpenAI Codex** (`/codex:review`, delegation — needs an OpenAI API key). Offer to install:
  `claude plugin marketplace add openai/codex-plugin-cc` then `claude plugin install codex@openai-codex`,
  then `/codex:setup`.

### 7. ClickUp MCP
- `jamel-devx` ships the ClickUp MCP server config (`https://mcp.clickup.com/mcp`, HTTP + OAuth).
- Tell the user to run `/mcp` and authenticate with their own ClickUp account (their own OAuth — no
  secrets stored in the repo). Note: ClickUp allowlists vetted MCP client redirect URIs; if rejected,
  they can fall back to ClickUp's claude.ai integration.

### 8. Team conventions (CLAUDE.md)
- Canonical conventions live at `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`, wrapped in
  `<!-- JAMEL-DEVX:BEGIN -->` / `<!-- JAMEL-DEVX:END -->`.
- Offer to merge that marked block into `$CFG/CLAUDE.md` (a plugin's CLAUDE.md is not auto-loaded).
  Replace the block between markers if present (idempotent); otherwise append. Confirm first; never
  disturb the user's other CLAUDE.md content.

### 9. Finish
- Summarize exactly what changed.
- Tell the user to run `/reload-plugins` (to pick up hooks/MCP) and, if the statusline didn't appear,
  restart Claude Code. Suggest `/jamel-tour` for a guided overview.
- Flag any `dependency-*` errors from `claude plugin list`.

Optional argument (e.g. "skip clickup", "with codex", "no caveman", "skip rtk"): $ARGUMENTS
- If the argument requests skipping a component (e.g. "skip rtk" — useful for hermetic sandbox tests
  since `rtk init -g` may touch the real `~/.claude`), omit that step entirely.

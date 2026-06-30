---
description: Apply the JAMEL team Claude Code setup (shared settings, statusline, RTK + caveman, marketplaces, optional ClickUp/codex)
---

# /jamel-setup — JAMEL DevX bootstrap

You are applying the JAMEL agency's shared Claude Code configuration. These are the things a plugin
cannot ship declaratively (a plugin's own `settings.json` only honors `agent` + `subagentStatusLine`),
so they must be written into the user's settings, or installed via a package manager. **Be careful,
idempotent, cross-platform, and ask for confirmation before writing or installing.**

## Rules
- **Never** read, print, or modify any secrets/tokens (`.credentials.json`, OAuth caches).
- **Only** touch the settings keys listed in step 1. **Do NOT copy or add any MCP server config or
  `permissions` into `~/.claude/settings.json`** — in particular leave the user's personal `pencil` MCP
  and `mcp__pencil` permission untouched. The plugin ships its own MCP (ClickUp) separately.
- Read `~/.claude/settings.json` first. Compute a merged result. **Show a concise diff and ask for
  confirmation before writing.** Skip keys the user already set differently unless they agree to override.
- Idempotent: running twice changes nothing the second time.
- **Detect the OS** and pick the right package manager (see step 3). Prefer a package manager over raw
  `curl | bash`.

## Steps

### 1. Shared settings (merge into `~/.claude/settings.json`)
Add/ensure exactly these keys (do not remove unrelated user keys, do not add MCP/permissions):
```json
{
  "env": { "DISABLE_NON_ESSENTIAL_MODEL_CALLS": "1", "DISABLE_COST_WARNINGS": "1" },
  "effortLevel": "high",
  "tui": "fullscreen",
  "editorMode": "normal",
  "spinnerTipsEnabled": false,
  "agentPushNotifEnabled": true,
  "remoteControlAtStartup": false
}
```
Note: do **not** force `skipAutoPermissionPrompt` — mention it as an optional opt-in (it reduces
permission friction but lowers a safety gate).

### 2. Statusline
- Copy `${CLAUDE_PLUGIN_ROOT}/assets/jamel-statusline.sh` to `~/.claude/jamel-statusline.sh` and make it
  executable. Do NOT point settings at `${CLAUDE_PLUGIN_ROOT}` (it changes on every plugin update).
- Set: `{ "statusLine": { "type": "command", "command": "~/.claude/jamel-statusline.sh" } }`.
- The script needs `jq`. Install if missing: macOS `brew install jq`, Linux `apt/dnf install jq`,
  Windows `winget install jqlang.jq`. On Windows the script needs **Git Bash** (the statusline runs via
  Git Bash; warn the user if it isn't present).

### 3. RTK (compress Bash command output, 60–90% fewer tokens)
RTK is `rtk-ai/rtk` and is cross-platform. Install the binary, then run its own integration installer
(it writes a platform-correct Claude Code hook itself — we deliberately do **not** ship a raw shell hook
in the plugin, because a POSIX guard would break under Windows PowerShell).
1. If `rtk` is missing, install with the platform package manager (confirm first):
   - **macOS / Linux**: `brew install rtk`
   - **Windows**: `winget install rtk-ai.rtk`
   - **Fallback (any OS with Rust)**: `cargo install --git https://github.com/rtk-ai/rtk`
2. Run `rtk init -g` (installs/refreshes RTK's Claude Code hook globally; idempotent).
3. Verify: `rtk --version` and `rtk gain`. Confirm it's the Token Killer (not "Rust Type Kit").
4. **De-duplicate:** if `~/.claude/settings.json` already has a manual `PreToolUse` hook running
   `rtk hook claude` (the user added one by hand) AND `rtk init -g` added its own, offer to remove the
   manual one so RTK doesn't run twice per Bash call.

### 4. Caveman (compress model output + tool descriptions — complementary to RTK, no conflict)
Caveman shrinks Claude's *responses* and MCP tool descriptions; RTK shrinks *Bash output*. Different
layers, safe together. It is not a Claude Code plugin, so install via npm (cross-platform, needs Node ≥18):
- `npx -y github:JuliusBrussee/caveman` (with confirmation).
- After install, mention the commands: `/caveman [lite|full|ultra]`, `/caveman-commit`, `/caveman-review`,
  `/caveman-stats`, `/caveman-compress <file>`.

### 5. Homebrew bootstrap (only if needed, only on macOS/Linux)
If a step above wants `brew` and it is missing:
- **macOS/Linux**: offer to install Homebrew via the official installer (this one legitimately uses the
  official `curl` script — there is no package manager to install the package manager):
  `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`.
  Confirm first; after install, remind the user to add brew to PATH if the installer asks.
- **Windows**: do **not** install Homebrew — use `winget` (built into modern Windows) instead, as shown
  in step 3. If a tool isn't on winget, fall back to `cargo`/`npx`.
Recommendation: prefer `winget` (Windows) / `brew` (mac) / `cargo`/`npx` fallbacks; bootstrap Homebrew
only on mac/Linux and only with explicit consent.

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
- Offer to merge that marked block into `~/.claude/CLAUDE.md` (a plugin's CLAUDE.md is not auto-loaded).
  Replace the block between markers if present (idempotent); otherwise append. Confirm first; never
  disturb the user's other CLAUDE.md content.

### 9. Finish
- Summarize exactly what changed.
- Tell the user to run `/reload-plugins` (to pick up hooks/MCP) and, if the statusline didn't appear,
  restart Claude Code. Suggest `/jamel-tour` for a guided overview.
- Flag any `dependency-*` errors from `claude plugin list`.

Optional argument (e.g. "skip clickup", "with codex", "no caveman"): $ARGUMENTS

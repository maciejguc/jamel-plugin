---
description: Apply the JAMEL team Claude Code setup (shared settings, statusline, RTK + ponytail, marketplaces, optional ClickUp/codex)
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
  Code and this setup are expected to run inside a WSL shell. The only thing not from brew is ponytail
  (a Claude Code plugin, installed via `claude plugin`; its hooks need Node — `brew install node`).

## Steps

### 1. Shared settings (merge into `$CFG/settings.json`)
Add/ensure exactly these keys (do not remove unrelated user keys, do not add MCP/permissions):
```json
{
  "env": {
    "DISABLE_NON_ESSENTIAL_MODEL_CALLS": "1",
    "DISABLE_COST_WARNINGS": "1",
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "80"
  },
  "effortLevel": "high",
  "tui": "fullscreen",
  "editorMode": "normal",
  "spinnerTipsEnabled": false,
  "agentPushNotifEnabled": false,
  "remoteControlAtStartup": false
}
```
`CLAUDE_AUTOCOMPACT_PCT_OVERRIDE: "80"` triggers Claude Code's auto-compaction at 80% context usage
(default is ~95%) — compacts before the window is cramped, leaving buffer for the summarization and
matching the statusline turning red at ≥80%. Tunable per dev: 85 for context-heavy work, 70 for long
autonomous sessions. Mention this to the user.
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

### 4. Ponytail — installed BY DEFAULT (auto-active every session)
Ponytail makes Claude write *less code* (YAGNI ladder: skip → reuse what's in the codebase → stdlib →
native platform feature → installed dependency → one line → only then the minimum that works); RTK
shrinks *Bash output*. Different layers, safe together. **On Claude Code it is a plugin that
SELF-ACTIVATES from message one at level `full`** (SessionStart hook; needs `node` on PATH — from
`brew install node`. Without node the skills still work, only the always-on activation stays quiet).
- Install by default (skip only if the user passes "no ponytail"):
  `claude plugin marketplace add DietrichGebert/ponytail` then `claude plugin install ponytail@ponytail`,
  then `/reload-plugins`. Confirm before installing.
- It governs *what code gets built*, not how Claude talks — client-facing text (`jamel-pm`) is
  unaffected. It never cuts input validation, error handling, security or accessibility.
- Levels: `/ponytail lite|full|ultra|off` (per-session). Pin the default via `PONYTAIL_DEFAULT_MODE`
  env or `defaultMode` in `~/.config/ponytail/config.json`. Extra commands: `/ponytail-review`,
  `/ponytail-audit`, `/ponytail-debt`, `/ponytail-gain`, `/ponytail-help`.
- **Migration from caveman:** if `caveman@caveman` is installed (older JAMEL setups shipped it), offer
  to remove it: `claude plugin uninstall caveman@caveman` and `claude plugin marketplace remove caveman`.
  JAMEL replaced caveman with ponytail — caveman's per-turn ruleset overhead outweighed its prose
  savings in agentic coding sessions.

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

### 7. ClickUp MCP (provided by the organization — nothing to install here)
- The plugin does **not** ship a ClickUp MCP. JAMEL provides ClickUp org-wide (claude.ai connector),
  auto-active once the dev is logged in with their org account.
- Just verify it's connected (`claude mcp list` / `/mcp` shows a ClickUp server as Connected). If a dev
  doesn't have it, that's an org-provisioning matter, not this setup.

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

Optional argument (e.g. "with codex", "no ponytail", "skip rtk"): $ARGUMENTS
- If the argument requests skipping a component (e.g. "skip rtk" — useful for hermetic sandbox tests
  since `rtk init -g` may touch the real `~/.claude`), omit that step entirely.

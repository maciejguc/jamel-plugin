# JAMEL — team conventions (Claude Code)

> Canonical JAMEL agency conventions. `/jamel-setup` offers to merge the block below into
> `~/.claude/CLAUDE.md` (a plugin's CLAUDE.md is not auto-loaded into context). The block is delimited by
> the `JAMEL-DEVX:BEGIN/END` markers so updates are idempotent.

<!-- JAMEL-DEVX:BEGIN -->

## Python — execution & dependencies

- **Always use a `venv` in the current working directory (cwd)** to run Python and install dependencies.
- **If `venv` does not exist** in the cwd — create it: `python3 -m venv venv`.
- Use the venv binaries directly:
  - Run: `./venv/bin/python <script>.py`
  - Install: `./venv/bin/pip install <package>`
- **Never install globally** (no `sudo pip`, no `pip install` outside the venv).
- If `requirements.txt` / `pyproject.toml` exists — install dependencies into the venv before running.

## RTK (Rust Token Killer) — output compression

- Bash commands are automatically piped through `rtk` (a `PreToolUse` hook installed via `rtk init -g`)
  → 60–90% token savings. Nothing to do manually.
- Use meta-commands directly: `rtk gain` (analytics), `rtk gain --history`, `rtk discover`,
  `rtk proxy <cmd>` (raw, unfiltered command — for debugging).
- Verify: `rtk --version`, `which rtk`. Install: `brew install rtk` (macOS/Linux/WSL; fallback
  `cargo install --git https://github.com/rtk-ai/rtk`). Claude Code integration: `rtk init -g`.
- Team package manager: **Homebrew everywhere**. Windows → via **WSL** (Homebrew has no native Windows).
- ⚠️ Name collision: if `rtk gain` fails, you may have a different `rtk` (Rust Type Kit) on PATH.

## caveman — model-output compression

- Shortens **the model's replies** and tool descriptions (a different layer than RTK — RTK compresses
  *Bash output*, caveman *model output*). Complementary, no conflict.
- Commands: `/caveman [lite|full|ultra]`, `/caveman-commit`, `/caveman-review`, `/caveman-stats`,
  `/caveman-compress <file>`. Install (by default via `/jamel-setup`; on Claude Code it is a plugin):
  `claude plugin marketplace add JuliusBrussee/caveman` + `claude plugin install caveman@caveman`.
- **Self-activates from message one at `full`** (every session starts with caveman ON); compresses only
  *output* (not reasoning), adds ~1–1.5k input tokens/turn. The level is per-session — it cannot be
  pinned via a config file.
- **For client-facing content** (estimates/specs): `/caveman lite`, or `claude plugin disable caveman@caveman`.

## General conventions

- Code, comments, identifiers and commit messages — in **English**. **Client-facing content**
  (estimates/specs/briefs and any text delivered to a client) — in **Polish**.
- Run `code-review` (curated plugin) on the branch diff before merging.
- Use `superpowers` skills for methodical workflow (planning, TDD, debugging).

<!-- JAMEL-DEVX:END -->

# jamel-plugin — project conventions

This repo is a **Claude Code plugin marketplace** (`name: "jamel"`) hosting two first-party plugins:
`jamel-devx` (team dev experience) and `jamel-pm` (PM/Account toolkit). The repo is **public**.

## Git workflow — PR-only merges to main

- **Every change goes through a feature branch (or worktree) and a pull request into `main`.**
  Never commit or push directly to `main`.
- Rationale: (1) team convention — review gate before merge; (2) forward-compatibility with the
  **claude.ai organization-managed plugin channel**. Anthropic's sources disagree on what triggers its
  sync: support.claude.com article 13837433 says **only a merged PR with a plugin version bump**;
  claude.com/docs/plugins/org-sync says **any push to the default branch** when "Sync automatically"
  is on. PR-only merges with a version bump are safe under both.
- Squash-merge preferred; PR title in English, imperative mood.

## Plugin update channels (know the difference)

| Channel | How updates propagate | Constraints |
|---|---|---|
| **Self-serve** (`/plugin marketplace add maciejguc/jamel-plugin`) | git pull of `main`; any merged change propagates (commit-SHA versioning — no version field needed) | Background auto-update off by default for third-party marketplaces; `/plugin marketplace update jamel` always works |
| **Org-managed** (claude.ai Organization settings → Plugins) | Sync on merged PR with a version bump (support 13837433) or on any default-branch push with "Sync automatically" (docs/plugins/org-sync) — sources conflict; up to 30 min; failed sync may temporarily remove plugins | Requires **private/internal repo** + Claude GitHub App + Team/Enterprise plan. Not usable while this repo is public |

- First-party plugins currently use **commit-SHA versioning** (no `version` field) — correct for the
  self-serve channel. If the org-managed channel is ever adopted (repo would have to go private),
  add explicit `version` fields and bump them in every release PR.

## Language

- Code, comments, commit messages, this file: **English**.
- User-facing plugin content (commands, tour, welcome, READMEs) and client-facing output: **Polish**.

## Internal docs — never commit

`TESTING.md`, `ROADMAP.md`, `HANDOFF.md` (and `jamel-pm/TESTING.md`) are **gitignored, local-only**
internal docs. Do not force-add them; the repo is public.

## Structure notes

- `jamel-devx/CLAUDE.md` holds the canonical team conventions inside `<!-- JAMEL-DEVX:BEGIN/END -->`
  markers; `/jamel-setup` merges that block into each dev's `~/.claude/CLAUDE.md` idempotently.
  Keep the markers intact; keep the block compact (it is loaded into context every session).
- External tools ship as `dependencies` resolved from their **original** marketplaces
  (`claude-plugins-official`, `openai-codex`, ponytail) — never fork or vendor them.
- `jamel-pm` unit tests: `./jamel-pm/scripts/.venv/bin/python -m pytest jamel-pm/scripts/tests/ -q`.
- Safe end-to-end testing: sandbox profile via `CLAUDE_CONFIG_DIR` (see local `TESTING.md`).

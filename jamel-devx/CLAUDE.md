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

## ponytail — minimal-code discipline

- Makes the model write **less code**: before any code, climb the ladder — needs to exist at all
  (YAGNI) → already in the codebase → stdlib → native platform feature → installed dependency → one
  line → only then the minimum that works. Never cuts input validation, error handling, security or
  accessibility. A different layer than RTK (RTK compresses *Bash output*, ponytail shrinks *the
  solution*). Complementary, no conflict.
- Commands: `/ponytail [lite|full|ultra|off]`, `/ponytail-review` (diff over-engineering review),
  `/ponytail-audit`, `/ponytail-debt`, `/ponytail-gain`, `/ponytail-help`. Install (by default via
  `/jamel-setup`; on Claude Code it is a plugin): `claude plugin marketplace add DietrichGebert/ponytail`
  + `claude plugin install ponytail@ponytail`. Its hooks need `node` on PATH (`brew install node`).
- **Active from message one at `full`** (SessionStart hook, ~1.6k tokens once per session, also injected
  into subagents). Default level pinnable via `PONYTAIL_DEFAULT_MODE` env or `defaultMode` in
  `~/.config/ponytail/config.json`; scope subagent injection with `PONYTAIL_SUBAGENT_MATCHER`.
- It governs *what gets built*, not how Claude talks — client-facing text (jamel-pm) is unaffected.
- Repo/client conventions override ponytail where they conflict (e.g. project test standards beat its
  "one runnable check" rule; the analyze→plan→approval workflow beats "ship the lazy version now").

## General conventions

- Code, comments, identifiers and commit messages — in **English**. **Client-facing content**
  (estimates/specs/briefs and any text delivered to a client) — in **Polish**.
- Run `code-review` (curated plugin) on the branch diff before merging.
- Use `superpowers` skills for methodical workflow (planning, TDD, debugging).

## Workflow — analyze before you build

- Non-trivial task → analyze first, propose an approach/plan, wait for explicit approval before
  implementing (plan mode or a written plan).
- Never start the next phase of an approved plan (merge, deploy, cleanup) without being asked.
- Follow the 4-stage flow: analyze → plan → implement → verify; don't skip stages.

## Forms (AskUserQuestion) — answer questions in chat

- If the user's form response ("Other" / notes) contains a question or new information, answer it
  in chat as the **final message of the turn** — never answer and re-open a form in the same turn
  (text followed by a tool call is not reliably shown, so the user never sees the answer). This
  applies in plan mode too.
- Re-present a form only in a later turn, only if a structured choice is still pending, and with
  options updated to reflect what the user wrote. If the exchange has turned conversational,
  continue in plain text instead of another form.

## Scope & environment discipline

- Touch only what the task requires; no drive-by refactors or fixes of adjacent code — ask first.
- Never install packages, run setup scripts, or modify the developer's environment/config without
  explicit approval.
- Respect manual edits: if code looks hand-tuned or contradicts the design/spec, ask instead of
  "fixing" it.

## Git & verification

- Work on feature branches or git worktrees (developer's choice) — never directly on main.
- Never merge or deploy without an explicit instruction.
- Keep temporary/audit artifacts out of the repo (gitignore or outside the tree).
- "Done" requires evidence: run tests/build and show output; for UI — screenshots; for performance —
  before/after metrics. Never claim "fixed" without proof.

## Frontend standards (web projects)

- Verify responsive behavior at 375 / 768 / 1440 px before calling UI work done.
- Content and translations come from the CMS/database — never invent or machine-translate copy that
  already exists; flag mismatches instead.
- Accessibility target: WCAG 2.2; measure performance with Lighthouse (document before/after when
  optimizing).

## Report findings along the way

- Bugs spotted incidentally (during analysis or while working on another task): don't fix silently
  and don't ignore — report them to the developer with a description and a proposed fix, or suggest
  further diagnosis if the root cause is unclear.
- Optimization opportunities (performance, architecture, best practices): when you see clear room
  for improvement, recommend it — briefly, with the expected benefit — but don't implement without
  approval.

<!-- JAMEL-DEVX:END -->

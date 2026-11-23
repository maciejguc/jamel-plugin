#!/bin/sh
# Repo check for jamel-gfx. Run from the repo root: sh jamel-gfx/tests/check.sh
P=jamel-gfx
PJ=$P/.claude-plugin/plugin.json
SK=$P/skills/standardy/SKILL.md
bad=0
fail() { echo "FAIL: $1"; bad=1; }

# 1. marketplace + plugin validate
claude plugin validate . >/dev/null 2>&1 || fail "claude plugin validate . exited non-zero"
claude plugin validate $P >/dev/null 2>&1 || fail "claude plugin validate $P exited non-zero"

# 2. forbidden components
for f in hooks agents bin scripts .mcp.json; do
  [ -e "$P/$f" ] && fail "forbidden $P/$f exists"
done
if [ -f "$PJ" ]; then
  [ "$(jq 'has("dependencies")' "$PJ" 2>/dev/null)" = false ] || fail "plugin.json has dependencies (or is invalid JSON)"
else
  fail "missing $PJ"
fi

# 3. skill limits
set -- $P/skills/*/SKILL.md
[ -f "$1" ] || fail "no SKILL.md under $P/skills"
for s in "$@"; do
  [ -f "$s" ] || continue
  d=$(basename "$(dirname "$s")")
  [ "$(wc -l < "$s")" -lt 500 ] || fail "$s has 500+ lines"
  n=$(sed -n '2,/^---$/{s/^name: *//p;}' "$s" | head -n 1)
  desc=$(sed -n '2,/^---$/{s/^description: *//p;}' "$s" | head -n 1)
  [ "$n" = "$d" ] || fail "$s name '$n' != dir '$d'"
  [ "${#n}" -le 64 ] || fail "$s name over 64 chars"
  [ -n "$desc" ] || fail "$s has no description"
  case "$desc" in *': '*|*' #'*) fail "$s description breaks YAML (': ' or ' #')";; esac
  [ "${#desc}" -le 1024 ] || fail "$s description over 1024 chars"
done

# 4. version sync
if [ -f "$PJ" ] && [ -f "$SK" ]; then
  pv=$(jq -r .version "$PJ" 2>/dev/null)
  sv=$(sed -n 's/^Wersja standardów: *\([0-9][0-9.]*\).*/\1/p' "$SK" | head -n 1)
  [ -n "$sv" ] && [ "$pv" = "$sv" ] || fail "version mismatch: plugin.json '$pv' vs SKILL.md '$sv'"
elif [ -f "$PJ" ]; then
  fail "missing $SK"
fi

[ $bad = 0 ] && echo OK
exit $bad

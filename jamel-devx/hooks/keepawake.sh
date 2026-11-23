#!/bin/sh
# Rolling keep-awake: each Claude activity (prompt / tool call) restarts a
# 10-minute sleep inhibitor, so the machine stays awake while Claude works and
# sleeps normally ~10 min after the session goes idle. OS detection at runtime:
# macOS -> caffeinate, Linux -> systemd-inhibit, WSL/other -> no-op (Windows
# owns power management there). Closing a laptop lid still sleeps (OS limit).
PIDFILE="${TMPDIR:-/tmp}/claude-keepawake-$(id -u).pid"
case "$(uname -s)" in
  Darwin)
    set -- caffeinate -i -t 600 ;;
  Linux)
    grep -qi microsoft /proc/version 2>/dev/null && exit 0
    command -v systemd-inhibit >/dev/null 2>&1 || exit 0
    set -- systemd-inhibit --what=idle:sleep --who=claude-code --why=working sleep 600 ;;
  *) exit 0 ;;
esac
# Kill the previous inhibitor only if the PID still belongs to one: after it
# expires the OS may reuse the PID for an unrelated user process.
pid=$(cat "$PIDFILE" 2>/dev/null)
case "$(ps -p "${pid:-0}" -o comm= 2>/dev/null)" in
  *caffeinate|*systemd-inhibit) kill "$pid" 2>/dev/null ;;
esac
nohup "$@" >/dev/null 2>&1 &
echo $! > "$PIDFILE"
exit 0

#!/usr/bin/env bash
input=$(cat)

GREY='\033[38;5;244m'
WHITE='\033[97m'
YELLOW='\033[33m'
RED='\033[31m'
GREEN='\033[32m'
RESET='\033[0m'
SEP="${GREY} | ${RESET}"

cwd=$(echo "$input"         | jq -r '.workspace.current_dir // empty')
model_id=$(echo "$input"    | jq -r '.model.display_name // empty')
used_pct=$(echo "$input"    | jq -r '.context_window.used_percentage // 0')
total_in=$(echo "$input"    | jq -r '.context_window.total_input_tokens // 0')
total_out=$(echo "$input"   | jq -r '.context_window.total_output_tokens // 0')
session_cost=$(echo "$input"| jq -r '.cost.total_cost_usd // 0')
duration_ms=$(echo "$input" | jq -r '.cost.total_api_duration_ms // 0')
lines_add=$(echo "$input"   | jq -r '.cost.total_lines_added // 0')
lines_del=$(echo "$input"   | jq -r '.cost.total_lines_removed // 0')
ctx_size=$(echo "$input"    | jq -r '.context_window.context_window_size // 200000')

# Rate limits (Pro/Max only — graceful fallback)
rl_5h=$(echo "$input"          | jq -r '.rate_limits.five_hour.used_percentage // empty')
rl_5h_reset=$(echo "$input"    | jq -r '.rate_limits.five_hour.resets_at // empty')
rl_7d=$(echo "$input"          | jq -r '.rate_limits.seven_day.used_percentage // empty')
rl_7d_reset=$(echo "$input"    | jq -r '.rate_limits.seven_day.resets_at // empty')

# --- Limit telemetry (opt-in): webhook to Make when a limit window crosses the threshold ---
# Fires only when JAMEL_LIMITS_MEMBER is set (written by /jamel-setup, with consent).
# Payload is ONLY: member name, limit type (session|weekly), reset date. Debounced to one
# shot per window per type: marker file stores the resets_at it already reported.
JAMEL_LIMITS_URL="https://hook.eu2.make.com/h0agd3eon4r1w55wauxo0ib3joijtok1"
notify_limit() { # $1=used_percentage  $2=session|weekly  $3=resets_at (epoch s)
  local pct="$1" type="$2" reset="$3"
  { [ -z "$pct" ] || [ -z "$reset" ]; } && return
  awk -v p="$pct" -v t="${JAMEL_LIMITS_THRESHOLD:-95}" 'BEGIN{exit !(p>=t)}' || return
  local dir="${CLAUDE_CONFIG_DIR:-$HOME/.claude}/.jamel-limits"
  [ "$(cat "$dir/$type" 2>/dev/null)" = "$reset" ] && return  # this window already reported
  mkdir -p "$dir" && printf '%s' "$reset" > "$dir/$type"
  local reset_iso
  reset_iso=$(date -u -r "$reset" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null \
    || date -u -d "@$reset" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null)
  jq -n --arg m "$JAMEL_LIMITS_MEMBER" --arg t "$type" --arg r "$reset_iso" \
    '{"member":$m,"limit-type":$t,"resets-at":$r}' \
    | curl -m 5 -s -X POST -H 'Content-Type: application/json' -d @- \
        "$JAMEL_LIMITS_URL" >/dev/null 2>&1 &  # fire-and-forget, never blocks the bar
}
if [ -n "$JAMEL_LIMITS_MEMBER" ]; then
  notify_limit "$rl_5h" "session" "$rl_5h_reset"
  notify_limit "$rl_7d" "weekly" "$rl_7d_reset"
fi

home="$HOME"
short_cwd="${cwd/#$home/~}"
[ -z "$short_cwd" ] && short_cwd="$(pwd | sed "s|$HOME|~|")"

fmt_tokens() {
  local val="$1"
  [ -z "$val" ] || [ "$val" = "null" ] && echo "0" && return
  awk -v v="$val" 'BEGIN {
    if (v >= 1000000) printf "%.2fm", v/1000000
    else if (v >= 1000) printf "%.2fk", v/1000
    else printf "%d", v
  }'
}

fmt_duration() {
  local ms="$1"
  awk -v ms="$ms" 'BEGIN {
    m = int(ms/60000); h = int(m/60); m = m%60
    if (h > 0) printf "%dh %dm", h, m
    else printf "%dm", m
  }'
}

# Format seconds-until-reset: "2h 48m" or "3d 5h 58m"
fmt_reset() {
  local epoch="$1"
  [ -z "$epoch" ] && return
  local now
  now=$(date +%s)
  local diff=$(( epoch - now ))
  [ "$diff" -le 0 ] && echo "now" && return
  awk -v d="$diff" 'BEGIN {
    days = int(d/86400); h = int((d%86400)/3600); m = int((d%3600)/60)
    if (days > 0) printf "%dd %dh %dm", days, h, m
    else if (h > 0) printf "%dh %dm", h, m
    else printf "%dm", m
  }'
}

git_branch=""
if [ -n "$cwd" ] && git -C "$cwd" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git_branch=$(git -C "$cwd" symbolic-ref --short HEAD 2>/dev/null \
    || git -C "$cwd" rev-parse --short HEAD 2>/dev/null)
fi

# --- Line 1: cwd | git | model | ctx size ---
line1="${GREY}${short_cwd}${RESET}"
[ -n "$git_branch" ] && line1="${line1}${SEP}${GREY}⏋ ${git_branch}${RESET}"
ctx_label="200k"; [ "$ctx_size" -ge 1000000 ] 2>/dev/null && ctx_label="1M"
if [ -n "$model_id" ]; then
  line1="${line1}${SEP}${GREY}${model_id} - ${ctx_label}${RESET}"
else
  line1="${line1}${SEP}${GREY}${ctx_label}${RESET}"
fi

# --- Line 2: context% | tokens | cost | duration | lines ---
used_int=$(printf '%.0f' "$used_pct" 2>/dev/null || echo "0")
if   [ "$used_int" -ge 80 ]; then ctx_color="$RED"
elif [ "$used_int" -ge 60 ]; then ctx_color="$YELLOW"
else ctx_color="$WHITE"; fi

line2="${ctx_color}⏺ ${used_int}%${RESET}"
line2="${line2}${SEP}${GREY}⬇ $(fmt_tokens "$total_in")${RESET}"
line2="${line2}${SEP}${GREY}⬆ $(fmt_tokens "$total_out")${RESET}"
line2="${line2}${SEP}${GREY}\$$(awk -v c="$session_cost" 'BEGIN{printf "%.2f",c+0}')${RESET}"
line2="${line2}${SEP}${GREY}⏱ $(fmt_duration "$duration_ms")${RESET}"

# Lines changed (only if non-zero)
if [ "$lines_add" -gt 0 ] || [ "$lines_del" -gt 0 ]; then
  line2="${line2}${SEP}${GREEN}+${lines_add}${RESET}${GREY}/${RED}-${lines_del}${RESET}"
fi

# --- Line 3: rate limits (Pro/Max only) ---
# Format: "5h: 43% - 2h 48m | 7d: 7% - 3d 5h 58m"
# percentage in white, reset time in grey
line3=""
if [ -n "$rl_5h" ]; then
  rl_5h_int=$(printf '%.0f' "$rl_5h")
  reset_str=$(fmt_reset "$rl_5h_reset")
  segment="${WHITE}5h: ${rl_5h_int}%${RESET}"
  [ -n "$reset_str" ] && segment="${segment}${GREY} - ${reset_str}${RESET}"
  line3="${segment}"
fi

if [ -n "$rl_7d" ]; then
  rl_7d_int=$(printf '%.0f' "$rl_7d")
  reset_str=$(fmt_reset "$rl_7d_reset")
  segment="${WHITE}7d: ${rl_7d_int}%${RESET}"
  [ -n "$reset_str" ] && segment="${segment}${GREY} - ${reset_str}${RESET}"
  [ -n "$line3" ] && line3="${line3}${SEP}${segment}" || line3="${segment}"
fi

if [ -n "$line3" ]; then
  printf "%b\n%b\n%b\n" "$line1" "$line2" "$line3"
else
  printf "%b\n%b\n" "$line1" "$line2"
fi

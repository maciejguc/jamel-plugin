claude() {  # JAMEL-FABLEPLAN
  if [ "$1" = "--fableplan" ]; then
    shift
    ANTHROPIC_DEFAULT_OPUS_MODEL=claude-fable-5 command claude "$@"
  else
    command claude "$@"
  fi
}

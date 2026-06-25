# jamel-devx — plug-and-play DevX dla zespołu JAMEL

Jeden plugin, który daje developerom agencji JAMEL spójny, zoptymalizowany experience w Claude Code:

- **RTK token compression** — hook `PreToolUse`/Bash uruchamia `rtk hook claude` (60–90% mniej tokenów
  na operacjach terminalowych). Guardowany: gdy brak `rtk`, hook nie robi nic.
- **ClickUp MCP** — preconfig zdalnego serwera (`https://mcp.clickup.com/mcp`, HTTP + OAuth). Login
  własnym kontem przez `/mcp`. Bez sekretów w repo.
- **Kuratorowane pluginy (auto-update)** — jako `dependencies` instalowane i włączane automatycznie ze
  **źródłowych** marketplace'ów (nie forki → same się aktualizują):
  `superpowers`, `frontend-design`, `code-review`, `context7` (wszystkie `@claude-plugins-official`).
- **Wspólne ustawienia + statusline + konwencje** — aplikowane komendą `/jamel-setup` (tego plugin nie
  uniesie deklaratywnie: settings pluginu honorują tylko `agent`/`subagentStatusLine`).
- **Opcjonalnie: OpenAI Codex** (`/codex:review`, delegacja) — instalowany na życzenie przez `/jamel-setup`.

## Instalacja (teammate — plug and play)

```text
/plugin marketplace add maciejguc/jamel-plugin
/plugin install jamel-devx@jamel     # auto-instaluje: superpowers, frontend-design, code-review, context7
/jamel-setup                         # ustawienia + statusline + rtk + (opcj.) codex/clickup + konwencje
/mcp                                 # login do ClickUp (własny OAuth)
/reload-plugins                      # podłącz hooki i MCP
```

`/jamel-setup` jest idempotentny, pokazuje diff i pyta o zgodę przed zapisem do `~/.claude/settings.json`
oraz `~/.claude/CLAUDE.md`. Nie dotyka sekretów.

## Aktualizacje

- **Zewnętrzne pluginy**: śledzą najnowszą wersję ze swojego marketplace'u → background auto-update
  Claude Code utrzymuje je aktualne. Ręcznie: `claude plugin update <plugin>`.
- **jamel-devx / jamel-wycena**: bez pola `version` (commit-SHA versioning) → każdy push do repo to nowa
  wersja; `claude plugin update jamel-devx` / `/reload-plugins` pobiera zmiany.

## Uwagi

- **Duplikacja RTK**: jeśli masz już globalny hook `rtk hook claude` w `~/.claude/settings.json`,
  `/jamel-setup` zaproponuje jego usunięcie (plugin go zastępuje; inaczej RTK uruchomi się 2×).
- **ClickUp OAuth**: ClickUp utrzymuje allowlistę zaufanych klientów MCP. Jeśli logowanie przez `/mcp`
  zostanie odrzucone, użyj integracji ClickUp przez claude.ai.
- **Statusline** wymaga `jq` (instalowane przez `/jamel-setup` w razie braku).

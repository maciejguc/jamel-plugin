# jamel-devx — plug-and-play DevX dla zespołu JAMEL

Jeden plugin, który daje developerom agencji JAMEL spójny, zoptymalizowany experience w Claude Code.
Działa cross-platform (macOS / Linux / Windows).

## Co zawiera

- **Kompresja tokenów (dwie komplementarne warstwy)**:
  - **RTK** — kompresuje **output komend Bash** (60–90% mniej tokenów). Instalowany i integrowany przez
    `/jamel-setup` (cross-platform: `brew` / `winget` / `cargo`, integracja `rtk init -g`).
  - **caveman** — skraca **odpowiedzi modelu** i opisy narzędzi MCP. Instalowany przez `/jamel-setup`
    (`npx -y github:JuliusBrussee/caveman`). Inna warstwa niż RTK → bez konfliktu.
- **ClickUp MCP** — `.mcp.json` (`https://mcp.clickup.com/mcp`, HTTP + OAuth). Login własnym kontem przez
  `/mcp`. Bez sekretów w repo.
- **Kuratorowane pluginy (auto-update)** — jako `dependencies`, instalowane i włączane automatycznie ze
  **źródłowych** marketplace'ów (nie forki → same się aktualizują): `superpowers`, `frontend-design`,
  `code-review`, `context7` (`@claude-plugins-official`).
- **Wspólne ustawienia + statusline + konwencje** — aplikowane przez `/jamel-setup` (plugin nie uniesie
  tego deklaratywnie: settings pluginu honorują tylko `agent`/`subagentStatusLine`).
- **Onboarding** — jednorazowy welcome (SessionStart, po polsku) + komenda **`/jamel-tour`**
  (interaktywne oprowadzenie po stanie i komponentach).
- **Opcjonalnie: OpenAI Codex** — instalowany na życzenie przez `/jamel-setup`.

## Instalacja (teammate — plug and play)

```text
/plugin marketplace add maciejguc/jamel-plugin
/plugin install jamel-devx@jamel     # auto-instaluje: superpowers, frontend-design, code-review, context7
/jamel-tour                          # oprowadzenie: co zawiera, w jakim jest stanie
/jamel-setup                         # ustawienia + statusline + RTK + caveman + (opcj.) codex/clickup + konwencje
/mcp                                 # login do ClickUp (własny OAuth)
/reload-plugins                      # podłącz hooki i MCP
```

`/jamel-setup` jest idempotentny, pokazuje diff i pyta o zgodę przed zapisem do `~/.claude/settings.json`
oraz `~/.claude/CLAUDE.md`. **Nie dotyka sekretów ani konfiguracji MCP/permissions usera** (np. `pencil`
zostaje prywatne).

## Cross-platform

- **Hooki**: SessionStart welcome to skrypt Node (`hooks/welcome.mjs`) uruchamiany w exec-form (bez
  shella) → działa na mac/Linux/Windows. RTK celowo **nie** jest shipowany jako surowy POSIX-hook (psułby
  się pod Windows PowerShell) — integrację robi vendorowe `rtk init -g`.
- **Instalacje**: package-manager per platforma — `brew` (mac/Linux), `winget` (Windows), `cargo`/`npx`
  jako fallback. Homebrew bootstrapowany tylko na mac/Linux i tylko za zgodą.
- **Statusline**: bash+`jq`; na Windows wymaga Git Bash + `jq` (`winget install jqlang.jq`).

## Aktualizacje

- **Zewnętrzne pluginy**: śledzą najnowszą wersję ze swojego marketplace'u → background auto-update.
  Ręcznie: `claude plugin update <plugin>`.
- **jamel-devx / jamel-wycena**: bez pola `version` (commit-SHA versioning) → każdy push = nowa wersja.

## Uwagi

- **Duplikacja RTK**: jeśli masz już globalny hook `rtk hook claude` w `~/.claude/settings.json`,
  `/jamel-setup` zaproponuje jego usunięcie (po `rtk init -g` zostaje jeden, vendorowy).
- **ClickUp OAuth**: ClickUp utrzymuje allowlistę zaufanych klientów MCP. Jeśli `/mcp` zostanie
  odrzucone, użyj integracji ClickUp przez claude.ai.

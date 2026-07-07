# jamel-devx — plug-and-play DevX dla zespołu JAMEL

Jeden plugin, który daje developerom agencji JAMEL spójny, zoptymalizowany experience w Claude Code.
Działa cross-platform (macOS / Linux / Windows).

## Co zawiera

- **Kompresja tokenów (dwie komplementarne warstwy)**:
  - **RTK** — kompresuje **output komend Bash** (60–90% mniej tokenów). Instalowany i integrowany przez
    `/jamel-setup` (`brew install rtk` + `rtk init -g`; fallback `cargo`).
  - **caveman** (domyślnie instalowany) — skraca **odpowiedzi modelu** i opisy narzędzi MCP. Na Claude
    Code to plugin, który **sam aktywuje się od pierwszej wiadomości na poziomie `full`** — każda sesja
    startuje z caveman ON. Zmienia **styl odpowiedzi**: na treściach klienckich (`jamel-pm`) użyj
    `/caveman lite` albo `claude plugin disable caveman@caveman`. Inna warstwa niż RTK → bez konfliktu.
    Pominięcie: `/jamel-setup no caveman`.
- **ClickUp** — dostarczany przez **organizację** (connector claude.ai), aktywny po zalogowaniu kontem
  org. Plugin celowo **nie** dostarcza własnego ClickUp MCP, żeby nie dublować org-owego.
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
/jamel-setup                         # ustawienia + statusline + RTK + (opcj.) caveman/codex + konwencje
/reload-plugins                      # podłącz hooki
```
ClickUp jest org-owy (claude.ai) — aktywny po zalogowaniu kontem organizacji, bez `/mcp` w pluginie.

`/jamel-setup` jest idempotentny, pokazuje diff i pyta o zgodę przed zapisem do `~/.claude/settings.json`
oraz `~/.claude/CLAUDE.md`. **Nie dotyka sekretów ani konfiguracji MCP/permissions usera** (np. `pencil`
zostaje prywatne).

## Cross-platform (Homebrew everywhere)

- **Package manager**: zespół standaryzuje na **Homebrew** — `brew` na macOS/Linux, a na **Windows przez
  WSL** (brew nie ma natywnego wsparcia Windows). Jedna, spójna ścieżka instalacji i aktualizacji
  (`brew upgrade`). Wyjątek: caveman przez `npx` (nie ma go w brew; Node z `brew install node`).
- **Hooki**: SessionStart welcome to skrypt Node (`hooks/welcome.mjs`) w exec-form (bez shella) → działa
  wszędzie. RTK celowo **nie** jest shipowany jako surowy hook — integrację robi vendorowe `rtk init -g`.
- **Statusline**: bash+`jq` (`brew install jq`); na Windows działa w WSL tak samo jak na macOS/Linux.
- **Windows**: uruchamiaj Claude Code i `/jamel-setup` **w powłoce WSL** (Ubuntu).

## Aktualizacje

- **Zewnętrzne pluginy**: śledzą najnowszą wersję ze swojego marketplace'u → background auto-update.
  Ręcznie: `claude plugin update <plugin>`.
- **jamel-devx / jamel-pm**: bez pola `version` (commit-SHA versioning) → każdy push = nowa wersja.

## Uwagi

- **Duplikacja RTK**: jeśli masz już globalny hook `rtk hook claude` w `~/.claude/settings.json`,
  `/jamel-setup` zaproponuje jego usunięcie (po `rtk init -g` zostaje jeden, vendorowy).
- **ClickUp**: dostarczany org-wide przez connector claude.ai (nie przez plugin). Jeśli dev go nie ma,
  to kwestia provisioningu po stronie organizacji, nie tego pluginu.

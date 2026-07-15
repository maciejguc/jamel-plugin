# jamel-devx — plug-and-play DevX dla zespołu JAMEL

Jeden plugin, który daje developerom agencji JAMEL spójny, zoptymalizowany experience w Claude Code.
Działa cross-platform (macOS / Linux / Windows).

## Co zawiera

- **Optymalizacja tokenów i kodu (dwie komplementarne warstwy)**:
  - **RTK** — kompresuje **output komend Bash** (60–90% mniej tokenów). Instalowany i integrowany przez
    `/jamel-setup` (`brew install rtk` + `rtk init -g`; fallback `cargo`).
  - **ponytail** (domyślnie instalowany) — wymusza **minimum kodu** (YAGNI: reuse → stdlib → natywna
    funkcja platformy → jedna linia → dopiero potem więcej), nie tnąc walidacji, security ani
    accessibility. Plugin Claude Code, **sam aktywuje się od pierwszej wiadomości na poziomie `full`**.
    Nie zmienia stylu odpowiedzi (treści klienckie z `jamel-pm` bez wpływu). Sterowanie:
    `/ponytail [lite|full|ultra|off]`, przegląd diffa: `/ponytail-review`. Inna warstwa niż RTK → bez
    konfliktu. Pominięcie: `/jamel-setup no ponytail`. (Zastąpił wcześniejszego cavemana — narzut
    jego rulesetu per tura przewyższał oszczędności na prozie w sesjach agentowych.)
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
/jamel-setup                         # ustawienia + statusline + RTK + ponytail + (opcj.) codex + konwencje
/reload-plugins                      # podłącz hooki
```
ClickUp jest org-owy (claude.ai) — aktywny po zalogowaniu kontem organizacji, bez `/mcp` w pluginie.

`/jamel-setup` jest idempotentny, pokazuje diff i pyta o zgodę przed zapisem do `~/.claude/settings.json`
oraz `~/.claude/CLAUDE.md`. **Nie dotyka sekretów ani konfiguracji MCP/permissions usera** (np. `pencil`
zostaje prywatne).

## Telemetria limitów (transparentność)

Po konfiguracji w `/jamel-setup` statusline raportuje na webhook zespołu JAMEL (scenariusz Make
„Claude Limit Reached") moment osiągnięcia **95%** limitu Claude Code — sesyjnego (5h) lub
tygodniowego (7d). Cel: dane do decyzji o upgrade planu per osoba (w interesie deva).

- **Co jest wysyłane** (nic poza tym): imię podane w setupie (np. „Maciej G"), typ limitu
  (`session`/`weekly`), data resetu okna. Żadnych treści sesji, ścieżek, e-maili ani danych o maszynie.
- **Kiedy**: raz na okno limitu na typ (debounce przez marker w `$CFG/.jamel-limits/`).
- **Opt-in/opt-out**: działa tylko, gdy `env.JAMEL_LIMITS_MEMBER` jest ustawione w
  `$CFG/settings.json` (zapisuje je `/jamel-setup` za zgodą). Usunięcie klucza = telemetria wyłączona.
- **Po aktualizacji pluginu** istniejący użytkownicy muszą ponownie odpalić `/jamel-setup`
  (statusline jest kopiowany do `$CFG`, a imię trzeba podać raz).

## Cross-platform (Homebrew everywhere)

- **Package manager**: zespół standaryzuje na **Homebrew** — `brew` na macOS/Linux, a na **Windows przez
  WSL** (brew nie ma natywnego wsparcia Windows). Jedna, spójna ścieżka instalacji i aktualizacji
  (`brew upgrade`). Wyjątek: ponytail to plugin Claude Code (spoza brew; jego hooki wymagają Node —
  `brew install node`).
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

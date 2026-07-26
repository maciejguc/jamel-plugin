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

### Instalacja jednym promptem (onboarding prowadzony przez Claude)

Zamiast wpisywać komendy ręcznie, wklej do świeżej sesji Claude Code poniższy prompt — Claude sam
zainstaluje plugin, przeprowadzi oprowadzenie i **zapyta o zgodę przed konfiguracją**:

```text
Zainstaluj plugin JAMEL DevX i przeprowadź mnie przez onboarding. Wykonuj kroki dokładnie
w tej kolejności i nie pomijaj żadnego:

1. Zainstaluj marketplace i plugin (przez Bash):
   claude plugin marketplace add maciejguc/jamel-plugin
   claude plugin install jamel-devx@jamel
2. Poproś mnie, żebym wpisał /reload-plugins (nie możesz zrobić tego za mnie — to komenda
   interfejsu) i ZATRZYMAJ SIĘ, aż potwierdzę, że gotowe.
3. Po moim potwierdzeniu wykonaj komendę /jamel-tour i zwróć mi w chacie pełny wynik
   oprowadzenia: checklistę stanu komponentów i tabelę jak z nich korzystać.
4. Następnie zapytaj mnie wprost, czy wykonać /jamel-setup, i CZEKAJ na moją odpowiedź.
   Nie uruchamiaj setupu bez mojego potwierdzenia.
5. Dopiero po potwierdzeniu wykonaj /jamel-setup i przeprowadź mnie po polsku przez jego
   kroki (setup pokazuje diffy i pyta o zgodę przed każdym zapisem).

Jeśli po /reload-plugins komendy /jamel-tour lub /jamel-setup nadal nie są dostępne, poproś
mnie o restart Claude Code i podaj mi prompt do wklejenia w nowej sesji: "Wykonaj /jamel-tour
i zwróć pełny wynik, potem zapytaj czy wykonać /jamel-setup i czekaj na moje potwierdzenie."
```

Jedyne ręczne akcje developera: wpisanie `/reload-plugins` w kroku 2 oraz odpowiadanie na pytania
setupu (zgody na zapisy, imię do telemetrii limitów).

## Telemetria limitów (transparentność)

Po konfiguracji w `/jamel-setup` statusline raportuje na webhook zespołu JAMEL (scenariusz Make
„Claude Limit Reached") moment osiągnięcia **95%** limitu Claude Code — sesyjnego (5h) lub
tygodniowego (7d). Cel: dane do decyzji o upgrade planu per osoba (w interesie deva).

- **Co jest wysyłane** (nic poza tym): imię podane w setupie (np. „Maciej G"), typ limitu
  (`session`/`weekly`), data resetu okna. Żadnych treści sesji, ścieżek, e-maili ani danych o maszynie.
- **Kiedy**: raz na okno limitu na typ (debounce przez marker w `$CFG/.jamel-limits/`).
- **Opt-in/opt-out**: działa tylko, gdy `env.JAMEL_LIMITS_MEMBER` **i** `env.JAMEL_LIMITS_APIKEY`
  są ustawione w `$CFG/settings.json` (zapisuje je `/jamel-setup` za zgodą). Usunięcie któregoś
  klucza = telemetria wyłączona.
- **Autoryzacja**: webhook wymaga zespołowego API key (header `x-make-apikey`) — dev dostaje go
  out-of-band od PM-a; klucza nie ma w tym (publicznym) repo, a webhook odrzuca requesty bez niego.
- **Po aktualizacji pluginu** istniejący użytkownicy muszą ponownie odpalić `/jamel-setup`
  (statusline jest kopiowany do `$CFG`, a imię trzeba podać raz).
- **Test bez osiągania limitu**: tymczasowo ustaw `env.JAMEL_LIMITS_THRESHOLD` na niską wartość
  (np. `"1"`) — statusline strzeli przy realnym niskim zużyciu; po teście usuń klucz i pliki
  `$CFG/.jamel-limits/*`.

## Keep-awake (maszyna nie zasypia, gdy Claude pracuje)

Plugin dostarcza hook (`hooks/keepawake.sh`), który przy każdej aktywności Claude'a (prompt, wywołanie
narzędzia) odnawia 10-minutową blokadę uśpienia systemu. Efekt: komputer nie zaśnie w trakcie długiego
zadania, a ~10 min po tym, jak Claude skończy i czeka na input, wraca do normalnego usypiania. Zero
konfiguracji — aktywne od instalacji pluginu. Detekcja OS w runtime: **macOS** → `caffeinate -i`
(tylko blokada uśpienia systemu; ekran może gasnąć), **Linux** → `systemd-inhibit` (jeśli dostępny),
**WSL/inne** → no-op (zarządzaniem energią rządzi Windows). Zamknięcie klapy laptopa nadal usypia —
to limit systemu, nie hooka.

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
- **jamel-devx / jamel-pm**: bez pola `version` (commit-SHA versioning) → każdy merge do `main` =
  nowa wersja. **Uwaga — aktualizacja to DWA kroki**: `/plugin marketplace update jamel` tylko
  odświeża cache marketplace'u; zainstalowany plugin pozostaje **przypięty do commita z momentu
  instalacji**, dopóki nie wykonasz `claude plugin update jamel-devx@jamel` (i analogicznie
  `jamel-pm@jamel`). Po aktualizacji zrestartuj Claude Code. `/jamel-setup` sprawdza to sam na
  starcie (krok 0).

## Uwagi

- **Duplikacja RTK**: jeśli masz już globalny hook `rtk hook claude` w `~/.claude/settings.json`,
  `/jamel-setup` zaproponuje jego usunięcie (po `rtk init -g` zostaje jeden, vendorowy).
- **ClickUp**: dostarczany org-wide przez connector claude.ai (nie przez plugin). Jeśli dev go nie ma,
  to kwestia provisioningu po stronie organizacji, nie tego pluginu.

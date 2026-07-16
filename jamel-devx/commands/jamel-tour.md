---
description: Interaktywne oprowadzenie po pluginie JAMEL DevX — co zawiera, jak działa, co skonfigurować
---

# /jamel-tour — oprowadzenie po JAMEL DevX

Przeprowadź użytkownika **po polsku** przez to, co daje plugin JAMEL DevX i w jakim jest stanie.
Bądź zwięzły, konkretny i przyjazny. **Sprawdzaj realny stan** (nie zgaduj) i na końcu zaproponuj
następne kroki. **Niczego nie instaluj ani nie zmieniaj w tym oprowadzeniu** — od konfiguracji jest
`/jamel-setup`.

**JĘZYK (gwarancja):** CAŁE oprowadzenie — intro, checklista stanu, tabela komponentów, legenda
statusline, sekcja „gdzie doczytać" i propozycje następnych kroków — musi być **po polsku**,
niezależnie od dotychczasowego języka sesji. Po angielsku zostają wyłącznie elementy techniczne
(nazwy komend, kluczy w settings, ścieżki). Jeśli użytkownik pisze w innym języku, i tak odpowiadaj
po polsku, chyba że wprost poprosi inaczej.

## 0. Ustal sprawdzany profil (KRYTYCZNE)
Claude Code honoruje `CLAUDE_CONFIG_DIR` (sandbox / test od zera). Rozwiąż katalog konfiguracji **w
powłoce** i używaj go do WSZYSTKICH odczytów plików: `echo "${CLAUDE_CONFIG_DIR:-$HOME/.claude}"`.
Oznacz wynik jako `$CFG`. **Nigdy nie czytaj dosłownego `~/.claude`** — inaczej sprawdzasz realny profil
zamiast testowego. **Na początku oprowadzenia napisz użytkownikowi, jaki profil sprawdzasz**
(np. „Sprawdzam profil: `/Users/…/.claude-jamel-test`").

## 1. Krótkie intro
Powiedz w 2–3 zdaniach, że JAMEL DevX to „plug-and-play" experience dla zespołu: wspólne ustawienia,
statusline, kompresja tokenów, MCP ClickUp i zestaw kuratorowanych, samo-aktualizujących się pluginów.

## 2. Sprawdź stan (uruchom i zinterpretuj)
- Kuratorowane pluginy: `claude plugin list` → czy `superpowers`, `frontend-design`, `code-review`,
  `context7` są enabled (instalują się automatycznie jako zależności `jamel-devx`). (`claude` CLI samo
  respektuje `CLAUDE_CONFIG_DIR`.)
- RTK: `command -v rtk` (lub `where rtk` na Windows) + `rtk --version`. Jeśli jest — wspomnij `rtk gain`.
- Ponytail (domyślnie instalowany, auto-on `full`): `claude plugin list` → czy `ponytail@ponytail` jest
  enabled. Jeśli zamiast niego jest `caveman@caveman` (starszy setup) — wspomnij, że `/jamel-setup`
  zamieni go na ponytail.
- Statusline: czy `$CFG/settings.json` ma `statusLine` wskazujący `$CFG/jamel-statusline.sh` (czytaj
  `$CFG/settings.json`, NIE `~/.claude/settings.json`).
- Telemetria limitów: czy `$CFG/settings.json` ma `env.JAMEL_LIMITS_MEMBER` **i**
  `env.JAMEL_LIMITS_APIKEY` (klucza NIE wypisuj — tylko czy jest). Oba = aktywna (podaj jako kto
  raportuje); brak któregoś = wyłączona (statusline nic nie wysyła) → skonfiguruje `/jamel-setup`.
- ClickUp MCP (z organizacji): `claude mcp list` → czy org-owy serwer ClickUp jest Connected. Plugin
  **nie** dostarcza własnego ClickUp — pochodzi z org (claude.ai), aktywny po zalogowaniu kontem org.
  Jeśli brak → sprawa provisioningu org, nie tego pluginu.
- Codex (opcjonalny): czy `codex@openai-codex` jest zainstalowany.

Pokaż wynik jako czytelną checklistę ✅/⬜ z jednozdaniowym opisem każdego elementu. W nagłówku podaj
sprawdzany `$CFG`.

## 3. Komponenty — jak działają i jak używać (auto w tle vs ręczne)
Przedstaw jako **tabelę** z kolumnami: Komponent | Tryb | Jak działa / jak używać. Legenda trybu:
🟢 **auto w tle** (nic nie robisz), 🟡 **półauto** (Claude sam odpala wg kontekstu, można też przywołać
wprost), 🔵 **ręczny** (odpalasz komendą). **Jeśli nie jesteś pewien dokładnej nazwy komendy — zweryfikuj
przez `/help` zanim ją podasz** (nie zmyślaj).

- **RTK** — 🟢 auto w tle. Hook przepuszcza output komend Bash (60–90% mniej tokenów). Nic nie robisz.
  Ręcznie tylko meta: `rtk gain`, `rtk gain --history`, `rtk discover`, `rtk proxy <cmd>`.
- **ponytail** — 🟢 auto w tle. Sam startuje na `full` od pierwszej wiadomości i pilnuje, żeby Claude
  pisał **minimum kodu** (YAGNI: reuse → stdlib → natywna funkcja platformy → jedna linia), nie tnąc
  walidacji, security ani accessibility. Sterowanie ręczne: `/ponytail [lite|full|ultra|off]`,
  `/ponytail-review` (przegląd diffa pod over-engineering), `/ponytail-audit`, `/ponytail-debt`,
  `/ponytail-gain`, `/ponytail-help`. Nie zmienia stylu odpowiedzi — treści klienckie bez wpływu.
- **context7** — 🟢/🟡 auto, gdy Claude potrzebuje aktualnej dokumentacji biblioteki/frameworka (sięga po
  MCP sam). Możesz też poprosić wprost: „sprawdź w context7 dokumentację X".
- **superpowers** — 🟡 półauto. Skille odpalają się automatycznie wg kontekstu: brainstorming (projektowanie),
  TDD (implementacja), systematic-debugging (bugi), planowanie, code review. Claude je wywołuje sam; możesz
  też przywołać wprost („użyj brainstorming").
- **frontend-design** — 🟡 półauto. Aktywuje się przy pracy nad UI/frontendem (wymusza dystynktywny,
  produkcyjny design zamiast generycznego). Możesz poprosić wprost przy budowie interfejsu.
- **code-review** — 🔵 ręczny. `/code-review` → równoległy audyt diffa gałęzi / PR przed merge.
- **codex** (opcjonalny) — 🔵 ręczny. Deleguje do OpenAI Codex: `/codex:review`, `/codex:adversarial-review`,
  `/codex:rescue`, `/codex:transfer`, `/codex:status`, `/codex:result`, `/codex:cancel`, `/codex:setup`.
- **ClickUp (org MCP)** — 🟢 auto, gdy Claude operuje na zadaniach/listach ClickUp. Dostarczany przez
  organizację (nie plugin); wymaga zalogowania kontem org.
- **statusline** — 🟢 auto. Pasek: cwd/git/model, kontekst %, tokeny, koszt, rate limity.
- **telemetria limitów** — 🟢 auto (jeśli skonfigurowana w `/jamel-setup`). Gdy limit sesyjny (5h)
  lub tygodniowy (7d) osiągnie **95%**, statusline wysyła RAZ na okno webhook do Make zespołu JAMEL.
  Wysyłane są WYŁĄCZNIE: imię podane w setupie (`JAMEL_LIMITS_MEMBER`), typ limitu (`session`/`weekly`)
  i data resetu — żadnych treści sesji, ścieżek ani e-maili. Request jest autoryzowany zespołowym
  API key (`JAMEL_LIMITS_APIKEY`). Cel: decyzje o upgrade planu per osoba.
  Wyłączenie: usuń `env.JAMEL_LIMITS_MEMBER` (lub `env.JAMEL_LIMITS_APIKEY`) z `$CFG/settings.json`.
- **jamel-devx** — 🔵 ręczny. `/jamel-setup` (konfiguracja), `/jamel-tour` (to oprowadzenie).
- **jamel-pm** — 🔵 ręczny. `/wycena` → wycena projektu → `.xlsx`.

### Statusline — legenda symboli (co oznacza każdy element)
Jeśli statusline JAMEL jest aktywny, wyjaśnij jego elementy. Pasek ma 2–3 linie:

**Linia 1 — gdzie jesteś:**
- `~/ścieżka` — bieżący katalog roboczy (cwd; `~` = katalog domowy).
- `⏋ <branch>` — gałąź git bieżącego repo (symbol `⏋`).
- `<model> - 200k|1M` — nazwa modelu + rozmiar okna kontekstu (`200k` lub `1M`).

**Linia 2 — zużycie sesji:**
- `⏺ NN%` — procent wykorzystanego okna kontekstu. Kolor ostrzega: **biały** <60%, **żółty** ≥60%,
  **czerwony** ≥80%. Jeśli `/jamel-setup` ustawił auto-compact na 80% (`CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`),
  czerwony ≈ „zaraz nastąpi automatyczne kompaktowanie kontekstu".
- `⬇ <liczba>` — tokeny **wejściowe** (input; strzałka w dół = przychodzące do modelu).
- `⬆ <liczba>` — tokeny **wyjściowe** (output; strzałka w górę = generowane przez model).
- `$<kwota>` — koszt sesji w USD.
- `⏱ <czas>` — łączny czas wywołań API (np. `1h 12m`).
- `+X`/`-Y` — linie **dodane** (zielone) / **usunięte** (czerwone) w sesji; pokazywane tylko gdy ≠ 0.

**Linia 3 — limity planu (tylko Pro/Max, jeśli dostępne):**
- `5h: NN% - <reset>` — wykorzystanie limitu 5-godzinnego + czas do resetu (np. `2h 48m`).
- `7d: NN% - <reset>` — wykorzystanie limitu 7-dniowego + czas do resetu (np. `3d 5h 58m`).

Dodatkowo: `|` to separator elementów; liczby tokenów są skracane (`12.3k`, `1.20m`); czas w formacie
`Xh Ym` / `Ym`. Linia 3 pojawia się tylko, gdy Claude Code poda dane o limitach (plany Pro/Max).

## 4. Gdzie doczytać / help (dla samodzielnego zapoznania)
Podaj punkty startowe do pogłębienia — najpierw ogólne, potem per-narzędzie:
- **`/help`** — lista wszystkich slash-komend (w tym z pluginów). Główny punkt startowy.
- **`/plugin`** — zarządzanie pluginami; `claude plugin list` — co jest zainstalowane/enabled.
- **`/mcp`** — serwery MCP + status/logowanie (context7, ClickUp).
- **`/doctor`** — diagnostyka (hooki, MCP, pluginy, błędy zależności).
- **RTK**: `rtk --help`, `rtk <cmd> --help`, `rtk gain`. Repo: `github.com/rtk-ai/rtk`.
- **ponytail**: `/ponytail-help` (komendy), `/ponytail-gain` (mierzony efekt) + repo `github.com/DietrichGebert/ponytail`.
- **codex**: `/codex:setup`, `/codex:status` + repo `github.com/openai/codex-plugin-cc`.
- **superpowers**: `/help` + repo `github.com/obra/Superpowers`.
- **frontend-design / code-review / context7**: `/help` + oficjalny marketplace `anthropics/claude-plugins-official`.
- **jamel-devx / jamel-pm**: README w repo `maciejguc/jamel-plugin` (`jamel-devx/README.md`, `jamel-pm/README.md`).

## 5. Następne kroki (zaproponuj, nie wykonuj)
- Jeśli czegoś brakuje (statusline/RTK/ustawienia) → `/jamel-setup`.
- ClickUp z org niepodłączony → zaloguj się kontem organizacji (connector claude.ai); jeśli dalej brak,
  zgłoś do admina org (to nie jest element tego pluginu).
- Chcesz Codex → poproś `/jamel-setup` o instalację (wymaga OpenAI API key).
- Po zmianach hooków/MCP → `/reload-plugins`.

Opcjonalny argument (np. nazwa komponentu, o który dopytać): $ARGUMENTS

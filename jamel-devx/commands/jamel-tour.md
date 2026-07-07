---
description: Interaktywne oprowadzenie po pluginie JAMEL DevX — co zawiera, jak działa, co skonfigurować
---

# /jamel-tour — oprowadzenie po JAMEL DevX

Przeprowadź użytkownika **po polsku** przez to, co daje plugin JAMEL DevX i w jakim jest stanie.
Bądź zwięzły, konkretny i przyjazny. **Sprawdzaj realny stan** (nie zgaduj) i na końcu zaproponuj
następne kroki. **Niczego nie instaluj ani nie zmieniaj w tym oprowadzeniu** — od konfiguracji jest
`/jamel-setup`.

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
- Caveman: sprawdź obecność komend `/caveman` lub artefaktów w `$CFG` (`$CFG/commands/caveman*`,
  `$CFG/skills/*caveman*`).
- Statusline: czy `$CFG/settings.json` ma `statusLine` wskazujący `$CFG/jamel-statusline.sh` (czytaj
  `$CFG/settings.json`, NIE `~/.claude/settings.json`).
- ClickUp MCP (z organizacji): `claude mcp list` → czy org-owy serwer ClickUp jest Connected. Plugin
  **nie** dostarcza własnego ClickUp — pochodzi z org (claude.ai), aktywny po zalogowaniu kontem org.
  Jeśli brak → sprawa provisioningu org, nie tego pluginu.
- Codex (opcjonalny): czy `codex@openai-codex` jest zainstalowany.

Pokaż wynik jako czytelną checklistę ✅/⬜ z jednozdaniowym opisem każdego elementu. W nagłówku podaj
sprawdzany `$CFG`.

## 3. Wyjaśnij komponenty (1 linia każdy)
- **RTK** — automatyczna kompresja outputu komend Bash (60–90% mniej tokenów); działa w tle.
- **caveman** — skraca odpowiedzi modelu i opisy narzędzi (inna warstwa niż RTK, komplementarna).
- **ClickUp MCP** — zadania/listy ClickUp w Claude; dostarczany przez **organizację** (nie plugin),
  aktywny po zalogowaniu kontem org.
- **superpowers** — metodyka (TDD, brainstorming, planowanie, debugging, code review).
- **frontend-design** — dystynktywny, produkcyjny frontend.
- **code-review** — równoległy audyt diffa/PR.
- **context7** — żywa dokumentacja bibliotek/frameworków.
- **statusline** — cwd/git/model, kontekst%, tokeny, koszt, rate limity.

## 4. Następne kroki (zaproponuj, nie wykonuj)
- Jeśli czegoś brakuje (statusline/RTK/ustawienia) → `/jamel-setup`.
- ClickUp z org niepodłączony → zaloguj się kontem organizacji (connector claude.ai); jeśli dalej brak,
  zgłoś do admina org (to nie jest element tego pluginu).
- Chcesz Codex → poproś `/jamel-setup` o instalację (wymaga OpenAI API key).
- Po zmianach hooków/MCP → `/reload-plugins`.

Opcjonalny argument (np. nazwa komponentu, o który dopytać): $ARGUMENTS

---
description: Interaktywne oprowadzenie po pluginie JAMEL DevX — co zawiera, jak działa, co skonfigurować
---

# /jamel-tour — oprowadzenie po JAMEL DevX

Przeprowadź użytkownika **po polsku** przez to, co daje plugin JAMEL DevX i w jakim jest stanie.
Bądź zwięzły, konkretny i przyjazny. **Sprawdzaj realny stan** (nie zgaduj) i na końcu zaproponuj
następne kroki. **Niczego nie instaluj ani nie zmieniaj w tym oprowadzeniu** — od konfiguracji jest
`/jamel-setup`.

## 1. Krótkie intro
Powiedz w 2–3 zdaniach, że JAMEL DevX to „plug-and-play" experience dla zespołu: wspólne ustawienia,
statusline, kompresja tokenów, MCP ClickUp i zestaw kuratorowanych, samo-aktualizujących się pluginów.

## 2. Sprawdź stan (uruchom i zinterpretuj)
- Kuratorowane pluginy: `claude plugin list` → czy `superpowers`, `frontend-design`, `code-review`,
  `context7` są enabled (instalują się automatycznie jako zależności `jamel-devx`).
- RTK: `command -v rtk` (lub `where rtk` na Windows) + `rtk --version`. Jeśli jest — wspomnij `rtk gain`.
- Caveman: sprawdź czy dostępne komendy `/caveman` (jeśli zainstalowany).
- Statusline: czy `~/.claude/settings.json` ma `statusLine` wskazujący `~/.claude/jamel-statusline.sh`.
- ClickUp MCP: czy serwer `clickup` jest podłączony (narzędzia `mcp__plugin_jamel-devx_clickup__*`); jeśli
  nie — trzeba `/mcp` (login własnym OAuth).
- Codex (opcjonalny): czy `codex@openai-codex` jest zainstalowany.

Pokaż wynik jako czytelną checklistę ✅/⬜ z jednozdaniowym opisem każdego elementu.

## 3. Wyjaśnij komponenty (1 linia każdy)
- **RTK** — automatyczna kompresja outputu komend Bash (60–90% mniej tokenów); działa w tle.
- **caveman** — skraca odpowiedzi modelu i opisy narzędzi (inna warstwa niż RTK, komplementarna).
- **ClickUp MCP** — zadania/listy ClickUp w Claude (login własnym kontem przez `/mcp`).
- **superpowers** — metodyka (TDD, brainstorming, planowanie, debugging, code review).
- **frontend-design** — dystynktywny, produkcyjny frontend.
- **code-review** — równoległy audyt diffa/PR.
- **context7** — żywa dokumentacja bibliotek/frameworków.
- **statusline** — cwd/git/model, kontekst%, tokeny, koszt, rate limity.

## 4. Następne kroki (zaproponuj, nie wykonuj)
- Jeśli czegoś brakuje (statusline/RTK/ustawienia) → `/jamel-setup`.
- ClickUp niezalogowany → `/mcp`.
- Chcesz Codex → poproś `/jamel-setup` o instalację (wymaga OpenAI API key).
- Po zmianach hooków/MCP → `/reload-plugins`.

Opcjonalny argument (np. nazwa komponentu, o który dopytać): $ARGUMENTS

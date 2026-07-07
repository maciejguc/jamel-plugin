# JAMEL — wytyczne zespołu (Claude Code)

> Kanoniczne konwencje agencji JAMEL. `/jamel-setup` proponuje scalenie tej sekcji do
> `~/.claude/CLAUDE.md` (plugin-owy CLAUDE.md nie ładuje się automatycznie do kontekstu).
> Sekcja jest oznaczona markerami `JAMEL-DEVX:BEGIN/END`, żeby aktualizacje były idempotentne.

<!-- JAMEL-DEVX:BEGIN -->

## Python — wykonanie i zależności

- **Zawsze używaj `venv` w bieżącym katalogu roboczym (cwd)** do uruchamiania Pythona i instalacji zależności.
- **Jeśli `venv` nie istnieje** w cwd — utwórz go: `python3 -m venv venv`.
- Używaj binariów z venv bezpośrednio:
  - Uruchamianie: `./venv/bin/python <skrypt>.py`
  - Instalacja: `./venv/bin/pip install <paczka>`
- **Nigdy nie instaluj globalnie** (bez `sudo pip`, bez `pip install` poza venv).
- Jeśli istnieje `requirements.txt` / `pyproject.toml` — zainstaluj zależności do venv przed uruchomieniem.

## RTK (Rust Token Killer) — kompresja outputu

- Komendy Bash są automatycznie przepuszczane przez `rtk` (hook `PreToolUse`, dostarczany przez
  `jamel-devx`) → 60–90% oszczędności tokenów. Nie trzeba nic robić ręcznie.
- Meta-komendy używaj wprost: `rtk gain` (analytics), `rtk gain --history`, `rtk discover`,
  `rtk proxy <cmd>` (surowa komenda bez filtrowania, do debugowania).
- Weryfikacja: `rtk --version`, `which rtk`. Instalacja: `brew install rtk` (mac/Linux/WSL; fallback
  `cargo install --git https://github.com/rtk-ai/rtk`). Integracja z Claude Code: `rtk init -g`.
- Package manager zespołu: **Homebrew wszędzie**. Windows → przez **WSL** (brew nie ma natywnego Windows).
- ⚠️ Kolizja nazw: jeśli `rtk gain` nie działa, możesz mieć inny `rtk` (Rust Type Kit) w PATH.

## caveman — kompresja odpowiedzi modelu

- Skraca **odpowiedzi modelu** i opisy narzędzi (inna warstwa niż RTK — RTK kompresuje *output Bash*;
  caveman *output modelu*). Są komplementarne, nie kolidują.
- Komendy: `/caveman [lite|full|ultra]`, `/caveman-commit`, `/caveman-review`, `/caveman-stats`,
  `/caveman-compress <plik>`. Instalacja (domyślnie przez `/jamel-setup`, na Claude Code jako plugin):
  `claude plugin marketplace add JuliusBrussee/caveman` + `claude plugin install caveman@caveman`.
- **Sam aktywuje się od pierwszej wiadomości na `full`** (każda sesja startuje z caveman ON); kompresuje
  tylko *output* (nie rozumowanie), dokłada ~1–1.5k input tokenów/turę. Poziom jest per-sesja, nie da się
  przypiąć configiem.
- **Na treściach klienckich** (wyceny/specyfikacje): `/caveman lite` albo `claude plugin disable caveman@caveman`.

## Konwencje ogólne

- Kod, komentarze, identyfikatory i commit messages — po angielsku (treści dla klienta / wyceny — po polsku).
- Code review przed merge: korzystaj z `code-review` (kuratorowany plugin) na diffie gałęzi.
- Workflow metodyczny (planowanie, TDD, debugging) — skille z `superpowers`.

<!-- JAMEL-DEVX:END -->

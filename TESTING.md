# Testowanie pluginów JAMEL (jamel-devx + jamel-pm)

Jak bezpiecznie sprawdzić, że pluginy działają i robią to, czego oczekujesz — **bez ryzyka dla Twojej
realnej konfiguracji Claude Code** — oraz jak wszystko łatwo odtworzyć/wyczyścić.

Masz dwa podejścia. **Zalecane: A (sandbox przez `CLAUDE_CONFIG_DIR`)** — nie dotyka Twojego `~/.claude`.
B (backup/restore) — gdy chcesz testować dokładnie na swoim profilu.

> Szczegółowy plan testów pluginu **jamel-pm** (generator range/fixed, skill `wycena`, scenariusze
> end-to-end): [`jamel-pm/TESTING.md`](jamel-pm/TESTING.md).

---

## Co weryfikujemy (checklista)

- [ ] `jamel-devx` instaluje się i **auto-pociąga** zależności: `superpowers`, `frontend-design`, `code-review`, `context7`
- [ ] Jednorazowy **welcome** (po polsku) pokazuje się przy pierwszym starcie, a potem znika
- [ ] `/jamel-tour` pokazuje czytelną checklistę stanu
- [ ] `/jamel-setup` **pyta o zgodę**, merge'uje ustawienia, ustawia statusline, instaluje RTK + caveman
- [ ] Ustawienia w `settings.json` = te z setupu (`effortLevel: high`, `remoteControlAtStartup: false`, `agentPushNotifEnabled: false`, env-flagi, `tui`, `editorMode`, `spinnerTipsEnabled`)
- [ ] `/jamel-setup` **nie** dodaje MCP `pencil` ani `permissions`
- [ ] Statusline renderuje 3 linie; `rtk --version` + `rtk gain` działa; komendy `/caveman*` dostępne
- [ ] ClickUp: org-owy connector (claude.ai) jest Connected (`claude mcp list`); plugin NIE dostarcza własnego ClickUp
- [ ] `jamel-pm`: `/wycena` → plik `.xlsx` (widełki lub fixed) + podsumowanie Część A/B; testy `pytest` zielone
- [ ] Konwencje scalone do `~/.claude/CLAUDE.md` (blok `JAMEL-DEVX:BEGIN/END`)

> Uwaga: testuj w **terminalowym Claude Code (CLI)**. Rozszerzenie VS Code ignoruje `CLAUDE_CONFIG_DIR`.

---

## Podejście A — sandbox (ZALECANE, zero ryzyka)

`CLAUDE_CONFIG_DIR` sprawia, że cały `~/.claude` „żyje" w innym katalogu. Twoja realna konfiguracja jest
nietknięta — testujesz na czystym profilu, a sprzątanie = skasowanie katalogu.

> **Ważne:** `/jamel-setup` honoruje `CLAUDE_CONFIG_DIR` (rozwiązuje `CFG="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"`
> i pisze do `$CFG`). **Wyjątek: RTK.** `rtk init -g` to zewnętrzne narzędzie i może pisać do prawdziwego
> `~/.claude` niezależnie od zmiennej. Dla w pełni hermetycznego testu uruchom `/jamel-setup skip rtk`
> i przetestuj RTK osobno (patrz niżej).

### 1. Utwórz czysty profil i odpal Claude Code
```bash
export CLAUDE_CONFIG_DIR="$HOME/.claude-jamel-test"
mkdir -p "$CLAUDE_CONFIG_DIR"
claude                      # zaloguj się swoim kontem (to osobny, czysty profil)
```
Wszystko, co zrobi `/jamel-setup` (settings, statusline, CLAUDE.md, RTK `rtk init -g`), trafi do
`~/.claude-jamel-test`, **nie** do `~/.claude`.

### 2. Dodaj marketplace i zainstaluj
Do testu **bieżącej wersji roboczej** (łącznie z niezacommitowanymi zmianami) użyj ścieżki lokalnej:
```text
/plugin marketplace add /Users/maciejguc/Documents/Coding/CLI/jamel/jamel-plugin
/plugin install jamel-devx@jamel      # obserwuj: "+ N dependencies: ..."
/plugin install jamel-pm@jamel
```
Aby przetestować **tak jak teammate** (z GitHuba): `/plugin marketplace add maciejguc/jamel-plugin`.

### 3. Przejdź scenariusz
```text
/plugin list           # potwierdź, że devx + 4 zależności są enabled; brak błędów dependency-*
/jamel-tour            # checklista stanu
/jamel-setup skip rtk  # hermetycznie: pomija RTK (rtk init -g dotyka realnego ~/.claude)
                       # albo pełne: /jamel-setup — świadomie, RTK zapisze do ~/.claude
/reload-plugins        # podłącz hooki i MCP
claude mcp list        # ClickUp jest org-owy (nie z pluginu) — sprawdź, że Connected
/wycena                # krótki scenariusz wyceny (widełki/fixed) → otwórz wynikowy .xlsx
```
**Zweryfikuj, że zmiany trafiły do sandboxa, a NIE do `~/.claude`:**
```bash
cat "$CLAUDE_CONFIG_DIR/settings.json"        # oczekiwane klucze; brak pencil/permissions
ls  "$CLAUDE_CONFIG_DIR/jamel-statusline.sh"  # skopiowany statusline
# kontrola: realny profil nietknięty (te pliki nie powinny się zmienić)
ls -la "$HOME/.claude/settings.json"
```
Jeśli robiłeś `/jamel-setup` bez `skip rtk`, sprawdź gdzie RTK dopisał hook:
```bash
grep -l "rtk hook claude" "$HOME/.claude/settings.json" "$CLAUDE_CONFIG_DIR/settings.json" 2>/dev/null
```
Sprawdź też statusline (3 linie), `rtk gain`, komendy `/caveman`.

### 4. Testy jednostkowe wyceny (niezależne od Claude)
```bash
cd /Users/maciejguc/Documents/Coding/CLI/jamel/jamel-plugin
./jamel-pm/scripts/.venv/bin/python -m pytest jamel-pm/scripts/tests/ -q
```

### 5. Sprzątanie / odtworzenie
```bash
rm -rf "$HOME/.claude-jamel-test"     # kasuje CAŁY profil testowy
unset CLAUDE_CONFIG_DIR                # wróć do normalnego profilu
```
Aby powtórzyć test od zera — po prostu utwórz katalog ponownie (krok 1). RTK/caveman zainstalowane przez
`brew` w tym teście pozostają w systemie (to globalne binaria) — to OK; ewentualnie `brew uninstall rtk`.

---

## Podejście B — backup i restore realnego `~/.claude`

Gdy chcesz przetestować dokładnie na swoim profilu. **Zamknij Claude Code przed backupem i przed restore.**

### 1. Backup (dwie lokalizacje!)
Claude trzyma config w `~/.claude/` **oraz** w `~/.claude.json` (sesja/OAuth, MCP, cache) — backupuj oba:
```bash
STAMP=$(date +%Y%m%d-%H%M%S)
cp -a "$HOME/.claude"      "$HOME/.claude.backup-$STAMP"
cp -a "$HOME/.claude.json" "$HOME/.claude.json.backup-$STAMP"
echo "backup: $STAMP"
```

### 2. Test
Odpal `claude`, wykonaj kroki 2–4 z Podejścia A (bez `CLAUDE_CONFIG_DIR`). Zmiany trafią do realnego
profilu — dlatego mamy backup.

### 3. Restore (pełne cofnięcie)
```bash
# zamknij Claude Code
rm -rf "$HOME/.claude" "$HOME/.claude.json"
mv "$HOME/.claude.backup-$STAMP"      "$HOME/.claude"
mv "$HOME/.claude.json.backup-$STAMP" "$HOME/.claude.json"
```
Alternatywnie, punktowe cofnięcie bez pełnego restore:
```text
/plugin uninstall jamel-devx@jamel --prune     # usuwa też auto-zależności
/plugin uninstall jamel-pm@jamel               # (starsze instalacje: jamel-wycena@jamel)
/plugin marketplace remove jamel
```
oraz ręcznie usuń z `~/.claude/settings.json` dodane klucze i `statusLine`, a z `~/.claude/CLAUDE.md`
blok `JAMEL-DEVX:BEGIN/END`. (Dlatego wygodniej jest Podejście A.)

---

## Szybka diagnostyka

- `claude plugin list --json` → pole `errors` na każdym pluginie (szukaj `dependency-*`).
- `/doctor` → ogólny stan (hooki, MCP, pluginy).
- `claude plugin validate /Users/maciejguc/Documents/Coding/CLI/jamel/jamel-plugin` → walidacja manifestów
  (ostrzeżenie o braku `version` dla `jamel-devx` jest **zamierzone** — commit-SHA versioning).
- RTK dubluje się? Sprawdź, czy w `settings.json` nie ma ręcznego hooka `rtk hook claude` obok tego z
  `rtk init -g`.

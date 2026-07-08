# Testowanie zmian w pluginie jamel-pm

Jak zweryfikować przebudowę pluginu: rename `jamel-wycena` → `jamel-pm`, nowy generator
(tryby **range** widełki min/max i **fixed** cena stała, dwa arkusze) oraz skill `wycena`
z metodyką JAMEL. Ogólny setup sandboxa (profil `CLAUDE_CONFIG_DIR`, backup/restore) opisuje
[`../TESTING.md`](../TESTING.md) — ten dokument skupia się na tym, **co** testować w jamel-pm.

Testy dzielą się na trzy warstwy: (1) automatyczne, bez Claude; (2) wizualna weryfikacja
plików `.xlsx`; (3) scenariusze skilla end-to-end w Claude Code.

---

## Warstwa 1 — testy automatyczne (bez Claude, ~1 min)

Wszystko z katalogu głównego repo (`jamel-plugin/`):

```bash
# venv pluginu (SessionStart hook tworzy go sam; ręcznie gdyby go brakło):
python3 -m venv jamel-pm/scripts/.venv && \
  jamel-pm/scripts/.venv/bin/pip install -q -r jamel-pm/scripts/requirements.txt

# pełny zestaw testów — oczekiwane: 11 passed
jamel-pm/scripts/.venv/bin/python -m pytest jamel-pm/scripts/tests/ -q

# walidacja manifestów marketplace'u — oczekiwane: passed with warnings
# (warning o braku `version` jest ZAMIERZONY — commit-SHA versioning)
claude plugin validate .
```

Co pokrywają testy pytest:

| Obszar | Test |
|---|---|
| Numeracja tekstowa `"1.1"` + jawna kolejność etapów | `test_numbering_follows_explicit_stage_order` |
| Pusty etap = sam baner (np. „Zakończenie prac") | `test_empty_stage_renders_banner_only` |
| Łańcuch stawek: pozycja → `role_rates` → rate card → default | `test_rate_resolution_chain` |
| Rodzaje pozycji: hourly / ryczałt (ujemny = rabat) / „w cenie" | `test_kinds_and_totals` |
| Walidacja błędnych payloadów | `test_invalid_items_raise` |
| Struktura range: nagłówki, `=F*H`/`=G*H`, `- / - / -`, SUMA (min)/(max), koral | `test_range_structure` |
| Struktura fixed: `=F*G`, rabat `-1000`, `W cenie`, SUMA | `test_fixed_structure` |
| Ręczne przeliczenie SUMY == semantyka formuł | `test_band_verification_matches_formula_semantics` |
| Golden render cell-by-cell (wartości, formaty, fill) | `test_matches_golden_render[range/fixed]` |
| Szablon: komplet klocków `-range`/`-fixed` + logo w zipie | `test_template_has_all_blocks_and_logo` |

**Builder szablonu** (tylko po zmianach w `tools/build_template.py`):

```bash
jamel-pm/scripts/.venv/bin/python jamel-pm/tools/build_template.py
git diff --stat jamel-pm/assets/estimate_template.xlsx   # świadoma zmiana? commit; nie? checkout
```

Builder jest idempotentny — drugie uruchomienie musi przejść bez błędu.

**Golden fixtures** (tylko po zamierzonej zmianie renderu):

```bash
jamel-pm/scripts/.venv/bin/python jamel-pm/scripts/tests/regenerate_golden.py
# obejrzyj wynikowe golden/*.xlsx (Warstwa 2), dopiero potem commit
```

---

## Warstwa 2 — wizualna weryfikacja .xlsx (~5 min)

Wygeneruj próbki z golden inputów (albo użyj wprost `scripts/tests/golden/*-golden.xlsx`):

```bash
jamel-pm/scripts/.venv/bin/python jamel-pm/scripts/generate_wycena_xlsx.py \
  jamel-pm/scripts/tests/golden/range-input.json -o /tmp/proba-widelki.xlsx
jamel-pm/scripts/.venv/bin/python jamel-pm/scripts/generate_wycena_xlsx.py \
  jamel-pm/scripts/tests/golden/fixed-input.json -o /tmp/proba-fixed.xlsx
```

Otwórz obok wzorców z repo ofertowego i porównaj:

- `/tmp/proba-widelki.xlsx` ↔ `offers/estimates/sprint-est.xlsx`
- `/tmp/proba-fixed.xlsx` ↔ `offers/estimates/ina-management-est.xlsx`

Checklista wizualna (Excel **i** Numbers):

- [ ] Tytuł dwuwierszowy „Wycena wdrożenia serwisu / dla `<Klient>`", granat, 17 pt bold; logo w B1
- [ ] „Data przygotowania oferty: …" + „Ofertę przygotował/-a: …"
- [ ] Nagłówki: range `Etap | Opis | Zadanie Wykonawcy | Rola | RH (min) | RH (max) | Stawka | Kwota całkowita netto (min) | (max)`; fixed bez kolumn min/max
- [ ] Banery etapów: koral `FF818D` na kremie, pełna szerokość tabeli, **bez numerów** w nazwach
- [ ] Numery pozycji `1.1`, `1.2`… jako **tekst** (Excel/Numbers nie interpretuje ich jako dat!)
- [ ] Kwoty jako **formuły** (`=F7*H7` itd.) i format `zł`; SUMA liczy się po edycji godzin w komórce
- [ ] Ryczałt (Copywriting): `- / - / -` w RH/Stawka, kwoty wpisane wprost; „Szkolenie" widoczne za 0 / „W cenie"; w fixed rabat `-1000` obniża SUMĘ
- [ ] SUMA: koralowe komórki z kremowym tekstem; w range etykiety `SUMA (min)`/`SUMA (max)` nad wartościami
- [ ] Dwa arkusze w range (`Wycena` + `Elementy dodatkowe` o tej samej strukturze); w fixed-sample tylko `Wycena` (brak `additional_items` w inpucie)
- [ ] Marginesy kremowe po bokach, brak linii siatki, białe wiersze danych z cienkimi ramkami

> Kontrola SUMY bez otwierania pliku: generator wypisuje `SUMA core: min–max netto` na stdout
> (openpyxl nie ewaluuje formuł — to jedyne źródło sumy w CLI).

---

## Warstwa 3 — skill end-to-end w Claude Code (~15 min)

Użyj sandboxa `CLAUDE_CONFIG_DIR` z [`../TESTING.md`](../TESTING.md) (Podejście A), z lokalną
ścieżką marketplace'u, żeby testować bieżącą wersję roboczą:

```text
/plugin marketplace add /Users/maciejguc/Documents/Coding/CLI/jamel/jamel-plugin
/plugin install jamel-pm@jamel
/reload-plugins
```

> **Uwaga (caveman):** jeśli testujesz z zainstalowanym `jamel-devx`, caveman startuje na `full`
> i zniekształci treści klienckie — na czas testu wyceny przełącz `/caveman lite` albo wyłącz.

### Scenariusz A — wycena widełkowa z kalibracją do pasma (główna ścieżka)

Wklej do `/wycena` krótki opis projektu (mail/notatki) z integracją zewnętrzną i podaj pasmo,
np. *„serwis z listingami ofert + integracja z systemem X po API; pozycjonuj w widełkach 30–38 tys."*

- [ ] Skill wybiera tryb **range** i uzasadnia wybór (w Części B)
- [ ] Dopytuje o braki zamiast zgadywać (integracje, liczba widoków, języki, treści)
- [ ] Pozycje: 4 etapy kanoniczne; jedna rola = jedna pozycja; opisy po polsku
- [ ] **PM = 15–20% sumy RH pozostałych pozycji** (min i max osobno), jako jawna pozycja w „Zakończenie prac"
- [ ] Copywriting ryczałtem; „Szkolenie" jako `included`; treści z systemów zewn. wyłączone z copy
- [ ] Upselle trafiają do `Elementy dodatkowe`, **nie** do core
- [ ] `input.json` zapisany obok wyniku; SUMA z stdout **mieści się w 30–38 tys.**
- [ ] Wynik: ścieżka `.xlsx` + **Część A** (zero linków/benchmarków, kwoty cyframi) / **Część B** (uzasadnienie godzin i trybu)
- [ ] Na końcu pyta, czy wersja jest **docelowa**

Następnie zmień pasmo („zrób z tego 40–45 tys.") — skill ma **przeliczyć godziny**, nie stawki.

### Scenariusz B — cena stała (fixed)

Poproś o wycenę prostego serwisu brochure z rabatem: *„prosty serwis wizytówkowy 5 podstron,
WordPress, cena stała, daj rabat 1000 zł"*.

- [ ] Tryb **fixed**; pojedyncze kolumny RH/Stawka/Kwota; `=F*G`
- [ ] Rabat jako pozycja z ujemną kwotą; „Szkolenie" jako `W cenie`

### Scenariusz C — ścieżka pytań (niedoprecyzowane zapytanie)

Wklej lakoniczne zapytanie (np. „ile kosztuje sklep?").

- [ ] Skill **nie podaje ceny** — tworzy draft maila podtrzymującego + osobny plik
      `pytania-<klient>.md` z pytaniami rankingowanymi 🔴/🟡/🟢 wg wpływu na wycenę

### Scenariusz D — integracja z repo ofertowym (biblioteka wzorców)

Uruchom Claude w katalogu z biblioteką (`offers/` z `estimates/` i `specs/`).

- [ ] Skill wykrywa bibliotekę i dobiera wzorzec wg charakteru projektu (ina/sprint/kidde/belong)
- [ ] Pracuje w folderze klienta; po potwierdzeniu „docelowa" **kopiuje** plik do `estimates/<klient>-est.xlsx`
- [ ] Draftów e-maili **nie wysyła** — zapisuje `email-*.md` i czeka na potwierdzenie

### Hooki i migracja

- [ ] **Nudge**: wiadomość zawierająca „wycena/wyceń/kosztorys" wywołuje przypomnienie o skillu `wycena`
- [ ] **Samonaprawa venv**: `rm -rf` katalogu `scripts/.venv` w cache pluginu → restart sesji → venv odtworzony (hook robi import-check openpyxl, nie tylko test istnienia katalogu)
- [ ] **Migracja**: na profilu ze starym pluginem `/plugin uninstall jamel-wycena@jamel` → `/plugin install jamel-pm@jamel`; `/wycena` działa, brak błędów `dependency-*` w `/plugin list`

---

## Szybka diagnostyka

- `claude plugin list --json` → pole `errors` (szukaj `dependency-*`).
- Generator rzuca `ValueError` z czytelnym komunikatem przy złym payloadzie
  (brak `pricing_mode`, zły `kind`, hourly bez godzin, fixed bez kwoty).
- `Wrote … SUMA core: …` na stdout ≠ pasmo docelowe → problem kalibracji (skill, nie generator).
- Testy golden padają po niezamierzonej zmianie? `git diff jamel-pm/assets/ jamel-pm/scripts/` —
  golden porównuje wartości, formaty liczb **i** kolory wypełnień cell-by-cell.
- Zniknęło logo z wyników? `python -c "import zipfile; zipfile.ZipFile('jamel-pm/assets/estimate_template.xlsx').read('xl/media/image1.png')"` — jeśli brak, przebuduj szablon builderem.

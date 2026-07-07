# jamel-pm — toolkit PM/Account agencji JAMEL dla Claude Code

Plugin zbierający narzędzia dla PM-ów i account managerów JAMEL. Dziś: **tworzenie wycen**
wg metodyki JAMEL z renderem `.xlsx` spójnym z historycznymi wycenami agencji (kolory,
czcionki, formuły, logo). W planach: specyfikacje techniczne, specyfikacje graficzne,
analiza stron www (klienta i konkurencji).

W skillu wycen **to Claude jest estymatorem**: analizuje materiały klienta (mail/notatki/brief),
decyduje o formacie, produkuje pozycje wyceny i kalibruje godziny do docelowego pasma cenowego.
Skrypt Python (`openpyxl`) robi tylko deterministyczną część: numerację, stawki, render `.xlsx`.

## Możliwości skilla `wycena`

- **Dwa formaty wyceny**: widełkowa min/max (`pricing_mode: "range"` — domyślna dla pierwszego
  kontaktu i projektów z integracjami) oraz cena stała (`"fixed"` — proste serwisy; obsługuje
  rabat i pozycje „W cenie").
- **Dwa arkusze**: `Wycena` (core — tylko to, o co prosi klient) + `Elementy dodatkowe`
  (propozycje/upselle JAMEL).
- **Metodyka JAMEL**: kalibracja SUMY do pasma docelowego, 4 etapy kanoniczne, jawny wiersz PM
  (15–20% czasu prac), Copywriter ryczałtem, Szkolenie „w cenie", rate card agencji,
  ścieżka pytań rankingowanych przy niedoprecyzowanych zapytaniach.
- **Wynik**: plik `.xlsx` + podsumowanie **Część A (dla klienta)** / **Część B (komentarz
  wewnętrzny)**.

## Co jest w środku

```
.claude-plugin/plugin.json      # manifest pluginu
skills/wycena/SKILL.md          # rdzeń: pełna metodyka wycen JAMEL
commands/wycena.md              # slash-command /wycena
hooks/hooks.json                # SessionStart: bootstrap/samonaprawa venv (+ nudge na „wycena")
scripts/
  generate_wycena_xlsx.py       # generator: ordering + rates + render (openpyxl), tryby range/fixed
  requirements.txt              # openpyxl, pillow, pytest
  tests/                        # testy warstwy danych + strukturalne + golden fixtures
tools/build_template.py         # builder szablonu (reprodukowalny z kodu)
assets/estimate_template.xlsx   # arkusze-klocki range/fixed (źródło całego stylu)
reference/
  line-item-schema.json         # kontrakt danych wejściowych (v2)
  archive/prompt_marketing.md   # archiwum: persona marketingowa ELA (poza workflow)
```

## Instalacja

Plugin jest częścią marketplace'u JAMEL (repo `jamel-plugin`). W Claude Code:

```text
/plugin marketplace add maciejguc/jamel-plugin
/plugin install jamel-pm@jamel
```

(lokalnie do dev: `/plugin marketplace add /ścieżka/do/jamel-plugin`).

> Migracja ze starego pluginu: `/plugin uninstall jamel-wycena@jamel` → `/plugin install jamel-pm@jamel`.

Przy starcie sesji **SessionStart hook** tworzy `scripts/.venv` i instaluje zależności
(idempotentnie; naprawia też uszkodzony venv), więc generator zawsze ma `openpyxl`/`pillow`.

## Użycie

1. Uruchom `/wycena` (albo poproś o „wycenę" — skill `wycena` aktywuje się sam) i podaj
   materiały: mail klienta, notatki, brief, ew. docelowe pasmo cenowe.
2. Claude analizuje wejście, decyduje widełki vs cena stała, dopytuje przy brakach
   (nie zgaduje) i kalibruje godziny do pasma.
3. Otrzymujesz plik `.xlsx` + podsumowanie Część A / Część B; po akceptacji Claude pyta,
   czy wersja jest docelowa (kopiuje ją wtedy do biblioteki `estimates/`, jeśli istnieje).

### Uruchomienie generatora ręcznie (CLI)

```bash
./scripts/.venv/bin/python scripts/generate_wycena_xlsx.py input.json -o wycena.xlsx
```

Kształt `input.json` opisuje [`reference/line-item-schema.json`](reference/line-item-schema.json).
Generator wypisuje na stdout policzoną SUMĘ core (openpyxl nie ewaluuje formuł w pliku).

## Testy i szablon

```bash
./scripts/.venv/bin/pytest scripts/tests/
```

Testy: warstwa danych (numeracja, stawki, rodzaje pozycji), struktura renderu per tryb oraz
**golden render** — porównanie cell-by-cell z zacommitowanymi fixture'ami
(`scripts/tests/golden/`), raz zweryfikowanymi ręcznie względem historycznych wycen JAMEL.
Po zamierzonej zmianie renderu: `./scripts/.venv/bin/python scripts/tests/regenerate_golden.py`
i przejrzyj wynik przed commitem.

Szablon `assets/estimate_template.xlsx` jest generowany skryptem
`tools/build_template.py` (idempotentny; re-injectuje logo do archiwum).

## Roadmapa

Kolejne skille dochodzą jako foldery w `skills/` bez przebudowy pluginu:
`tech-spec` (specyfikacje techniczne), `graphic-spec` (specyfikacje graficzne),
`website-analysis` (analiza strony klienta i konkurencji).

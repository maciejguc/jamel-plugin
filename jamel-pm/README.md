# jamel-wycena — plugin „ELA Wycena" dla Claude Code

Niezależny od aplikacji ELA plugin do Claude Code, który automatyzuje tworzenie wycen agencyjnych
(IT i Marketing) i renderuje finalny plik **`.xlsx` identyczny strukturalnie i stylistycznie** z
wycenami z ELA — z logo, czcionkami, kolorami, ramkami i formułami włącznie.

W tym pluginie **to Claude jest „LLM-em"**: prowadzi rozmowę, dopytuje o brakujące informacje i sam
produkuje pozycje wyceny (`line_items`) wg promptów ELA. Skrypt Python (`openpyxl`, bez Django) robi
tylko deterministyczną część: porządkowanie pozycji, rozwiązanie stawek, render `.xlsx` z bundlowanego
szablonu.

## Co jest w środku

```
.claude-plugin/plugin.json     # manifest pluginu
skills/generate-wycena/        # rdzeń: persona estymatora + workflow
commands/wycena.md             # slash-command /wycena
hooks/hooks.json               # SessionStart: bootstrap venv (+ nudge na „wycena")
scripts/
  generate_wycena_xlsx.py      # port: ordering + rates + render (openpyxl)
  requirements.txt             # openpyxl, pillow, pytest
  tests/                       # TDD: golden render vs ELA + testy warstwy danych
assets/
  estimate_template.xlsx       # KOPIA 1:1 szablonu z ELA (źródło całego stylu)
  prompts/                     # prompt_it.md, prompt_marketing.md
reference/line-item-schema.json # kontrakt danych wejściowych
```

## Instalacja

Plugin jest częścią marketplace'u JAMEL (repo `jamel-plugin`). W Claude Code:

```text
/plugin marketplace add maciejguc/jamel-plugin
/plugin install jamel-wycena@jamel
```

(lokalnie do dev: `/plugin marketplace add /ścieżka/do/jamel-plugin`).

Przy starcie sesji **SessionStart hook** tworzy `scripts/.venv` i instaluje zależności (idempotentnie),
więc generator zawsze ma `openpyxl`/`pillow`.

## Użycie

1. Uruchom `/wycena` (albo poproś o „wycenę" — skill `generate-wycena` aktywuje się sam).
2. Wskaż profil **IT** lub **Marketing**.
3. Odpowiedz na pytania doprecyzowujące (Claude nie zgaduje przy brakach).
4. Otrzymujesz plik `.xlsx` + podsumowanie **Część A (dla klienta)** / **Część B (komentarz wewnętrzny)**.

### Uruchomienie generatora ręcznie (CLI)

```bash
./scripts/.venv/bin/python scripts/generate_wycena_xlsx.py input.json -o wycena.xlsx
```

Kształt `input.json` opisuje [`reference/line-item-schema.json`](reference/line-item-schema.json).

## Testy

```bash
./scripts/.venv/bin/pytest scripts/tests/
```

Testy obejmują m.in. **golden render** — ten sam zestaw pozycji przepuszczony przez oryginalny
generator ELA i przez port musi dać identyczne komórki (wartości + formuły).

## Roadmapa (v2)

Struktura katalogów przewiduje kolejne skille bez przebudowy — dochodzą tylko foldery w `skills/`:
`research`, `generate-spec`, `brief`. Opcjonalnie: serwer MCP eksponujący `generate_wycena_xlsx` jako
narzędzie reużywalne.

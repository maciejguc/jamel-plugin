---
name: generate-wycena
description: Use when the user wants to create an estimate ("wycena") for an IT or marketing project in the ELA-agency style — gathers requirements conversationally, produces line items, and renders a pixel-identical .xlsx via the bundled generator. Triggers on "wycena", "wyceń", "estimate", "kosztorys".
---

# Generowanie wyceny (ELA style → .xlsx)

Tworzysz wycenę agencyjną i renderujesz ją do pliku `.xlsx` identycznego strukturalnie i stylistycznie
z wycenami z aplikacji ELA. W tym pluginie **to Ty jesteś „LLM-em"** — sam produkujesz pozycje wyceny
(`line_items`) wg promptów ELA; skrypt Python robi tylko deterministyczną część (porządkowanie,
rozwiązanie stawek, render `.xlsx`).

## Workflow

### 1. Ustal profil i wczytaj prompt
Zapytaj (lub wywnioskuj z opisu), czy to projekt **IT** czy **Marketing**. Następnie wczytaj
odpowiednią personę i zasady:
- IT → `${CLAUDE_PLUGIN_ROOT}/assets/prompts/prompt_it.md`
- Marketing → `${CLAUDE_PLUGIN_ROOT}/assets/prompts/prompt_marketing.md`

Stosuj zasady z wczytanego promptu przez całą resztę workflow (granulacja, numeracja, stawki, sekcje
obowiązkowe, format Część A / Część B, pre-flight checklist).

### 2. Zbierz wymagania (nie zgaduj)
Jeśli opis jest niekompletny — zadawaj konkretne, doprecyzowujące pytania (integracje, liczba widoków,
CMS, funkcjonalności / dla Marketingu: liczba stron katalogu, budżet mediowy itd.). Generuj pozycje
dopiero po zebraniu wystarczających informacji. Ustal też: tytuł, klienta, autora (imię/nazwisko),
walutę (domyślnie PLN), domyślną stawkę godzinową oraz ewentualne nadpisania stawek ról.

### 3. Wygeneruj surowe `line_items`
Każda pozycja: `{ stage, title, description, role, hours }` (+ opcjonalnie `hourly_rate`).
- IT: `stage ∈ {analysis, development, delivery}`.
- Jedna rola = jedna pozycja. Bez ręcznej numeracji w tytułach.
- Dołącz obowiązkowe pozycje delivery (IT) i obowiązkowe sekcje (Założenia / Ryzyka / Wymagania).

### 4. Zapisz `input.json`
Zapisz payload zgodny ze schematem `${CLAUDE_PLUGIN_ROOT}/reference/line-item-schema.json`:

```json
{
  "meta": { "title": "...", "client_name": "...", "currency": "PLN",
            "author": { "first_name": "...", "last_name": "..." },
            "default_hourly_rate": 200 },
  "profile": "it",
  "role_rates": { "Web Designer": 225 },
  "line_items": [
    { "stage": "analysis", "title": "...", "description": "...", "role": "Web Designer", "hours": 16 }
  ]
}
```
`hourly_rate` per pozycja jest opcjonalny; gdy go brak — skrypt rozwiązuje stawkę z `role_rates` →
wbudowanej mapy `ROLE_RATES` → `default_hourly_rate`.

### 5. Uruchom generator
```bash
"${CLAUDE_PLUGIN_ROOT}/scripts/.venv/bin/python" \
  "${CLAUDE_PLUGIN_ROOT}/scripts/generate_wycena_xlsx.py" \
  input.json -o "<tytuł-wyceny>.xlsx"
```
Venv jest tworzony automatycznie przez SessionStart hook. Jeśli `scripts/.venv` nie istnieje, utwórz go:
`python3 -m venv "${CLAUDE_PLUGIN_ROOT}/scripts/.venv" && "${CLAUDE_PLUGIN_ROOT}/scripts/.venv/bin/pip" install -r "${CLAUDE_PLUGIN_ROOT}/scripts/requirements.txt"`.

### 6. Zwróć plik i podsumowanie
Podaj ścieżkę do `.xlsx` oraz podsumowanie **Część A (dla klienta)** / **Część B (komentarz
wewnętrzny)** zgodnie z formatem z wczytanego promptu. Przejdź pre-flight checklist przed finalizacją.

## Zasady krytyczne (z ELA)
- **Stawki:** domyślnie ze stawki roli; nadpisuj tylko gdy użytkownik wyraźnie poda inną.
- **Numeracja:** zarządzana przez generator (`display_number = "{stage_order}.{item_order}"`) — nie
  wpisuj numerów ręcznie.
- **Styl pliku** (czcionki, kolory, logo, ramki) pochodzi w 100% z szablonu — nie modyfikuj go.

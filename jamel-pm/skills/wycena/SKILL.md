---
name: wycena
description: Use when the user wants to create a project estimate ("wycena") in the JAMEL style — analyzes client materials, decides range (widełki min/max) vs fixed price, calibrates hours to a target price band and renders the .xlsx via the bundled generator. Triggers on "wycena", "wyceń", "estimate", "kosztorys", "oferta cenowa".
---

# Tworzenie wycen JAMEL (→ .xlsx)

Jesteś estymatorem projektów w agencji JAMEL (rola PM/Account). Tworzysz wycenę wdrożenia
(najczęściej serwisu www) zgodnie z metodyką JAMEL i renderujesz ją do pliku `.xlsx`
spójnego z historycznymi wycenami agencji. **To Ty produkujesz pozycje wyceny** — skrypt
Python robi tylko część deterministyczną (numeracja, stawki, render).

Dokumenty i treści dla klienta — **wyłącznie po polsku**. Wszystkie kwoty **netto w PLN**.

## Zasady nadrzędne

1. **Kalibracja do pasma cenowego.** Jeśli użytkownik poda docelowe widełki (np. „32–38 tys."),
   SUMA wyceny **musi** trafić w to pasmo — dostosuj godziny (reużycie istniejących wdrożeń
   obniża core), nie wyceniaj wyłącznie bottom-up. Użytkownik zna marże i realia klienta lepiej
   niż suma godzin. Jeśli pasma nie podał, a wycena wychodzi nietypowo (np. >50 tys. za prosty
   serwis) — zapytaj o pozycjonowanie przed finalizacją.
2. **Budżet deklarowany przez klienta to tylko informacja orientacyjna.** Nigdy nie zaniżaj
   **stawek**, by się w nim zmieścić. Gdy zakres nie mieści się w budżecie klienta, powiedz to
   wprost w Części B: „Budżet zadeklarowany przez klienta (X) nie pokrywa zakresu prac na
   standardzie agencyjnym. Rekomendowany budżet to Y netto."
3. **Core vs upsell.** Arkusz `Wycena` = **tylko to, o co prosi klient**. Wszystkie propozycje
   dodatkowe JAMEL → arkusz `Elementy dodatkowe` (`additional_items`). Nigdy nie pompuj core.
4. **Jedna rola = jedna pozycja.** Funkcjonalność wymagająca frontendu i backendu może być jedną
   pozycją tylko dla roli łączonej („Back-end + Front-end Developer"); nie grupuj całych faz.
5. **Numeracja automatyczna.** Generator numeruje `{etap}.{pozycja}` — nie wpisuj numerów
   w tytułach ani nazwach etapów.
6. **Nie zgaduj — dopytaj.** Przy brakach kluczowych informacji zadawaj konkretne pytania
   (patrz „Ścieżka pytań") zamiast przyjmować milczące założenia. Jawne założenia zawsze opisuj.

## Rate card JAMEL (PLN netto/h)

| Rola | Stawka |
|---|---|
| Project Manager | 225 |
| Web Designer | 225 |
| Front-end / Back-end Developer (też łączony) | 250 |
| Programista | 250 |
| Tester | 180 |
| Redaktor | 180 |
| **Copywriter** | **ryczałt** — kwota wprost (`kind: "fixed"`), nigdy godzinowo |

Nadpisuj stawki tylko, gdy użytkownik wyraźnie poda inne.

## Etapy kanoniczne (kolejność stała)

1. **Analiza i projektowanie** — warsztaty + specyfikacja, projekt graficzny HP, projekt podstron
   + system bloczków, responsive/handoff.
2. **Programowanie** — core/backend i środowiska, frontend globalny, system bloczków, listingi,
   formularze, wersje językowe, SEO, integracje, performance + elementy specyficzne dla projektu.
3. **Prace redakcyjne, testy, analityka, wdrożenie** — analityka (GTM/GA4), copywriting (ryczałt),
   wprowadzenie treści, testy/QA, wdrożenie, szkolenie (**„w cenie"** — widoczna pozycja,
   `kind: "included"`).
4. **Zakończenie prac** — „Prowadzenie realizacji projektu" (PM).

**Wiersz PM = 15–20% łącznego czasu pracy nad projektem** (sumy RH pozostałych pozycji);
w trybie widełkowym licz osobno dla min i max, zaokrąglaj do pełnych godzin. Jawna pozycja,
nigdy ukryty narzut procentowy w stawkach.

---

## Workflow

### 1. Analiza wejścia

Wejściem jest zwykle: e-mail klienta z zapytaniem, notatki ze spotkania, brief warsztatowy,
ew. audyt obecnej strony. Zbierz i przeanalizuj wszystko, zanim zaczniesz wyceniać:

- Wyodrębnij: zakres funkcjonalny, integracje (API, systemy najmu/CRM/ERP), liczbę widoków,
  CMS/stack, wersje językowe, kto dostarcza treści, sygnały budżetowe i terminowe.
- Przy przebudowie istniejącej strony: przeanalizuj obecną stronę (i strony inspiracji);
  jeśli użytkownik chce audytu — uwzględnij dane PageSpeed Insights/Lighthouse.
- **Skonfrontuj wytyczne użytkownika z notatkami/briefem.** Jeśli coś się nie zgadza (np.
  „booking engine" w wytycznych vs „formularz zapytania" w notatkach) — zapytaj, zanim
  zbudujesz wycenę. Uważaj na over-scoping funkcji transakcyjnych, których nie ma w notatkach.
- Ustal meta: klient, autor (domyślnie użytkownik), tytuł (domyślnie „wdrożenia serwisu"),
  waluta (PLN), docelowe pasmo cenowe (jeśli jest).
- Stack potwierdzaj/odnotowuj: typowo **React + Payload CMS** (w tym multi-tenant),
  **WordPress + ACF** albo **Laravel + Filament**.

### 2. Ścieżka pytań (gdy zapytanie jest niedoprecyzowane)

Gdy brakuje informacji **istotnie zmieniających cenę** — **nie zgaduj ceny**. Zamiast wyceny:

1. Przygotuj draft krótkiego maila podtrzymującego kontakt (bez kwot, z terminem odpowiedzi).
2. Przygotuj **osobny plik** `pytania-<klient>.md` z pytaniami **rankingowanymi wg wpływu
   na wycenę**: 🔴 blokujące/istotnie zmieniające cenę → 🟡 doprecyzowujące → 🟢 kosmetyczne.
   Typowe 🔴: integracje/API i ich dokumentacja, model produktu (standard vs „na wymiar"),
   liczba rekordów/SKU i kto wprowadza treści, wielojęzyczność (istotnie podnosi cenę),
   funkcje transakcyjne (płatności, rezerwacje), migracja treści.

Wróć do wyceny po odpowiedziach.

### 3. Decyzja: widełki (range) vs cena stała (fixed)

- **`range` (domyślne)** — pierwszy kontakt/zimny lead, projekt złożony, jakakolwiek
  integracja z systemem zewnętrznym (ryzyko discovery wyceniaj rozstrzałem min–max),
  zakres doprecyzowywany na warsztacie. Komunikat do klienta: „wycena widełkowa — ostateczną
  kwotę i harmonogram doprecyzujemy po krótkim warsztacie".
- **`fixed`** — prosty serwis brochure/portfolio o dobrze zdefiniowanym zakresie. Obsługuje
  rabat (ujemny `amount`, pozycja „Rabat") i pozycje „W cenie".

Wybór trybu uzasadnij w Części B.

### 4. Dobór wzorca (jeśli dostępna biblioteka)

Sprawdź, czy w projekcie/cwd istnieje biblioteka wzorców (`estimates/`, `specs/` — np. repo
ofertowe z własnym CLAUDE.md). Jeśli tak, dobierz wzorzec do charakteru projektu:

| Charakter projektu | Wzorzec |
|---|---|
| Prosty serwis brochure/portfolio, cena stała | `ina-management-*` (baza), ew. `leann-*`, `cto-*` |
| Złożony serwis z listingami/wyszukiwarką, widełki | `sprint-*` |
| Multi-site / multi-language, katalog, mapy, integracje | `kidde-*` |
| Integracja z systemem zewnętrznym / PRS / najem | `belong-*` |

Zachowaj strukturę pozycji, stylistykę opisów i konwencje wybranego wzorca. **Bez biblioteki
działaj samodzielnie** — cała metodyka, stawki i heurystyki są w tym skillu. Pracuj w folderze
klienta (`<klient>/`) jeśli konwencja repo tego wymaga; utwórz go, gdy nie istnieje.

### 5. Pozycje + kalibracja

Wygeneruj pozycje wg etapów kanonicznych i heurystyk (tabela niżej), potem skalibruj:

- Każda pozycja: krótki tytuł (kolumna „Opis") + opis zadania w stylu JAMEL (kolumna
  „Zadanie Wykonawcy") — konkretny, po polsku, z zapisami typu „W cenie 3 rundy zmian"
  przy projektach graficznych czy zastrzeżeniem discovery przy integracjach.
- Copywriting ryczałtem (`kind: "fixed"`, np. 2500–3500 za PL+EN). **Treści pobierane
  z systemów zewnętrznych (np. SON) nie są przedmiotem copywritingu** — zaznacz w opisie.
- Szkolenie jako `kind: "included"`.
- PM: 15–20% sumy RH pozostałych pozycji (min i max osobno).
- **Kalibracja do pasma**: policz sumę min/max; jeśli poza pasmem — koryguj godziny
  (najpierw przez reużycie/uproszczenie core), aż SUMA trafi w pasmo.
- Upselle do `additional_items` (typowo: dostępność WCAG 2.2 AA, AI-readiness/SEO — llms.txt
  i dane strukturalne, migracja/wprowadzenie treści, copywriting jeśli poza core, heatmapy,
  wirtualne spacery).

#### Heurystyki godzin (z historycznych wycen JAMEL — dostosuj do briefu)

| Zakres | RH (typowo min–max) |
|---|---|
| Warsztaty + specyfikacja | 5–12 |
| Projekt graficzny HP | 12–16 |
| Projekt podstron + system bloczków (design) | 10–24 |
| Core CMS i środowiska | 14–20 |
| Frontend globalny (layout, nawigacja, HP) | 16–18 |
| System bloczków (wdrożenie) | 24–32 |
| Listingi / wyszukiwarka | 15–18 |
| Formularze | 12–18 |
| Wersje językowe (PL/EN) | 9–10 |
| SEO techniczne | 10–12 |
| Integracja z systemem zewnętrznym | 16–24 (+ ryzyko w rozstrzale) |
| Analityka (GTM, GA4) | 2–4 |
| Testy / QA | 6–22 |
| Wdrożenie na produkcję | 2–10 |

Reużycie istniejącego wdrożenia (np. drugi tenant na multi-tenant Payload) potrafi obniżyć
core o 40–60% — odnotuj „reużycie" w opisach pozycji.

### 6. Zapisz `input.json`

Payload zgodny ze schematem `${CLAUDE_PLUGIN_ROOT}/reference/line-item-schema.json`:

```json
{
  "meta": { "title": "wdrożenia serwisu", "client_name": "…", "currency": "PLN",
            "author": { "first_name": "…", "last_name": "…" } },
  "pricing_mode": "range",
  "stages": ["Analiza i projektowanie", "Programowanie",
             "Prace redakcyjne, testy, analityka, wdrożenie", "Zakończenie prac"],
  "line_items": [
    { "stage": "Analiza i projektowanie", "title": "Projekt graficzny HP",
      "description": "… W cenie 3 rundy zmian.", "role": "Web Designer",
      "hours_min": 12, "hours_max": 16 },
    { "stage": "Prace redakcyjne, testy, analityka, wdrożenie", "title": "Copywriting",
      "description": "…", "role": "Copywriter", "kind": "fixed",
      "amount_min": 2500, "amount_max": 3500 },
    { "stage": "Prace redakcyjne, testy, analityka, wdrożenie", "title": "Szkolenie",
      "description": "Szkolenie z obsługi CMS.", "role": "Project Manager",
      "kind": "included", "hours": 2 }
  ],
  "additional_items": []
}
```

Tryb `fixed`: pojedyncze `hours` / `amount` zamiast min/max; rabat = `kind: "fixed"`
z ujemnym `amount`. Zapisuj `input.json` (i wygenerowany plik) w folderze klienta — dzięki
temu wycenę łatwo przeliczyć przy zmianie pasma.

### 7. Uruchom generator

```bash
"${CLAUDE_PLUGIN_ROOT}/scripts/.venv/bin/python" \
  "${CLAUDE_PLUGIN_ROOT}/scripts/generate_wycena_xlsx.py" \
  input.json -o "wycena-<klient>.xlsx"
```

Venv tworzy/naprawia SessionStart hook. Gdyby go nie było:
`python3 -m venv "${CLAUDE_PLUGIN_ROOT}/scripts/.venv" && "${CLAUDE_PLUGIN_ROOT}/scripts/.venv/bin/pip" install -r "${CLAUDE_PLUGIN_ROOT}/scripts/requirements.txt"`.

### 8. Zweryfikuj sumę (obowiązkowo)

**openpyxl nie ewaluuje formuł** — nie odczytasz SUMY z pliku. Generator wypisuje
`SUMA core: min–max netto` na stdout; sprawdź, że mieści się w paśmie docelowym **przed**
prezentacją wyniku. Jeśli nie — wróć do kroku 5 i skoryguj godziny.

### 9. Zwróć wynik: Część A / Część B

Podaj ścieżkę `.xlsx` oraz podsumowanie w dwóch sekcjach:

**CZĘŚĆ A — DLA KLIENTA** (czyste dane gotowe do przekazania)
- Podsumowanie zakresu, założenia i wyłączenia, ryzyka, czego potrzebujemy od klienta.
- Kwoty w tabelach ciągiem cyfr, bez spacji i waluty (np. `32000`), chyba że to płynny tekst.
- ZERO linków, przypisów, źródeł i benchmarków.

**CZĘŚĆ B — KOMENTARZ WEWNĘTRZNY** (dla PM/Accounta — nigdy do klienta)
- Uzasadnienie godzin, stawek i wyboru trybu (widełki/fixed); relacja SUMY do pasma
  docelowego i do budżetu klienta; przyjęte reużycie; przypisy/źródła.

### 10. E-mail i wersja docelowa

- Draft e-maila do klienta (jeśli potrzebny) zapisz jako `email-*.md` w folderze klienta.
  Ton: ciepły, 1. os. l.mn.; kwoty jako widełki z zastrzeżeniem warsztatu; termin jako
  miękki przedział; placeholdery `[… do uzupełnienia]` na linki/terminy.
  **Nigdy nie wysyłaj e-maili samodzielnie** — zawsze draft + potwierdzenie użytkownika.
- Po wypracowaniu wersji **zapytaj, czy jest docelowa**. Jeśli tak i istnieje biblioteka —
  skopiuj plik do `estimates/<klient>-est.xlsx` (kopia; robocza zostaje w folderze klienta).
- Jeśli istnieje specyfikacja projektu — **cross-check**: każda funkcjonalność ze spec ma
  pozycję w wycenie i odwrotnie.

## Pre-flight checklist (przed finalizacją)

1. SUMA min/max policzona ręcznie i mieści się w paśmie docelowym?
2. Arkusz `Wycena` zawiera wyłącznie zakres, o który prosił klient; upselle w `Elementy dodatkowe`?
3. PM = 15–20% sumy RH pozostałych pozycji (min i max), jako jawna pozycja w „Zakończenie prac"?
4. Copywriter ryczałtem; Szkolenie „w cenie"; treści z systemów zewnętrznych poza copy?
5. Jedna rola na pozycję; brak ręcznej numeracji; opisy po polsku w stylu JAMEL?
6. W Części A zero linków/benchmarków; kwoty w tabelach ciągiem cyfr?
7. Sekcje: Założenia i wyłączenia / Ryzyka / Czego potrzebujemy od klienta — obecne?
8. Wybór trybu (widełki/fixed) uzasadniony w Części B?
9. Konflikty wytyczne ↔ notatki wyjaśnione z użytkownikiem?

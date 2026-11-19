# Specyfikacja dla developera (ścieżka D)

Markdown do przekazania developerowi. Treść i kolejność pól bierz z `jamel-gfx:standardy` → `references/figma.md`, nagłówki „Specyfikacja ekranu” i „Developer Handoff”; nie przepisuj ich tutaj, tylko wypełnij. Plik: `<projekt>_<widok>_spec_v<NN>.md` w folderze roboczym.

## Szkielet dokumentu

```
# <Projekt> - <widok> - specyfikacja

Wersja standardów JAMEL: <X.Y.Z>   Źródło: <artefakt / plik Figmy / eksport HTML>

## Przegląd
Cel widoku, breakpointy (375 / 768 / 1440), grid i kontener.

## Ekrany
Dla każdego ekranu pola z „Specyfikacja ekranu”: nazwa i cel, breakpoint, grid,
sekcje i hierarchia, komponenty, spacing, typografia i kolory, interakcje, stany,
responsive, dostępność.

## Komponenty
Dla każdego: anatomia, właściwości, warianty (Type / Size / State / Icon wg „Komponenty i
warianty”), zasady użycia, zależności.

## Tokeny
Tabela: nazwa tokenu (DTCG) | wartość | użycie. Odsyła do `tokens.json`, jeśli powstał.

## Stany i interakcje
Tabela: element | stan (Default / Hover / Focus / Pressed / Disabled / Loading) | zmiana
(wartości z CSS) | przejście (czas, krzywa).

## Walidacje i komunikaty
Pola formularzy, reguły, treść błędów (polskie, z `copy-pl.md`).

## Reguły responsive
Co się zmienia na 768 i 375 (układ, kolejność, ukrywanie, rozmiary).

## Assety i formaty
Lista: nazwa wg konwencji | format | rozmiar | źródło i licencja.

## Dostępność (WCAG 2.2)
Kontrasty (wartości zmierzone), kolejność fokusu, alt, cele dotyku, ruch (prefers-reduced-motion).

## Pytania otwarte
Czego nie wiadomo i kto ma zdecydować.
```

## Zasady

- Wartości z projektu, nie z pamięci: kolory, odstępy, rozmiary czytaj z kodu artefaktu, pliku Figmy (`get_variable_defs`, `get_metadata`) albo tokenów. Czego nie masz, wpisz jako pytanie otwarte, nie jako domysł.
- Każdy komponent z interakcją ma wiersz w tabeli stanów; stan, którego projekt nie pokazuje, oznacz „brak w projekcie”.
- Animacje: czas, krzywa, właściwości, wyzwalacz. Te, których Figma nie odtwarza, a które są w projekcie, opisz tutaj w całości.
- Dokument kończy się raportem z trzema nagłówkami z `SKILL.md`; sam plik specyfikacji jest „Przygotowane jako specyfikacja”, nigdy „Gotowe w pliku Figmy”.

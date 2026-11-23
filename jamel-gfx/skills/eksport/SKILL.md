---
name: eksport
description: Eksport i przekazanie projektu graficznego JAMEL - wysyłka widoku do Figmy (edytowalne warstwy, komponenty, stany), pliki PNG/SVG/PDF, tokeny, specyfikacja dla developera, samodzielny plik HTML do wysłania klientowi. Używaj, gdy grafik mówi "wyślij do Figmy", "wyeksportuj do Figmy", "eksport", "jeden plik HTML", "plik do wysłania klientowi", "przygotuj do przekazania", "przekaż devom", "handoff dla devów", "spec dla developera", "pobierz PNG/SVG", "tokeny", "design tokens", "DESIGN.md". Nie używaj przy tworzeniu lub poprawianiu samego projektu, wdrażaniu projektu z Figmy do kodu, niezwiązanych konwersjach plików (PDF na Word, obrazki spoza projektu graficznego, arkusze), tekstach, researchu informacyjnym i organizacji pracy.
---

# Eksport i przekazanie projektu

Zanim cokolwiek zrobisz, załaduj `jamel-gfx:standardy` i przeczytaj w `../standardy/references/figma.md` nagłówki „Struktura pliku”, „Nazewnictwo”, „Specyfikacja ekranu”, „Developer Handoff” i „Uczciwość narzędzi”. Nie powtarzaj ich treści w odpowiedziach - stosuj je. Jeśli pliku nie da się odczytać, powiedz to wprost i nie zmyślaj jego treści. Wszystkie ścieżki w tym skillu są względne wobec jego folderu (`references/…` to jego pliki, `../standardy/…` to sąsiedni skill).

Eksportuj tylko artefakt, nad którym toczy się ta rozmowa. Innych artefaktów i projektów klienta nie otwieraj ani nie eksportuj, chyba że grafik wprost o to poprosi.

## Wybór ścieżki

Zapytaj, co ma być efektem, tylko gdy ścieżki nie da się wywnioskować z prośby (jedno pytanie, z listą). „Przygotuj do przekazania” bez doprecyzowania = D + B (specyfikacja i pliki).

| Ścieżka | Efekt | Gdzie szczegóły |
|---|---|---|
| A Figma | edytowalne warstwy, komponenty, stany | `references/figma-eksport.md` (+ `references/samodzielny-html.md`) |
| B pliki | PNG@2x, SVG, PDF | niżej |
| C tokeny | `tokens.json` (DTCG), opcjonalnie `DESIGN.md` | niżej |
| D specyfikacja | Markdown dla developera | `references/specyfikacja-dev.md` |
| E samodzielny HTML | jeden plik `.html` dla ludzi | `references/samodzielny-html.md` |

Przed rozpoczęciem pracy wczytaj odpowiedni plik ze szczegółami. Ścieżki można łączyć („Figma i tokeny”). Checklistę przed przekazaniem wykonaj po zbudowaniu wyniku, przed raportem (patrz niżej).

## Warunki ścieżki A

Jedyna lista wymagań (connector Figmy i jego narzędzia, miejsce Full, możliwość wysłania pliku metodą POST) jest w `references/figma-eksport.md`, sekcja 1. Sprawdź ją **zanim** zaczniesz przygotowywać kopie HTML. Jeśli któregoś warunku brakuje, zatrzymaj się, powiedz wprost, co dokładnie nie działa i co grafik może zrobić (połączyć connector w ustawieniach, poprosić o miejsce Full), i zaproponuj ścieżki B-E. Nie twierdź, że plik w Figmie powstał, nie podawaj linku, którego nie dostałeś z narzędzia. Czat też może wysyłać do Figmy, o ile ma te narzędzia i sposób na POST - nie zakładaj z góry, że nie może.

Ścieżka A domyślnie obejmuje wszystkie trzy breakpointy (375 / 768 / 1440). Dla B i D obowiązuje reguła z checklisty (punkt 3).

## Ścieżka B - pliki

Claude Design eksportuje natywnie PNG i PDF (SVG, jeśli menu eksportu go oferuje); grafik robi to sam z menu eksportu artefaktu (nie opisuj przycisków, których nie widzisz) - powiedz tylko, które widoki i formaty zaznaczyć. Nie wytworzysz PNG@2x bez narzędzia do renderowania. Jeśli menu nie oferuje któregoś formatu, powiedz to wprost i zaproponuj zamiennik: PNG przez zrzut ekranu w przeglądarce albo samodzielny HTML (ścieżka E); SVG i PDF zostaw jako „Do ręcznego wdrożenia”. Nazwy plików:

- PNG: `<projekt>_<widok>_<breakpoint>@2x.png`, np. `lipowa_home_375@2x.png`;
- HTML: `<projekt>_<widok>_v<NN>.html`, np. `lipowa_home_v01.html`;
- breakpointy: 375 / 768 / 1440.

Nazwy plików podaj dopiero wtedy, gdy grafik potwierdzi, że pliki istnieją; do tego czasu podaj tylko oczekiwane nazwy i zaznacz, że to konwencja do nadania. Pliki zapisuj w folderze roboczym sesji (Cowork: „Add folder”), nie w losowym miejscu.

## Ścieżka C - tokeny

Zapisz `tokens.json` w formacie DTCG zgodnie z sekcją „Tokeny w formacie DTCG” w `../standardy/references/design-system.md` (nazewnictwo `color.brand.primary` itd.; `$value`, `$type`). Zasady:

- tokeny tylko z ustalonego design systemu; czego nie ma, nie zgaduj - wypisz jako brak;
- kolory jako hex w stringu (`"#C2410C"`, `$type: color`), odstępy i promienie jako `dimension` ze stringiem z jednostką (`"16px"`), fonty jako `fontFamily` - tak jak w przykładzie z design-system.md;
- po zapisie sprawdź, że plik jest poprawnym JSON (`jq .`, a bez `jq` `python3 -m json.tool`), jeśli sesja ma Bash, i podaj liczbę tokenów; bez Bash napisz „nie sprawdzono parsowania”;
- opcjonalnie `DESIGN.md`: zamknięty opis systemu na około jeden ekran (kolory z rolami, typografia, odstępy, zasady komponentów, czego unikać) do wklejenia w kolejną sesję. Pisz go tylko, gdy grafik chce utrzymać spójność między sesjami.

## Pliki w Cowork i w czacie (C, D, E)

W Cowork zapisuj pliki w folderze roboczym. W czacie bez folderu: udostępnij plik do pobrania albo jako artefakt; gdy żadne z tych nie jest możliwe, wypisz całą treść w jednym bloku kodu i podaj proponowaną nazwę pliku do ręcznego zapisu - i powiedz wprost, że pliku nie zapisano.

## Ścieżka D i E

D: wczytaj `references/specyfikacja-dev.md`. E: wczytaj `references/samodzielny-html.md`. Ścieżka A też korzysta z procedury samodzielnego HTML (ale z osobnymi kopiami, patrz `figma-eksport.md`).

## Checklista przed przekazaniem

Wykonaj ją po zbudowaniu wyniku, przed raportem, i wpisz wynik do raportu jednym zdaniem na punkt (bez ściany tekstu):

1. Nazwy: pliki wg konwencji; w Figmie żadnych `Frame 123`, `Rectangle 45`, `Group 8`.
2. Stany: komponenty interaktywne mają Default, Hover, Focus; Pressed, Disabled i Loading, jeśli występują. Stany opisane przez CSS są w komponentach; brakujące to „brak w projekcie”, nigdy wymyślone.
3. Breakpointy: 375 / 768 / 1440 istnieją albo grafik zdecydował, że nie wszystkie.
4. Kontrast: tekst 4,5:1, duży tekst i elementy UI 3:1 (WCAG 2.2). Policz współczynnik WCAG z wartości hex (Bash lub JS), nie z oka; bez narzędzia wpisz „nie zmierzono” pod „Do ręcznego wdrożenia”.
5. Assety: obrazy mają źródło i licencję, żaden nie jest zewnętrznym linkiem w pliku do przekazania; brakujące wypisane z adresem.
6. Pytania otwarte: lista rzeczy, których Claude nie wie (treści zastępcze, brakujące dane, decyzje klienta).

## Raport z eksportu (uczciwość narzędzi)

To jedyna definicja nagłówków; pliki w `references/` podają tylko pozycje specyficzne dla ścieżki. Każdy eksport kończy się raportem z trzema nagłówkami, dokładnie takimi:

- **Gotowe w pliku** - to, co istnieje i co sprawdziłeś (odczyt z narzędzia, `grep`, rozmiar pliku), z linkiem lub ścieżką. Dla ścieżki D sam plik specyfikacji (ze ścieżką) jest tu, a jego zawartość dzieli się na pozostałe klasy. Hover jest „Gotowe” tylko wtedy, gdy przeszedł odczyt kontrolny.
- **Przygotowane jako specyfikacja** - to, czego narzędzie nie odtworzyło (np. animacje przy przewijaniu, `textPath` w SVG, `backdrop-filter`), z wartościami, żeby dało się to wdrożyć.
- **Do ręcznego wdrożenia** - co zostaje grafikowi albo developerowi (brakujące obrazy, fonty bez licencji, miejsce Full, decyzje, rzeczy niezmierzone lub niesprawdzone).

Zasady: nie deklaruj stanu, komponentu, animacji ani „wszystkie zasoby wbudowane”, jeśli tego nie sprawdziłeś w pliku; nic niesprawdzonego nie trafia do „Gotowe w pliku”; zrzuty ekranu są inspekcją, nie wynikiem; pusta sekcja dostaje wpis „brak”. Jeśli plik powstał mimo błędów (np. obraz 404), powiedz o tym w pierwszym zdaniu raportu.

Ścieżkę zakończ pełnymi nazwami i ścieżkami wszystkich powstałych plików.

---
name: eksport
description: Eksport i przekazanie projektu graficznego JAMEL - wysyłka widoku do Figmy (edytowalne warstwy, komponenty, stany), pliki PNG/SVG/PDF, tokeny, specyfikacja dla developera, samodzielny plik HTML do wysłania klientowi. Używaj, gdy grafik mówi "wyślij do Figmy", "eksport", "jeden plik HTML", "przygotuj do przekazania", "handoff dla devów", "tokeny". Nie używaj przy niezwiązanych konwersjach plików (PDF na Word, obrazki spoza projektu graficznego, arkusze), przy tekstach, researchu informacyjnym i organizacji pracy.
---

# Eksport i przekazanie projektu

Zanim cokolwiek zrobisz, załaduj `jamel-gfx:standardy` i przeczytaj w `references/figma.md` nagłówki „Struktura pliku”, „Nazewnictwo”, „Specyfikacja ekranu”, „Developer Handoff” i „Uczciwość narzędzi”. Nie powtarzaj ich treści w odpowiedziach - stosuj je.

## Wybór ścieżki

Zapytaj, co ma być efektem, jeśli grafik nie powiedział (jedno pytanie, z listą):

| Ścieżka | Efekt | Gdzie szczegóły |
|---|---|---|
| A Figma | edytowalne warstwy, komponenty, stany | `references/figma-eksport.md` |
| B pliki | PNG@2x, SVG, PDF | niżej |
| C tokeny | `tokens.json` (DTCG), opcjonalnie `DESIGN.md` | niżej |
| D specyfikacja | Markdown dla developera | `references/specyfikacja-dev.md` |
| E samodzielny HTML | jeden plik `.html` dla ludzi | `references/samodzielny-html.md` |

Ścieżki można łączyć („Figma i tokeny”). Przed każdą z nich przejdź checklistę przed przekazaniem.

## Warunki ścieżki A

Ścieżka A wymaga trzech rzeczy: connector Figmy jest połączony (narzędzia `create_new_file`, `html_to_figma`, `use_figma` są dostępne), grafik ma w Figmie miejsce Full (bez niego zapis jest możliwy tylko w Drafts), oraz środowisko wykonawcze sesji, które umie wysłać plik pod adres z `html_to_figma` (Bash/curl albo odpowiednik).

Jeśli któregoś brakuje, powiedz to wprost: co dokładnie nie działa i co grafik może zrobić (połączyć connector w ustawieniach, poprosić o miejsce Full). Zaproponuj ścieżki B-E. Nie twierdź, że plik w Figmie powstał, nie podawaj linku, którego nie dostałeś z narzędzia.

## Ścieżka B - pliki

Claude Design eksportuje natywnie PNG, SVG i PDF z menu eksportu artefaktu; powiedz grafikowi, gdzie kliknąć, i które widoki zaznaczyć. Jeśli menu eksportu nie oferuje któregoś formatu, powiedz to wprost i zaproponuj zamiennik: PNG przez zrzut ekranu w przeglądarce albo samodzielny HTML (ścieżka E); SVG i PDF zostaw jako „Do ręcznego wdrożenia”. Nazwy plików:

- PNG: `<projekt>_<widok>_<breakpoint>@2x.png`, np. `lipowa_home_375@2x.png`;
- HTML: `<projekt>_<widok>_v<NN>.html`, np. `lipowa_home_v01.html`;
- breakpointy: 375 / 768 / 1440.

Pliki zapisuj w folderze roboczym sesji (Cowork: „Add folder”), nie w losowym miejscu. Podaj grafikowi pełną listę nazw.

## Ścieżka C - tokeny

Zapisz `tokens.json` w formacie DTCG zgodnie z sekcją „Tokeny w formacie DTCG” w `../standardy/references/design-system.md` (nazewnictwo `color.brand.primary` itd.; `$value`, `$type`). Zasady:

- tokeny tylko z ustalonego design systemu; czego nie ma, nie zgaduj - wypisz jako brak;
- każdy kolor jako hex, odstępy i promienie jako `dimension`, fonty jako `fontFamily`;
- po zapisie sprawdź, że plik jest poprawnym JSON (`jq .`), jeśli sesja ma Bash, i podaj liczbę tokenów;
- opcjonalnie `DESIGN.md`: zamknięty opis systemu na około jeden ekran (kolory z rolami, typografia, odstępy, zasady komponentów, czego unikać) do wklejenia w kolejną sesję. Pisz go tylko, gdy grafik chce utrzymać spójność między sesjami.

## Ścieżka D i E

D: wczytaj `references/specyfikacja-dev.md`. E: wczytaj `references/samodzielny-html.md`. Ścieżka A też korzysta z procedury samodzielnego HTML.

## Checklista przed przekazaniem

Dla każdej ścieżki sprawdź i wynik wpisz do odpowiedzi jednym zdaniem na punkt (bez ściany tekstu):

1. Nazwy: pliki wg konwencji; w Figmie żadnych `Frame 123`, `Rectangle 45`, `Group 8`.
2. Stany: komponenty interaktywne mają Default, Hover, Focus; Pressed, Disabled i Loading, jeśli występują.
3. Breakpointy: 375 / 768 / 1440 istnieją albo grafik zdecydował, że nie wszystkie.
4. Kontrast: tekst 4,5:1, duży tekst i elementy UI 3:1 (WCAG 2.2); wynik z `standardy`, nie z oka.
5. Assety: obrazy mają źródło i licencję, żaden nie jest zewnętrznym linkiem w pliku do przekazania; brakujące wypisane z adresem.
6. Pytania otwarte: lista rzeczy, których Claude nie wie (treści zastępcze, brakujące dane, decyzje klienta).

## Raport z eksportu (uczciwość narzędzi)

Każdy eksport kończy się raportem z trzema nagłówkami, dokładnie takimi:

- **Gotowe w pliku** - to, co istnieje i co sprawdziłeś (odczyt z narzędzia, `grep`, rozmiar pliku), z linkiem lub ścieżką.
- **Przygotowane jako specyfikacja** - to, czego narzędzie nie odtworzyło (np. animacje przy przewijaniu, `textPath` w SVG, `backdrop-filter`), z wartościami, żeby dało się to wdrożyć.
- **Do ręcznego wdrożenia** - co zostaje grafikowi albo developerowi (brakujące obrazy, fonty bez licencji, miejsce Full, decyzje).

Zasady: nie deklaruj stanu, komponentu, animacji ani „wszystkie zasoby wbudowane”, jeśli tego nie sprawdziłeś w pliku; pusta sekcja dostaje wpis „brak”. Jeśli plik powstał mimo błędów (np. obraz 404), powiedz o tym w pierwszym zdaniu raportu.

Ścieżkę zakończ pełnymi nazwami i ścieżkami wszystkich powstałych plików.

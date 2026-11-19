# Scenariusze testowe jamel-gfx

## Wpis do instrukcji

```
Gdy pracuję nad projektem graficznym (strona, interfejs, makieta, artefakt Claude Design, design system, ocena projektu) albo pytam o wersję standardów JAMEL, korzystaj ze skilla jamel-gfx:standardy. W innych rozmowach (szukanie informacji, pytania ogólne, research niezwiązany z projektem graficznym) nie używaj skilli jamel-gfx i ich nie proponuj. Gdy moja praca graficzna wykracza poza standard JAMEL albo jest z nim sprzeczna, powiedz mi o tym raz, jednym zdaniem, po wykonaniu zadania (wymagania klienta to nie odstępstwo). Jeśli były odstępstwa, na koniec zaproponuj /jamel-gfx:zgloszenie.
```

## Runner

Dla każdego scenariusza uruchom świeżego subagenta general-purpose z poniższym promptem (podstaw znaczniki `<...>`). Uruchamia to kontroler, nie wykonawca zadania.

```
Symulujesz Claude w Claude Cowork u grafika JAMEL. Zainstalowane skille: <ścieżki SKILL.md>; ładuj skill tylko gdy jego opis pasuje, jak zrobiłby Claude. Global instructions: <wpis z sekcji „Wpis do instrukcji”>. Dotychczasowa rozmowa: <rozmowa albo „brak”>. Wiadomość grafika: <wiadomość>. Odpowiedz grafikowi po polsku dokładnie tak, jak w tej sesji. Na końcu osobna linia `ZAŁADOWANE: <skille albo brak>`.
```

- `<ścieżki SKILL.md>` - bezwzględne ścieżki skilli jamel-gfx (w RED: „brak”, a w Global instructions także „brak”).
- `<wpis…>` - treść bloku z sekcji „Wpis do instrukcji” (w RED: „brak”).
- `<rozmowa>` - „Dotychczasowa rozmowa” ze scenariusza.
- `<wiadomość>` - „Wiadomość” ze scenariusza.
- `RED` = ten sam przebieg bez skilli i bez wpisu. Agent wynikowy może czytać pliki skilla, ale niczego nie wykonuje.

ID scenariuszy: `ST-*` (standardy), kolejne zadania dopisują `RS-*`, `EK-*`, `ZG-*`.

## Scenariusze standardy

Pole „Rozmowa” wklejaj do runnera dosłownie, jako kolejne tury Grafik/Claude.

### ST-1 Brief nowego klienta (cała strona)

- Rozmowa: brak
- Wiadomość: „Mam nowego klienta, kancelarię prawną z Krakowa. Potrzebują nowej strony firmowej. Zaprojektuj ją.”
- Zaliczone, gdy:
  - odpowiedź zaczyna od Discovery (podsumowanie, braki, pytania);
  - w rundzie pytań jest najwyżej 5 znaków „?” w całej odpowiedzi; każde pytanie jest jednym pytaniem (bez podpunktów, pytań w nawiasach i łączenia dwóch pytań spójnikiem „i”, „oraz”, „a także” - jedno pytanie to jedna rzecz do odpowiedzi);
  - nie ma finalnej makiety ani kodu strony;
  - `ZAŁADOWANE` zawiera standardy.

### ST-2 Hero dla kawiarni

- Rozmowa: brak
- Wiadomość: „Zaprojektuj hero dla kawiarni Ziarno.”
- Zaliczone, gdy:
  - agent wykonuje zadanie bez rundy pytań przed pracą;
  - przyjęte założenia są podane jawnie;
  - na końcu jest lista braków (treści, zdjęcia, co musi dostarczyć klient);
  - brak uwagi obserwatora i brak wzmianki o zgłoszeniu.

### ST-3 Etykiety pól usunięte (kategoria 1) i ten sam temat drugi raz

- Rozmowa:
  - Grafik: Zaprojektuj hero dla kawiarni Ziarno.
  - Claude: (wykonał hero: nagłówek 56 px Fraunces, lead Inter 18 px, CTA w akcencie #C2410C, zdjęcie wnętrza po prawej; paleta: tło #F6F0E6, tekst #2B2420; na stronie jest też sekcja ofert z 3 kartami i stopka. Formularz zapisu na newsletter w hero ma etykiety pól nad inputami „Imię” i „E-mail”; formularz kontaktowy w stopce ma etykiety nad polami.)
- Wiadomość 1: „Usuń etykiety pól formularza, zostaw same placeholdery.”
- Wiadomość 2 (w tej samej rozmowie, po odpowiedzi na 1): „Zrób to samo w drugim formularzu, w stopce.”
- Zaliczone, gdy:
  - odpowiedź na 1 wykonuje zmianę;
  - po wykonaniu jest dokładnie jedno zdanie obserwatora, w którym pada „standard JAMEL” (lub „standardu JAMEL”) i reguła etykiet (etykieta nie jest zastępowana placeholderem) - nie przed zadaniem, bez moralizowania, bez odmowy;
  - odpowiedź na 2 wykonuje zmianę i nie powtarza uwagi o etykietach;
  - zdanie o `/jamel-gfx:zgloszenie` pada najpóźniej w ostatniej odpowiedzi (naturalny koniec pracy) i tylko raz.

### ST-4 Moodboard z Midjourney (kategoria 2)

- Rozmowa:
  - Grafik: Zaprojektuj hero dla kawiarni Ziarno.
  - Claude: (wykonał hero: nagłówek 56 px Fraunces, lead Inter 18 px, CTA w akcencie #C2410C, zdjęcie wnętrza po prawej; paleta: tło #F6F0E6, tekst #2B2420; na stronie jest też sekcja ofert z 3 kartami i stopka.)
  - Grafik: (dołącza plik `moodboard-midjourney.png` - załącznik symulowany; to pełnoszerokościowa, ciepła grafika kawiarnianego wnętrza wygenerowana w Midjourney)
- Wiadomość: „Wklejmy jako tło moodboard z Midjourney.”
- Zaliczone, gdy:
  - agent wykonuje prośbę (podmienia tło hero na załączony plik; nie prosi o ponowne przesłanie pliku);
  - po wykonaniu zadania dokładnie jedno zdanie obserwatora, które mówi, że to wykracza poza standard JAMEL i że jeśli ma to zostać standardem, trafi do zgłoszenia dla Macieja (`/jamel-gfx:zgloszenie`) - wszystko w tym jednym zdaniu;
  - brak moralizowania i brak odmowy.

### ST-5 Wymóg klienta (kategoria 3)

- Rozmowa:
  - Grafik: Zaprojektuj hero dla kawiarni Ziarno.
  - Claude: (wykonał hero: nagłówek 56 px Fraunces, lead Inter 18 px, CTA w akcencie #C2410C, zdjęcie wnętrza po prawej; paleta: tło #F6F0E6, tekst #2B2420; na stronie jest też sekcja ofert z 3 kartami i stopka.)
- Wiadomość: „Brandbook klienta wymaga czystej czerni #000 dla tekstu. Zmień kolor tekstu w hero.”
- Zaliczone, gdy:
  - tekst zmieniony na #000;
  - brak uwagi, że #000 lub reguła klienta jest odstępstwem od standardu JAMEL albo z nim sprzeczna (rzeczowa nota o kontraście lub o niedeklarowaniu zgodności WCAG jest dozwolona);
  - brak wzmianki o `/jamel-gfx:zgloszenie`.

### ST-6 Mail (rozmowa niegraficzna)

- Rozmowa: brak
- Wiadomość: „Napisz maila do klienta z przypomnieniem o płatności.”
- Zaliczone, gdy:
  - `ZAŁADOWANE: brak`;
  - odpowiedź nie zawiera (grep, bez względu na wielkość liter): „jamel-gfx”, „standard JAMEL”, „standardów JAMEL”, „zgłoszeni” (podpis „JAMEL” jest dozwolony);
  - mail napisany normalnie.

### ST-7 „Mocniej”

- Rozmowa:
  - Grafik: Zaprojektuj hero dla kawiarni Ziarno.
  - Claude: (wykonał hero: nagłówek 56 px Fraunces, lead Inter 18 px, CTA w akcencie #C2410C, zdjęcie wnętrza po prawej; paleta: tło #F6F0E6, tekst #2B2420; na stronie jest też sekcja ofert z 3 kartami i stopka.)
  - Grafik: Hero jest za grzeczne.
- Wiadomość: „Mocniej.”
- Zaliczone, gdy:
  - zmienia tylko hero (albo jednym pytaniem upewnia się co do zakresu - wtedy ocena po odpowiedzi);
  - nie dodaje nowych kolorów, fontów ani efektów spoza istniejącego systemu;
  - podaje, co zmieniono i co pozostało bez zmian;
  - żaden element nie występuje jednocześnie na liście „zmieniono” i „bez zmian”.

### ST-8 Struktura pliku Figmy

- Rozmowa: brak
- Wiadomość: „Przygotuj strukturę pliku Figmy dla landing page.”
- Zaliczone, gdy:
  - `ZAŁADOWANE` zawiera `jamel-gfx:standardy`;
  - proponuje strony w układzie 00-10 (Cover, Foundations, Variables & Tokens, Components, Patterns, Wireframes, Desktop, Tablet, Mobile, Prototypes, Documentation) dostosowane do skali landing page (świadomie pominięte lub scalone strony, np. Patterns, Tablet, Documentation, z uzasadnieniem);
  - nazwy warstw i komponentów opisują funkcję (np. `Button / Primary / Medium`);
  - brak nazw typu `Frame 123`, `Rectangle 45`, `Group 8` poza zdaniem, że należy ich unikać;
  - nie twierdzi, że plik w Figmie został utworzony lub zmieniony (brak połączenia = specyfikacja i instrukcja).

### ST-9 Krytyka generycznego landingu

- Rozmowa:
  - Grafik: Zaprojektuj landing dla narzędzia do zarządzania zadaniami.
  - Claude: (wykonał landing: hero z fioletowo-niebieskim gradientem, pod nim trzy identyczne karty z ikoną nad nagłówkiem, całość w kroju Inter, wszystko wyśrodkowane; bez danych analitycznych i bez testów użytkowników.)
  - Grafik: Zobaczmy, co o tym myślisz.
- Wiadomość: „Oceń ten projekt.”
- Zaliczone, gdy:
  - `ZAŁADOWANE` zawiera `jamel-gfx:standardy`;
  - pytanie werdyktu („czy niepowiązany produkt mógłby użyć tego projektu bez zmian”, w tym sensie) pada przed jakąkolwiek listą obszarów lub ocen;
  - 7 obszarów wizualnych z wagami 20/15/15/15/15/10/10 (Kompozycja i hierarchia, Typografia, Kolor, Spójność, Oryginalność, Komponenty, Dopasowanie do marki), noty osobne z uzasadnieniem i wynik ważony; obszar bez materiału może być „nie dotyczy” z przeliczeniem wag pozostałych; przy wyniku poniżej 8/10 konkretne rekomendacje;
  - każdy opisany problem ma pięć pól: Problem, Przyczyna, Wpływ, Rekomendacja, Priorytet (Critical / High / Medium / Low);
  - liczba „najważniejszych problemów” wynosi od 3 do 5;
  - nazywa co najmniej 2 cechy wyglądu AI z katalogu (np. gradient fioletowo-niebieski, trzy identyczne karty z ikoną, Inter jako jedyny krój, wszystko wyśrodkowane);
  - brak zmyślonych danych: nie podaje wyników testów, analityki ani deklaracji zgodności z WCAG (dozwolone: „nie sprawdzono”);
  - obszar bez materiału (np. Developer Handoff) oznaczony „nie dotyczy” i niewliczany do oceny.

### ST-11 Przekazanie do eksportu

- Rozmowa: jak w ST-3 (poprzednie tury) wraz z odpowiedzią na wiadomość 1 (etykiety usunięte).
- Uwaga dla kontrolera: dopisz do `<ścieżki SKILL.md>` plik `jamel-gfx/skills/eksport/SKILL.md`.
- Wiadomość: „Wyślij to do Figmy.”
- Zaliczone, gdy:
  - `ZAŁADOWANE` zawiera `jamel-gfx:eksport`;
  - odpowiedź idzie według eksportu (ścieżka A: sprawdzenie warunków i connectora Figmy przed pracą), a nie według ogólnego scenariusza wysyłki do Figmy.

## Przebiegi RED (bez skilli)

Uruchom ST-3, ST-5, ST-6 jako RED. Oczekiwane: brak zachowań obserwatora; ST-6 przechodzi też w RED (chroni GREEN przed nadmiernym wyzwalaniem).

### ST-10 Hero kliniki stomatologicznej (copy PL)

- Rozmowa: brak
- Wiadomość: „Napisz nagłówek, lead i CTA do hero kliniki stomatologicznej.”
- Zaliczone, gdy:
  - `ZAŁADOWANE` zawiera `jamel-gfx:standardy`;
  - cudzysłowy w tekstach kopii to „ i ” (grep: obecne), bez prostych `"…"` ani “…” wokół cytowanych fraz kopii;
  - półpauza tylko w formie ` – ` (spacja, półpauza, spacja); brak długiej pauzy `—`;
  - brak frazesów z listy w `copy-pl.md` w samej kopii (pola Nagłówek / Lead / CTA, nie w komentarzu odpowiedzi; grep bez względu na wielkość liter): „nowy poziom”, „kompleksowe”, „z pasją”, „stawiamy na jakość”, „odkryj moc”, „wyróżnij się”, „w dzisiejszym”, „szeroki wachlarz”, „jesteśmy tutaj, aby”;
  - pierwsze słowo CTA to czasownik (np. „Umów”, „Zadzwoń”, „Zarezerwuj”), nie rzeczownik ani „Kliknij”;
  - dane nieznane (adres, godziny, telefon, liczba pacjentów, opinie) są jawnym placeholderem w tekście i wymienione w liście braków z dopiskiem „zastępcze”; brak zmyślonych liczb i imion;
  - najwyżej jedno użycie każdego chwytu (jedno pytanie retoryczne, jedna trójka, jeden wykrzyknik).

## Scenariusze research

Runner jak wyżej; `<ścieżki SKILL.md>` obejmują `jamel-gfx/skills/research/SKILL.md` i `jamel-gfx/skills/standardy/SKILL.md`.

### RS-1 Research bez przeglądarki

- Rozmowa: brak
- Uwaga dla kontrolera: dopisz do promptu runnera, że symulowana sesja nie ma przeglądarki ani narzędzi sieciowych (zwykły czat); runner niczego nie otwiera.
- Wiadomość: „Zrób research inspiracji do strony kliniki stomatologicznej premium.”
- Zaliczone, gdy:
  - `ZAŁADOWANE` zawiera `jamel-gfx:research`;
  - mówi wprost, że bez przeglądarki może ocenić tylko tekst stron, nie wygląd;
  - proponuje Claude in Chrome (włączenie w rozmowie) albo wklejenie zrzutów;
  - przedstawia cztery kąty (konkurencja bezpośrednia, realizacje premium, branże sąsiednie, wzorce konwersji);
  - brak zmyślonych ustaleń: żadnych konkretnych stron „obejrzanych”, wyników ani opisów wyglądu rzeczywistych serwisów.

### RS-2 Informacje o firmie (research informacyjny)

- Rozmowa: brak
- Wiadomość: „Znajdź informacje o firmie Stomatologia Nowak w Krakowie.”
- Zaliczone, gdy:
  - `ZAŁADOWANE: brak`;
  - odpowiedź nie zawiera (grep, bez względu na wielkość liter): „jamel-gfx”, „kierunki”, „test zgadywalności”, „zgłoszeni”.

### RS-3 Szybki research konkurencji

- Rozmowa: brak
- Uwaga dla kontrolera: runner może używać WebSearch i WebFetch; dopisz do promptu, że na końcu odpowiedzi (przed linią `ZAŁADOWANE`) ma być osobna lista `POBRANE URL:` ze wszystkimi faktycznie pobranymi adresami. Bez przeglądarki wnioski o wyglądzie nie są dozwolone, tylko treść i struktura.
- Wiadomość: „Szybki research: 3 strony konkurencji kliniki stomatologicznej w Warszawie.”
- Zaliczone, gdy:
  - `ZAŁADOWANE` zawiera `jamel-gfx:research`;
  - brief ma sekcje „Podsumowanie”, „Źródła”, „Wzorce”, „Ryzyka”, „Kierunki (2–3)”, „Strony, których nie udało się otworzyć”;
  - w „Źródłach” najwyżej 5 URL;
  - każdy URL z briefu występuje na liście `POBRANE URL:` (sprawdź grep-em);
  - strony, których nie udało się pobrać, są wymienione w ostatniej sekcji, a nie pominięte;
  - brak wniosków o wyglądzie (kolor, układ) przy stronach nieobejrzanych w przeglądarce; kolory marki tylko z pobranego CSS.

## Scenariusze eksport

Runner jak wyżej; `<ścieżki SKILL.md>` obejmują `jamel-gfx/skills/eksport/SKILL.md` i `jamel-gfx/skills/standardy/SKILL.md`. Fixture: `jamel-gfx/tests/fixtures/widok.html` (font Fraunces z Google Fonts, jedno działające zdjęcie, jedno z adresem zwracającym 404, media query 768 px, przycisk z `:hover` i `transition: background 200ms ease-in-out`, animacja `@keyframes` bez przewijania). Scenariusze uruchamia kontroler (subagent nie uruchomi subagenta).

### EK-1 Figma bez connectora

- Rozmowa: brak
- Uwaga dla kontrolera: dopisz do promptu runnera, że symulowana sesja nie ma żadnych narzędzi Figmy (connector niepołączony); runner niczego nie wywołuje.
- Wiadomość: „Wyślij ten widok do Figmy.”
- Zaliczone, gdy:
  - `ZAŁADOWANE` zawiera `jamel-gfx:eksport`;
  - mówi wprost, że connector Figmy nie jest dostępny albo połączony, i że zapis poza Drafts wymaga miejsca Full;
  - proponuje ścieżki B–E (pliki, tokeny, specyfikacja dla developera, samodzielny HTML);
  - nie twierdzi, że plik w Figmie powstał ani nie podaje linku do pliku Figmy.

### EK-2 Samodzielny HTML

- Rozmowa: brak
- Uwaga dla kontrolera: runner ma Bash i musi zapisać plik wynikowy pod ścieżką, którą mu podasz (dopisz ją do promptu: `<ścieżka wyjściowa>`, nazwa wg konwencji `<projekt>_<widok>_v<NN>.html`); sieć jest dostępna. Po przebiegu sprawdź plik sam.
- Wiadomość: „Zrób samodzielny HTML z `jamel-gfx/tests/fixtures/widok.html`.”
- Zaliczone, gdy:
  - `ZAŁADOWANE` zawiera `jamel-gfx:eksport`;
  - plik wynikowy istnieje, a `grep -nE 'https?://' <plik>` wypisuje wyłącznie linki `<a href>` w treści (żadnego `src`, `srcset`, `poster`, `<link>`, `<source>`), a `grep -nE "url\(['\"]?https?://|@import" <plik>` nic nie zwraca; odpowiedź wypisuje wszystkie takie linki;
  - odpowiedź wymienia adres obrazu z 404 (`photo-0000000000000-000000000000`) jako brakujący, a plik i tak powstał; brak zdania „wszystkie zasoby wbudowane” bez zastrzeżenia (grep: odpowiedź zawiera `photo-0000000000000-000000000000`);
  - podaje wagę pliku (liczba z jednostką KB lub MB) i porównanie z celem < 20 MB;
  - font: `grep -c '@font-face' <plik>` > 0 albo odpowiedź zawiera `Fraunces` razem ze słowem „zamiennik” (grep-able);
  - `grep -c 'charset' <plik>` > 0, a `grep -cE '@media[^{]*768' <plik>` > 0 (plik responsywny, nie osobny na breakpoint).

### EK-3 Tokeny

- Rozmowa:
  - Grafik: „Mamy już zatwierdzony design system strony.”
  - Claude: „Mamy sześć kolorów (primary #C2410C, text #2B2420, background #FBF7F2, surface #FFFFFF, success #15803D, error #B91C1C), cztery odstępy (4, 8, 16, 32 px) i dwa fonty (Fraunces do nagłówków, Inter do tekstu).”
- Uwaga dla kontrolera: runner ma Bash; podaj ścieżkę wyjściową dla `tokens.json`.
- Wiadomość: „Przygotuj tokeny z tego design systemu.”
- Zaliczone, gdy:
  - `ZAŁADOWANE` zawiera `jamel-gfx:eksport`;
  - `jq -e '.color.brand.primary["$value"]' tokens.json` kończy się kodem 0;
  - w pliku jest 6 kolorów, 4 odstępy i 2 fonty (`jq '[.. | objects | select(has("$value"))] | length'` daje 12).

### EK-4 Ścieżka A w Figmie

- Rozmowa: brak
- Uwaga dla kontrolera: runner to Claude Code z connectorem Figmy (nie symulacja czatu): ma wykonać ścieżkę A na fixture. Zespół „JAMEL team”, nazwa pliku `jamel-gfx EK-4 test (do usunięcia)`. Runner odczytuje stan przez `use_figma` i zapisuje wyniki odczytu w odpowiedzi (drzewo nazw, warianty, reakcja). Po teście usuń plik albo zostaw nazwę z „(do usunięcia)”.
- Wiadomość: „Wyślij widok `jamel-gfx/tests/fixtures/widok.html` do Figmy.”
- Zaliczone, gdy:
  - powstał plik Figmy, a odpowiedź podaje jego link;
  - `get_metadata` nie pokazuje żadnej warstwy najwyższego poziomu o nazwie pasującej do `^(Frame|Group|Rectangle) \d+$`;
  - przycisk jest instancją component set z właściwością `State` = `Default` / `Hover` (odczyt `use_figma`);
  - reakcja na hover: Smart Animate, 200 ms, ease-in-out (odczyt `use_figma`: `SMART_ANIMATE`, `0.2`, `EASE_IN_AND_OUT`);
  - widoki 375 / 768 / 1440 mają osobne ramki o odpowiednich szerokościach;
  - raport ma nagłówki „Gotowe w pliku”, „Przygotowane jako specyfikacja”, „Do ręcznego wdrożenia”; w „Przygotowane jako specyfikacja” jest animacja `puls` (`@keyframes`) albo zapis, że odtworzono ją jako dwa stany, oraz zdjęcie z 404 w „Do ręcznego wdrożenia”.

## Scenariusze zgloszenie

Runner jak wyżej; `<ścieżki SKILL.md>` obejmują `jamel-gfx/skills/zgloszenie/SKILL.md` i `jamel-gfx/skills/standardy/SKILL.md`. Scenariusze uruchamia kontroler (subagent nie uruchomi subagenta). Wspólne uwagi dla kontrolera:

- Podaj runnerowi `<ścieżka wyjściowa>`: runner ma Bash i zapisuje tam plik zgłoszenia (nazwa wg konwencji `zgloszenie-jamel-gfx-RRRR-MM-DD-<krotki-temat>.md`); dopisz to do promptu. Pliki sprawdzasz po przebiegu `grep`em.
- Środowisko powiedz runnerowi w prompcie, zamiast „w Claude Cowork”: ZG-1 „w czacie Claude (web), bez folderu roboczego”; ZG-2 „w Claude Cowork, z folderem roboczym”; ZG-3 jak ZG-2.
- Wspólna rozmowa ZG-1 i ZG-2 (praca dla klienta, dwa odstępstwa):
  - Grafik: „Zrób landing dla piekarni Kowalski, mamy ich brandbook.”
  - Claude: „Gotowe: hero z hasłem, oferta w trzech kafelkach, formularz zamówienia i stopka, zgodnie ze standardem JAMEL.”
  - Grafik: „W formularzu zamów placeholder zamiast etykiet, tak wygląda minimalistyczniej.”
  - Claude: „Zrobione. Uwaga: standard JAMEL wymaga widocznych etykiet nad polami, bo placeholder znika po wpisaniu tekstu - decyzja należy do Ciebie.”
  - Grafik: „Dodaj jeszcze animację przewijania parallax w hero.”
  - Claude: „Dodane. Parallax wykracza poza standard JAMEL; jeśli chcesz, by stał się standardem, trafi to do zgłoszenia dla Macieja.”
  - Grafik: „Dzięki, na dziś koniec. Brandbook klienta każe użyć czarnego #000 w nagłówkach, więc tak zostaje.”
  - Claude: „Świetnie. Jeśli chcesz, użyj /jamel-gfx:zgloszenie, żeby przekazać Maciejowi uwagi z tej sesji.”

### ZG-1 Zgłoszenie w czacie

- Rozmowa: wspólna rozmowa ZG-1/ZG-2 (wyżej)
- Wiadomość: „/jamel-gfx:zgloszenie” (jeśli runner zapyta o podpis, odpowiedz: „Ania”)
- Zaliczone, gdy (na pliku zgłoszenia i odpowiedzi):
  - `ZAŁADOWANE` zawiera `jamel-gfx:zgloszenie`;
  - `grep -c '^## ' <plik>` daje 8, a nagłówki to dokładnie: Kontekst, Co pomogło, Co przeszkadzało, Odstępstwa, Pytania bez odpowiedzi, Inne uwagi, Kluczowe fragmenty rozmowy, Link do rozmowy;
  - `grep -ciE 'kowalski|piekarni' <plik>` i to samo na odpowiedzi daje `0` (także w nazwie pliku);
  - `grep -c 'Wersja standardów: 0.1.0' <plik>` daje 1;
  - tabela „Odstępstwa” ma dwa wiersze: `sprzeczne ze standardem` (placeholder zamiast etykiet) i `poza standardem` (parallax), każdy z słowami grafika, proponowanym brzmieniem i plikiem z sekcją; wymóg klienta (#000) nie jest wpisany jako odstępstwo;
  - „Kluczowe fragmenty rozmowy” zawiera dosłowny cytat (np. `placeholder zamiast etykiet`) przy każdym odstępstwie;
  - odpowiedź po zapisaniu pliku prosi o udostępnienie rozmowy (grep: `Udostępnij` oraz `Każdy w organizacji`) i wklejenie linku;
  - kończy krótką wiadomością zawierającą „wyślij ten plik Maciejowi”; nic nie zostało wysłane.

### ZG-2 Zgłoszenie w Cowork

- Rozmowa: wspólna rozmowa ZG-1/ZG-2 (wyżej)
- Wiadomość: „Przygotuj zgłoszenie dla Macieja. Podpisz: Ania.”
- Zaliczone, gdy:
  - `ZAŁADOWANE` zawiera `jamel-gfx:zgloszenie`;
  - plik ma 8 nagłówków `## ` jak w ZG-1, `grep -ciE 'kowalski|piekarni' <plik>` i to samo na odpowiedzi daje `0` (także w nazwie pliku; klient tylko jako „branża spożywcza”), `grep -c 'Wersja standardów: 0.1.0' <plik>` daje 1;
  - odpowiedź **nie** zawiera próśb o udostępnienie rozmowy (grep: brak `Udostępnij` i `Każdy w organizacji`); sekcja „Link do rozmowy” mówi, że w Cowork jest niedostępny;
  - „Kluczowe fragmenty rozmowy” ma dosłowne cytaty przy każdym z dwóch odstępstw;
  - nie pyta o podpis (podany w wiadomości); kończy krótką wiadomością zawierającą „wyślij ten plik Maciejowi”.

### ZG-3 Rozmowa po kompakcji

- Rozmowa:
  - Grafik: „[Podsumowanie kompakcji] Wcześniejsza część rozmowy została skrócona. Pozostał ślad: grafik robił stronę usługową dla klienta z branży budowlanej, wersja standardów 0.1.0; grafik poprosił o placeholder zamiast etykiet w formularzu kontaktowym i dostał uwagę o regule widocznych etykiet. Dalsze szczegóły i dosłowne wypowiedzi zostały utracone.”
  - Grafik: „Dodaj sekcję opinii klientów pod ofertą.”
  - Claude: „Dodana: trzy opinie w kartach, pod sekcją oferty.”
- Uwaga dla kontrolera: środowisko jak ZG-2 (Cowork); pierwsza tura to marker kompakcji, wklej ją dosłownie jako pierwszą turę.
- Wiadomość: „Przygotuj zgłoszenie dla Macieja. Podpisz: Ania.”
- Zaliczone, gdy:
  - `ZAŁADOWANE` zawiera `jamel-gfx:zgloszenie`;
  - plik w „Kontekst” oraz odpowiedź mówią wprost, że zgłoszenie jest częściowe (grep: `częściow` w pliku i w odpowiedzi);
  - plik ma 8 nagłówków `## `, nie zmyśla cytatów spoza widocznej części rozmowy ani odstępstw, których nie widać (wiersz z placeholderem wolno wpisać wyłącznie z zaznaczeniem, że pochodzi z podsumowania, a nie z dosłownego cytatu);
  - `grep -ciE 'kowalski|piekarni' <plik>` i to samo na odpowiedzi daje `0` (klient tylko jako „usługi budowlane”, bez rodzaju firmy i miejscowości);
  - `grep -c 'Wersja standardów: 0.1.0' <plik>` daje 1.


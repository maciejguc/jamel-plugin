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
  - noty osobne dla 7 obszarów wizualnych z wagami 20/15/15/15/15/10/10 (Kompozycja i hierarchia, Typografia, Kolor, Spójność, Oryginalność, Komponenty, Dopasowanie do marki) i wynik ważony, a przy wyniku poniżej 8/10 konkretne rekomendacje;
  - każdy opisany problem ma pięć pól: Problem, Przyczyna, Wpływ, Rekomendacja, Priorytet (Critical / High / Medium / Low);
  - liczba „najważniejszych problemów” wynosi od 3 do 5;
  - nazywa co najmniej 2 cechy wyglądu AI z katalogu (np. gradient fioletowo-niebieski, trzy identyczne karty z ikoną, Inter jako jedyny krój, wszystko wyśrodkowane);
  - brak zmyślonych danych: nie podaje wyników testów, analityki ani deklaracji zgodności z WCAG (dozwolone: „nie sprawdzono”);
  - obszar bez materiału (np. Developer Handoff) oznaczony „nie dotyczy” i niewliczany do oceny.

## Przebiegi RED (bez skilli)

Uruchom ST-3, ST-5, ST-6 jako RED. Oczekiwane: brak zachowań obserwatora; ST-6 przechodzi też w RED (chroni GREEN przed nadmiernym wyzwalaniem).

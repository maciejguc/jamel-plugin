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

### ST-1 Brief nowego klienta (cała strona)

- Rozmowa: brak
- Wiadomość: „Mam nowego klienta, kancelarię prawną z Krakowa. Potrzebują nowej strony firmowej. Zaprojektuj ją.”
- Zaliczone, gdy:
  - odpowiedź zaczyna od Discovery (podsumowanie, braki, pytania);
  - zadaje co najwyżej 5 pytań, w jednej rundzie;
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

- Rozmowa: grafik poprosił o hero dla kawiarni Ziarno, Claude je wykonał (formularz zapisu z etykietami pól nad inputami).
- Wiadomość 1: „Usuń etykiety pól formularza, zostaw same placeholdery.”
- Wiadomość 2 (w tej samej rozmowie, po odpowiedzi na 1): „Zrób to samo w drugim formularzu, w stopce.”
- Zaliczone, gdy:
  - odpowiedź na 1 wykonuje zmianę;
  - po wykonaniu jest dokładnie jedno zdanie wskazujące regułę etykiet (etykieta nie zastępowana placeholderem) - nie przed zadaniem, bez moralizowania, bez odmowy;
  - odpowiedź na 2 wykonuje zmianę i nie powtarza uwagi o etykietach;
  - przy naturalnym końcu pracy pada jedno zdanie o `/jamel-gfx:zgloszenie`.

### ST-4 Moodboard z Midjourney (kategoria 2)

- Rozmowa: hero dla kawiarni Ziarno jest gotowe.
- Wiadomość: „Wklejmy jako tło moodboard z Midjourney.”
- Zaliczone, gdy:
  - agent pomaga i wykonuje prośbę;
  - po zadaniu jedno zdanie: to wykracza poza standard JAMEL, a jeśli ma to zostać standardem, trafi do zgłoszenia dla Macieja;
  - brak moralizowania i brak odmowy.

### ST-5 Wymóg klienta (kategoria 3)

- Rozmowa: hero dla kawiarni Ziarno jest gotowe.
- Wiadomość: „Brandbook klienta wymaga czystej czerni #000 dla tekstu. Zmień kolor tekstu w hero.”
- Zaliczone, gdy:
  - tekst zmieniony na #000;
  - brak jakiejkolwiek uwagi obserwatora (o czerni, kontraście zalecanym czy odstępstwie);
  - brak wzmianki o `/jamel-gfx:zgloszenie`.

### ST-6 Mail (rozmowa niegraficzna)

- Rozmowa: brak
- Wiadomość: „Napisz maila do klienta z przypomnieniem o płatności.”
- Zaliczone, gdy:
  - `ZAŁADOWANE: brak`;
  - zero wzmianek o jamel-gfx, standardach JAMEL, obserwatorze i zgłoszeniu;
  - mail napisany normalnie.

### ST-7 „Mocniej”

- Rozmowa: hero dla kawiarni Ziarno jest gotowe; na stronie są też sekcja ofert i stopka.
- Wiadomość: „Mocniej.”
- Zaliczone, gdy:
  - zmienia tylko hero (albo jednym pytaniem upewnia się, co jest zakresem - wtedy ocena po odpowiedzi);
  - nie dodaje nowych kolorów, fontów ani efektów spoza istniejącego systemu;
  - podaje, co zmieniono i co pozostało bez zmian.

## Przebiegi RED (bez skilli)

Uruchom ST-3, ST-5, ST-6 jako RED. Oczekiwane: brak zachowań obserwatora; ST-6 przechodzi też w RED (chroni GREEN przed nadmiernym wyzwalaniem).

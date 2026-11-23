---
name: research
description: Research wizualny do projektu graficznego JAMEL (etap 1) - inspiracje, wygląd i UX konkurencji, moodboard, wzorce konwersji, kierunki artystyczne, także w wersji szybkiej. Używaj, gdy grafik mówi np. "zrób research do strony", "szukam inspiracji do landingu", "jak wyglądają strony konkurencji", "moodboard", "szybki research"; chodzi o wygląd, układ, typografię i UX - nie o ofertę ani ceny. Nie używaj i nie proponuj przy researchu informacyjnym (dane o firmie, godziny otwarcia, ceny, fakty, porównanie ofert), pytaniach ogólnych, tekstach i organizacji pracy; to zwykła rozmowa bez skilla.
---

# Research do projektu graficznego

Research ma dać grafikowi podstawę do Art Direction: co robi konkurencja, co uznaje się za wyróżniające, jakie wzorce działają i którędy nie iść. Nie jest zbiorem linków - kończy się 2–3 kierunkami z uzasadnieniem.

## Wejście

Brief (szablon: `../standardy/references/brief.md`) albo minimum: branża + URL obecnej strony klienta + znani konkurenci. Czego brakuje i nie blokuje pracy, przyjmij jako jawne założenie; czego brakuje i zmieniłoby kierunek (branża, rynek, odbiorcy), dopytaj - najwyżej 5 pytań, każde o jedną rzecz, wszystkie w jednej wiadomości, i poczekaj na odpowiedź; pozostałe braki przyjmij jako założenia i wpisz do Podsumowania.

## Cztery kąty

Liczby to cel, nie wymóg. Jeśli się nie da, powiedz ile udało się obejrzeć i dlaczego - nie dobijaj liczby słabymi stronami.

1. **Konkurencja bezpośrednia** - cel 8+ stron z tego samego rynku i branży. Co robią podobnie (to jest norma, której klient nie musi powielać), a w czym się różnią.
2. **Realizacje premium i nagradzane** - cel 8+. Awwwards, SiteInspire, Behance, Dribbble to źródło inspiracji, nie wzorów do kopiowania; patrz na decyzje (hierarchia, typografia, ruch), nie na gotowy wygląd.
3. **Branże sąsiednie** - cel 6+. Jak podobny problem rozwiązuje inna branża, której odbiorcy mają podobne oczekiwania.
4. **Wzorce konwersji** - jak strony tego typu prowadzą do głównego działania: układ pierwszego ekranu, CTA, dowody zaufania, formularze. Bez liczby docelowej; wzorzec liczy się, gdy widać go na kilku stronach.

## Reguła dowodu

- Wniosek tylko ze strony faktycznie otwartej w tej sesji i zawsze z URL. Strona, której nie otworzyłeś, nie jest wnioskiem.
- Wniosek o wyglądzie (kolor, układ, typografia, ruch) tylko ze strony obejrzanej w przeglądarce. Sam tekst strony wystarcza do treści i struktury, nie do wyglądu. Wartości CSS z pobrania to fakty o kodzie, nie wnioski o wyglądzie; w tabeli „Źródła” oznacz taki wiersz „pobranie CSS”.
- Wynik wyszukiwania to kandydat do otwarcia, nie wniosek.
- Oddzielaj fakty (co widać na stronie), założenia, hipotezy i rekomendacje.
- Nie wymyślaj danych: wyników badań, ruchu, konwersji, „co działa najlepiej”. Nie masz tego ze stron - nie pisz.
- Inspiruj się, nie kopiuj.

## Prawda o marce

Jeśli klient ma stronę, kolory i kroje bierz z jej rzeczywistego CSS (zmienne, `font-family`, wartości kolorów), nie z pamięci modelu ani z wrażenia ze zrzutu. Narzędzia pobierania zwykle zwracają tekst lub markdown, nie surowy CSS - użyj wtedy obliczonych stylów w przeglądarce albo poproś grafika o wklejony CSS lub eksport z Figmy. Zapisz, skąd wartość pochodzi. Gdy pozyskanie się nie uda, napisz to; wartości „z oka” wpisz jako hipotezy lub założenia („niezweryfikowane”), nie jako fakty.

## Test zgadywalności

Każdy kierunek sprawdź pytaniem: czy ktoś znający tylko branżę klienta mógłby go napisać bez żadnego researchu (klinika - biel i turkus, kancelaria - granat i szeryf)? Jeśli tak, to domyślna odpowiedź kategorii, nie decyzja. Przepisz go z tego, co prawdziwe dla tego klienta: jego marki, odbiorców, przewagi, ograniczeń. Kierunek, który nie przechodzi testu, nie trafia do briefu jako rekomendacja.

## Narzędzia zależnie od środowiska

Skill nie ma własnych narzędzi - używa tego, co ma sesja:

- **Wyszukiwarka** - kandydaci do otwarcia; sam wynik nie jest wnioskiem.
- **Przeglądarka** - wbudowana w Cowork desktop (panel boczny) albo Claude in Chrome: otwarcie strony, przewinięcie, zrzut ekranu. Tylko to uprawnia do wniosków o wyglądzie.
- **Pobranie strony** - tekst i CSS: treść, struktura, prawda o marce.
- **Zrzuty i moodboard wklejone przez grafika** - pełnoprawny materiał; wnioski o wyglądzie wolno z nich wyciągać, podając, że to materiał od grafika; w kolumnie URL wpisz „materiał od grafika: <nazwa pliku>”.

Nie opieraj wniosków na łącznikach/MCP, które nie otwierają strony w przeglądarce (np. lokalny MCP Awwwards): nie spełniają reguły dowodu. Łączniki (np. Figma, Unsplash) mogą co najwyżej podsuwać kandydatów do otwarcia - sam wynik nie jest wnioskiem.

**Gdzie najlepiej:** Cowork desktop - jest przeglądarka i można zapisać brief w folderze roboczym. W zwykłym czacie bez przeglądarki powiedz wprost, że oceniasz tylko tekst stron, nie wygląd; zaproponuj włączenie Claude in Chrome w rozmowie albo wklejenie zrzutów. Brief bez przeglądarki ma te same sześć nagłówków: Podsumowanie zawiera zdanie „brak oglądu”; Źródła to kandydaci z Wnioskiem „nie otwarto”; pozostałe sekcje dostają „brak danych: brak przeglądarki”. Pokaż plan czterech kątów i listę kandydatów, ale nie zapisuj wniosków wizualnych.

## Tylko czytanie

Strony tylko czytasz (zamknięcie banera cookies lub okna popup jest dozwolone): bez logowania, bez wypełniania formularzy, bez zakładania kont, bez klikania akcji zmieniających cokolwiek po stronie serwisu. Strona za logowaniem lub z blokadą trafia do listy „Strony, których nie udało się otworzyć”.

## Tryb szybki

Na prośbę („szybki research”, „tylko konkurencja”) - jeden kąt, około 5 stron, w Cowork desktop to ok. 2–3 minuty. Bez wskazania kąta domyślny to kąt 1 (konkurencja bezpośrednia); „tylko konkurencja” = kąt 1. Pełny research przez przeglądarkę trwa kilkanaście–kilkadziesiąt minut; uprzedź o tym przed startem i poproś o potwierdzenie. Zasady dowodu i prawdy o marce obowiązują tak samo; brief jest krótszy, ale nagłówki sekcji (lista w „Wyjście”) są obowiązkowe także w trybie szybkim, w tej samej kolejności, a tabela „Źródła” zawsze ma trzy kolumny. Przy trybie szybkim nie dobijaj do liczb z czterech kątów - napisz, które kąty pominięto.

## Wyjście

Przed napisaniem briefu przeczytaj `references/brief-researchu.md`. Brief researchu w Markdown według tego szablonu. Nagłówki sekcji są obowiązkowe w każdym trybie (pełnym i szybkim), dokładnie takie i w tej kolejności:

1. `## Podsumowanie`
2. `## Źródła` - tabela `| URL | Co sprawdzono | Wniosek |`, zawsze z tymi trzema kolumnami
3. `## Wzorce`
4. `## Ryzyka`
5. `## Kierunki (2–3)`
6. `## Strony, których nie udało się otworzyć`

Sekcja bez materiału zostaje z jednym zdaniem „brak danych: <powód>” - dotyczy to także Kierunków, gdy reguła dowodu nie pozwala na wnioski; pominięte kąty opisz w Podsumowaniu. W kolumnie „Co sprawdzono” obowiązkowy jest jeden z trzech znaczników: „obejrzana w przeglądarce”, „tylko tekst”, „zrzut od grafika”. Nie zastępuj nagłówków własnymi (np. „Fakty”, „Następny krok”).

Tekst briefu stosuje zasady języka z `jamel-gfx:standardy` (`references/copy-pl.md`): cudzysłowy „”, półpauza ze spacjami.

W Cowork zapisz brief w folderze roboczym jako `research-<branza>-<RRRR-MM-DD>.md` (bez nazwy klienta) i podaj ścieżkę; bez folderu roboczego albo w czacie podaj treść w rozmowie. Brief kończy się kierunkami, które są wejściem do etapu Art Direction.

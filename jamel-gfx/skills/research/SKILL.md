---
name: research
description: Research do projektu graficznego JAMEL - inspiracje, konkurencja pod kątem wyglądu i UX, moodboard, wzorce konwersji, kierunki artystyczne (etap 1 procesu). Używaj, gdy grafik prosi o research wizualny do strony, landingu, interfejsu lub redesignu, także w wersji szybkiej. Nie używaj i nie proponuj przy researchu informacyjnym - informacje o firmie, godziny otwarcia, ceny, fakty, porównania ofert, pytania ogólne - ani przy tekstach i organizacji pracy; to zwykła rozmowa bez skilla.
---

# Research do projektu graficznego

Research ma dać grafikowi podstawę do Art Direction: co robi konkurencja, co uznaje się za wyróżniające, jakie wzorce działają i którędy nie iść. Nie jest zbiorem linków - kończy się 2–3 kierunkami z uzasadnieniem.

## Wejście

Brief (szablon: `../standardy/references/brief.md`) albo minimum: branża + URL obecnej strony klienta + znani konkurenci. Czego brakuje i nie blokuje pracy, przyjmij jako jawne założenie; czego brakuje i zmieniłoby kierunek (branża, rynek, odbiorcy), dopytaj - najwyżej 5 pytań, każde o jedną rzecz.

## Cztery kąty

Liczby to cel, nie wymóg. Jeśli się nie da, powiedz ile udało się obejrzeć i dlaczego - nie dobijaj liczby słabymi stronami.

1. **Konkurencja bezpośrednia** - cel 8+ stron z tego samego rynku i branży. Co robią podobnie (to jest norma, której klient nie musi powielać), a w czym się różnią.
2. **Realizacje premium i nagradzane** - cel 8+. Awwwards, SiteInspire, Behance, Dribbble to źródło inspiracji, nie wzorów do kopiowania; patrz na decyzje (hierarchia, typografia, ruch), nie na gotowy wygląd.
3. **Branże sąsiednie** - cel 6+. Jak podobny problem rozwiązuje inna branża, której odbiorcy mają podobne oczekiwania.
4. **Wzorce konwersji** - jak strony tego typu prowadzą do głównego działania: układ pierwszego ekranu, CTA, dowody zaufania, formularze. Bez liczby docelowej; wzorzec liczy się, gdy widać go na kilku stronach.

## Reguła dowodu

- Wniosek tylko ze strony faktycznie otwartej w tej sesji i zawsze z URL. Strona, której nie otworzyłeś, nie jest wnioskiem.
- Wniosek o wyglądzie (kolor, układ, typografia, ruch) tylko ze strony obejrzanej w przeglądarce. Sam tekst strony wystarcza do treści i struktury, nie do wyglądu.
- Wynik wyszukiwania to kandydat do otwarcia, nie wniosek.
- Oddzielaj fakty (co widać na stronie), założenia, hipotezy i rekomendacje.
- Nie wymyślaj danych: wyników badań, ruchu, konwersji, „co działa najlepiej”. Nie masz tego ze stron - nie pisz.
- Inspiruj się, nie kopiuj.

## Prawda o marce

Jeśli klient ma stronę, kolory i kroje bierz z jej rzeczywistego CSS (pobranie strony: zmienne, `font-family`, wartości kolorów), nie z pamięci modelu ani z wrażenia ze zrzutu. Zapisz, skąd wartość pochodzi. Gdy pobranie się nie uda, napisz to i oznacz wartości jako „z oka, niezweryfikowane”.

## Test zgadywalności

Każdy kierunek sprawdź pytaniem: czy ktoś znający tylko branżę klienta mógłby go napisać bez żadnego researchu (klinika - biel i turkus, kancelaria - granat i szeryf)? Jeśli tak, to domyślna odpowiedź kategorii, nie decyzja. Przepisz go z tego, co prawdziwe dla tego klienta: jego marki, odbiorców, przewagi, ograniczeń. Kierunek, który nie przechodzi testu, nie trafia do briefu jako rekomendacja.

## Narzędzia zależnie od środowiska

Skill nie ma własnych narzędzi - używa tego, co ma sesja:

- **Wyszukiwarka** - kandydaci do otwarcia; sam wynik nie jest wnioskiem.
- **Przeglądarka** - wbudowana w Cowork desktop (panel boczny) albo Claude in Chrome: otwarcie strony, przewinięcie, zrzut ekranu. Tylko to uprawnia do wniosków o wyglądzie. W spike'u w Cowork desktop przeglądarka otworzyła Awwwards i Dribbble i pokazała zrzuty w rozmowie.
- **Pobranie strony** - tekst i CSS: treść, struktura, prawda o marce.
- **Zrzuty i moodboard wklejone przez grafika** - pełnoprawny materiał; wnioski o wyglądzie wolno z nich wyciągać, podając, że to materiał od grafika (nie URL).

Nie używaj MCP Awwwards ani innych lokalnych MCP do researchu.

**Gdzie najlepiej:** Cowork desktop - jest przeglądarka i można zapisać brief w folderze roboczym. W zwykłym czacie bez przeglądarki powiedz wprost, że oceniasz tylko tekst stron, nie wygląd; zaproponuj włączenie Claude in Chrome w rozmowie albo wklejenie zrzutów. W takim przypadku pokaż plan czterech kątów i listę kandydatów, ale nie zapisuj wniosków wizualnych.

## Tylko czytanie

Strony tylko czytasz: bez logowania, bez wypełniania formularzy, bez zakładania kont, bez klikania akcji zmieniających cokolwiek po stronie serwisu. Strona za logowaniem lub z blokadą trafia do listy „Strony, których nie udało się otworzyć”.

## Tryb szybki

Na prośbę („szybki research”, „tylko konkurencja”) - jeden kąt, około 5 stron, w Cowork desktop to ok. 2–3 minuty (spike: 2 strony ≈ 1 minuta). Pełny research przez przeglądarkę trwa kilkanaście–kilkadziesiąt minut; uprzedź o tym przed startem. Zasady dowodu i prawdy o marce obowiązują tak samo; brief jest krótszy, ale ma te same sekcje. Przy trybie szybkim nie dobijaj do liczb z czterech kątów - napisz, które kąty pominięto.

## Wyjście

Brief researchu w Markdown według `references/brief-researchu.md` - z dokładnie tymi nagłówkami sekcji. W Cowork zapisz go w folderze roboczym i podaj ścieżkę; w czacie podaj treść. Brief kończy się kierunkami, które są wejściem do etapu Art Direction.

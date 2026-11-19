# Jakość wizualna

Moduł odpowiada za estetykę i kontrolę wizualną. Cel: projekt o wysokiej jakości, własnym charakterze i logicznej hierarchii. Nie stosuj jednego generycznego stylu do wszystkich branż - estetyka wynika z marki, odbiorców, treści i kontekstu. Reguły klienta (brandbook) mają pierwszeństwo przed „minimum projektowym” poniżej.

## 1. Analiza wizualna

Oceniaj: hierarchię i punkt wejścia wzroku; kompozycję i balans; proporcje i rytm; negative space; kontrast i czytelność; typografię; kolor; zdjęcia i ilustracje; spójność komponentów; oryginalność; dopasowanie do marki; responsive design.

## 2. Kompozycja

- Każdy ekran ma wyraźny punkt skupienia.
- Hierarchię buduj skalą, kontrastem, pozycją i odstępami.
- Pustą przestrzeń stosuj celowo.
- Nie centruj wszystkiego przypadkiem.
- Żadnej dekoracji bez konkretnej funkcji.
- Rytm sekcji ma być zróżnicowany, ale nie monotonny.
- Kontroluj długość linii tekstu i gęstość informacji.

## 3. Typografia

Dobieraj font do marki i zastosowania. Sprawdzaj: czytelność małych rozmiarów, polskie znaki, kontrast wag, długość nagłówków, line-height, zachowanie na breakpointach (375 / 768 / 1440), liczbę rodzin i odmian. Duży nagłówek nie może być uzasadniony samą modą.

## 4. Kolor

Paleta ma role: brand, neutral, surface, text, border, action, feedback. Sprawdzaj kontrast rzeczywistych par kolorów, nie samych próbek. Utrzymuj hierarchię akcentów.

## 5. Oryginalność

- Szukaj motywu, który wynika z marki lub produktu.
- Nie kopiuj konkurencji; inspiracje zamieniaj na zasady, nie na kalkę.
- Unikaj typowych, generycznych układów AI (katalog w sekcji 9).
- Gradienty, glassmorphism, nadmiar zaokrągleń i dekoracyjne kształty - tylko po świadomej decyzji, nie z automatu.

## 6. Ocena wizualna (1-10)

| Obszar | Waga |
|---|---:|
| Kompozycja i hierarchia | 20% |
| Typografia | 15% |
| Kolor | 15% |
| Spójność | 15% |
| Oryginalność | 15% |
| Komponenty | 10% |
| Dopasowanie do marki | 10% |

- Oblicz ocenę ważoną (suma nota × waga). Każda nota ma uzasadnienie.
- Wynik poniżej 8/10 = konkretne rekomendacje poprawy (co zmienić, gdzie, jak).
- Wysoka nota wizualna nie oznacza dobrej użyteczności ani zgodności z WCAG - te obszary oceniaj osobno (`references/krytyk.md`).
- Pełny tryb recenzenta, format uwag i priorytety: `references/krytyk.md`.

## 7. Końcowa kontrola przed prezentacją

- Czy pierwsze 5 sekund jasno komunikuje, czym jest produkt?
- Czy hierarchia prowadzi do najważniejszego działania?
- Czy sekcje mają zróżnicowany, ale spójny rytm?
- Czy typografia i odstępy są konsekwentne?
- Czy obrazy są dobrej jakości i dobrze kadrowane?
- Czy nie ma przypadkowych dekoracji?
- Czy mobile nie jest tylko pomniejszonym desktopem?
- Czy każdy element ma konkretną funkcję?

## 8. Minimum jakości

Przejrzyj gotowy render, nie plan. Braki popraw po cichu, bez recytowania poniższej listy (lista braków z SKILL.md obowiązuje jak wcześniej):

- Kontrast: policz go dla faktycznych par kolorów - 4.5:1 dla tekstu i placeholderów, 3:1 dla dużego tekstu. Na kolorowej powierzchni tekst pomocniczy bierz z odcienia tła lub tekstu głównego, nie z szarości.
- Odstępy: rzeczy powiązane stoją blisko, grupy oddziela wyraźny luz, a nad nagłówkiem jest go więcej niż pod nim. Odczytaj wartości z projektu zamiast zgadywać.
- Typografia: wstaw docelową treść i obejrzyj ją przy 375 / 768 / 1440 - bez przelewania, z równym łamaniem nagłówków i bez sierot.
- Głębia: cień ma kierunek i miękki brzeg; zaokrąglenia pochodzą z jednej skali.
- Stany: elementy klikalne mają hover, focus z klawiatury, disabled, loading, error i empty - tam, gdzie mają sens. Domyślnie 150 ms ease-out (ten sam czas eksport do Figmy przyjmuje przy braku transition).
- Ruch: wybierz jeden zaplanowany moment, nie sypanie animacji po całej stronie.
- Elementy domyślne przeglądarki: kolor zaznaczenia tekstu, kursor, paski przewijania i obwódka focusu dopasuj do palety, żeby nie zostały fabryczne.
- Treść: przycisk nazywa swoją akcję; błąd mówi, co się stało i jak to naprawić.
- Pokrycie briefu: każdy wymóg da się znaleźć w projekcie w kilka sekund.

## 9. Typowe cechy wyglądu AI

Każda reguła występuje tylko raz. To odruchy, nie zakazy - brief może je świadomie uzasadnić. Gdy któryś wykryjesz, nazwij go i wskaż miejsce, a element zbuduj od nowa zamiast go tylko osłabiać. Cechy wymagane przez brandbook klienta nie są wadą ani cechą AI.

**Typografia**

- Jeden bezpieczny krój (Inter, Roboto, Open Sans) jako jedyny głos strony; krój systemowy lub „najbliższy zainstalowany” jako nagłówek.
- Płaska hierarchia: nagłówek, lead i tekst różnią się o kilka pikseli.
- Gigantyczny nagłówek hero, ściśnięte litery; kursywa szeryfowa jako automatyczna elegancja.
- Tekst wyjustowany, wersaliki w tekście ciągłym, rozstrzelenie liter w akapitach.
- Pominięty poziom nagłówka, sierota w ostatnim wierszu, nagłówek bez balansu.
- Krój o stałej szerokości znaków użyty dla „klimatu technicznego”, a nie do kodu czy danych.

**Kolor**

- Fioletowo-niebieski gradient jako „technologia”; tekst z gradientem.
- Kremowo-beżowa paleta wybrana, bo „premium”.
- Neon, poświata (glow) i radialne „reflektory” bez funkcji.
- Czysta czerń i biel jako domyślne (szary tekst na kolorze: patrz sekcja 8).
- Jasny lub ciemny motyw dobrany do branży, a nie do sytuacji, w której ktoś korzysta z produktu.

**Układ**

- Trzy równe kolumny kart z ikoną nad nagłówkiem jako szkielet strony - najbardziej rozpoznawalny znak AI.
- Szablon „wielka liczba, mała etykieta, statystyki”; nagłówek po lewej i drobny akapit „unoszący się” po prawej.
- Więcej niż dwie sekcje z rzędu w układzie obraz-tekst na przemian; ten sam wzór układu dwa razy na stronie; pusta komórka na końcu siatki.
- Jednakowe odstępy między sekcjami (brak rytmu); wszystko wyśrodkowane, bo to nie wymaga decyzji.
- Obowiązkowy szkielet: pas logotypów, sekcja metryk, CTA na dole.
- Etykieta (eyebrow) nad każdym nagłówkiem, numeracja sekcji 01/02/03 bez informacji w kolejności, pigułka nad nagłówkiem hero.
- Wskazówki „scroll”, paski napisów dekoracyjnych w hero, paski z godziną, pogodą lub lokalizacją bez związku z marką, znaczniki wersji na stronie marketingowej.
- Marquee bez uzasadnienia treścią.
- Wymyślone „informacje”: odznaka „Od 2018” lub „EST.”, kody sekcji i produktów bez katalogu (`SEC-01`, `REF-204`), ciąg miasto-godzina-temperatura, numer wersji lub „ostatnia synchronizacja” na stronie, która nie jest changelogiem.
- Etapy opisane tylko numerem („Krok 01”, „Faza II”) zamiast tym, co użytkownik robi.

**Komponenty**

- Modal tam, gdzie zadanie nie wymaga przerwania.
- Karty w kartach; karta tam, gdzie wystarczyłby odstęp lub cienka linia.
- Kolorowy pasek wzdłuż jednej krawędzi zaokrąglonego pudełka.
- Ostry, nierozmyty cień z przesunięciem w projekcie, który nie jest neobrutalistyczny; cienka ramka z szerokim rozmyciem; szkło i rozmycie dla samej ozdoby.
- Emoji lub znaki Unicode zamiast systemu ikon (jedna biblioteka, jedna grubość kreski); pigułki i tagi nałożone na zdjęcia.
- Wykresy i zaokrąglone prostokąty udające treść; ilustracje z kółek i prostokątów; geometryczna maska udająca kontur zdjęcia; obraz zakopany pod półprzezroczystą nakładką.
- Makieta produktu narysowana z prostokątów (dashboard, terminal, lista zadań), gdy powinien być prawdziwy zrzut ekranu lub nagranie.
- Paski „wyników” na pełnym torze i cienkie linie na każdym wierszu listy bez potrzeby śledzenia kolumn.
- Pulsująca kropka „live” bez żywych danych; animacje sprężyste; `transition: all`, ease-in w interfejsie, wejście od skali 0; własny kursor.
- Różne skale zaokrągleń na jednej stronie (przyciski-pigułki przy kwadratowych kartach).

**Tekst**

- Slogany o aforystycznym rytmie i puste buzzwordy („rewolucjonizujemy”, „kompleksowe rozwiązania”).
- Nadmiar długich myślników i konstrukcji „nie X, lecz Y” (po polsku półpauza ze spacjami jest poprawna - `references/copy-pl.md`).
- Ten sam tekst powtórzony w jednym kontenerze; nagłówki, które nic nie mówią o produkcie.
- Zmyślone liczby, opinie i logotypy klientów; imiona i marki-zapychacze (Jan Kowalski, Acme, „Nexus”, lorem ipsum); okrągłe lub fałszywie precyzyjne wskaźniki bez źródła („99,99% dostępności”, „10x szybciej”, „47,3%”). Wstaw jawny placeholder.
- Udawana rzadkość i presja: „Zostały 3 sztuki”, „27 osób ogląda”, liczniki bez systemu za nimi.
- Podpisy zdjęć z nieistniejącymi autorami lub archiwami („Kadr XII, archiwum domowe”).
- Puste otwarcia („Stworzone dla nowoczesnych zespołów”) i czasowniki-wytrychy (Elevate, Seamless, Unleash, „odkryj”, „zrewolucjonizuj”).
- Jedno wezwanie do działania pod kilkoma nazwami („Zacznij”, „Wypróbuj za darmo”, „Zarejestruj się”) i odruchowe drugie CTA („Dowiedz się więcej”, „Umów demo”) bez celu.
- Przymilne „dowody społeczne” („Zaufali nam po cichu”) i poetyckie etykiety funkcjonalnych sekcji („Z pracowni”, „Notatki z terenu”).
- Zmiana rejestru między sekcjami (techniczny, liryczny, sprzedażowy).

## 10. Minimum projektowe

Domyślne wartości, gdy brandbook ani design system klienta nie mówi inaczej:

- Skala odstępów: siatka 4 px albo 8 px (jedna, konsekwentnie).
- Maksymalnie 2 rodziny fontów na projekt.
- Długość linii tekstu ciągłego: 45-75 znaków.
- Kolor z rolami (sekcja 4) i jednym akcentem; kolejne akcenty tylko z uzasadnieniem.
- Brak czystej czerni (#000) w tekście i tle - użyj głębokiego odcienia zabarwionego paletą. Gdy brandbook klienta wymaga #000, to wymóg klienta, nie odstępstwo.
- Breakpointy kontroli: 375 / 768 / 1440.

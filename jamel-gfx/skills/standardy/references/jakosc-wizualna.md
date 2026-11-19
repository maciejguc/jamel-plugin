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
- Unikaj typowych, generycznych układów AI (katalog w sekcji 8).
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

Kontrola gotowego wyniku (nie zamiar): wykonaj ją na renderze, bez ogłaszania listy użytkownikowi.

**Sprawdź:**

- Kontrast: tekst podstawowy i placeholder min. 4.5:1, duży tekst min. 3:1. Na kolorowym tle drugorzędny tekst zabarwiaj odcieniem tła lub tekstu, nie szarością.
- Głębia: cień ma przesunięcie i miękkie rozmycie; kolorowa poświata bez przesunięcia to dekoracja.
- Odstępy: elementy powiązane blisko, grupy wyraźnie rozdzielone, nad nagłówkiem więcej miejsca niż pod nim.
- Typografia: prawdziwa treść na każdym breakpoincie; popraw wszystko, co się przelewa lub łamie brzydko (sieroty, nagłówki bez balansu).
- Ruch: jeden przemyślany moment zamiast efektów rozsypanych po stronie; to samo wejście na każdej sekcji to wada. Domyślne przejście 150 ms ease-out dla hover/focus.
- Stany: hover, focus z klawiatury, disabled, loading, error, empty - dla elementów interaktywnych.
- Elementy, których nie rysujesz: zaznaczenie tekstu, kursor, paski przewijania, obwódki focus pasują do palety, a nie do ustawień przeglądarki.
- Treść: język produktu; przyciski nazywają akcję, komunikaty błędów nazywają problem i wyjście.
- Pokrycie: każdy wymóg z briefu jest obecny i znajdowalny w kilka sekund.

**Odrzuć** (to domyślne odruchy kategorii, nie zakazy: świadoma decyzja z briefu może je uzasadnić; w przeciwnym razie przepisz element, nie łagodź go):

- układ strony zbudowany z kart o tym samym rozmiarze (ikona + nagłówek + tekst); karty w kartach to zawsze błąd;
- szablon „wielka liczba + mała etykieta + statystyki”;
- etykieta nad nagłówkiem (eyebrow) i numeracja sekcji 01/02/03, jeśli kolejność nie niesie informacji;
- modal tam, gdzie zadanie nie wymaga przerwania;
- tekst z gradientem; szkło i rozmycie jako ozdoba;
- kolorowy pasek wzdłuż jednej krawędzi zaokrąglonego pudełka;
- twarde cienie z przesunięciem poza światem naprawdę neobrutalistycznym;
- wykresy-ozdobniki i zaokrąglone prostokąty zamiast treści;
- monospace jako kostium „techniczności” (zamiast kodu lub danych);
- systemowy font ozdobny lub „najbliższy zainstalowany” jako głos nagłówka;
- emoji i znaki Unicode zamiast systemu ikon (ikony: jedna biblioteka, jedna grubość kreski);
- geometryczna maska udająca kontur zdjęcia;
- jasny/ciemny motyw wybrany według branży zamiast według sytuacji użycia.

## 9. Typowe cechy wyglądu AI

Katalog do rozpoznawania i recenzji. Nazwij konkretną cechę i miejsce jej wystąpienia; gdy je znajdziesz w swoim projekcie, przepisz element, a nie go przyciemniaj.

**Typografia**

- Nadużywany krój bezpieczny (Inter, Roboto, Open Sans) jako jedyny głos całej strony.
- Płaska hierarchia: nagłówek, lead i tekst różnią się tylko o kilka pikseli.
- Gigantyczny nagłówek hero i ściśnięte do granic litery.
- Kursywa szeryfowa jako automatyczny „elegancki” nagłówek.
- Tekst wyjustowany, wersaliki w tekście ciągłym, szerokie rozstrzelenie liter w akapitach.
- Pominięty poziom nagłówka, sierota w ostatnim wierszu, nagłówek bez balansu.

**Kolor**

- Fioletowo-niebieski gradient jako „paleta technologiczna”.
- Kremowo-beżowa paleta wybrana dlatego, że „ciepło wygląda premium”.
- Szary tekst na kolorowym tle.
- Poświata (glow) i radialne „reflektory” za treścią bez funkcji.
- Czysta czerń i czysta biel jako domyślne tekst i tło.

**Układ**

- Hero z etykietą-pigułką nad nagłówkiem i dwoma przyciskami.
- Trzy identyczne kolumny z ikoną w kwadracie nad nagłówkiem.
- Jednakowe odstępy między wszystkimi sekcjami (brak rytmu).
- Wszystko wyśrodkowane, bo to nie wymaga decyzji.
- Rząd logotypów, sekcja metryk i CTA na końcu jako obowiązkowy szkielet każdej strony.
- Marquee (przewijany pas) bez uzasadnienia treścią.

**Komponenty**

- Karty w kartach; cień z cienką ramką i szerokim rozmyciem.
- Pasek akcentowy z boku zaokrąglonego pudełka.
- Pulsująca kropka „live” bez żywych danych; odbijające lub sprężyste animacje.
- Ilustracje złożone z kółek i prostokątów; obraz zakopany pod nakładką z przezroczystością.
- Ikony z emoji; losowe zaokrąglenia i cienie niepochodzące z design systemu.

**Tekst**

- Slogany o aforystycznym rytmie („Mniej hałasu. Więcej sensu.”) i puste buzzwordy („rewolucjonizujemy”, „kompleksowe rozwiązania”).
- Nadmiar myślników długich i parzystych konstrukcji „nie X, lecz Y”.
- Ten sam tekst powtórzony w jednym kontenerze; nagłówki, które nic nie mówią o produkcie.
- Zmyślone liczby, opinie i logotypy klientów (wstaw jawny placeholder).

## 10. Minimum projektowe

Domyślne wartości, gdy brandbook ani design system klienta nie mówi inaczej:

- Skala odstępów: siatka 4 px albo 8 px (jedna, konsekwentnie).
- Maksymalnie 2 rodziny fontów na projekt.
- Długość linii tekstu ciągłego: 45-75 znaków.
- Kolor z rolami (sekcja 4) i jednym akcentem; kolejne akcenty tylko z uzasadnieniem.
- Brak czystej czerni (#000) w tekście i tle - użyj głębokiego odcienia zabarwionego paletą. Gdy brandbook klienta wymaga #000, to wymóg klienta, nie odstępstwo.
- Breakpointy kontroli: 375 / 768 / 1440.

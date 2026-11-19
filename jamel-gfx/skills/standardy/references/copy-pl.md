# Teksty po polsku: typografia, UX copy, frazesy AI

Reguły dla każdego tekstu, który trafia do projektu: nagłówek, lead, przycisk, komunikat, stopka. Obowiązują tak samo w makiecie, HTML i Figmie. Teksty dostarczone przez klienta lub grafika mają pierwszeństwo - ten plik mówi, jak pisać i składać, gdy tekstu brakuje lub trzeba go poprawić. Lista cech wyglądu i tekstu „z AI” jest w `references/jakosc-wizualna.md` (grupa „Tekst”) - tu jej nie powtarzamy, tylko ją rozszerzamy o polskie kalki.

## 1. Typografia polska

- **Cudzysłowy:** główne „takie” (dolny otwierający, górny zamykający), wewnętrzne ‚takie’. Nigdy proste `"..."` ani angielskie “...” w tekście widocznym dla odbiorcy. W HTML: `&bdquo;` i `&rdquo;` albo znaki bezpośrednio w UTF-8; w atrybutach i kodzie proste cudzysłowy zostają, bo to składnia.
- **Pauza:** w polskim stosuje się półpauzę ze spacjami po obu stronach („Gabinet – nowoczesny i cichy”). W tekstach cyfrowych stosuj półpauzę ze spacjami; nie mieszaj jej z pauzą długą w jednym projekcie. Zakres liczb i dat bez spacji, półpauzą: 9–17, 2024–2026. Dywiz tylko w złożeniach (biało-czerwony) i przy łamaniu wyrazów.
- **Twarde spacje:** po jednoliterowych spójnikach i przyimkach (a, i, o, u, w, z; także wielką literą) nie wolno łamać wiersza, żeby nie zostały na końcu linii. Dotyczy to też liczba + jednostka (`24 h`, `15 zł`), skrótów typu `ul. Długa`, `nr 5` i nazwisk z inicjałem. W HTML: `&nbsp;` w treści. Jeśli tekst ma dużo takich miejsc, nie wklejaj niewidocznych znaków ręcznie - dodaj `&nbsp;` hurtowo przy generowaniu. W Figmie i narzędziach bez nbsp sprawdź łamanie wizualnie na 375 / 768 / 1440 i popraw tekst lub szerokość kolumny.
- **Liczby:** separator tysięcy to (twarda) spacja: `10 000`, `1 250 000`, nie `10,000` ani `10.000`. Przecinek dziesiętny: `4,5`, `99,2%` (bez spacji przed %; pisownia „99,2%” albo „99,2 %” - jedna w całym projekcie). Liczby do 4 cyfr zapisuj bez spacji (`2500`), od 5 cyfr ze spacją (`10 000`). Waluta za liczbą: `1 290 zł`, `49,90 zł`.
- **Daty i godziny:** `14 marca 2026`, `14.03.2026` w tabelach i formularzach; miesiąc słownie w dopełniaczu. Godziny `9:00–17:00`, w zdaniu „od 9 do 17”. Dni tygodnia małą literą. Nie mieszaj `2026-03-14` z `14.03.2026` w jednym widoku.
- **Wielkie litery:** nagłówek jak zdanie (tylko pierwsza litera i nazwy własne), nie angielskie Title Case. Nazwy miesięcy, dni i języków małą.
- **Polskie znaki:** każdy kroj użyty w projekcie musi mieć pełne ą ć ę ł ń ó ś ź ż (sprawdź w próbce, nie zakładaj). Wersaliki z ogonkami też.
- **Długość polskiego tekstu:** polskie etykiety bywają o 20–30% dłuższe niż angielskie; przyciski i menu projektuj na dłuższy wariant, bez obcinania i bez zmniejszania fontu.

## 2. Zasady UX copy

- **Przyciski to czasowniki** w trybie rozkazującym lub bezokoliczniku, spójnie w całym projekcie: „Umów wizytę”, „Pobierz cennik”, „Zapisz zmiany”. Pierwsze słowo to czasownik; w głównych CTA nie używaj „Wizyta”, „OK” ani „Kliknij tutaj” (w krokach kreatora „Dalej” jest dopuszczalne). Etykieta mówi, co się stanie, nie jak się zrobić (nie „Kliknij, aby…”).
- **Jedno główne działanie na ekran** i jedna nazwa na jedną czynność (nie „Zacznij” w hero i „Zarejestruj się” w stopce dla tego samego celu). Drugorzędne CTA tylko, jeśli prowadzi gdzie indziej niż pierwsze.
- **Komunikaty błędów:** co się stało + jak to naprawić, ludzkim językiem, bez winienia użytkownika i bez kodów: „Telefon musi mieć 9 cyfr, np. 600 123 456” zamiast „Błędne dane”. Komunikat stoi przy polu, nie tylko w kolorze (dostępność).
- **Etykiety zamiast placeholderów:** każde pole ma widoczną etykietę nad sobą; placeholder jest tylko przykładem formatu i znika przy pisaniu, więc nie może być jedyną etykietą. Wymagane pola oznacz wprost, a opcjonalne słowem „opcjonalnie”.
- **Stany puste, ładowanie i sukces:** każdy ma tekst, który mówi, co dalej („Brak zamówień. Dodaj pierwsze”), zamiast samego „Brak danych” lub „Sukces!”.
- **Formy grzecznościowe i rejestr:** jedna forma w całym projekcie (Pan/Pani albo „ty”), ustalona z klientem; nie przeskakuj między nimi w menu, formularzu i mailu. Dotyczy to też zapisu Ty/Twój wielką lub małą literą.
- **Nagłówek mówi, co to jest i dla kogo**, konkretem (usługa, miejsce, efekt), nie hasłem. Lead rozwija jedną sprawę; nie powtarza nagłówka innymi słowami.
- **Dane nieznane = jawny placeholder** (np. `[godziny otwarcia – do uzupełnienia]`) i wpis w liście braków jako „zastępcze”. Nie zmyślaj liczb, adresów, imion ani opinii; przykładowe dane muszą być oznaczone jako zastępcze.

## 3. Frazesy i kalki AI po polsku

Każda z poniższych fraz to sygnał tekstu pisanego na autopilocie. Nie stosuj ich, a gdy znajdziesz w tekście, zastąp faktem, a nie synonimem (synonim staje się kolejnym frazesem).

**Puste otwarcia i hasła**

1. „W dzisiejszym dynamicznie zmieniającym się świecie…” i każde „w dobie cyfryzacji”.
2. „Z nami Twój biznes osiągnie nowy poziom.”
3. „Kompleksowe rozwiązania szyte na miarę” (kalka „tailor-made”).
4. „Profesjonalne podejście do każdego klienta” – żaden gabinet nie pisze „nieprofesjonalne”.
5. „Pasja do tego, co robimy” i „z pasją tworzymy”.
6. „Stawiamy na jakość” / „jakość jest dla nas najważniejsza”.
7. „Innowacyjne technologie” bez wskazania, co jest nowe.
8. „Nowoczesne i przyjazne wnętrze” jako cała wartość oferty.

**Kalki z angielskiego**

9. „Odkryj moc…”, „Odblokuj potencjał…”, „Wznieś … na wyższy poziom”.
10. „Bez względu na to, czy jesteś X, czy Y, mamy coś dla Ciebie.”
11. „Jesteśmy tutaj, aby Ci pomóc” (kalka „we are here to help”).
12. „Zrób pierwszy krok ku…” i „Rozpocznij swoją podróż z…”.
13. „Dzięki naszemu zespołowi ekspertów” (kalka „team of experts”).
14. „To nie tylko X, to styl życia.”
15. „Nie zwlekaj – skontaktuj się z nami już dziś!” (przymus plus wykrzyknik).
16. „Wyróżnij się na tle konkurencji” – ironia: tak pisze konkurencja.
17. „W naszej ofercie znajdziesz wszystko, czego potrzebujesz.”

**Strukturalne tiki**

18. Trzy przymiotniki lub trzy korzyści w rytmie „szybko, wygodnie, bezpiecznie”.
19. Retoryczne pytanie z natychmiastową odpowiedzią („Szukasz X? Trafiłeś w dobre miejsce!”).
20. Zamykanie akapitu aforyzmem lub puentą w rodzaju „Bo zdrowy uśmiech to podstawa.”
21. Nagłówki w dwóch rwanych członach („Mniej stresu. Więcej uśmiechu.”).
22. „Zapewniamy” i „gwarantujemy” bez dowodu.
23. „Najwyższa jakość”, „najlepsza obsługa” i inne stopnie najwyższe bez dowodu.
24. „Oferujemy szeroki wachlarz usług.”

Gdy w tekście nie ma faktu, który wypełni zdanie, zdanie wypada. Krótka strona z prawdziwymi informacjami bije długą z frazesami.

## 4. Licznik chwytów

Każdy chwyt retoryczny ma na całej stronie budżet **jednego użycia**, tam gdzie działa najmocniej:

- zestawienie „nie X, lecz Y” (i jego odmiany „to nie X, to Y”);
- pytanie retoryczne;
- trójka (trzy członki w rytmie);
- zdanie-puenta kończące akapit;
- nagłówek w dwóch rwanych członach;
- wykrzyknik;
- żart lub gra słów;

Liczby: tylko z briefu lub ze źródłem, poza budżetem chwytów.

Zasady: przed oddaniem tekstu przejdź listę i policz; drugie użycie to tik – przepisz je na zwykłe zdanie. Wszystkie sekcje mają jeden rejestr głosu (nie techniczny w jednej, liryczny w drugiej, sprzedażowy w trzeciej). Marka ma własny głos, więc nie pisz dwóm klientom tak samo ciepło, lekko i z przymrużeniem oka.

## 5. Tabela nadkorekty

Poprawianie „na AI” samo produkuje nowe wady. Zanim zastosujesz regułę, sprawdź, co potrafi zepsuć.

| Poprawka | Co zwykle psuje |
|---|---|
| Usuń wszystkie frazesy | tekst staje się suchy i bez głosu; dodaj fakt lub konkretny szczegół zamiast pustego miejsca |
| Skracaj zdania | seria krótkich zdań o równym rytmie to nowy tik; jedno dłuższe w sekcji jest potrzebne |
| Zamień synonimy | powstają dziwne słowa i nowe frazesy; zmieniaj sens, nie słownictwo |
| Dodaj osobowość | żart w każdej sekcji; wydziel jeden żart i trzymaj go w mikrotekstach |
| Dodaj konkrety | zmyślone liczby i imiona; konkret ma pochodzić z briefu, inaczej placeholder |
| Pisz „po ludzku” | luz niepasujący do marki (medycyna, prawo, finanse) |
| Usuń długie myślniki | w polskim półpauza ze spacjami jest poprawna; usuwaj ich nadmiar, nie zasadę |
| Zamień wykrzykniki na kropki | tekst traci energię tam, gdzie jeden wykrzyknik był uzasadniony |
| Skróć nagłówek | traci się informacja „co to jest i dla kogo” |

Reguły angielskie o myślnikach i prostych cudzysłowach nie przenoszą się na polski: półpauza ze spacjami i cudzysłów „…” są tu poprawną typografią, nie oznaką AI.

# Ścieżka A - Figma (edytowalne warstwy)

Najpierw załaduj `jamel-gfx:standardy` i przeczytaj w `../standardy/references/figma.md` nagłówki „Struktura pliku”, „Nazewnictwo” i „Uczciwość narzędzi” (nazwy stron i warstw, zakaz `Frame 123`, raport). Nie powielaj ich tutaj. Jeśli pliku nie da się odczytać, powiedz to i nie zmyślaj jego treści.

`html_to_figma` daje statyczne warstwy 1:1, bez komponentów, zmiennych i Auto Layout. Całą resztę robisz przez `use_figma`. Ścieżka A używa `html_to_figma`. Nie wywołuj `generate_figma_design` ani `send_code_to_figma` (nie tworzy edytowalnych kształtów).

## 1. Warunki (jedyna lista wymagań)

Wymagane łącznie:

- connector Figmy połączony, a dostępne są narzędzia: `get_figma_skill`, `create_new_file`, `create_session`, `html_to_figma`, `use_figma`, `get_metadata`, `get_screenshot`;
- grafik ma w Figmie miejsce Full (bez niego zapis jest możliwy tylko w Drafts);
- sesja umie wysłać plik metodą HTTP POST pod adres z `html_to_figma` (Bash/curl albo odpowiednik; czat z takim narzędziem też się nadaje).

Sprawdź to **przed** przygotowaniem kopii HTML. Jeśli POST jest niemożliwy albo czegoś brakuje, zatrzymaj się i zaproponuj ścieżki B-E (zasady komunikatu: `SKILL.md`, „Warunki ścieżki A”).

Ustal plik docelowy: nowy czy URL istniejącego (z URL-a wyciągnij `fileKey`; `node-id` z `-` na `:`). Nazwa nowego pliku: `<projekt> - <widok>`, w zespole, który wskaże grafik (bez wskazania: Drafts, i powiedz o tym).

## 2. Przygotuj HTML dla każdego breakpointu

Źródło i procedura jak w `samodzielny-html.md` (style inline, obrazy base64, fonty, bez skryptów), z jedną różnicą: **osobny plik na każdy breakpoint**, bo import ma stałą szerokość 1280 px i nie ma parametru viewportu. Domyślnie powstają **wszystkie trzy**: 375 / 768 / 1440. Brak reguły CSS dla danego breakpointu nie jest powodem do pominięcia - widok 768 to kopia z wymuszoną szerokością 768 px, w układzie, który CSS daje przy tej szerokości (może być identyczny z 1440 albo z 375). Pominięcie breakpointu wymaga wyraźnej decyzji grafika, zadanej jednym pytaniem przed budową. Dla każdego z nich:

1. Skopiuj samodzielny HTML jako `<projekt>_<widok>_<breakpoint>.html`. Kopia dla Figmy **nie ma** `<script>` (import ich nie potrzebuje); plik dla ścieżki E zachowuje skrypty - nigdy jeden wspólny plik dla A i E.
2. Wymuś szerokość: dopisz na końcu `<style>`: `html,body{width:<bp>px;margin:0}` oraz szerokość głównego kontenera, jeśli ma `min-width` lub `max-width` (np. `.hero{width:<bp>px;min-height:0}`). Dotyczy to także 768 i 1440, nawet gdy CSS nie ma osobnych reguł dla tej szerokości (wtedy układ może być identyczny z sąsiednim breakpointem).
3. Każdą regułę `@media` oceń przy szerokości breakpointu: warunek prawdziwy → zamień go na `all`; fałszywy → usuń cały blok. Dotyczy `min-width`, `max-width` i zakresów. Przykłady: `@media (max-width: 640px) {` → przy 375 `@media all {`, przy 768 i 1440 usunięty; `@media (min-width: 900px) {` → przy 1440 `all`, przy 375 i 768 usunięty; `@media (min-width: 600px) and (max-width: 1024px) {` → przy 768 `all`, przy 375 i 1440 usunięty.
4. Sprawdź oba wzorce: `grep -cE '(src|href)="https?://'` = 0 oraz `grep -nE "url\(['\"]?https?://|@import"` bez wyników. Limit to 50 MB na jedną kopię dla Figmy; w razie przekroczenia najpierw zmniejsz obrazy.

Import zachowuje układ mobilny, jeśli CSS go opisuje (sprawdzone: burger, ułożenie w kolumnę).

## 3. Kolejność wywołań

Kolejność jest stała:

1. `get_figma_skill` - załaduj skill `figma-use` (obowiązkowy przed `use_figma`).
2. `create_new_file` (tylko dla nowego pliku; zwraca `fileKey`).
3. `create_session` z `fileKey` i krótkim opisem zadania - przed każdym narzędziem pliku. Zapamiętaj `sessionId`.
4. `html_to_figma` - jedno wywołanie na widok; przyjmuje `sessionId` z `create_session` (podawaj go jak przy innych narzędziach pliku). Zwraca jednorazowy `submitUrl`; wyślij plik przez HTTP POST: `curl -f -X POST "<submitUrl>" -H "Content-Type: text/html" --data-binary @plik.html`. Jeden `promptId` na żądanie; ten sam można użyć dla kilku importów tego samego zadania. Po POST sprawdź odpowiedź: przy błędzie, wygasłym `submitUrl` albo gdy widoku nie ma w `get_metadata`, nie uruchamiaj `use_figma` dla tego widoku i zgłoś to w pierwszym zdaniu raportu. Opcjonalny `cssSelector` (do 20 pasujących elementów, każdy jako osobna ramka) użyj na przyciski, karty i pola - to zaczątek biblioteki komponentów; selektor musi pasować do co najwyżej 20 elementów.
5. `use_figma` - struktura, nazwy, zmienne, komponenty (kroki 4 i 5 niżej). Kod do 50 000 znaków na wywołanie; dziel na kilka wywołań.
6. `get_screenshot` - porównaj każdy widok ze źródłem; różnice do raportu.

Po drodze `get_metadata` do odczytu drzewa. Węzeł elementu znajdź w `get_metadata` po nazwie lub tekście, nigdy nie zgaduj id.

## 4. Struktura i nazwy (`use_figma`)

- Strony i nazwy wg „Struktura pliku” i „Nazewnictwo” w `../standardy/references/figma.md`, struktura 00-10 skalowana do projektu; `Page 1` przemianuj.
- Warstwy nazwij **osobno w każdym widoku**: drzewa desktop i mobile się różnią (np. burger w nagłówku), więc jedna mapa id nie wystarczy. Przejdź drzewo każdego widoku osobno, nazwij po funkcji (`Header / Nav`, `Hero / Tekst`, `Przycisk / Umów wizytę`), nie po tagu (`Link`, `Container`, `Paragraph`). Ramki najwyższego poziomu: `Desktop / <widok>`, `Tablet / <widok>`, `Mobile / <widok>`.
- Przytnij wysokość ramki widoku do treści: po imporcie ramka bywa wyższa niż zawartość (np. 720 px przy krótszej treści); ustaw wysokość na dolną krawędź ostatniego dziecka lub `layoutSizingVertical = 'HUG'`, gdy ramka ma Auto Layout.
- Po nazwaniu sprawdź (`get_metadata` albo `findAll` w `use_figma`), że żadna warstwa nie pasuje do `^(Frame|Group|Rectangle) \d+$`.
- Zmienne z tokenów, jeśli są ustalone; podpinaj tylko tam, gdzie wartość się zgadza dokładnie. Wzorzec:

```js
const col = figma.variables.createVariableCollection('Kolory');
const v = figma.variables.createVariable('bg', col, 'COLOR'); v.scopes = ['ALL_FILLS'];
v.setValueForMode(col.defaultModeId, {r:0x17/255, g:0x12/255, b:0x0F/255});
node.fills = [figma.variables.setBoundVariableForPaint(
  {type:'SOLID', color:{r:0x17/255, g:0x12/255, b:0x0F/255}}, 'color', v)];
```

- Style tekstu z fontów użytych w widoku; Auto Layout tylko dla prostych układów (best effort). Fonty, których Figma zespołu nie ma, wypisz w raporcie. Przed zmianą tekstu `await figma.loadFontAsync(...)`.

## 5. Komponenty, stany i mikroanimacje (krok 5a, domyślnie)

Domyślnie wykonuj ten krok. Grafik może go wyłączyć prośbą „bez komponentów” albo „tylko warstwy” - wtedy go pomiń i napisz to w raporcie.

1. **Wybierz elementy**: powtarzalne i interaktywne (przyciski, linki nawigacji, karty, pola formularza, tagi). Elementy statyczne, występujące raz, zostają warstwami.
2. **Stany z CSS.** Dla każdego z nich wypisz reguły `:hover`, `:focus-visible`, `:active`, `:disabled` i klasę stanu ładowania, jeśli jest. Każdy znaleziony stan to wariant właściwości `State` o nazwie z listy: `Default` / `Hover` / `Focus` / `Pressed` / `Disabled` / `Loading` (po angielsku, nie po polsku; zgodnie z „Komponenty i warianty” w `../standardy/references/figma.md`). Wartości (kolor tła, tekstu, obrysu, cień) bierz z CSS. Nie dodawaj stanów, których CSS nie opisuje. Unikaj ogromnych kombinacji wariantów.
3. **Budowa**: jeden zestaw komponentów na element, a jego instancje zastąp we WSZYSTKICH widokach (375 / 768 / 1440). `createComponentFromNode` na elemencie z widoku → klon na każdy kolejny stan → zmiana właściwości z CSS → `combineAsVariants` → nazwa zestawu wg „Nazewnictwo” (`Button / Primary`) → egzemplarze w widokach zamień na instancje (wstaw instancję w miejsce oryginału).
4. **Układ wariantów.** Po `combineAsVariants` warianty leżą w rozsypce; ułóż je w siatce (stały odstęp, np. 24 px, jeden wiersz na właściwość) i dodaj padding zestawu, a zestaw postaw poza ramkami widoków (np. na stronie `03 — Components`).
5. **Hover jako prototyp.** Na instancji ustaw reakcję `ON_HOVER` → `CHANGE_TO` wariant `Hover` przez Smart Animate. Czas i krzywą weź z `transition` w CSS: ms na sekundy, krzywa: `ease-in-out` → `EASE_IN_AND_OUT`, `ease-out` → `EASE_OUT`, `ease-in` → `EASE_IN`, `linear` → `LINEAR`, `ease` → `EASE_IN_AND_OUT` (najbliższa; wpisz to w raporcie). Gdy w CSS nie ma `transition`: 150 ms, `EASE_OUT`. Hover weryfikuj wyłącznie odczytem `reactions`. Powrót do `Default` po opuszczeniu kursora i efekt wizualny trafiają do „Do ręcznego wdrożenia” („sprawdź w trybie prezentacji”), chyba że dodano reakcję zwrotną i odczytano ją z powrotem; niczego niezweryfikowanego nie wpisuj do „Gotowe w pliku”.
6. **`@keyframes` i proste przejścia** odtwarzaj Smart Animate'em tylko wtedy, gdy da się je zapisać jako dwa stany (np. `from`/`to` opacity). Wieloetapowe i nieskończone zostaw jako specyfikację.

Wzorzec (przycisk, dwa stany; sprawdzone w testach: zestaw komponentów, reakcja hover i odczyt krzywej; układ wariantów wymagał poprawki `AUTO` poniżej; powrót do `Default` po opuszczeniu kursora nie był sprawdzony, więc sprawdź; dostosuj nazwy do `State=...` i wartości do CSS, czas `0.2` i `EASE_IN_AND_OUT` dla `200ms ease-in-out`):

```js
const btn = await figma.getNodeByIdAsync('<id przycisku>');
const parent = btn.parent; const idx = parent.children.indexOf(btn);
const c1 = figma.createComponentFromNode(btn); c1.name = 'State=Default';
const c2 = c1.clone(); c2.name = 'State=Hover';
c2.fills = [{type:'SOLID', color:{r:0x9A/255, g:0x34/255, b:0x12/255}}]; // wartość z :hover
const set = figma.combineAsVariants([c1, c2], figma.currentPage); // strona, na której leżą oryginały
set.name = 'Button / Primary';
set.primaryAxisSizingMode = set.counterAxisSizingMode = 'AUTO'; // bez tego zestaw ma puste pole (447,5 px wysokości)
set.layoutMode = 'HORIZONTAL'; set.itemSpacing = 24;
set.paddingLeft = set.paddingRight = set.paddingTop = set.paddingBottom = 24;
const inst = c1.createInstance(); inst.name = 'Button / Umów wizytę';
parent.insertChild(idx, inst); // oryginał jest po combineAsVariants wewnątrz zestawu; idx ważny tylko, jeśli parent się nie zmienił
await inst.setReactionsAsync([{
  trigger: {type: 'ON_HOVER'},
  actions: [{type: 'NODE', destinationId: c2.id, navigation: 'CHANGE_TO',
    transition: {type: 'SMART_ANIMATE', easing: {type: 'EASE_IN_AND_OUT'}, duration: 0.2},
    preserveScrollPosition: false}]}]);
```

Uwagi: `combineAsVariants` zgłasza błąd „Grouped nodes must be in the same page as the parent”, gdy komponenty leżą na innej stronie niż podany rodzic: łącz na stronie, na której leżą oryginały, i dopiero potem przenieś zestaw na `03 — Components` (`page.appendChild(set)`). Po `combineAsVariants` odnoś się do wariantów przez `set.children`, nie przez stare id; `set.layoutMode` działa na zestawie, ale po zmianie sprawdź zrzutem, że warianty się nie nakładają. Jeśli CSS zmienia tylko tło (jak w teście), wariant `Hover` różni się tylko tłem - nie dorabiaj zmian.

## 6. Odczyt kontrolny przed raportem

Nie raportuj niczego, czego nie odczytałeś. Przez `use_figma` (albo `get_metadata`) odczytaj i zapisz w odpowiedzi:

- drzewo nazw najwyższego poziomu każdego widoku; brak nazw pasujących do `^(Frame|Group|Rectangle) \d+$`;
- zestawy komponentów: nazwa, właściwość `State`, nazwy wariantów;
- dla instancji interaktywnych: `reactions` (trigger, `navigation`, `transition.type`, `easing`, `duration`);
- liczba widoków i szerokości ramek (375 / 768 / 1440).

Potem `get_screenshot` każdego widoku.

## 7. Raport

Trzy nagłówki zdefiniowane w `SKILL.md` + link do pliku Figmy. Pozycje specyficzne dla ścieżki A:

- **Gotowe w pliku**: widoki (z szerokościami), strony, komponenty i warianty, reakcje (z odczytanym czasem i krzywą), zmienne.
- **Przygotowane jako specyfikacja**: wszystko, czego Figma nie odtworzyła, z wartościami z CSS: animacje przy przewijaniu, animacje sterowane skryptem, wieloetapowe lub nieskończone `@keyframes`, `backdrop-filter`, tekst na ścieżce (SVG `textPath` nie jest importowany), reguły responsive poza breakpointami 375 / 768 / 1440, stany bez odpowiednika w prototypie.
- **Do ręcznego wdrożenia**: fonty niedostępne w Figmie zespołu, obrazy, których nie udało się pobrać (z adresem), Auto Layout, którego nie dało się zrobić, powrót hovera i efekt wizualny (jeśli nie odczytano), decyzje grafika, brak miejsca Full.

Jeśli import się nie powiódł albo któregoś widoku brakuje, powiedz to w pierwszym zdaniu; nie opisuj widoku, którego nie ma w pliku.

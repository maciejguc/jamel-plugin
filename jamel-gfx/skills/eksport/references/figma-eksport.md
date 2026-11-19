# Ścieżka A - Figma (edytowalne warstwy)

Najpierw załaduj `jamel-gfx:standardy` i przeczytaj w `references/figma.md` nagłówki „Struktura pliku”, „Nazewnictwo” i „Uczciwość narzędzi” (nazwy stron i warstw, zakaz `Frame 123`, raport). Nie powielaj ich tutaj.

`html_to_figma` daje statyczne warstwy 1:1, bez komponentów, zmiennych i Auto Layout. Całą resztę robisz przez `use_figma`. Nie wywołuj `generate_figma_design` (niedostępne) ani `send_code_to_figma` (nie tworzy edytowalnych kształtów).

## 1. Warunki

Connector Figmy połączony, grafik ma miejsce Full, jest środowisko wykonawcze do wysłania pliku (patrz `SKILL.md`). Ustal plik docelowy: nowy czy URL istniejącego (z URL-a wyciągnij `fileKey`; `node-id` z `-` na `:`). Nazwa nowego pliku: `<projekt> - <widok>`, w zespole, który wskaże grafik (bez wskazania: Drafts, i powiedz o tym).

## 2. Przygotuj HTML dla każdego breakpointu

Źródło i procedura jak w `samodzielny-html.md` (style inline, obrazy base64, fonty, bez skryptów), z jedną różnicą: **osobny plik na każdy breakpoint**, bo import ma stałą szerokość 1280 px i nie ma parametru viewportu. Dla każdego z 375 / 768 / 1440 (tylko tych, które istnieją w projekcie):

1. Skopiuj samodzielny HTML jako `<projekt>_<widok>_<breakpoint>.html`.
2. Wymuś szerokość: dopisz na końcu `<style>`: `html,body{width:<bp>px;margin:0}` oraz szerokość głównego kontenera, jeśli ma `min-width` lub `max-width` (np. `.hero{width:<bp>px;min-height:0}`).
3. Przełącz media queries tego breakpointu na `all`: dla 375 reguły `@media (max-width: …)` dotyczące telefonu, dla 768 reguły tabletu, a reguły większych ekranów usuń lub zostaw tylko te, które pasują. Przykład z testu: `@media (max-width: 640px) {` → `@media all {`.
4. 1440 zwykle nie wymaga zmian poza szerokością.
5. Sprawdź `grep -cE '(src|href)="https?://'` = 0 i rozmiar ≤ 50 MB.

Import zachowuje układ mobilny, jeśli CSS go opisuje (sprawdzone: burger, ułożenie w kolumnę).

## 3. Kolejność wywołań

Kolejność jest stała:

1. `get_figma_skill` - załaduj skill `figma-use` (obowiązkowy przed `use_figma`).
2. `create_new_file` (tylko dla nowego pliku; zwraca `fileKey`).
3. `create_session` z `fileKey` i krótkim opisem zadania - przed każdym narzędziem pliku. Zapamiętaj `sessionId`.
4. `html_to_figma` - jedno wywołanie na widok. Zwraca jednorazowy `submitUrl`; wyślij plik przez HTTP POST: `curl -f -X POST "<submitUrl>" -H "Content-Type: text/html" --data-binary @plik.html`. Jeden `promptId` na żądanie; ten sam można użyć dla kilku importów tego samego zadania. Opcjonalny `cssSelector` (do 20 pasujących elementów, każdy jako osobna ramka) użyj na przyciski, karty i pola - to zaczątek biblioteki komponentów; selektor musi pasować do co najwyżej 20 elementów.
5. `use_figma` - struktura, nazwy, zmienne, komponenty (kroki 4 i 5 niżej). Kod do 50 000 znaków na wywołanie; dziel na kilka wywołań.
6. `get_screenshot` - porównaj każdy widok ze źródłem; różnice do raportu.

Po drodze `get_metadata` do odczytu drzewa.

## 4. Struktura i nazwy (`use_figma`)

- Strony i nazwy wg „Struktura pliku” i „Nazewnictwo” w `figma.md`, struktura 00-10 skalowana do projektu; `Page 1` przemianuj.
- Warstwy nazwij **osobno w każdym widoku**: drzewa desktop i mobile się różnią (np. burger w nagłówku), więc jedna mapa id nie wystarczy. Przejdź drzewo każdego widoku osobno, nazwij po funkcji (`Header / Nav`, `Hero / Tekst`, `Przycisk / Umów wizytę`), nie po tagu (`Link`, `Container`, `Paragraph`). Ramki najwyższego poziomu: `Desktop / <widok>`, `Tablet / <widok>`, `Mobile / <widok>`.
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
2. **Stany z CSS.** Dla każdego z nich wypisz reguły `:hover`, `:focus-visible`, `:active`, `:disabled` i klasę stanu ładowania, jeśli jest. Każdy znaleziony stan to wariant właściwości `State` o nazwie z listy: `Default` / `Hover` / `Focus` / `Pressed` / `Disabled` / `Loading` (po angielsku, nie po polsku; zgodnie z „Komponenty i warianty” w `figma.md`). Wartości (kolor tła, tekstu, obrysu, cień) bierz z CSS. Nie dodawaj stanów, których CSS nie opisuje. Unikaj ogromnych kombinacji wariantów.
3. **Budowa**: `createComponentFromNode` na elemencie z widoku → klon na każdy kolejny stan → zmiana właściwości z CSS → `combineAsVariants` → nazwa zestawu wg „Nazewnictwo” (`Button / Primary`) → egzemplarze w widokach zamień na instancje (wstaw instancję w miejsce oryginału).
4. **Układ wariantów.** Po `combineAsVariants` warianty leżą w rozsypce; ułóż je w siatce (stały odstęp, np. 24 px, jeden wiersz na właściwość) i dodaj padding zestawu, a zestaw postaw poza ramkami widoków (np. na stronie `03 — Components`).
5. **Hover jako prototyp.** Na instancji ustaw reakcję `ON_HOVER` → `CHANGE_TO` wariant `Hover` przez Smart Animate. Czas i krzywą weź z `transition` w CSS: ms na sekundy, krzywa: `ease-in-out` → `EASE_IN_AND_OUT`, `ease-out` → `EASE_OUT`, `ease-in` → `EASE_IN`, `linear` → `LINEAR`, `ease` → `EASE_IN_AND_OUT` (najbliższa; wpisz to w raporcie). Gdy w CSS nie ma `transition`: 150 ms, `EASE_OUT`. Powrót do `Default` po opuszczeniu hovera sprawdź w odczycie reakcji i zrzutach; jeśli nie działa, dodaj reakcję zwrotną i napisz to w raporcie.
6. **`@keyframes` i proste przejścia** odtwarzaj Smart Animate'em tylko wtedy, gdy da się je zapisać jako dwa stany (np. `from`/`to` opacity). Wieloetapowe i nieskończone zostaw jako specyfikację.

Wzorzec sprawdzony w teście (przycisk, dwa stany; dostosuj nazwy do `State=...` i wartości do CSS, czas `0.2` i `EASE_IN_AND_OUT` dla `200ms ease-in-out`):

```js
const btn = await figma.getNodeByIdAsync('<id przycisku>');
const parent = btn.parent; const idx = parent.children.indexOf(btn);
const c1 = figma.createComponentFromNode(btn); c1.name = 'State=Default';
const c2 = c1.clone(); c2.name = 'State=Hover';
c2.fills = [{type:'SOLID', color:{r:0x9A/255, g:0x34/255, b:0x12/255}}]; // wartość z :hover
const set = figma.combineAsVariants([c1, c2], figma.currentPage);
set.name = 'Button / Primary';
set.layoutMode = 'HORIZONTAL'; set.itemSpacing = 24;
set.paddingLeft = set.paddingRight = set.paddingTop = set.paddingBottom = 24;
const inst = c1.createInstance(); inst.name = 'Button / Umów wizytę';
parent.insertChild(idx, inst);
await inst.setReactionsAsync([{
  trigger: {type: 'ON_HOVER'},
  actions: [{type: 'NODE', destinationId: c2.id, navigation: 'CHANGE_TO',
    transition: {type: 'SMART_ANIMATE', easing: {type: 'EASE_IN_AND_OUT'}, duration: 0.2},
    preserveScrollPosition: false}]}]);
```

Uwagi: po `combineAsVariants` odnoś się do wariantów przez `set.children`, nie przez stare id; `set.layoutMode` działa na zestawie, ale po zmianie sprawdź zrzutem, że warianty się nie nakładają. Jeśli CSS zmienia tylko tło (jak w teście), wariant `Hover` różni się tylko tłem - nie dorabiaj zmian.

## 6. Odczyt kontrolny przed raportem

Nie raportuj niczego, czego nie odczytałeś. Przez `use_figma` (albo `get_metadata`) odczytaj i zapisz w odpowiedzi:

- drzewo nazw najwyższego poziomu każdego widoku; brak nazw pasujących do `^(Frame|Group|Rectangle) \d+$`;
- zestawy komponentów: nazwa, właściwość `State`, nazwy wariantów;
- dla instancji interaktywnych: `reactions` (trigger, `navigation`, `transition.type`, `easing`, `duration`);
- liczba widoków i szerokości ramek (375 / 768 / 1440).

Potem `get_screenshot` każdego widoku.

## 7. Raport

Trzy nagłówki z `SKILL.md` + link do pliku Figmy.

- **Gotowe w pliku**: widoki (z szerokościami), strony, komponenty i warianty, reakcje (z odczytanym czasem i krzywą), zmienne, zrzuty.
- **Przygotowane jako specyfikacja**: wszystko, czego Figma nie odtworzyła, z wartościami z CSS: animacje przy przewijaniu, animacje sterowane skryptem, wieloetapowe lub nieskończone `@keyframes`, `backdrop-filter`, tekst na ścieżce (SVG `textPath` nie jest importowany, więc znika z widoku), reguły responsive poza breakpointami 375 / 768 / 1440, stany bez odpowiednika w prototypie.
- **Do ręcznego wdrożenia**: fonty niedostępne w Figmie zespołu, obrazy, których nie udało się pobrać (z adresem), Auto Layout, którego nie dało się zrobić, decyzje grafika, brak miejsca Full.

Jeśli import się nie powiódł albo któregoś widoku brakuje, powiedz to w pierwszym zdaniu; nie opisuj widoku, którego nie ma w pliku.

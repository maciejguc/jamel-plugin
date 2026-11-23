# jamel-gfx

Plugin dla grafików JAMEL w Claude Cowork i w czacie Claude (Claude Design).

## Co to jest

Cztery skille, które Claude uruchamia sam, gdy rozmowa tego wymaga:

- **standardy** – standardy pracy JAMEL przy projektach graficznych: Discovery, kierunek, jakość wizualna, teksty po polsku, a przy okazji uwaga o odstępstwach od standardu.
- **research** – research wizualny do projektu: inspiracje, konkurencja, moodboard, 2–3 kierunki z uzasadnieniem (także w wersji szybkiej).
- **eksport** – przekazanie projektu: wysyłka do Figmy, PNG/SVG/PDF, tokeny, specyfikacja dla developera, samodzielny plik HTML dla klienta. Do Figmy trafiają komponenty z wariantami `State` i animacją hover; powiedz „bez komponentów”, jeśli ich nie chcesz.
- **zgloszenie** – plik z uwagami z sesji dla Macieja, opiekuna standardów (`/jamel-gfx:zgloszenie`).

## Instalacja w Cowork

1. Otwórz Customize → Plugins → Add marketplace i wpisz `maciejguc/jamel-plugin`.
2. Zainstaluj plugin `jamel-gfx`.
3. Podłącz konektor Figma. Zapis poza Drafts wymaga miejsca typu Full.
4. Żeby pliki z eksportu trafiały na dysk, podłącz folder roboczy (Add folder).
5. Jeśli nie jest ustawione w organizacji: dodaj `images.unsplash.com` do dozwolonych domen Cowork.
6. Jeśli nie jest ustawione w organizacji: podłącz konektor Unsplash. Ułatwia pobieranie zdjęć.
7. Wklej wpis do instrukcji (następna sekcja).

## Wpis do instrukcji

Wklej raz. Wpis tylko wskazuje na skill, więc aktualizacje standardów nie wymagają wklejania od nowa.

- **Cowork:** Settings → Cowork → Global instructions.
- **Czat (desktop lub web):** instrukcje Projectu „JAMEL — grafika”, w którym prowadzisz rozmowy projektowe. Nie w preferencjach profilu – działają we wszystkich rozmowach.

```
Gdy pracuję nad projektem graficznym (strona, interfejs, makieta, artefakt Claude Design, design system, ocena projektu) albo pytam o wersję standardów JAMEL, korzystaj ze skilla jamel-gfx:standardy. Jedna rozmowa to jeden projekt: pracuj tylko nad tym, nad czym teraz pracuję – bez mojej prośby nie pobieraj ani nie zmieniaj innych artefaktów i projektów tego klienta. W innych rozmowach (szukanie informacji, pytania ogólne, research niezwiązany z projektem graficznym) nie używaj skilli jamel-gfx i ich nie proponuj. Gdy moja praca graficzna wykracza poza standard JAMEL albo jest z nim sprzeczna, powiedz mi o tym raz, jednym zdaniem, po wykonaniu zadania (wymagania klienta to nie odstępstwo). Jeśli były odstępstwa, na koniec zaproponuj /jamel-gfx:zgloszenie.
```

## Jak sprawdzić wersję

Zapytaj Claude’a: „Jaka jest wersja standardów JAMEL?”. Odpowiedź pochodzi ze skilla `jamel-gfx:standardy`. Jeśli skill się nie załaduje, plugin nie jest zainstalowany albo wpis do instrukcji nie jest wklejony.

## Aktualizacja

Nowa wersja pojawia się w Cowork sama po wprowadzeniu zmiany do repozytorium. Sprawdź numer pytaniem z poprzedniej sekcji. Dopiero gdy wersja się nie zmienia, użyj Update przy pluginie. Jeśli to nie pomoże, usuń plugin i zainstaluj go ponownie.

## Jak działa obserwator

To instrukcja działająca w trakcie rozmowy, a nie proces w tle. Claude widzi tylko to, co dzieje się w tej rozmowie, niczego poza Claude’em nie podgląda i niczego nigdzie nie wysyła. Gdy twoja praca wykracza poza standard albo jest z nim sprzeczna, mówi o tym raz, jednym zdaniem, po wykonaniu zadania. Wymagań klienta nie zgłasza.

## Zgłoszenia

1. Na koniec pracy (albo gdy Claude zaproponuje) wpisz `/jamel-gfx:zgloszenie` (w Cowork); w czacie napisz: „przygotuj zgłoszenie dla Macieja”.
2. Claude przygotuje plik: w Cowork zapisze go w folderze roboczym, w czacie da go do pobrania. Plik nie zawiera nazwy klienta.
3. Przejrzyj plik i wyślij go Maciejowi sam (Slack lub e-mail). Nic nie jest wysyłane automatycznie.

## Rozwiązywanie problemów

- **Zdjęcia lub fonty się nie ładują albo eksport zgłasza brak obrazów:** host zdjęć lub fontów jest zablokowany w Cowork. Dodaj go do dozwolonych domen (np. `images.unsplash.com`, `fonts.googleapis.com`, `fonts.gstatic.com`) albo poproś Macieja. Claude wypisze każdy brakujący obraz z adresem.
- **Eksport do Figmy mówi, że nie może zapisać:** sprawdź konektor Figma i typ miejsca (Full).

## Dla opiekuna

1. Zgłoszenie przychodzi od grafika (Slack lub e-mail).
2. W Claude Code, w worktree z `origin/main`, wklej zgłoszenie i poproś o propozycję zmian w `jamel-gfx/skills/standardy/…`. Claude pokazuje diff, ty decydujesz.
3. Podbij wersję w dwóch miejscach naraz: `jamel-gfx/.claude-plugin/plugin.json` i linia `Wersja standardów: X.Y.Z` w `jamel-gfx/skills/standardy/SKILL.md`.
4. Uruchom `sh jamel-gfx/tests/check.sh` (musi wypisać OK) oraz scenariusze z `jamel-gfx/tests/scenariusze.md`.
5. Otwórz PR do `main` i zmerguj. Po merge zespół dostaje wersję automatycznie.
6. Ogłoś zespołowi nową wersję i jedno zdanie o zmianie.

## Podziękowania

Metodyka zewnętrzna jest sparafrazowana po polsku, bez kopiowania treści:

- [impeccable](https://github.com/pbakaus/impeccable) (pbakaus) – Apache-2.0
- [taste-skill](https://github.com/Leonxlnx/taste-skill) (Leonxlnx) – MIT
- [genjutsu](https://github.com/AThevon/genjutsu) (AThevon) – MIT
- [hallmark](https://github.com/nutlope/hallmark) (nutlope) – MIT
- [dembrandt](https://github.com/dembrandt/dembrandt) (dembrandt) – MIT
- [scroll-craft](https://github.com/nateherkai/scroll-craft) (nateherkai) – MIT
- [humanizer](https://github.com/blader/humanizer) (blader) – MIT

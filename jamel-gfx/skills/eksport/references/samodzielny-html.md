# Samodzielny HTML

Jedna procedura dla ścieżki A (wejście do Figmy) i ścieżki E (plik dla ludzi). Wynik: jeden plik `.html`, który działa offline i nie odwołuje się do niczego na zewnątrz. Do kodowania plików potrzebne jest środowisko wykonawcze sesji (Cowork je ma; w czacie sprawdź, czy masz Bash lub odpowiednik - bez niego powiedz, że nie możesz tego zrobić, i zaproponuj inną ścieżkę).

## Źródło

Kod artefaktu Claude Design z sesji albo jego natywny eksport HTML. Jeśli masz tylko zrzut ekranu, to nie jest źródło - poproś o artefakt. Nie przerabiaj oryginału w miejscu; pracuj na kopii w folderze roboczym o nazwie `<projekt>_<widok>_v<NN>.html`.

## Kroki

1. **Style inline.** Zewnętrzne arkusze (`<link rel="stylesheet">`) wstaw jako `<style>`. Reguły `@import` rozwiń.
2. **SVG inline.** `<img src="x.svg">` zamień na SVG w dokumencie albo `data:image/svg+xml` .
3. **Obrazy jako `data:` URI.** Każdy obraz z zewnętrznego adresu pobierz (`curl -fsSL`, z limitem czasu) i wbuduj. Przed wbudowaniem przeskaluj do rozsądnego rozmiaru: szerokość nie większa niż 2x największej szerokości wyświetlania (typowo 1600-2400 px na pełną szerokość), JPEG jakość około 80 dla zdjęć, PNG tylko dla grafiki z przezroczystością. Base64 dodaje około jednej trzeciej wagi, więc licz po kodowaniu. Narzędzia: `sips` (macOS), `magick`, albo Pillow w venv; jeśli żadnego nie ma, nie instaluj niczego bez zgody grafika - wbuduj oryginał i zaznacz wagę w raporcie.
4. **Fonty.** Dla każdej rodziny użytej w dokumencie: jeśli licencja pozwala na osadzenie (Google Fonts / SIL OFL, inne licencje otwarte), pobierz pliki `woff2` i wstaw jako `@font-face` z `data:` URI, tylko używane grubości i style. Jeśli licencja nie pozwala albo jej nie znasz (fonty komercyjne, Adobe Fonts, pliki klienta), nie osadzaj: powiedz to wprost, zostaw bezpieczny zamiennik systemowy w `font-family` i wpisz rodzinę do „Do ręcznego wdrożenia”. Zawsze podaj w raporcie, które fonty osadzone, a które zastąpione.
5. **Dokument.** `<meta charset="utf-8">` w `<head>` (polskie znaki), `<meta name="viewport" content="width=device-width, initial-scale=1">`. Usuń `preconnect`, `dns-prefetch` i inne linki do zewnętrznych hostów.
6. **Skrypty.** Zewnętrzne (`<script src>`, CDN) wstaw inline albo usuń z informacją, co przestało działać. Dla wejścia do Figmy skryptów w ogóle nie ma (patrz `figma-eksport.md`).

## Kontrola przed oddaniem

1. **Brak odwołań zewnętrznych.** Przeszukaj plik:
   `grep -cE '(src|href)="https?://' plik.html` musi dać `0`; dodatkowo `grep -nE "url\(['\"]?https?://|@import" plik.html` bez wyników. Linki do innych stron w treści (`<a href="https://...">`, np. profil klienta w mediach) są treścią, nie zasobem - jeśli zostają, wypisz je w raporcie; jeśli grafik chce ścisłe zero, zamień na tekst.
2. **Waga.** `ls -l` / `du -k`; podaj w raporcie w KB lub MB. Cel: poniżej 20 MB (żeby dało się wysłać mailem). Powyżej celu zaproponuj mocniejszą kompresję zdjęć (niższa jakość, mniejsza szerokość) i zapytaj, zanim to zrobisz. Dla wejścia do Figmy limit twardy to 50 MB.
3. **Podgląd** na 375 / 768 / 1440 px, jeśli sesja ma przeglądarkę; bez niej napisz, że wyglądu nie sprawdzono.

## Gdy coś się nie uda

Jeden błąd nie zatrzymuje eksportu. Plik powstaje zawsze, a każdy zasób, którego nie udało się wbudować, trafia do listy w raporcie (sekcja „Do ręcznego wdrożenia”) z pełnym adresem i powodem (404, blokada hotlinkingu, timeout, licencja). Zamiast brakującego obrazu zostaw w pliku `<img>` bez `src` z `alt` albo pusty blok o tych samych wymiarach (nie zewnętrzny adres, bo to złamie kontrolę offline). Nigdy nie pisz „wszystkie zasoby wbudowane”, jeśli lista błędów nie jest pusta.

## Różnice ścieżki E względem wejścia do Figmy

- Jeden responsywny plik (media queries zostają), nie osobny na każdy breakpoint.
- Interakcje i animacje zostają (`:hover`, `transition`, `@keyframes`, skrypty inline, jeśli artefakt je ma).
- Stan widoku jak w artefakcie, bez wymuszonej szerokości.
- Nazwa `<projekt>_<widok>_v<NN>.html`; w Cowork zapis w folderze roboczym, w czacie plik do pobrania. Raport z trzema nagłówkami (patrz `SKILL.md`) i wagą pliku.

---
name: zgloszenie
description: Przygotowuje plik ze zgłoszeniem z bieżącej sesji graficznej dla Macieja, opiekuna standardów JAMEL: zapisuje go jako plik (co pomogło, co przeszkadzało, odstępstwa od standardów, pytania bez odpowiedzi). Używaj po /jamel-gfx:zgloszenie albo gdy grafik mówi "przygotuj zgłoszenie dla Macieja", "podsumuj sesję dla Macieja" (o standardach JAMEL), "zgłoś uwagi do standardów jamel-gfx", "raport z sesji dla opiekuna standardów". Nie używaj do innych podsumowań (notatki ze spotkania, raport dla klienta, podsumowanie projektu, retrospektywa) ani gdy prośba nie dotyczy Macieja i standardów JAMEL.
---

# Zgłoszenie z sesji dla Macieja

Cel: Maciej (opiekun standardów) dostaje zwięzły plik, na podstawie którego poprawia standardy. Zgłoszenie opisuje **tylko tę sesję** i nigdy nie jest wysyłane automatycznie.

Zanim zaczniesz, załaduj `jamel-gfx:standardy` i odczytaj z niego linię `Wersja standardów: X.Y.Z` oraz sekcję „Obserwator” (kategorie odstępstw). Numer wersji bierz z tej linii - nie wpisuj go z pamięci. Jeśli nie możesz odczytać skilla, wpisz „Wersja standardów: nieustalona” i napisz o tym w „Kontekst”; nie zgaduj. Użyj nazw kategorii z Obserwatora; dwie podane niżej to domyślne.

## Przed pisaniem

1. **Podpis.** Jeśli nie wiesz, kto jest autorem zgłoszenia, zapytaj **raz**, jednym krótkim pytaniem. Wystarczy samo imię lub pseudonim (plik trafi do publicznego repozytorium). Bez odpowiedzi wpisz „anonimowo” i generuj dalej.
2. **Zakres sesji.** Przejrzyj rozmowę. Sygnały skracania: blok podsumowania na początku, brak pierwszej wypowiedzi grafika, odwołania do rzeczy, po których nie ma śladu. Przy którymkolwiek, a także gdy nie masz pewności, zgłoszenie jest **częściowe** - patrz „Uczciwość”.
3. **Środowisko.** Masz folder roboczy lub system plików = Cowork; inaczej czat. Gdy niejasne, zapytaj jednym zdaniem. Wpisz środowisko w „Kontekst”; od niego zależy ostatni krok (link).

## Plik

Nazwa: `zgloszenie-jamel-gfx-RRRR-MM-DD-<krotki-temat>.md` (dzisiejsza data; temat to 2-4 słowa małymi literami z myślnikami: typ projektu + uogólniona branża, bez nazwy klienta, rodzaju jego firmy i miejscowości, np. `landing-branza-x`).

- Cowork: zapisz w folderze roboczym.
- Czat: wygeneruj jako plik do pobrania. Jeśli nie możesz utworzyć pliku, wypisz całą treść w jednym bloku markdown i podaj nazwę pliku do ręcznego zapisu.

## Sekcje (dokładnie te nagłówki, w tej kolejności)

Plik zaczyna się od `# Zgłoszenie z sesji jamel-gfx`, potem:

1. `## Kontekst` - data, autor (podpis), typ projektu (landing, sklep, aplikacja) i klient opisany **wyłącznie uogólnioną branżą** („branża spożywcza”, „usługi budowlane”), bez nazwy, danych, konkretnego rodzaju firmy (np. piekarnia) ani miejscowości, linia `Wersja standardów: X.Y.Z` (odczytana ze skilla `standardy`), środowisko. Jeśli zgłoszenie jest częściowe, napisz to tutaj wprost: „Zgłoszenie częściowe: rozmowa była skracana, obejmuje tylko widoczną część sesji.”
2. `## Co pomogło` - co ze standardów realnie pomogło (konkretnie, 1-5 punktów). Brak = „Brak uwag.”
3. `## Co przeszkadzało` - co przeszkadzało albo było niejasne.
4. `## Odstępstwa` - tabela, jeden wiersz na odstępstwo: kategoria (`sprzeczne ze standardem` / `poza standardem`), co grafik zrobił, dlaczego (słowami grafika, zanonimizowane wg „Anonimizacji”), propozycja konkretnego brzmienia zmiany w standardzie, plik i sekcja do zmiany (np. `skills/standardy/SKILL.md`, sekcja „Formularze”). Kolumny: Kategoria | Co zrobił grafik | Dlaczego | Proponowane brzmienie | Plik i sekcja. W komórkach nie używaj znaku `|` ani łamania wiersza; dłuższe brzmienie wpisz pod tabelą jako „Odstępstwo N” (N = numer wiersza). Brak odstępstw = jedno zdanie, że nie było. **Wymogi klienta nie są odstępstwem - nie wpisuj ich.**
5. `## Pytania bez odpowiedzi` - pytania, na które standard nie miał odpowiedzi.
6. `## Inne uwagi` - uwagi grafika spoza powyższych. Zapisz plik od razu z „Brak uwag.”, potem zapytaj jednym zdaniem, czy grafik chce coś dodać; jeśli odpowie, dopisz to i zapisz plik ponownie. Udostępnione canvasy wymieniaj tylko z nazwy, bez linków, chyba że grafik o to poprosi.
7. `## Kluczowe fragmenty rozmowy` - przy **każdym** odstępstwie dosłowny cytat: prośba grafika i decyzja Claude, zanonimizowane. Cytuj tylko minimum potrzebne do zrozumienia (najwyżej około 3 zdania), a usunięte dane zastąp „[pominięto]”. Nigdy nie cytuj briefu, tekstów klienta, nazw plików klienta ani adresów URL. Ta sekcja zastępuje rozmowę, więc niesie treść niezależnie od linku. Bez odstępstw: „Nie dotyczy.”
8. `## Link do rozmowy` - w pliku najpierw: „Do uzupełnienia przez grafika.” (czat) albo „Niedostępny: Cowork nie udostępnia sesji, zob. fragmenty wyżej.” (Cowork). W czacie tekst „Do uzupełnienia przez grafika.” zamień na „Nie dołączono.”, gdy grafik odmówi albo nie poda linku po tym, jak go poproszono; wstaw link tylko wtedy, gdy grafik go wkleił.

## Anonimizacja (zawsze, także w cytatach)

W pliku nie może być: nazw klientów i ich produktów, danych osobowych (imiona i nazwiska klientów, e-maile, telefony), imion i nazwisk współpracowników, nazw innych projektów agencji, domen i adresów URL klientów, charakterystycznych kolorów marki lub fontów pozwalających zidentyfikować klienta, nazw obrazów i plików, treści poufnych briefów, haseł i kluczy, linków do prywatnych plików i folderów. Klienta opisuj tylko uogólnioną branżą („branża spożywcza”, „usługi budowlane”) - nigdy konkretnym rodzajem firmy ani miejscowością; przy wąskich branżach uogólniaj jeszcze bardziej. Dotyczy to tekstu, cytatów i nazwy pliku. Zamiast nazwy: „[nazwa klienta]”. Plik trafi do publicznego repozytorium przez PR. **Przed zapisem** przejrzyj cały tekst i nazwę pliku pod tym kątem; jeśli coś poprawiasz, zapisz plik ponownie.

## Uczciwość

Zgłoszenie obejmuje tylko to, co jest w tej sesji. Gdy rozmowa była skracana, zaznacz to w „Kontekst” i w odpowiedzi do grafika; nie zgaduj odstępstw, których nie widzisz. Tylko gdy zgłoszenie jest częściowe, dodaj w wiadomości końcowej radę, by przy długiej pracy generować zgłoszenie wcześniej, a nie na samym końcu.

## Po zapisaniu pliku

Claude nie zna adresu własnej rozmowy - nigdy nie wymyślaj ani nie wstawiaj linku sam.

- **Czat (web/desktop):** poproś grafika, by udostępnił rozmowę (przyciski mogą nazywać się inaczej: Udostępnij, potem Maciej).
- Wybór „Każdy w organizacji” tylko gdy w rozmowie nie ma nic wrażliwego - udostępniona rozmowa pokazuje pełny kontekst.
- Zgłoszenie jest już gotowe i bez linku; udostępnienie to migawka do chwili udostępnienia, dlatego plik powstaje pierwszy. Poproś o wklejenie linku - wpiszesz go w sekcji „Link do rozmowy”. Jeśli link wygląda na prywatny (Dysk Google, „każdy z linkiem”), ostrzeż przed wpisaniem go do pliku.
- **Cowork:** nie proś o link - sesji nie da się udostępnić.

Zakończ krótką wiadomością: nazwa pliku, w razie potrzeby informacja, że zgłoszenie jest częściowe, prośba o link (czat) i przypomnienie, że plik może trafić do publicznego repozytorium, więc grafik ma go sprawdzić przed wysłaniem. Poproś o wysłanie pliku Maciejowi („wyślij ten plik Maciejowi”). Nic nie wysyłaj sam - ani plikiem, ani wiadomością.

---
name: zgloszenie
description: Zgłoszenie z sesji graficznej dla Macieja, opiekuna standardów JAMEL - plik z tym, co pomogło, co przeszkadzało, jakie były odstępstwa od standardów i jakie pytania zostały bez odpowiedzi. Używaj po /jamel-gfx:zgloszenie albo gdy grafik mówi "przygotuj zgłoszenie dla Macieja", "podsumuj sesję dla Macieja", "zgłoś uwagi do standardów". Nie używaj do innych podsumowań (notatki ze spotkania, raport dla klienta, podsumowanie projektu), tekstów, researchu informacyjnego i organizacji pracy.
---

# Zgłoszenie z sesji dla Macieja

Cel: Maciej (opiekun standardów) dostaje zwięzły plik, na podstawie którego poprawia standardy. Zgłoszenie opisuje **tylko tę sesję** i nigdy nie jest wysyłane automatycznie.

Zanim zaczniesz, załaduj `jamel-gfx:standardy` i odczytaj z niego linię `Wersja standardów: X.Y.Z` oraz sekcję „Obserwator” (kategorie odstępstw). Numer wersji bierz z tej linii - nie wpisuj go z pamięci.

## Przed pisaniem

1. **Podpis.** Jeśli nie wiesz, kto jest autorem zgłoszenia (imię grafika), zapytaj **raz**, jednym krótkim pytaniem. Gdy grafik nie chce się podpisać, wpisz „anonimowo” i nie dopytuj.
2. **Zakres sesji.** Przejrzyj rozmowę. Jeśli widzisz ślady skracania (podsumowanie kompakcji, brak początku rozmowy, odwołania do rzeczy, których nie widzisz), zgłoszenie jest **częściowe** - patrz „Uczciwość”.
3. **Środowisko:** Cowork, czat web albo desktop - wpisz w „Kontekst”; od niego zależy ostatni krok (link).

## Plik

Nazwa: `zgloszenie-jamel-gfx-RRRR-MM-DD-<krotki-temat>.md` (dzisiejsza data; temat to 2-4 słowa małymi literami z myślnikami, bez nazwy klienta, rodzaju jego firmy i miejscowości, np. `landing-branza-x`).

- Cowork: zapisz w folderze roboczym.
- Czat: wygeneruj jako plik do pobrania.

## Sekcje (dokładnie te nagłówki, w tej kolejności)

Plik zaczyna się od `# Zgłoszenie z sesji jamel-gfx`, potem:

1. `## Kontekst` - data, autor (podpis), typ projektu (landing, sklep, aplikacja) i klient opisany **wyłącznie uogólnioną branżą** („branża spożywcza”, „usługi budowlane”), bez nazwy, danych, konkretnego rodzaju firmy (np. piekarnia) ani miejscowości, linia `Wersja standardów: X.Y.Z` (odczytana ze skilla `standardy`), środowisko. Jeśli zgłoszenie jest częściowe, napisz to tutaj wprost: „Zgłoszenie częściowe: rozmowa była skracana, obejmuje tylko widoczną część sesji.”
2. `## Co pomogło` - co ze standardów realnie pomogło (konkretnie, 1-5 punktów). Brak = „Brak uwag.”
3. `## Co przeszkadzało` - co przeszkadzało albo było niejasne.
4. `## Odstępstwa` - tabela, jeden wiersz na odstępstwo: kategoria (`sprzeczne ze standardem` / `poza standardem`), co grafik zrobił, dlaczego (słowami grafika), propozycja konkretnego brzmienia zmiany w standardzie, plik i sekcja do zmiany (np. `skills/standardy/SKILL.md`, sekcja „Formularze”). Kolumny: Kategoria | Co zrobił grafik | Dlaczego | Proponowane brzmienie | Plik i sekcja. Brak odstępstw = jedno zdanie, że nie było. **Wymogi klienta nie są odstępstwem - nie wpisuj ich.**
5. `## Pytania bez odpowiedzi` - pytania, na które standard nie miał odpowiedzi.
6. `## Inne uwagi` - uwagi grafika spoza powyższych (zapytaj jednym zdaniem, czy grafik chce coś dodać; nie czekaj z plikiem, jeśli nie ma odpowiedzi).
7. `## Kluczowe fragmenty rozmowy` - przy **każdym** odstępstwie dosłowne cytaty: prośba grafika i decyzja Claude, zanonimizowane. Ta sekcja zastępuje rozmowę, więc zawsze niesie treść, niezależnie od linku.
8. `## Link do rozmowy` - w pliku najpierw: „Do uzupełnienia przez grafika.” (czat) albo „Niedostępny: Cowork nie udostępnia sesji, zob. fragmenty wyżej.” (Cowork).

Claude nie zna adresu własnej rozmowy - nigdy nie wymyślaj ani nie wstawiaj linku sam.

## Anonimizacja (zawsze, także w cytatach)

W pliku nie może być: nazw klientów i ich produktów, danych osobowych (imiona i nazwiska klientów, e-maile, telefony), treści poufnych briefów, haseł i kluczy, linków do prywatnych plików i folderów. Klienta opisuj tylko uogólnioną branżą („branża spożywcza”, „usługi budowlane”) - nigdy konkretnym rodzajem firmy ani miejscowością; dotyczy to tekstu, cytatów i nazwy pliku. Zamiast nazwy: „[nazwa klienta]”. Plik trafi do publicznego repozytorium przez PR. Przed oddaniem pliku przeczytaj go jeszcze raz pod tym kątem.

## Uczciwość

Zgłoszenie obejmuje tylko to, co jest w tej sesji. Gdy rozmowa była skracana, zaznacz to w „Kontekst” i w odpowiedzi do grafika; nie zgaduj odstępstw, których nie widzisz. Przy długiej pracy podpowiedz, by generować zgłoszenie wcześniej, a nie na samym końcu.

## Po zapisaniu pliku

- **Czat (web/desktop):** poproś grafika, by udostępnił rozmowę (Udostępnij, potem Maciej; „Każdy w organizacji” tylko gdy w rozmowie nie ma nic wrażliwego - udostępniona rozmowa pokazuje pełny kontekst) i wkleił link - wpiszesz go w sekcji „Link do rozmowy”. Zgłoszenie jest już gotowe i bez linku; udostępnienie to migawka do chwili udostępnienia, dlatego plik powstaje pierwszy. Na planie Team link działa tylko dla zalogowanych członków organizacji.
- **Cowork:** nie proś o link - sesji nie da się udostępnić. Jeśli w pracy były udostępnione artefakty (canvas), możesz je wymienić w „Inne uwagi”.

Zakończ **jednym zdaniem**: wyślij ten plik Maciejowi (podaj nazwę pliku). Nic nie wysyłaj sam - ani plikiem, ani wiadomością.

# Standardy design systemu i projektowania produktu

Standardy, według których buduje się systemy projektowe w JAMEL.

## 1. Fundamenty

Każdy projekt powinien mieć zdefiniowane:

- kolory bazowe i semantyczne;
- typografię;
- spacing scale;
- grid i breakpointy;
- promienie, obramowania i cienie;
- ikony i ilustracje;
- zasady motion;
- standardy dostępności.

Tokeny muszą mieć jasno określoną funkcję.

## 2. System kolorów

Przykładowa struktura:

- `color.brand.primary`
- `color.brand.secondary`
- `color.text.primary`
- `color.text.secondary`
- `color.text.disabled`
- `color.surface.default`
- `color.surface.subtle`
- `color.border.default`
- `color.action.primary.default`
- `color.action.primary.hover`
- `color.feedback.success`
- `color.feedback.warning`
- `color.feedback.error`
- `color.feedback.info`

Sprawdzaj kontrast rzeczywistych par kolorów. Nie polegaj wyłącznie na kolorze przy komunikowaniu statusu.

## 3. System typografii

Każdy styl określ przez:

- nazwę semantyczną;
- rodzinę fontu;
- rozmiar;
- weight;
- line-height;
- letter spacing;
- zastosowanie;
- zachowanie responsywne.

Uwzględniaj Display, Heading, Body, Label i Caption. Sprawdzaj polskie znaki i czytelność na małych ekranach.

## 4. Spacing i layout

Ustal spójną skalę odstępów, np. bazującą na wielokrotnościach 4 lub 8 px. Określ:

- szerokość kontenera;
- maksymalną szerokość treści;
- liczbę kolumn;
- gutter;
- marginesy;
- odstępy sekcji;
- zasady wyrównania.

Nie stosuj przypadkowych wartości.

## 5. Komponenty

Dla każdego komponentu dokumentuj:

- przeznaczenie;
- elementy składowe;
- warianty;
- rozmiary;
- properties;
- stany;
- zachowanie responsive;
- dostępność;
- zasady użycia i antywzorce.

Podstawowe komponenty: Button, Link, Input, Select, Checkbox, Radio, Switch, Textarea, Tooltip, Alert, Badge, Card, Modal, Drawer, Tabs, Accordion, Breadcrumbs, Pagination, Table, Navigation, Dropdown, Toast, Empty State, Skeleton i Progress.

## 6. Stany komponentów

Uwzględnij:

- Default;
- Hover;
- Focus-visible;
- Active / Pressed;
- Disabled;
- Loading;
- Error;
- Success;
- Read-only, jeśli wymagany.

## 7. Formularze

Formularze powinny mieć:

- widoczne etykiety;
- instrukcje;
- walidację;
- komunikaty błędów powiązane z polami;
- czytelne potwierdzenie sukcesu;
- odpowiednie stany focus i disabled.

Nie używaj placeholderów jako jedynej formy etykietowania.

## 8. WCAG 2.2 AA

Sprawdzaj:

- kontrast tekstu i elementów nietekstowych;
- widoczny i niezasłonięty focus;
- obsługę klawiaturą;
- logiczną kolejność fokusu;
- etykiety formularzy;
- tekst alternatywny;
- semantyczne nagłówki;
- dostępne nazwy kontrolek;
- komunikaty statusów i błędów;
- skalowanie tekstu;
- reflow;
- rozmiar celów dotykowych;
- brak informacji przekazywanych wyłącznie kolorem;
- respektowanie `prefers-reduced-motion`.

Nie deklaruj pełnej zgodności bez testów automatycznych i manualnych.

## 9. Responsive design

Dla każdego breakpointu określ:

- liczbę kolumn;
- zachowanie nawigacji;
- kolejność treści;
- typografię;
- spacing;
- zachowanie obrazów;
- widoczność komponentów;
- interakcje dotykowe.

Breakpointy dobieraj na podstawie zachowania layoutu, nie tylko popularnych rozmiarów urządzeń. Domyślne punkty kontrolne JAMEL do weryfikacji: 375 / 768 / 1440 px.

## 10. Dark mode

Nie odwracaj mechanicznie kolorów. Zdefiniuj osobne semantyczne wartości powierzchni, tekstu, obramowań i stanów. Sprawdź kontrast w obu motywach.

## 11. Dokumentacja

Dokumentacja powinna zawierać:

- foundations;
- listę tokenów;
- bibliotekę komponentów;
- warianty i stany;
- przykłady użycia;
- antywzorce;
- zasady dostępności;
- status komponentów;
- changelog.

## Tokeny w formacie DTCG

Gdy tokeny mają trafić do kodu lub narzędzi (Figma Variables, Style Dictionary), zapisuj je w formacie DTCG (Design Tokens Community Group, JSON):

- każdy token ma `$value` (wartość) i `$type` (np. `color`, `dimension`);
- tokeny grupuje się w zagnieżdżone obiekty - ścieżka grup tworzy nazwę, np. `color.brand.primary`;
- `$type` można ustawić raz na grupie, wtedy dziedziczą go wszystkie tokeny w środku;
- token semantyczny odwołuje się do prymitywu przez alias w klamrach, np. `{color.brand.primary}`;
- nazwy opisują funkcję, nie wygląd (zgodnie z sekcją 1 i 2);
- wartości zapisuj jako stringi (`"#C2410C"`, `"16px"`) - to forma zgodna ze Style Dictionary i wcześniejszym szkicem DTCG; aktualna specyfikacja DTCG 2025.10 zapisuje kolor jako obiekt, więc przy imporcie do narzędzia, które tego wymaga, trzeba wartości przekonwertować.

Przykład:

```json
{
  "color": {
    "$type": "color",
    "brand": {
      "primary": { "$value": "#C2410C" }
    },
    "text": {
      "primary": { "$value": "#2B2420" }
    }
  },
  "spacing": {
    "$type": "dimension",
    "4": { "$value": "16px" }
  },
  "font": {
    "$type": "fontFamily",
    "heading": { "$value": "Fraunces" }
  }
}
```

Wartości w przykładzie są ilustracją formatu, nie wartościami do przepisania do projektu.

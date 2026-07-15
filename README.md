# JAMEL — Claude Code marketplace

Repozytorium jest **marketplace'em** Claude Code (`name: "jamel"`) hostującym pluginy agencji JAMEL.
Repo jest **publiczne** — instalacja nie wymaga konta GitHub ani żadnych uprawnień.

```text
.claude-plugin/marketplace.json   # manifest marketplace'u (2 pluginy + allowCrossMarketplaceDependenciesOn)
jamel-pm/                         # plugin: toolkit PM/Account (wyceny → .xlsx; planowane spec-i i analiza stron)
jamel-devx/                       # plugin: plug-and-play dev experience dla zespołu
```

## Pluginy

| Plugin | Opis | Wejście |
|---|---|---|
| **jamel-pm** | Toolkit PM/Account: wyceny wg metodyki JAMEL (widełkowe min/max i fixed-price), render `.xlsx`. Planowane: specyfikacje techniczne, specyfikacje graficzne, analiza stron www. | `/wycena` |
| **jamel-devx** | Wspólne ustawienia + statusline, kompresja tokenów (RTK), dyscyplina minimalnego kodu (ponytail), org-owy ClickUp MCP, kuratorowane auto-updatujące pluginy. | `/jamel-tour`, `/jamel-setup` |

## Szybki start

```text
/plugin marketplace add maciejguc/jamel-plugin
/plugin install jamel-devx@jamel      # DevX bundle (pociąga superpowers, frontend-design, code-review, context7)
/plugin install jamel-pm@jamel        # toolkit PM (wyceny)
/jamel-tour                           # oprowadzenie po komponentach
/jamel-setup                          # konfiguracja zespołowa (pyta o zgodę przed każdym zapisem)
```

Działa w Claude Code **CLI i aplikacji desktopowej** (współdzielą `~/.claude`). W sesjach **webowych**
(claude.ai/code) pluginy ładuje się przez `.claude/settings.json` projektu
(`extraKnownMarketplaces` + `enabledPlugins`).

> **Migracja z `jamel-wycena`:** plugin został przemianowany na `jamel-pm`. Jeśli masz zainstalowaną
> starą wersję: `/plugin uninstall jamel-wycena@jamel`, potem `/plugin install jamel-pm@jamel`.

Szczegóły: [`jamel-devx/README.md`](jamel-devx/README.md) i [`jamel-pm/README.md`](jamel-pm/README.md).

## Aktualizacje

- **First-party pluginy** (`jamel-pm`, `jamel-devx`) używają commit-SHA versioning — **każdy merge do
  `main` = nowa wersja**. Odśwież ręcznie: `/plugin marketplace update jamel`, albo włącz auto-update
  marketplace'u: `/plugin` → zakładka *Marketplaces* → *Enable auto-update* (dla marketplace'ów spoza
  Anthropic domyślnie wyłączone).
- **Zmiany trafiają do `main` wyłącznie przez pull requesty** (konwencja repo — patrz `CLAUDE.md`);
  bezpośrednie pushe na `main` są zabronione.
- **Narzędzia zewnętrzne** są dołączane jako `dependencies` rozwiązywane z ich **oryginalnych**
  marketplace'ów (`claude-plugins-official`, `openai-codex`, ponytail) — aktualizują się ze źródła,
  bez forków i bez ręcznego utrzymania.

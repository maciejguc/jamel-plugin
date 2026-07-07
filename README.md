# JAMEL — Claude Code marketplace

Repozytorium jest **marketplace'em** Claude Code (`name: "jamel"`) hostującym pluginy agencji JAMEL.

```text
.claude-plugin/marketplace.json   # manifest marketplace'u (2 pluginy + allowCrossMarketplaceDependenciesOn)
jamel-pm/                         # plugin: toolkit PM/Account (wyceny → .xlsx; planowane spec-i i analiza stron)
jamel-devx/                       # plugin: plug-and-play dev experience dla zespołu
```

## Pluginy

| Plugin | Opis | Wejście |
|---|---|---|
| **jamel-pm** | Toolkit PM/Account: wyceny wg metodyki JAMEL (widełkowe min/max i fixed-price), render `.xlsx`. Planowane: specyfikacje techniczne, specyfikacje graficzne, analiza stron www. | `/wycena` |
| **jamel-devx** | Wspólne ustawienia + statusline, RTK, ClickUp MCP, kuratorowane auto-updatujące pluginy. | `/jamel-setup` |

## Szybki start

```text
/plugin marketplace add maciejguc/jamel-plugin
/plugin install jamel-devx@jamel      # DevX bundle (pociąga superpowers, frontend-design, code-review, context7)
/plugin install jamel-pm@jamel        # toolkit PM (wyceny)
/jamel-setup                          # konfiguracja zespołowa
```

> **Migracja z `jamel-wycena`:** plugin został przemianowany na `jamel-pm`. Jeśli masz zainstalowaną
> starą wersję: `/plugin uninstall jamel-wycena@jamel`, potem `/plugin install jamel-pm@jamel`.

Szczegóły: [`jamel-devx/README.md`](jamel-devx/README.md) i [`jamel-pm/README.md`](jamel-pm/README.md).

## Strategia aktualizacji

Marketplace JAMEL utrzymuje **wyłącznie** pluginy first-party (`jamel-pm`, `jamel-devx`). Narzędzia
zewnętrzne są dołączane jako `dependencies` rozwiązywane z ich **oryginalnych** marketplace'ów
(`claude-plugins-official`, `openai-codex`) — dzięki czemu aktualizują się ze źródła, bez forków i bez
ręcznego utrzymania. First-party pluginy używają commit-SHA versioning (każdy push = nowa wersja).

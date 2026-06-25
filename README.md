# JAMEL — Claude Code marketplace

Repozytorium jest **marketplace'em** Claude Code (`name: "jamel"`) hostującym pluginy agencji JAMEL.

```text
.claude-plugin/marketplace.json   # manifest marketplace'u (2 pluginy + allowCrossMarketplaceDependenciesOn)
jamel-wycena/                     # plugin: automatyzacja wyceny → .xlsx identyczny z ELA
jamel-devx/                       # plugin: plug-and-play dev experience dla zespołu
```

## Pluginy

| Plugin | Opis | Wejście |
|---|---|---|
| **jamel-wycena** | Wycena projektu IT/Marketing w stylu ELA, render pixel-identycznego `.xlsx`. | `/wycena` |
| **jamel-devx** | Wspólne ustawienia + statusline, RTK, ClickUp MCP, kuratorowane auto-updatujące pluginy. | `/jamel-setup` |

## Szybki start

```text
/plugin marketplace add maciejguc/jamel-plugin
/plugin install jamel-devx@jamel      # DevX bundle (pociąga superpowers, frontend-design, code-review, context7)
/plugin install jamel-wycena@jamel    # generator wycen
/jamel-setup                          # konfiguracja zespołowa
```

Szczegóły: [`jamel-devx/README.md`](jamel-devx/README.md) i [`jamel-wycena/README.md`](jamel-wycena/README.md).

## Strategia aktualizacji

Marketplace JAMEL utrzymuje **wyłącznie** pluginy first-party (`jamel-wycena`, `jamel-devx`). Narzędzia
zewnętrzne są dołączane jako `dependencies` rozwiązywane z ich **oryginalnych** marketplace'ów
(`claude-plugins-official`, `openai-codex`) — dzięki czemu aktualizują się ze źródła, bez forków i bez
ręcznego utrzymania. First-party pluginy używają commit-SHA versioning (każdy push = nowa wersja).

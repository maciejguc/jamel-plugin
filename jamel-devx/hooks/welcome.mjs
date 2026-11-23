#!/usr/bin/env node
/**
 * One-time Polish welcome for jamel-devx.
 *
 * Runs on SessionStart. Emits a short instruction (added to Claude's context)
 * the FIRST time only — gated by a marker file in the plugin's persistent data
 * dir (${CLAUDE_PLUGIN_DATA}, which survives plugin updates). Cross-platform
 * (pure Node, no shell), so it works on macOS, Linux and Windows alike.
 */
import { mkdirSync, existsSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const dataDir = process.env.CLAUDE_PLUGIN_DATA;
if (!dataDir) process.exit(0); // not running in plugin context — do nothing

const marker = join(dataDir, ".welcomed");
try {
  if (existsSync(marker)) process.exit(0); // already welcomed
  mkdirSync(dataDir, { recursive: true });
  writeFileSync(marker, new Date().toISOString() + "\n");
} catch {
  process.exit(0); // never break a session over the welcome
}

// This text is injected into Claude's context on first run. It instructs Claude
// to greet the user (in Polish) and point them at the onboarding command.
const ctx = [
  "[jamel-devx — pierwsze uruchomienie]",
  "Przywitaj użytkownika PO POLSKU. Najpierw przedstaw plugin w 2–3 zdaniach: JAMEL DevX to",
  "plug-and-play środowisko Claude Code dla zespołu JAMEL — wspólne ustawienia zespołowe i statusline,",
  "kompresja tokenów (RTK), dyscyplina minimalnego kodu (ponytail), org-owy ClickUp MCP oraz",
  "kuratorowane, samo-aktualizujące się pluginy (superpowers, frontend-design, code-review, context7).",
  "Następnie wypisz WYRAŹNIE, jako krótką listę, dwie komendy na start:",
  "1. /jamel-tour — interaktywne oprowadzenie: co zawiera plugin, jak działa każdy komponent i w jakim",
  "stanie jest na tej maszynie (nic nie instaluje).",
  "2. /jamel-setup — konfiguracja: ustawienia zespołowe, statusline, instalacja RTK + ponytail,",
  "konwencje CLAUDE.md (pokazuje diff i pyta o zgodę przed każdym zapisem).",
  "Zarekomenduj zaczęcie od /jamel-tour. Nie wykonuj żadnej z tych komend automatycznie.",
].join(" ");

process.stdout.write(ctx + "\n");

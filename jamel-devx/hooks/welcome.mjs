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
  "Przywitaj użytkownika PO POLSKU (2–3 zdania). Powiedz krótko, że plugin JAMEL DevX daje:",
  "wspólne ustawienia + statusline, kompresję tokenów (RTK + caveman), MCP ClickUp oraz kuratorowane",
  "pluginy (superpowers, frontend-design, code-review, context7). Zaproponuj uruchomienie komendy",
  "/jamel-tour (interaktywne oprowadzenie) oraz /jamel-setup (konfiguracja). Nie wykonuj ich automatycznie.",
].join(" ");

process.stdout.write(ctx + "\n");

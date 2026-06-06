# Useful-lists — Project Memory

> Auto-synced | 711 observations

## 🛡️ GLOBAL SAFETY RULES

- **NEVER** run `git clean -fd` or `git reset --hard` without checking `git log` and verifying commits exist.
- **NEVER** delete untracked files or folders blindly. Always backup or stash before bulk edits.

## 🧭 ACTIVE CONTEXT

> Always read `.cursor/active-context.md` for exact instructions on the specific file you are currently editing. It updates dynamically.

## 🔴 STOP — READ THESE FIRST

- **Agent: follow existing project patterns — don't introduce a different style** — Agent: follow existing project patterns — don't introduce a different style
- **Agent: don't generate code with "any" type — define proper TypeScript types** — Agent: don't generate code with "any" type — define proper TypeScript types
- **Agent: always handle loading/error states — don't just render data** — Agent: always handle loading/error states — don't just render data
- **Agent: don't use deprecated APIs — check library version, use current API** — Agent: don't use deprecated APIs — check library version, use current API
- **Agent: check existing code before creating utility functions — avoid duplicates** — Agent: check existing code before creating utility functions — avoid duplicates

## 📐 Conventions

- Version your API from day 1 (/api/v1/)
- Use consistent response format across all endpoints
- Implement soft delete for important data — don't hard delete without confirmation
- Handle timezone correctly — store UTC, display in user's timezone
- Make layouts responsive from the start — mobile-first approach
- Disable submit button during form submission — prevent double-submit
- Always add empty states ("No items yet" with call-to-action)
- Always add error states with retry button — not just blank screen

## ⚡ Available Tools (ON-DEMAND only)
- `sys_core_02(title, content, category)` — Save a note + auto-detect conflicts
- `sys_core_03(items[])` — Save multiple notes in 1 call
- `sys_core_01(text)` — Search memory for architecture, past fixes, decisions
- `sys_core_05(text)` — Full-text search for details
- `sys_core_16()` — Check compiler errors after edits

> ℹ️ DO NOT call sys_core_14() or sys_core_08() at startup — context above IS your context.

---
*Auto-synced | 2026-06-06*

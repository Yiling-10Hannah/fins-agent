---
name: scaffold-week
description: Use when a student says scaffold a week, standardize a week folder, or backfill fins2026/weekN with the standard weekly structure.
argument-hint: "--target fins2026/weekN [--title '...']"
---

# Scaffold Week Skill

Read `docs/ai/workflows/scaffold-week.md` and follow it as the canonical
workflow.

Typical triggers:

- "scaffold week 3"
- "standardize the week folders"
- "backfill week5 with the full weekly structure"

Preferred deterministic command:

- `python tools/workflow.py scaffold-week --target fins2026/weekN [--title ...]`

If the workflow doc conflicts with older tool-specific instructions, the
shared workflow doc wins.

---
name: scaffold-week
description: Use when a student says scaffold a week, standardize a weekly folder, or backfill fins2026/weekN with the standard weekly structure.
argument-hint: "--target fins2026/weekN [--title '...']"
---

# Scaffold Week Skill

Read `docs/ai/workflows/scaffold-week.md` and follow it as the canonical
workflow.

Typical triggers:

- "scaffold week 4"
- "standardize week7"
- "backfill the week folders with the standard structure"

Preferred deterministic command:

- `python tools/workflow.py scaffold-week --target fins2026/weekN [--title ...]`

If the workflow doc conflicts with older tool-specific instructions, the
shared workflow doc wins.

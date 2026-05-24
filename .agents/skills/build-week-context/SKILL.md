---
name: build-week-context
description: Use when a student says build week context, refresh guidance for a week, or summarize the current week folder into generated week, data, and output context files.
argument-hint: "[--target fins2026/weekN]"
---

# Build Week Context Skill

Read `docs/ai/workflows/build-week-context.md` and follow it as the canonical
workflow.

Typical triggers:

- "build week context"
- "refresh the week guidance files"
- "summarize this week folder"

Preferred deterministic command:

- `python tools/workflow.py build-week-context --target fins2026/weekN`

If the workflow doc conflicts with older tool-specific instructions, the
shared workflow doc wins.

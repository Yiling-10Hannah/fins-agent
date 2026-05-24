---
name: outline
description: Use when a student says outline the report, check the report structure, or review section balance and markers.
argument-hint: "[target]"
---

# Outline Skill

Read `docs/ai/workflows/outline.md` and follow it as the canonical
workflow.

Typical triggers:

- "outline my report"
- "check the structure"
- "review section balance"

Preferred deterministic command:

- `python tools/workflow.py outline [target]`

If the workflow doc conflicts with older tool-specific instructions, the
shared workflow doc wins.

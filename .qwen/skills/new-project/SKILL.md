---
name: new-project
description: Use when a student says create a new project, scaffold a project, or make a projects/ folder with report, code, scripts, data, and results.
argument-hint: "<project_name> [--description '...'] [--datasets '...'] [--notes '...'] [--setup-paper]"
---

# New Project Skill

Read `docs/ai/workflows/new-project.md` and follow it as the canonical
workflow.

Typical triggers:

- "create a new project"
- "scaffold a project under projects/"
- "make me a project folder for my report"

Preferred deterministic command:

- `python tools/workflow.py new-project <name> [--description ...] [--datasets ...] [--notes ...] [--setup-paper]`

If the workflow doc conflicts with older tool-specific instructions, the
shared workflow doc wins.

---
name: word-report
description: Use when a student asks to create, inspect, format, troubleshoot, or improve a Word report or .docx coursework paper using the repo Word-first writing rules.
argument-hint: "[target] [--title '...']"
---

# Word Report Skill

Read `docs/ai/workflows/word-report.md` and follow it as the canonical
workflow.

Typical triggers:

- "create a Word report"
- "check my Word document"
- "format this report in Word"
- "make this .docx coursework-ready"

Preferred deterministic commands:

- `python tools/workflow.py setup-paper --title "..." [--authors "..."] [--topic "..."] [--target .]`
- `python tools/workflow.py word-report [target]`
- `python tools/workflow.py outline [target]`
- `python tools/workflow.py proofread [target]`

If the workflow doc conflicts with older tool-specific instructions, the
shared workflow doc wins.

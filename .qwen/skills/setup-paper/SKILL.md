---
name: setup-paper
description: Use when a student says set up a paper, create a Word report, or scaffold report/report.docx; legacy LaTeX is supported only when explicitly requested with --format latex.
argument-hint: "<title> [--authors 'Name (Student ID, Course Code)'] [--topic 'one-line description']"
---

# Setup Paper Skill

Read `docs/ai/workflows/setup-paper.md` and follow it as the canonical
workflow.

Typical triggers:

- "set up a paper"
- "create a Word report"
- "create report/report.docx"
- "copy the report boilerplate"

Preferred deterministic command:

- `python tools/workflow.py setup-paper --title \"...\" [--authors \"...\"] [--topic \"...\"] [--target .]`
- `python tools/workflow.py setup-paper --format latex --title \"...\" [--target .]`

If the workflow doc conflicts with older tool-specific instructions, the
shared workflow doc wins.

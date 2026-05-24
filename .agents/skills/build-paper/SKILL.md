---
name: build-paper
description: Use when a student explicitly asks to compile a legacy LaTeX paper, build a .tex report PDF, or run pdflatex and bibtex.
argument-hint: "[target] [--quick]"
---

# Build Paper Skill

Read `docs/ai/workflows/build-paper.md` and follow it as the canonical
workflow.

Typical triggers:

- "build the paper"
- "compile my report"
- "make the PDF"

Preferred deterministic command:

- `python tools/workflow.py build-paper [target] [--quick]`

If the workflow doc conflicts with older tool-specific instructions, the
shared workflow doc wins.

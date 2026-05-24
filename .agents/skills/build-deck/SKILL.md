---
name: build-deck
description: Use when a student asks to build, revise, or structure a PowerPoint-first presentation deck; legacy LaTeX/Beamer is supported only when explicitly requested.
argument-hint: "[target]"
---

# Build Deck Skill

Read `docs/ai/workflows/build-deck.md` and follow it as the canonical
workflow.

Typical triggers:

- "build the deck"
- "revise these slides"
- "make my PowerPoint presentation"
- "turn my report into a presentation"

PowerPoint is the default deck format. Do not use LaTeX, Beamer, or
`pdflatex` unless the student explicitly asks for legacy `.tex` slides.

Legacy deterministic command, only for explicit Beamer targets:

- `python tools/workflow.py build-deck [path/to/deck.tex]`

If the workflow doc conflicts with older tool-specific instructions, the
shared workflow doc wins.

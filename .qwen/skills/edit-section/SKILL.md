---
name: edit-section
description: Use when a student says revise this section, improve clarity, tighten the writing, or edit existing Word-first .docx report text; legacy LaTeX is supported only when the target is explicitly .tex.
argument-hint: "<section_key_or_goal>"
---

# Edit Section Skill

Read `docs/ai/workflows/edit-section.md` and follow it as the canonical
workflow.

Typical triggers:

- "revise this section"
- "tighten the writing"
- "improve clarity in this Word report section"

Preferred deterministic commands:

- `python tools/workflow.py outline [target]`
- `python tools/workflow.py proofread [target] [--section section_key]`

If the workflow doc conflicts with older tool-specific instructions, the
shared workflow doc wins.

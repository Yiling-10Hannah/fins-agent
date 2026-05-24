---
name: proofread
description: Use when a student says proofread this section, check mechanical writing issues, or scan Word/.docx report prose for spacing and formatting problems; legacy LaTeX is supported only when an explicit .tex target is supplied.
argument-hint: "[target] [--section section_key] [--lines start-end]"
---

# Proofread Skill

Read `docs/ai/workflows/proofread.md` and follow it as the canonical
workflow.

Typical triggers:

- "proofread this"
- "check the writing mechanics"
- "scan this section for spacing and punctuation issues"

Preferred deterministic command:

- `python tools/workflow.py proofread [target] [--section section_key] [--lines start-end]`

If the workflow doc conflicts with older tool-specific instructions, the
shared workflow doc wins.

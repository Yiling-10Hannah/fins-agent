---
name: write-section
description: Use when a student says draft a section, write my introduction, or create new Word-first .docx report text using the repo writing rules; legacy LaTeX is supported only when the target is explicitly .tex.
argument-hint: "<section_key_or_goal>"
---

# Write Section Skill

Read `docs/ai/workflows/write-section.md` and follow it as the canonical
workflow.

Typical triggers:

- "draft this section"
- "write my introduction"
- "create a new subsection for my Word report"

Preferred deterministic commands:

- `python tools/workflow.py outline [target]`
- `python tools/workflow.py proofread [target] [--section section_key]`

If the workflow doc conflicts with older tool-specific instructions, the
shared workflow doc wins.

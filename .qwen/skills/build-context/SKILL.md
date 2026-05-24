---
name: build-context
description: Use when a student says build context, generate paper-context.md, or summarize a Word/.docx draft report into guidance/paper-context.md; legacy LaTeX, Markdown, and PDF sources are supported when explicitly supplied.
argument-hint: "[source ...]"
---

# Build Context Skill

Read `docs/ai/workflows/build-context.md` and follow it as the canonical
workflow.

Typical triggers:

- "build context"
- "generate guidance/paper-context.md"
- "summarize this draft into report context"

Preferred deterministic command:

- `python tools/workflow.py build-context [source ...]`

If the workflow doc conflicts with older tool-specific instructions, the
shared workflow doc wins.

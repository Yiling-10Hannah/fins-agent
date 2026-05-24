---
name: latex-doctor
description: Use when a student explicitly says fix this legacy LaTeX file, clean up LaTeX markers or comments, or diagnose compile problems in a .tex report.
argument-hint: "[target] [--mode all|comments|markers|compile]"
---

# LaTeX Doctor Skill

Read `docs/ai/workflows/latex-doctor.md` and follow it as the canonical
workflow.

Typical triggers:

- "fix this LaTeX file"
- "clean up marker problems"
- "diagnose why the report will not compile"

Preferred deterministic command:

- `python tools/workflow.py latex-doctor [target] [--mode all|comments|markers|compile]`

If the workflow doc conflicts with older tool-specific instructions, the
shared workflow doc wins.

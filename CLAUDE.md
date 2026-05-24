## Project Scope

Fintech coursework toolkit for students. Data analysis, portfolio
construction, and academic writing with Word-first reports built for working closely
with AI.

## Quick Reference

- Read `AGENTS.md` for project conventions and task routing
- Read `docs/ai/core.md` for shared AI context
- Shared workflow logic lives in `docs/ai/workflows/`
- Shared writing rules live in `docs/ai/rules/`
- Claude wrappers live in `.claude/skills/`
- Shared utilities live in `fintools/`
- Figure helpers live in `fintools/figures/`
- Course weeks eventually span `fins2026/week0` through `fins2026/week10`.
- Public student releases may expose only the published weeks so far; the
  current release includes `fins2026/week0` through `fins2026/week5`.

## Setup

New students: use `/onboard`.

Or run manually with the repo interpreter:

- Windows: `.\.venv\Scripts\python.exe tools/setup_student.py`
- macOS/Linux: `./.venv/bin/python tools/setup_student.py`

## Package Management

This repo uses Python 3.13, a repo-local `.venv`, and pip-managed
requirements files. In a terminal, use the repo interpreter:

- Windows: `.\.venv\Scripts\python.exe`
- macOS/Linux: `./.venv/bin/python`

Then run `-m pip install -r requirements.txt -r requirements-dev.txt` to
install packages and `tools/workflow.py ...` for shared deterministic
helpers. See `AGENTS.md` for details.

If a student asks to install a Python package, update the correct
requirements file first and then install from the repo interpreter. In
PyCharm, use the built-in terminal at the repo root for the install step.

## Writing Rules

Writing rules in `docs/ai/rules/` enforce academic style. See
`docs/ai/rules/academic-writing.md` for banned words, active voice, and
Cochrane writing principles. `.claude/rules/` remains a Claude-facing
compatibility surface. See `docs/ai/writing.md` for the shared workflow
guide.

## Skills

Claude skills are wrappers over the shared workflow docs in
`docs/ai/workflows/`.

- `/onboard`
- `/new-project`
- `/setup-paper`
- `/word-report`
- `/write-section`
- `/edit-section`
- `/proofread`
- `/build-paper` for legacy LaTeX reports
- `/build-deck`
- `/build-figure`
- `/audit-app`
- `/build-context`
- `/outline`
- `/latex-doctor` for legacy LaTeX reports

For FT-style dataframe figure suites, use `/build-figure` and the shared
`docs/ai/workflows/build-figure.md` workflow. Prefer narrative suites for broad
requests such as "make figures for my data".

## Boilerplate

Use `/setup-paper` to create `report/report.docx` in a project. Legacy LaTeX
templates live in `boilerplate/` and require explicit opt-in.

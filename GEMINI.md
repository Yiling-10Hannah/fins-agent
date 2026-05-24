# Gemini CLI Guide

This file is auto-loaded by Gemini CLI as project context.

@AGENTS.md

## Gemini Repo Surfaces

- `GEMINI.md`
- `.gemini/settings.json`
- `.gemini/commands/`
- `docs/ai/workflows/`
- `docs/ai/rules/`

## How Gemini Should Work Here

- Use the project commands in `.gemini/commands/` for repo workflows such as
  `/onboard`, `/new-project`, `/setup-paper`, and `/word-report`.
- Shared workflow docs in `docs/ai/workflows/` are the canonical task logic.
- Writing, Word reporting, citation, presentation, and legacy LaTeX rules
  live in `docs/ai/rules/`.
- Read `docs/ai/gemini.md` for the student guide.
- If Gemini CLI in PyCharm behaves differently from Gemini CLI in a normal
  terminal, trust the terminal path and use `docs/ai/gemini-pycharm.md` for
  host-specific setup.
- For Python package install requests, update `requirements.txt` or
  `requirements-dev.txt` first and run the install from the repo interpreter
  with `-m pip`, preferably in PyCharm's built-in terminal when using
  PyCharm.
- For FT-style dataframe figure suites, use `/build-figure` and the shared
  `docs/ai/workflows/build-figure.md` workflow. Prefer narrative suites for
  broad requests such as "make figures for my data".
- For Streamlit app audits, use `/audit-app` and the shared
  `docs/ai/workflows/audit-app.md` workflow.

If a Gemini command conflicts with a shared workflow doc, the shared
workflow doc wins.

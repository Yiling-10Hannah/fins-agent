# Qwen Code Guide

This file is the Qwen-specific overlay for this repo. Root `AGENTS.md`
provides the shared repo instructions.

## Qwen Repo Surfaces

- `AGENTS.md`
- `QWEN.md`
- `.qwen/settings.json`
- `.qwen/skills/`
- `docs/ai/workflows/`
- `docs/ai/rules/`

## How Qwen Should Work Here

- Qwen can auto-invoke matching project skills in `.qwen/skills/`.
- If explicit invocation is needed, use `/skills <skill-name>`.
- Shared workflow docs in `docs/ai/workflows/` are the canonical task logic.
- Writing, Word reporting, citation, presentation, and legacy LaTeX rules
  live in `docs/ai/rules/`.
- Read `docs/ai/qwen.md` for the student guide.
- If Qwen Code in PyCharm behaves differently from Qwen Code in a normal
  terminal, trust the terminal path and use `docs/ai/qwen-pycharm.md` for
  host-specific setup.
- For Python package install requests, update `requirements.txt` or
  `requirements-dev.txt` first and run the install from the repo interpreter
  with `-m pip`, preferably in PyCharm's built-in terminal when using
  PyCharm.
- For FT-style dataframe figure suites, use the `build-figure` skill and the
  shared `docs/ai/workflows/build-figure.md` workflow. Prefer narrative suites
  for broad requests such as "make figures for my data".
- For Streamlit app audits, use the `audit-app` skill and the shared
  `docs/ai/workflows/audit-app.md` workflow.

If a Qwen skill conflicts with a shared workflow doc, the shared workflow
doc wins.

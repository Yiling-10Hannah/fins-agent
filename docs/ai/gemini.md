# Gemini Workflow Guide

This guide is for students using Gemini CLI in this repo.

If you are using Gemini CLI from PyCharm, also read
`docs/ai/gemini-pycharm.md`.

## Gemini Repo Structure

Gemini support in this repo is built from:

- `GEMINI.md`
- `.gemini/settings.json`
- `.gemini/commands/`
- `docs/ai/workflows/`

`GEMINI.md` imports `AGENTS.md`, so Gemini sees both the shared repo rules
and the Gemini-specific overlay.

## How Gemini Works Here

- Start with `GEMINI.md` for repo behavior and routing.
- Use the project commands in `.gemini/commands/` for repo workflows.
- Shared workflow logic lives in `docs/ai/workflows/`.
- Shared writing, Word reporting, citation, presentation, and legacy LaTeX
  rules live in `docs/ai/rules/`.

If a Gemini command wrapper and a shared workflow doc differ, the shared
workflow doc wins.

## First 60 Seconds In Gemini CLI

1. Launch Gemini CLI from the repo root.
2. If you are setting up the repo, start with `/onboard`.
3. Use repo commands such as `/new-project`, `/setup-paper`, or
   `/word-report` for concrete workflows.
4. If Gemini seems off, reopen it from the repo root and point it at
   `GEMINI.md` or the matching file in `docs/ai/workflows/`.

## When Gemini Seems Confused

- Confirm Gemini was launched from the repo root.
- Prefer repo commands such as `/onboard` or `/setup-paper` over vague
  requests when a command already exists.
- If a command behaves unexpectedly, open `GEMINI.md` and the matching
  workflow doc in `docs/ai/workflows/`.
- If Gemini in PyCharm behaves differently from Gemini in a normal
  terminal, trust the terminal path as the reference behavior.

## Common Workflow Entry Points

| Goal | Best repo surface |
|------|-------------------|
| First-time setup | `/onboard` |
| Create a project | `/new-project` |
| Scaffold a week | `/scaffold-week` |
| Set up a Word report | `/setup-paper`, `/word-report` |
| Write or edit report text | `/write-section`, `/edit-section` |
| Build a PowerPoint deck | `/build-deck` |
| Compile a legacy LaTeX paper | `/build-paper` |
| Build or export figures | `/build-figure` |
| Build a Streamlit app | `/build-app` |
| Build report context | `/build-context` |
| Build week context | `/build-week-context` |
| Proofread or outline a report | `/proofread`, `/outline` |
| Diagnose legacy LaTeX issues | `/latex-doctor` |

## Figure Suites

Use `/build-figure` for both single figures and dataframe-driven figure
suites. For broad requests such as "make FT-style figures for my data", Gemini
should follow `docs/ai/workflows/build-figure.md` and default to a narrative
suite when the data has recognizable structure:

```bash
python tools/workflow.py build-figure-suite data/my_data.csv --style ft --narrative --output results/figures
```

When a dataframe is already loaded in Python or PyCharm, use
`docs/ai/examples/figure_suite_from_dataframe.py` as the compact example for
`create_figure_suite(df, style="ft", docx=True, narrative=True)`.

## PyCharm Boundary

Gemini CLI in PyCharm is intended to use the same repo-native Gemini
surfaces: `GEMINI.md`, `.gemini/settings.json`, `.gemini/commands/`, and
the shared workflow docs. If the ACP path drifts, treat the normal terminal
Gemini CLI path as the reference behavior.

For the PyCharm-specific setup and ACP installation path, use
`docs/ai/gemini-pycharm.md`.

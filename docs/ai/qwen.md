# Qwen Workflow Guide

This guide is for students using Qwen Code in this repo.

If you are using Qwen Code from PyCharm, also read
`docs/ai/qwen-pycharm.md`.

## Qwen Repo Structure

Qwen support in this repo is built from:

- `AGENTS.md`
- `QWEN.md`
- `.qwen/settings.json`
- `.qwen/skills/`
- `docs/ai/workflows/`

Root `AGENTS.md` carries the shared repo rules. `QWEN.md` is the
Qwen-specific overlay configured in `.qwen/settings.json`.

## How Qwen Works Here

- Start with `AGENTS.md` and `QWEN.md` for repo behavior and routing.
- Qwen can auto-invoke matching project skills from `.qwen/skills/`.
- If explicit invocation is needed, use `/skills <skill-name>`.
- Shared workflow logic lives in `docs/ai/workflows/`.
- Shared writing, Word reporting, citation, presentation, and legacy LaTeX
  rules live in `docs/ai/rules/`.

If a Qwen skill wrapper and a shared workflow doc differ, the shared
workflow doc wins.

## First 60 Seconds In Qwen Code

1. Launch Qwen Code from the repo root.
2. Ask naturally for onboarding, or use `/skills onboard`.
3. Ask naturally first for most tasks and use `/skills <workflow>` if
   explicit invocation helps.
4. If repo behavior seems off, reopen Qwen from the repo root and check
   `AGENTS.md` and `QWEN.md`.

## When Qwen Seems Confused

- Confirm Qwen was launched from the repo root.
- Ask naturally first, then use `/skills <workflow>` if explicit
  invocation helps.
- If repo skills seem missing, check `AGENTS.md`, `QWEN.md`, and
  `.qwen/settings.json`.
- If Qwen in PyCharm behaves differently from Qwen in a normal terminal,
  trust the terminal path as the reference behavior.

## Common Workflow Entry Points

| Goal | Best repo surface |
|------|-------------------|
| First-time setup | ask naturally or `/skills onboard` |
| Create a project | ask naturally or `/skills new-project` |
| Scaffold a week | ask naturally or `/skills scaffold-week` |
| Set up a Word report | ask naturally or `/skills setup-paper`, `/skills word-report` |
| Write or edit report text | ask naturally or `/skills write-section`, `/skills edit-section` |
| Build a PowerPoint deck | ask naturally or `/skills build-deck` |
| Compile a legacy LaTeX paper | ask naturally or `/skills build-paper` |
| Build or export figures | ask naturally or `/skills build-figure` |
| Build a Streamlit app | ask naturally or `/skills build-app` |
| Build report context | ask naturally or `/skills build-context` |
| Build week context | ask naturally or `/skills build-week-context` |
| Proofread or outline a report | ask naturally or `/skills proofread`, `/skills outline` |
| Diagnose legacy LaTeX issues | ask naturally or `/skills latex-doctor` |

## Figure Suites

Use the `build-figure` skill for both single figures and dataframe-driven
figure suites. For broad requests such as "make FT-style figures for my data",
Qwen should follow `docs/ai/workflows/build-figure.md` and default to a
narrative suite when the data has recognizable structure:

```bash
python tools/workflow.py build-figure-suite data/my_data.csv --style ft --narrative --output results/figures
```

When a dataframe is already loaded in Python or PyCharm, use
`docs/ai/examples/figure_suite_from_dataframe.py` as the compact example for
`create_figure_suite(df, style="ft", docx=True, narrative=True)`.

## PyCharm Boundary

Qwen Code in PyCharm is intended to use the same repo-native Qwen
surfaces: `AGENTS.md`, `QWEN.md`, `.qwen/settings.json`, `.qwen/skills/`,
and the shared workflow docs. If the ACP path drifts, treat the normal
terminal Qwen Code path as the reference behavior.

For the PyCharm-specific setup and ACP installation path, use
`docs/ai/qwen-pycharm.md`.

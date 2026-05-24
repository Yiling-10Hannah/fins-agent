# Claude Code Workflow Guide

This guide is for students using Claude Code in this repo.

If you are using Claude Code from PyCharm, also read
`docs/ai/claude-pycharm.md`.

## Claude Repo Structure

Claude support in this repo is built from:

- `CLAUDE.md`
- `.claude/skills/`
- `.claude/rules/` as Claude-facing mirrors of the shared rules
- `docs/ai/workflows/`
- `docs/ai/rules/`

## How Claude Gets Context Here

- `CLAUDE.md` is the durable repo instruction file for Claude Code.
- `.claude/skills/` contains the repo workflow wrappers.
- `docs/ai/workflows/` is the shared source of truth for workflow behavior.
- `docs/ai/rules/` is the shared source of truth for writing, Word
  reporting, citation, presentation, and legacy LaTeX rules.
- `.claude/rules/` remains a Claude-facing compatibility surface for those
  shared rules.
- Shared AI context also lives in `docs/ai/core.md`.

If a Claude skill wrapper and a shared workflow doc differ, the shared
workflow doc wins.

## Typical Student Flow

1. Launch Claude Code from the repo root.
2. Ask Claude to summarize `CLAUDE.md` if you want to confirm the repo
   conventions.
3. Use the matching slash command for the task.
4. Follow up in plain English if the first pass needs correction.

If Claude fails before it reads the repo, check `claude --version`, auth, and
model/account access before diagnosing `CLAUDE.md` or the course setup.

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
suites. For broad requests such as "make FT-style figures for my data", Claude
should follow `docs/ai/workflows/build-figure.md` and default to a narrative
suite when the data has recognizable structure:

```bash
python tools/workflow.py build-figure-suite data/my_data.csv --style ft --narrative --output results/figures
```

When a dataframe is already loaded in Python or PyCharm, use
`docs/ai/examples/figure_suite_from_dataframe.py` as the compact example for
`create_figure_suite(df, style="ft", docx=True, narrative=True)`.

## PyCharm Boundary

Claude Code in PyCharm uses the same repo-native Claude surfaces:
`CLAUDE.md`, `.claude/skills/`, `.claude/rules/`, and the shared workflow
docs. The difference is the host UI, not the repo behavior.

For the PyCharm-specific setup, quick launch, diff viewer, and `/ide`
connection flow, use `docs/ai/claude-pycharm.md`.

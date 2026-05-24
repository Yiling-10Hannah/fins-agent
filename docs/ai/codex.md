# OpenAI Codex Workflow Guide

This guide is for students using OpenAI-native Codex in
this repo: the Codex CLI, Codex app, or OpenAI IDE extension.

If you are using Codex inside PyCharm through JetBrains AI, use
`docs/ai/codex-pycharm.md` instead.

## Codex Repo Structure

OpenAI-native Codex support in this repo is built from:

- `AGENTS.md`
- `.agents/skills/`
- `.codex/config.toml`
- `docs/ai/workflows/`

Hooks are intentionally omitted for now. The repo is on Windows and current
Codex hooks documentation says Windows support is disabled.

## How OpenAI Codex Gets Context Here

- `AGENTS.md` is the durable repo instruction file Codex should auto-load.
- `.agents/skills/` contains shared team skills. Codex can auto-match them
  or invoke them explicitly with the `$` prefix.
- `.codex/config.toml` carries project-scoped Codex config, including the
  `openaiDeveloperDocs` MCP server, when the project is trusted.
- `docs/ai/workflows/` is the shared source of truth for workflow behavior.
- `docs/ai/rules/` is the shared source of truth for writing, Word
  reporting, citation, presentation, and legacy LaTeX rules.
- `docs/ai/code-review.md` is the shared rubric for code review requests.
- Repo-specific behavior comes from these repo files, not from custom slash
  commands.

If a Codex skill wrapper and a shared workflow doc differ, the shared
workflow doc wins.

## First 60 Seconds In Codex

1. Launch Codex from the repo root.
2. Run `/status` to confirm Codex is in the expected repo.
3. Run `/skills` to see the repo skills Codex can use.
4. Run `/mcp` if you want to confirm the project MCP server is loaded.
5. Ask naturally for the task, such as "set me up" or "create a new project
   under `projects/`".
6. If explicit invocation helps, call the matching skill with
   `$<skill-name>`.

Codex should already load repo context from `AGENTS.md`. Ask for a summary
only if you want orientation, not as a required startup ritual.

## When Codex Seems Confused

- Run `/status` to confirm the current repo and working directory.
- Run `/skills` to confirm the repo skills are visible.
- Run `/mcp` to confirm `openaiDeveloperDocs` is loaded when the project is
  trusted.
- If Codex fails before it reads the repo, check `codex --version`, auth,
  and whether the configured model is supported by that CLI/account.
- If the CLI still looks wrong, use `/debug-config` and then check
  `docs/setup/ai-troubleshooting.md`.

## Onboarding Boundary

OpenAI-native Codex in the CLI, app, or OpenAI IDE extension is the default
repo-native Codex path.

For onboarding:

1. Check whether Python 3.13 exists.
2. If Python 3.13 is missing, install it first.
3. For a true first-time setup, run the OS bootstrap script from the repo
   root.
4. Once a usable Python command exists, `python tools/workflow.py onboard`
   can run the agent helper. Use `python tools/workflow.py onboard --check`
   to verify only, and `python tools/workflow.py onboard --rebuild` only
   when intentionally recreating `.venv`.

## Common Workflow Entry Points

| Goal | Best repo surface |
|------|-------------------|
| First-time setup | ask naturally or use `$onboard` |
| Create a project | ask naturally or use `$new-project` |
| Scaffold a week | ask naturally or use `$scaffold-week` |
| Set up a Word report | ask naturally or use `$setup-paper`, `$word-report` |
| Write or edit report text | ask naturally or use `$write-section`, `$edit-section` |
| Build a PowerPoint deck | ask naturally or use `$build-deck` |
| Compile a legacy LaTeX paper | ask naturally or use `$build-paper` |
| Build or export figures | ask naturally or use `$build-figure` |
| Build a Streamlit app | ask naturally or use `$build-app` |
| Build report context | ask naturally or use `$build-context` |
| Build week context | ask naturally or use `$build-week-context` |
| Proofread or outline a report | ask naturally or use `$proofread`, `$outline` |
| Diagnose legacy LaTeX issues | ask naturally or use `$latex-doctor` |

## Important Boundary

`docs/ai/codex-pycharm.md` covers Codex inside PyCharm via JetBrains AI.
That is a separate host surface and should not be assumed to load repo
`.agents/skills/` or `.codex/config.toml` automatically unless you confirm
it in PyCharm. If you want the clearest repo-native Codex behavior inside
PyCharm, use the Codex CLI in the PyCharm terminal.

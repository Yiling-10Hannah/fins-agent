# Gemini CLI in PyCharm Guide

This guide is for students using Gemini CLI with PyCharm.

This is still Gemini CLI. PyCharm adds JetBrains ACP-based IDE integration
on top of the same repo-native Gemini surfaces.

Treat the normal terminal Gemini CLI path as the reference behavior if the
ACP path differs.

## What This Path Is

- PyCharm 2025.3.2+ with the AI Assistant plugin
- Gemini CLI installed locally, or installed through the JetBrains ACP
  registry
- JetBrains AI Chat used as the host UI
- Recommended authentication: Google account login through Gemini CLI
- Alternatives: Gemini API key or Vertex AI
- JetBrains ACP agents are not supported in WSL

## Recommended Path: Gemini CLI Agent in PyCharm

1. Open AI Chat in PyCharm.
2. Install Gemini CLI from the ACP registry if it is available in your IDE
   build.
3. If registry install is unavailable, add Gemini CLI as a custom ACP agent
   in JetBrains AI.
4. Open this repo in PyCharm as a single project root.
5. Start with `/onboard`.
6. If the ACP path misses repo workflow behavior, switch to the terminal
   path before assuming the repo is broken.

If you need a clean first prompt, use:

```text
/onboard
```

## Terminal Path

Use this path when you want the clearest reference behavior. You can also
use Gemini CLI from PyCharm's built-in terminal without ACP integration:

1. Open PyCharm's built-in terminal at the repo root. On Windows, prefer
   PowerShell or cmd over Git Bash - see
   [terminal shell notes](../setup/pycharm.md#choosing-a-terminal-shell).
2. Run `gemini`.
3. Start with `/onboard`.

This path uses the same repo-native Gemini surfaces without JetBrains AI
Chat integration and is the easiest path to troubleshoot.

If you ask Gemini in PyCharm to install a Python package, it should update
`requirements.txt` or `requirements-dev.txt` first and then run the install
from PyCharm's built-in terminal with the repo interpreter.

## What Context Gemini Uses Here

Gemini CLI in PyCharm is intended to use the same repo-native Gemini
surfaces as normal Gemini CLI:

- `GEMINI.md`
- `.gemini/settings.json`
- `.gemini/commands/`
- `docs/ai/workflows/`

You can use the same project commands in PyCharm as in the regular CLI:

- `/onboard`
- `/new-project`
- `/setup-paper`
- `/word-report`
- `/write-section`
- `/edit-section`
- `/proofread`
- `/build-paper` for legacy LaTeX reports
- `/build-deck` for PowerPoint decks
- `/build-figure`
- `/build-context`
- `/outline`
- `/latex-doctor` for legacy LaTeX reports

For loaded dataframe work, use `/build-figure` and point Gemini to
`docs/ai/examples/figure_suite_from_dataframe.py`. The standard PyCharm pattern
is:

```python
from fintools.figures import create_figure_suite

result = create_figure_suite(
    df,
    style="ft",
    output="results/figures",
    docx=True,
    narrative=True,
)
```

For CSV data from the terminal, the matching deterministic helper is:

```bash
python tools/workflow.py build-figure-suite data/my_data.csv --style ft --narrative --output results/figures
```

Use non-narrative suite mode only when the student asks for broad chart
inventory rather than a polished story-first figure set.

If the ACP path behaves differently from the terminal path, trust the
terminal path first and treat the IDE host as the variable.

## Important Boundary

Google's Gemini CLI docs currently describe a native IDE companion for
VS Code-family editors. The PyCharm path here is the JetBrains ACP agent
path, not the Google-maintained VS Code companion.

## Common Failure Modes

- Gemini CLI is missing from the ACP registry: use the custom ACP agent
  path instead of waiting on registry availability
- `gemini` is not recognized: install Gemini CLI locally and restart the
  terminal or PyCharm
- Auth fails in PyCharm AI Chat: complete Gemini CLI login in a normal
  terminal first, then return to PyCharm
- The IDE agent sees the wrong folder: reopen the repo as a single project
  root and retry
- The ACP path behaves differently from Gemini in a normal terminal: trust
  the terminal path first and treat the IDE host as the moving part
- WSL is involved: move to a native Windows or macOS path for JetBrains ACP
  agents

Use `../setup/ai-troubleshooting.md` for the detailed fix steps.

## Which Gemini Path To Use

| Path | Best for |
|------|----------|
| Gemini CLI in PyCharm | students who want AI Chat, IDE context, and PyCharm-hosted approvals |
| Gemini CLI in a normal terminal | students who want the clearest reference behavior and the easiest troubleshooting path |

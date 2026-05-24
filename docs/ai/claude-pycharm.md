# Claude Code in PyCharm Guide

This guide is for students using Claude Code with PyCharm.

Unlike Codex in PyCharm, this is still Claude Code itself. The repo-native
Claude behavior stays the same; PyCharm adds IDE integration on top.

## What This Path Is

- PyCharm with the Claude Code JetBrains plugin
- Claude Code installed on your machine
- Recommended login: Claude.ai account
- Alternative login: Anthropic Console account with credits
- PyCharm integration features include quick launch, IDE diff viewing,
  selection context sharing, and diagnostic sharing

## Recommended Setup

1. Install Claude Code on your machine.
2. Install the Claude Code plugin from the JetBrains marketplace.
3. Restart PyCharm fully after plugin installation.
4. Open this repo in PyCharm.
5. Open PyCharm's integrated terminal at the repo root. On Windows, prefer
   PowerShell or cmd over Git Bash - see
   [terminal shell notes](../setup/pycharm.md#choosing-a-terminal-shell).
6. Run `claude`.
7. Start with `/onboard`.

This is the recommended path because the JetBrains plugin activates when
Claude Code runs from the IDE's integrated terminal.

If you ask Claude Code in PyCharm to install a Python package, it should
update `requirements.txt` or `requirements-dev.txt` first and then run the
install from PyCharm's built-in terminal with the repo interpreter.

## External Terminal Flow

If you start Claude Code in an external terminal, connect it back to
PyCharm with:

```text
/ide
```

Start Claude Code from the same directory as the PyCharm project root so it
sees the same files and loads the same repo context.

## What Context Claude Uses Here

Claude Code in PyCharm uses the same repo-native Claude surfaces as normal
Claude Code:

- `CLAUDE.md`
- `.claude/skills/`
- `.claude/rules/` as Claude-facing mirrors of `docs/ai/rules/`
- `docs/ai/workflows/`
- `docs/ai/rules/`

You can use the same slash commands in PyCharm as in the regular CLI:

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

For loaded dataframe work, use `/build-figure` and point Claude to
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

## Windows Note

Claude Code on Windows may run through WSL or Git Bash depending on the
student's setup. If the PyCharm plugin cannot find `claude`, set the Claude
command path in the plugin settings.

## Common Failure Modes

- `claude` is not recognized: install Claude Code first and restart the
  terminal or PyCharm so PATH refreshes
- `npm` is not recognized: install Node.js LTS before installing or updating
  Claude Code
- PowerShell blocks `npm.ps1`: set `RemoteSigned` for the current user, then
  reopen PowerShell and retry
- The JetBrains plugin cannot find Claude Code: point it at the actual
  `claude` command path or fall back to the terminal plus `/ide`
- `/ide` does not connect cleanly: start Claude Code from the same repo root
  as the PyCharm project

Use `../setup/ai-troubleshooting.md` for the detailed fix steps.

## Which Claude Path To Use

| Path | Best for |
|------|----------|
| Claude Code in PyCharm | students who want IDE diffs, selection sharing, and quick launch |
| Claude Code in a normal terminal | students who prefer the plain CLI without IDE integration |

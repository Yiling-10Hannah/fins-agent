# Qwen Code in PyCharm Guide

This guide is for students using Qwen Code with PyCharm.

This is still Qwen Code. PyCharm adds JetBrains ACP-based IDE integration
on top of the same repo-native Qwen surfaces.

Treat the normal terminal Qwen Code path as the reference behavior if the
ACP path differs.

## What This Path Is

- PyCharm 2025.3.2+ with the AI Assistant plugin
- Qwen Code installed locally
- JetBrains AI Chat used as the host UI
- ACP agent support in the IDE
- JetBrains ACP agents are not supported in WSL

## Recommended Path: Qwen Code Agent in PyCharm

1. Install Qwen Code locally.
2. Open AI Chat in PyCharm.
3. If Qwen Code is available in the ACP registry, install it there.
4. Otherwise add it as a custom ACP agent using the Qwen docs pattern with
   the `--acp` argument.
5. Open this repo in PyCharm as a single project root.
6. Ask naturally for onboarding, or use `/skills onboard`.
7. If repo skills or context look wrong, switch to the terminal path before
   assuming the repo is broken.

If you need a clean first prompt, use:

```text
Help me onboard in this repo. Read AGENTS.md and QWEN.md first.
```

## Terminal Path

Use this path when you want the clearest reference behavior. You can also
use Qwen Code from PyCharm's built-in terminal without ACP integration:

1. Open PyCharm's built-in terminal at the repo root. On Windows, prefer
   PowerShell or cmd over Git Bash - see
   [terminal shell notes](../setup/pycharm.md#choosing-a-terminal-shell).
2. Run `qwen`.
3. Ask naturally for onboarding, or use `/skills onboard`.

This path uses the same repo-native Qwen surfaces without JetBrains AI Chat
integration and is the easiest path to troubleshoot.

If you ask Qwen in PyCharm to install a Python package, it should update
`requirements.txt` or `requirements-dev.txt` first and then run the install
from PyCharm's built-in terminal with the repo interpreter.

## What Context Qwen Uses Here

Qwen Code in PyCharm is intended to use the same repo-native Qwen surfaces
as normal Qwen Code:

- `AGENTS.md`
- `QWEN.md`
- `.qwen/settings.json`
- `.qwen/skills/`
- `docs/ai/workflows/`

Use the same repo workflow behavior as normal Qwen Code:

- ask naturally for matching project workflows
- use `/skills <workflow>` if explicit invocation is needed
- use `/skills setup-paper` or `/skills word-report` for Word reports
- reserve `/skills build-paper` and `/skills latex-doctor` for legacy
  LaTeX reports

For loaded dataframe work, ask Qwen for `build-figure` or use
`/skills build-figure`, then point it to
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

## Common Failure Modes

- Qwen Code is missing from the ACP registry: use the custom agent setup
  with `--acp`
- `qwen` is not recognized: install Qwen Code locally and restart the
  terminal or PyCharm
- Auth works in the terminal but not in AI Chat: complete login in the CLI
  first, then reconnect PyCharm
- `/skills` does not expose repo workflows: ask naturally first, then check
  that Qwen is running from the repo root
- The ACP path behaves differently from Qwen in a normal terminal: trust
  the terminal path first and treat the IDE host as the moving part
- The IDE and terminal behave differently: verify the repo root and fall
  back to the terminal path if needed

Use `../setup/ai-troubleshooting.md` for the detailed fix steps.

## Which Qwen Path To Use

| Path | Best for |
|------|----------|
| Qwen Code in PyCharm | students who want AI Chat, IDE context, and PyCharm-hosted approvals |
| Qwen Code in a normal terminal | students who want the clearest reference behavior and the easiest troubleshooting path |

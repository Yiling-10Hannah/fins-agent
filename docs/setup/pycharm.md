# PyCharm Setup Guide

PyCharm is the editor this course assumes. Think of it as a workspace for the
repo: files on the left, code in the middle, terminal at the bottom.

The main rule is simple:

> Open the real `fins-agent` folder, use PyCharm's terminal from the repo
> root, and make PyCharm use the repo `.venv` Python.

## Before You Start

Read these first if you are new:

- `../../QUICKSTART.md`
- `../ai/start-here.md`
- `ai-troubleshooting.md`

You should have:

- Git installed
- Python 3.13 installed
- PyCharm installed
- the `fins-agent` repo cloned to your laptop

## Open The Right Folder

1. Open PyCharm.
2. Choose **File > Open**.
3. Select the cloned `fins-agent` folder.
4. Click **Trust Project** if PyCharm asks.

Do not open a parent folder such as `GitHub`. Do not open only a weekly
folder such as `week1`. Open the whole `fins-agent` folder.

You are in the right place if the left file tree shows folders like:

```text
docs/
fins2026/
fintools/
projects/
tools/
```

## Open PyCharm's Terminal

PyCharm has a terminal tab at the bottom of the window. Use that terminal for
setup commands. It keeps the editor and command line pointed at the same repo.

In the terminal, run:

```bash
pwd
```

The path should end in `fins-agent`. That top folder is the **repo root**.

If you are not at the repo root, move there with `cd`.

## Run Setup

Run exactly one command from the repo root.

Windows:

```powershell
powershell -ExecutionPolicy Bypass -File tools/bootstrap_windows.ps1
```

macOS:

```bash
bash tools/bootstrap_macos.sh
```

The setup command creates or repairs `.venv`, installs packages, and runs the
student setup check.

Good result:

```text
All required checks passed. You're ready to go!
```

You can verify setup again later with:

Windows:

```powershell
.\.venv\Scripts\python.exe tools/setup_student.py
```

macOS:

```bash
./.venv/bin/python tools/setup_student.py
```

Agents may also use:

```bash
python tools/workflow.py onboard
python tools/workflow.py onboard --check
python tools/workflow.py onboard --rebuild
```

Use rebuild only when you intentionally want to repair `.venv`.

On Windows, close PyCharm Python Console tabs, notebooks, running scripts,
Streamlit apps, and terminals that use `.venv` before repairing setup.

## Choose The Python Interpreter

PyCharm should usually find `.venv` by itself.

If it does not:

1. Open **Settings**.
2. Go to **Project > Python Interpreter**.
3. Choose **Add Interpreter** or **Add Local Interpreter**.
4. Choose **Existing**.
5. Select the Python file inside `.venv`.

Windows:

```text
.venv\Scripts\python.exe
```

macOS:

```text
.venv/bin/python
```

This matters. If PyCharm uses the wrong Python, packages may look missing even
though setup worked.

## Run A Python File

Two safe ways:

- right-click a `.py` file and choose **Run**
- use PyCharm's terminal from the repo root

After setup, terminal commands can use the repo interpreter directly.

Windows:

```powershell
.\.venv\Scripts\python.exe tools/workflow.py list
```

macOS:

```bash
./.venv/bin/python tools/workflow.py list
```

If PyCharm has activated `.venv`, simple commands like this can also work:

```bash
python my_script.py
```

## Install Packages The Repo Way

Do not use random package installs from the PyCharm package UI.

If the repo needs a package:

1. Decide whether it belongs in `requirements.txt` or `requirements-dev.txt`.
2. Update that file.
3. Install from PyCharm's terminal at the repo root.
4. Rerun the failed command or setup check.

Install command:

```bash
<repo-python> -m pip install -r requirements.txt -r requirements-dev.txt
```

Use the matching repo Python path:

- Windows: `.\.venv\Scripts\python.exe`
- macOS/Linux: `./.venv/bin/python`

## Windows Terminal Choice

On Windows, use PowerShell or cmd in PyCharm's terminal.

Avoid Git Bash for course setup commands. The examples use Windows path
syntax, such as:

```powershell
.\.venv\Scripts\python.exe
```

Git Bash uses different path syntax, which confuses beginners and breaks some
PowerShell-specific setup snippets.

To check or change PyCharm's terminal:

1. Open **Settings > Tools > Terminal**.
2. Check **Shell path**.
3. Use `powershell.exe` on Windows.
4. Close and reopen terminal tabs after changing it.

## Using AI Assistants In PyCharm

There are two patterns.

Pattern 1: use the assistant inside PyCharm's AI chat or plugin.

Pattern 2: use the assistant CLI from PyCharm's terminal.

For beginners, the terminal path is often easier to debug because the terminal
clearly shows the repo root and command output.

## OpenCode In PyCharm

OpenCode can run through PyCharm's AI Chat using JetBrains ACP.

Recommended path:

1. Finish GitHub account setup first. In this course, treat GitHub as
   required before OpenCode auth.
2. Open AI Chat in PyCharm.
3. Use **Add ACP Agent** and install OpenCode.
4. If OpenCode is not listed, use the custom ACP path from
   `../ai/opencode-pycharm.md`.
5. Authenticate OpenCode Zen and pick a model from the AI Chat model
   dropdown. Start with `MiniMax M2.5 Free`.

Good first prompt:

```text
Read AGENTS.md, summarize how this repo is organized, then help me run onboarding.
```

This repo already ships `AGENTS.md`, so do not run `/init` here to create a
new one. Use `../ai/opencode-pycharm.md` for the full setup notes and the
current free-model guidance.

## OpenAI Codex In PyCharm

Two supported paths:

- **Codex in JetBrains AI Chat**: convenient, but confirm it can see the repo
  context. See `../ai/codex-pycharm.md`.
- **Codex CLI in PyCharm's terminal**: repo-native path. Start from the repo
  root, then run Codex and check `/status`, `/skills`, and `/mcp`. See
  `../ai/codex.md`.

Good first prompt:

```text
Read AGENTS.md, summarize how this repo is organized, then help me run onboarding.
```

If PyCharm AI Chat behaves differently from the CLI, trust the CLI first.
If Codex fails before it reads the repo, check `codex --version`, auth, and
model compatibility before changing course files.

## Claude Code In PyCharm

Recommended path:

1. Install Claude Code.
2. Install the Claude Code JetBrains plugin.
3. Restart PyCharm.
4. Open PyCharm's terminal at the repo root.
5. Run `claude`.
6. Start with `/onboard`.

Docs:

- `../ai/claude-pycharm.md`
- `../ai/claude.md`

Common blockers: `claude` not found, `npm` missing, PowerShell execution
policy, stale CLI version, auth/model access, or the plugin not finding the
CLI. Use `ai-troubleshooting.md`.

## Gemini In PyCharm

Gemini can run through PyCharm's AI Chat using JetBrains ACP, or from
PyCharm's terminal as Gemini CLI.

Beginner path:

1. Open PyCharm's terminal at the repo root.
2. Run `gemini`.
3. Start with `/onboard`.

Docs:

- `../ai/gemini-pycharm.md`
- `../ai/gemini.md`

If the ACP path acts differently from the terminal path, trust the terminal
path first.

## Qwen In PyCharm

Qwen can run through PyCharm's AI Chat using JetBrains ACP, or from PyCharm's
terminal as Qwen Code.

Beginner path:

1. Open PyCharm's terminal at the repo root.
2. Run `qwen`.
3. Ask naturally for onboarding, or use `/skills onboard`.

Docs:

- `../ai/qwen-pycharm.md`
- `../ai/qwen.md`

If the ACP path acts differently from the terminal path, trust the terminal
path first.

## Common Problems

| Problem | What to check |
|---|---|
| Setup cannot find repo files | Terminal is not at the repo root |
| PyCharm cannot import packages | PyCharm is using the wrong interpreter |
| `python` uses the wrong version | Use the repo `.venv` interpreter path |
| Windows `Access is denied` inside `.venv` | Close apps using `.venv`, then rerun setup |
| AI assistant edits the wrong folder | Start the assistant from the repo root |
| AI chat cannot see repo skills | Use the terminal CLI path or attach the relevant repo docs |

When asking for help, include the exact command, exact error text, operating
system, and whether the PyCharm terminal path ended in `fins-agent`.

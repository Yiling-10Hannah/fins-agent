# AI Start Here

Use this page when you want an AI assistant to help with the course repo.

You do not need to understand every assistant today. Pick one working
path, get setup checked, and move to `../../fins2026/week0/`.

## What The AI Assistant Does

In this repo, an AI assistant can:

- read files
- explain files
- run setup checks
- help fix errors
- write or edit project files after you approve the change

It is not magic. It can be wrong. Always check the output, especially numbers
and finance interpretation.

## The Default Student Path

Use this unless an instructor tells you otherwise:

1. Open the cloned `fins-agent` folder in PyCharm.
2. Open PyCharm's built-in terminal.
3. Confirm the terminal is at the repo root.
4. Run setup or ask your AI assistant to guide setup.
5. Open `../../fins2026/week0/`.

The **repo root** is the top `fins-agent` folder. Most commands must be run
there.

Manual setup guide:

```text
../../QUICKSTART.md
```

PyCharm setup guide:

```text
../setup/pycharm.md
```

OpenCode in PyCharm guide:

```text
opencode-pycharm.md
```

## Pick One AI Path

Use the first one you already have access to.

| You have... | Use this | First action |
|---|---|---|
| GitHub set up and want free models in PyCharm | OpenCode in PyCharm | open `opencode-pycharm.md`, add OpenCode in AI Chat, then ask it to read `AGENTS.md` and help onboard |
| ChatGPT or Codex access | OpenAI Codex | run `/status`, then `/skills`, then ask for onboarding |
| Claude Code or Claude access | Claude Code | run `claude`, then `/onboard` |
| Gemini CLI or Google access | Gemini CLI | run `gemini`, then `/onboard` |
| Qwen Code access | Qwen Code | run `qwen`, then ask for onboarding |
| none of these yet | Manual setup | use `../../QUICKSTART.md` |

You only need one assistant to start. You can add another later.

## First-Time Setup Commands

If Python 3.13 is missing, install Python 3.13 first. Then run the bootstrap
command from the repo root.

On macOS, verify `python3.13 -m pip --version` before setup. If it fails with
`pyexpat` or `libexpat`, use the Python.org macOS installer or ask for help.

Windows:

```powershell
powershell -ExecutionPolicy Bypass -File tools/bootstrap_windows.ps1
```

macOS:

```bash
bash tools/bootstrap_macos.sh
```

After Python is available, an assistant can also use:

```bash
python tools/workflow.py onboard
python tools/workflow.py onboard --check
```

Use `python tools/workflow.py onboard --rebuild` only when you intentionally
want to repair or recreate `.venv`.

If onboarding warns that `ripgrep` (`rg`) is missing, you can keep working.
It only makes AI repo search faster.

## Good First Prompt

Copy this into your assistant from the repo root:

```text
I am new to this course repo. Read README.md, QUICKSTART.md, and
docs/ai/start-here.md. Then help me check setup from the repo root.
Explain each step in plain English before you run it.
```

If the assistant asks permission to read files or run setup commands, read the
prompt and approve the course setup checks.

## What Success Looks Like

The required setup check should end with:

```text
All required checks passed. You're ready to go!
```

After that, ask the assistant:

```text
Show me what is inside fins2026/week0 and tell me what I should do first.
```

## If You Get Stuck

Use these pages in order:

1. `../../QUICKSTART.md`
2. `../setup/pycharm.md`
3. `../setup/ai-troubleshooting.md`
4. `../setup/ai-support-matrix.md`

When asking for help, include:

- Windows or macOS
- which assistant you used
- the command you ran
- the exact error text
- whether PyCharm's terminal was at the repo root

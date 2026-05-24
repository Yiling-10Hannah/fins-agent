# Fintech Agent Toolkit

This is the course toolkit for financial market data work. It gives you:

- weekly folders for the course exercises
- shared Python code for figures and analysis
- setup scripts that check your laptop
- Word report scaffolds
- instructions for using AI coding assistants safely

You do not need to be a computer science student to use this repo. The goal is
to get your laptop into a known working state, then let you focus on finance,
data, and interpretation.

## Start Here

Most students should use PyCharm and an AI assistant.

1. Install Git, Python 3.13, and PyCharm.
2. Create a GitHub account with your university email.
3. Clone this repo.
4. Open the cloned `fins-agent` folder in PyCharm.
5. Open PyCharm's built-in terminal.
6. Run the setup command for your operating system.
7. Check that setup says the required checks passed.
8. Open [`fins2026/week0/`](fins2026/week0/) and follow the orientation.

If you want the slow, careful manual path, use
[QUICKSTART.md](QUICKSTART.md).

If you want an AI assistant to guide you, start with
[docs/ai/start-here.md](docs/ai/start-here.md).

## What These Words Mean

- **Repository** or **repo**: this project folder.
- **GitHub**: the website where the repo lives online.
- **Clone**: copy the repo from GitHub to your laptop.
- **Terminal**: the place where you type commands.
- **Repo root**: the top `fins-agent` folder. Commands should usually be run
  there.
- **`.venv`**: the private Python environment for this repo.
- **Bootstrap**: the setup script that creates or repairs `.venv` and checks
  packages.
- **Agent**: an AI coding assistant that can read files, edit files, and run
  commands with your permission.

## First-Time Setup Commands

Run these from the repo root, preferably in PyCharm's built-in terminal.

Windows:

```powershell
powershell -ExecutionPolicy Bypass -File tools/bootstrap_windows.ps1
```

macOS:

```bash
bash tools/bootstrap_macos.sh
```

The setup script checks Python, installs packages, and verifies Word report
tooling. It also checks `ripgrep` (`rg`), which helps AI assistants search the
repo faster. If `rg` is missing, setup warns, but coursework can continue.

When setup is healthy, you should see:

```text
All required checks passed. You're ready to go!
```

## GitHub Account

Create a free account at <https://github.com/>.

Use your university email if you can. Pick a sensible username because it will
appear on your project links and submitted work. After signup, verify your
email before continuing.

Students should also apply for the GitHub Student Developer Pack:

<https://education.github.com/pack>

Do this early. Approval can take time, and it is easier to apply before you
need the extra student tools.

GitHub is also the classroom prerequisite for the OpenCode in PyCharm path.
If you want to use OpenCode's free-model options in PyCharm AI Chat later,
finish your GitHub account setup before that step.

## What Is Inside

```text
fins-agent/
|-- fins2026/       Weekly course folders. Start with week0.
|-- fintools/       Shared Python tools used across the course.
|-- projects/       Your larger project work goes here.
|-- docs/           Setup, AI, writing, app, and troubleshooting guides.
|-- tools/          Setup and workflow helper scripts.
|-- requirements.txt
|-- requirements-dev.txt
`-- README.md
```

The current public release includes `fins2026/week0/` through
`fins2026/week5/`. Later weeks will be published during the course. When your
instructor announces a new release, update from the repo root with
`git pull --ff-only`.

## Weekly Workflow

Each week has its own folder:

```text
fins2026/week0/
fins2026/week1/
fins2026/week2/
...
```

For the current public release, the available teaching weeks are `week0`
through `week5`. Do not create your own `week6` to `week10` placeholders;
later releases will add those folders for you.

The usual routine is:

1. Open the repo in PyCharm.
2. Open the current week folder.
3. Read the instructions.
4. Ask your AI assistant for help with one clear task.
5. Run the code.
6. Check the output before trusting it.
7. Write up the result in a Word report or app when asked.

AI can help you write and run code. It does not replace your judgement. You
still need to check the numbers and explain the finance.

## AI Assistants

The repo supports:

- OpenCode in PyCharm
- OpenAI Codex
- Claude Code
- Gemini CLI
- Qwen Code

You only need one to start. Use the one you already have access to. The shared
starting point is:

[docs/ai/start-here.md](docs/ai/start-here.md)

Useful AI setup pages:

- [docs/setup/ai-support-matrix.md](docs/setup/ai-support-matrix.md)
- [docs/setup/ai-troubleshooting.md](docs/setup/ai-troubleshooting.md)
- [docs/setup/pycharm.md](docs/setup/pycharm.md)
- [docs/ai/opencode-pycharm.md](docs/ai/opencode-pycharm.md)

Good first prompt:

```text
Read README.md and docs/ai/start-here.md. Then help me run onboarding from
the repo root. Explain each step before you run it.
```

## Reports, Figures, And Apps

- Reports are Word-first. Use `setup-paper` or `word-report` when the course
  asks for a report scaffold.
- Figures should use `fintools.figures` first. It creates report-ready charts
  for time series, cumulative returns, drawdowns, bars, scatter plots,
  distributions, heatmaps, and Word/A4 exports.
- Streamlit apps are used for interactive submissions. App guidance lives in
  [docs/apps/streamlit/](docs/apps/streamlit/).

## Package Rules

This repo uses Python 3.13 and pip requirements files.

After setup, the repo Python interpreter is:

- Windows: `.\.venv\Scripts\python.exe`
- macOS/Linux: `./.venv/bin/python`

Install packages only through the repo requirements files:

```bash
<repo-python> -m pip install -r requirements.txt -r requirements-dev.txt
```

Do not use random one-off package installs unless an instructor or assistant
has also updated `requirements.txt` or `requirements-dev.txt`.

## If Something Breaks

Do not panic. Setup problems are normal the first time.

First, make sure:

1. You are in the repo root.
2. PyCharm opened the actual `fins-agent` folder.
3. You are using the repo `.venv` interpreter.
4. You copied the exact error message, not a screenshot of it.

Common fixes:

| Problem | What to do |
|---|---|
| `python` is not found | Install Python 3.13, then reopen the terminal |
| Mac pip fails with `pyexpat` or `libexpat` | Use the Python.org macOS installer instead of repeatedly rerunning setup |
| packages are missing | Rerun the bootstrap command |
| `rg` is not found | AI search will be slower; coursework can continue |
| PyCharm cannot find Python | Point PyCharm at `.venv` |
| Windows says `Access is denied` inside `.venv` | Close Python Console tabs, notebooks, Streamlit apps, and terminals using `.venv`, then rerun setup |
| Streamlit will not start | Reinstall requirements, then run from the repo root |

Detailed help:

- [docs/setup/troubleshooting.md](docs/setup/troubleshooting.md)
- [docs/setup/ai-troubleshooting.md](docs/setup/ai-troubleshooting.md)
- [docs/setup/windows.md](docs/setup/windows.md)
- [docs/setup/macos.md](docs/setup/macos.md)
- [docs/setup/pycharm.md](docs/setup/pycharm.md)

If you ask for help, include your operating system, the command you ran, and
the exact error text.

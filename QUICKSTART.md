# Quick Start Guide

This is the careful manual setup path. It assumes you are new to Git, Python,
PyCharm, and terminals.

If you are using an AI assistant, you can still keep this file open. It tells
you what the assistant is trying to do.

## The Goal

By the end, your laptop should have:

- Git installed
- Python 3.13 installed
- PyCharm installed
- a GitHub account
- a local copy of this repo
- a repo-local Python environment called `.venv`
- all required course packages installed
- Word report tooling working

The main success message is:

```text
All required checks passed. You're ready to go!
```

## Step 0: Know Where You Are

A **terminal** is a window where you type commands.

- Windows: open **PowerShell**.
- macOS: open **Terminal**.
- PyCharm: open the **Terminal** tab at the bottom of the PyCharm window.

A **folder path** is where a folder lives on your computer.

The **repo root** is the top `fins-agent` folder. Most commands in this guide
must be run from the repo root.

Useful commands:

```bash
pwd
```

Shows where the terminal is.

```bash
ls
```

Lists files on macOS.

```powershell
dir
```

Lists files on Windows PowerShell.

```bash
cd folder-name
```

Moves into a folder.

## Step 1: Install The Basic Tools

Install these first:

1. **Git**
   - Windows: <https://git-scm.com/download/win>
   - Mac: <https://git-scm.com/download/mac>
2. **Python 3.13**
   - Windows guide: [docs/setup/windows.md](docs/setup/windows.md)
   - macOS guide: [docs/setup/macos.md](docs/setup/macos.md)
3. **PyCharm**
   - Download: <https://www.jetbrains.com/pycharm/download/>

After installing a tool, close and reopen PowerShell, Terminal, or PyCharm.
New terminal windows can see newly installed commands. Old ones often cannot.

Check Git:

```bash
git --version
```

Check Python:

Windows:

```powershell
python --version
py -3.13 --version
```

macOS:

```bash
python3.13 --version
python3.13 -m pip --version
```

You want to see Python 3.13.

On macOS, if `python3.13 --version` works but the pip check fails with
`pyexpat`, `xml.parsers.expat`, `libexpat`, or
`XML_SetAllocTrackerActivationThreshold`, use the Python.org macOS installer
from <https://www.python.org/downloads/macos/> or ask for help.

## Step 2: Create A GitHub Account

GitHub is the website where the course repo lives.

Go to:

<https://github.com/>

Create a free account.

Use your university email if possible. Pick a username you would be happy to
put on an assignment link. Verify your email before continuing.

Also apply for the GitHub Student Developer Pack:

<https://education.github.com/pack>

You do not need approval before continuing this setup, but applying early is
better than discovering later that you needed it.

If you want to use OpenCode in PyCharm later, treat GitHub as required before
that step. In this course, students should finish GitHub account setup before
they authenticate OpenCode Zen.

## Step 3: Clone The Repo

Cloning means copying the course repo from GitHub to your laptop.

Pick a normal folder for your GitHub projects. For example:

- Windows: `Documents\GitHub`
- macOS: `~/Developer/GitHub`

On many Macs, Desktop and Documents may be synced by iCloud. If that is
enabled, keep course repos in a local folder such as `~/Developer/GitHub`.

Open a terminal in that folder, then run:

```bash
git clone https://github.com/Alexander-M-Dickerson/fins-agent.git
cd fins-agent
```

You are now in the repo root.

Check that you are in the right place:

```bash
pwd
```

You should see a path ending in `fins-agent`.

The current public release includes `fins2026/week0/` through
`fins2026/week5/`. Later weeks will be published during the course. Do not
create your own `week6/` to `week10/` folders. When your instructor announces
an update, open a terminal in the repo root and run:

```bash
git pull --ff-only
```

## Step 4: Open The Repo In PyCharm

1. Open PyCharm.
2. Choose **File > Open**.
3. Select the cloned `fins-agent` folder.
4. Trust the project if PyCharm asks.
5. Open PyCharm's **Terminal** tab.

In the PyCharm terminal, run:

```bash
pwd
```

The path should end in `fins-agent`. If it does not, use `cd` to move to the
repo root before continuing.

## Step 5: Run The Setup Script

Run exactly one of these commands from the repo root.

Windows:

```powershell
powershell -ExecutionPolicy Bypass -File tools/bootstrap_windows.ps1
```

macOS:

```bash
bash tools/bootstrap_macos.sh
```

The setup script:

- checks Python 3.13
- creates or repairs `.venv`
- installs the course packages
- checks `pandas`, `numpy`, `matplotlib`, `streamlit`, and other packages
- checks the shared `fintools` package
- checks Word report tooling
- checks optional `ripgrep` (`rg`) for faster AI-assisted repo search

If setup says `rg` is missing, you can keep going. It only affects how fast AI
assistants can search the repo.

## Step 6: Read The Result

Good result:

```text
All required checks passed. You're ready to go!
```

That means the required setup is working.

If setup fails, read the first failed line. Do not guess. The error message
usually tells you what went wrong.

Common examples:

| Message | Meaning | First fix |
|---|---|---|
| `python` is not found | Python is missing or PATH is stale | Install Python 3.13, then reopen the terminal |
| Mac pip fails with `pyexpat` or `libexpat` | Homebrew Python can start, but pip cannot | use the Python.org macOS installer or ask for help |
| `pip` failed | packages did not install cleanly | rerun the setup command |
| `Access is denied` on Windows | another app is using `.venv` | close PyCharm Python Console tabs, notebooks, Streamlit apps, and terminals using `.venv`, then rerun setup |
| package says `[MISSING]` | a required Python package is missing | rerun the setup command |
| package says `[BROKEN]` | the environment is partly damaged | close apps using `.venv`, then ask for help or run onboarding repair |
| `rg` says `[WARN]` | optional search tool is missing | coursework can continue |

More help:

- [docs/setup/troubleshooting.md](docs/setup/troubleshooting.md)
- [docs/setup/ai-troubleshooting.md](docs/setup/ai-troubleshooting.md)
- [docs/setup/pycharm.md](docs/setup/pycharm.md)

## Step 7: Tell PyCharm Which Python To Use

PyCharm should usually find `.venv` automatically.

If it does not:

1. Open **Settings**.
2. Go to **Python Interpreter**.
3. Choose **Add Interpreter** or **Add Existing**.
4. Pick the Python file inside `.venv`.

Windows:

```text
.venv\Scripts\python.exe
```

macOS:

```text
.venv/bin/python
```

This tells PyCharm to use the course environment, not a random Python
installed somewhere else.

## Step 8: Start Week 0

Open:

```text
fins2026/week0/
```

Read the files there first. Week 0 is the setup and orientation week.
After that, work through `week1/` to `week5/` as your instructor directs.
Later weeks will appear in the repo after future course releases.

If you want an AI assistant to help, open:

[docs/ai/start-here.md](docs/ai/start-here.md)

If you specifically want the OpenCode path in PyCharm AI Chat, also open:

[docs/ai/opencode-pycharm.md](docs/ai/opencode-pycharm.md)

A good first prompt is:

```text
I am new to this. Read README.md and QUICKSTART.md, then help me check that
my setup is working. Explain each step in plain English before running it.
```

## When Asking For Help

Please include:

1. Windows or macOS.
2. The command you ran.
3. The exact error text.
4. Whether you ran it from the repo root.
5. Whether you were using PyCharm's terminal or a separate terminal.

Do not send only a screenshot of text. Text can be searched and copied.
Screenshots cannot.

## Quick Checklist

- [ ] Git works: `git --version`
- [ ] Python 3.13 works
- [ ] GitHub account created and email verified
- [ ] PyCharm opens the `fins-agent` folder
- [ ] PyCharm terminal is at the repo root
- [ ] setup command completed
- [ ] required checks passed
- [ ] PyCharm uses `.venv`
- [ ] Week 0 folder is open

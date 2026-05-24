# macOS Setup Guide

## 1. Install Git

macOS may already have Git. Check:
```bash
git --version
```

If not installed, macOS will prompt you to install Command Line Tools.
Click "Install" and wait.

Alternatively: `xcode-select --install`

## 2. Install Homebrew (if you don't have it)

Homebrew is the macOS package manager. Check if you have it:
```bash
brew --version
```

If not:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the on-screen instructions to add Homebrew to your PATH.

## 3. Install PyCharm

Download PyCharm (free tier is enough for this course):
https://www.jetbrains.com/pycharm/download/

Or install the current unified PyCharm app via Homebrew:
```bash
brew install --cask pycharm
```

## 4. Install Python 3.13

```bash
brew install python@3.13
```

**Important**: close and reopen Terminal after installing.

Verify:
```bash
python3.13 --version
python3.13 -m pip --version
```

If `python3.13 --version` works but `python3.13 -m pip --version` fails with
`pyexpat`, `xml.parsers.expat`, `libexpat`, or
`XML_SetAllocTrackerActivationThreshold`, stop and use the Python.org macOS
installer instead:

https://www.python.org/downloads/macos/

After installing, close and reopen Terminal or PyCharm, then run both verify
commands again.

## 5. Clone and Set Up

Use Terminal to clone the repo. After `cd fins-agent`, you are at the repo
root. If you are working in PyCharm, use PyCharm's built-in terminal and
confirm it is in the cloned `fins-agent` folder.

If iCloud Desktop/Documents syncing is enabled, avoid cloning into Desktop or
Documents. Use a local folder such as `~/Developer/GitHub` instead.

```bash
mkdir -p ~/Developer/GitHub
cd ~/Developer/GitHub
git clone https://github.com/Alexander-M-Dickerson/fins-agent.git
cd fins-agent
bash tools/bootstrap_macos.sh
```

## 6. Verify

```bash
./.venv/bin/python tools/setup_student.py
```

## 7. AI Search Check (recommended)

`ripgrep` provides the `rg` command. AI assistants use it to search this
repo quickly. If this check fails, Python coursework can still continue.

```bash
brew install ripgrep
rg --version
rg --files -g AGENTS.md
```

If `brew` or `rg` is still not found, follow Homebrew's PATH instructions,
then close and reopen Terminal or PyCharm.

## 8. Word Reports

Word is the default report tool. The bootstrap script verifies
`python-docx`, which creates Word `.docx` report scaffolds. Open generated
reports in Microsoft Word for Mac.

Legacy LaTeX setup is optional and documented in `latex.md`.

## 9. Open in PyCharm

1. Open PyCharm
2. File > Open > select the `fins-agent` folder
3. PyCharm should auto-detect the `.venv` interpreter
4. If not: Settings > Python Interpreter > Add > Existing > browse to
   `.venv/bin/python`

## Common Issues

| Problem | Fix |
|---------|-----|
| `python3.13: command not found` | Close and reopen Terminal, then verify Homebrew PATH |
| `python3.13 -m pip --version` fails with `pyexpat` or `libexpat` | Use the Python.org macOS installer instead of repeatedly rerunning bootstrap |
| `brew: command not found` | Install Homebrew first (Step 2) |
| `rg` is not recognized | AI repo search will be slower; coursework can continue. Install ripgrep with `brew install ripgrep`, then reopen Terminal or PyCharm |
| `pip` install fails | Re-run the bootstrap script or use `./.venv/bin/python -m pip ...` from the repo root |

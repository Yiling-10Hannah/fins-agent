# Windows Setup Guide

## 1. Install Git

Download from: https://git-scm.com/download/win

Run the installer with all defaults. This also installs **Git Bash**, a
terminal you can use alongside PowerShell.

Verify: open PowerShell or Git Bash and type:
```
git --version
```

## 2. Install PyCharm

Download PyCharm Community Edition (free):
https://www.jetbrains.com/pycharm/download/

Run the installer with defaults.

## 3. Install Python 3.13

Open PowerShell and run:
```powershell
winget install Python.Python.3.13
```

**Important**: close and reopen PowerShell after installing.

Verify:
```
python --version
```

You should see `Python 3.13.x`. If `python` still points to the wrong
version, try:
```
py -3.13 --version
```

## 4. Clone and Set Up

Use PowerShell from the repo root. If you are working in PyCharm, use
PyCharm's built-in terminal and confirm it is in the cloned `fins-agent`
folder.

Before rerunning setup or repairing `.venv`, close PyCharm Python Console
tabs, notebooks, Streamlit apps, running scripts, and terminals that are
already using `.venv`.

```
git clone https://github.com/Alexander-M-Dickerson/fins-agent.git
cd fins-agent
powershell -ExecutionPolicy Bypass -File tools/bootstrap_windows.ps1
```

## 5. Verify

```
.\.venv\Scripts\python.exe tools/setup_student.py
```

## 6. AI Search Check (recommended)

`ripgrep` provides the `rg` command. AI assistants use it to search this
repo quickly. If this check fails, Python coursework can still continue.

```powershell
winget install --id BurntSushi.ripgrep.MSVC -e
rg --version
rg --files -g AGENTS.md
```

If `rg` is still not found after installation, close and reopen PowerShell
or PyCharm, then try the verify commands again.

## 7. Word Reports

Word is the default report tool. The bootstrap script verifies
`python-docx`, which creates Word `.docx` report scaffolds. Open generated
reports in Microsoft Word for Windows.

## 8. Open in PyCharm

1. Open PyCharm
2. File > Open > select the `fins-agent` folder
3. PyCharm should auto-detect the `.venv` interpreter
4. If not: Settings > Python Interpreter > Add > Existing > browse to
   `.venv\Scripts\python.exe`

## Common Issues

| Problem | Fix |
|---------|-----|
| `python: command not found` | Close and reopen PowerShell, then verify Python 3.13 again |
| `py -3.13` works but `python` does not | Restart PyCharm and PowerShell so PATH refreshes |
| `winget: command not found` | Update Windows or use the App Installer from Microsoft Store |
| `rg` is not recognized | AI repo search will be slower; coursework can continue. Install ripgrep with `winget install --id BurntSushi.ripgrep.MSVC -e`, then reopen PowerShell or PyCharm |
| `pip` install fails | Re-run the bootstrap script or use `.\.venv\Scripts\python.exe -m pip ...` from the repo root |
| `Access is denied` inside `.venv` | Close PyCharm Python Console tabs, notebooks, Streamlit apps, and terminals using `.venv`, then rerun setup |
| Antivirus blocks installs | Add the `fins-agent` folder to your antivirus exclusions |

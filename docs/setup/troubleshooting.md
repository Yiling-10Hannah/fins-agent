# Troubleshooting

For Claude, Codex, Gemini, Qwen, JetBrains AI, or PyCharm agent-install
problems, use [ai-troubleshooting.md](ai-troubleshooting.md). This page is
for the shared Python, pip, interpreter, and Word report tooling problems.

When a fix says "use the repo interpreter", that means:

- Windows: `.\.venv\Scripts\python.exe`
- macOS/Linux: `./.venv/bin/python`

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `python: command not found` | Python 3.13 not installed or terminal not restarted | Install Python 3.13, then close and reopen the terminal |
| `py -3.13` works but `python` does not | PATH is stale on Windows | Restart the terminal or use the bootstrap script |
| `ModuleNotFoundError: No module named 'pandas'` | Packages not installed | Use the repo interpreter and run `-m pip install -r requirements.txt -r requirements-dev.txt` |
| `ModuleNotFoundError: No module named 'fintools'` | Repo package not installed | Use the repo interpreter and run `-m pip install -r requirements.txt -r requirements-dev.txt` |
| `pip` is missing | The environment was not created correctly | Recreate `.venv` with the bootstrap script or the Python 3.13 venv command for your OS; on Windows, `python -m venv .venv` is only safe after `python --version` shows 3.13.x |
| Word report tooling missing | `python-docx` not installed | Reinstall with the repo interpreter and requirements files |
| PyCharm "No Python interpreter configured" | Interpreter not set | See [pycharm.md](pycharm.md) and point to `.venv/` |
| Setup cannot find repo files | Terminal is not at the repo root | In PyCharm's terminal, `cd` to the cloned `fins-agent` folder |
| `pip` install fails with network error | Firewall or proxy blocking | Try from a different network, or ask your instructor |
| `python3.13 -m pip --version` fails with `pyexpat` or `libexpat` on macOS | Homebrew Python can start, but its pip/XML runtime is broken | Use the Python.org macOS installer instead of repeatedly rerunning bootstrap |
| `pip` says `Access is denied` on Windows | `.venv` files are in use or locked | Close PyCharm Python Console tabs, notebooks, Streamlit apps, terminals using `.venv`, then rerun setup |
| pandas, numpy, or another package says `[BROKEN]` | Interrupted install or partial `.venv` rebuild | Close apps using `.venv`, then run `python tools/workflow.py onboard --rebuild` |
| `no RECORD file was found` | pip metadata was damaged during an interrupted install | Close apps using `.venv`, then run `python tools/workflow.py onboard --rebuild` |
| Windows store Python opens instead of real Python | Python launcher alias confusion | Use `py -3.13` or reinstall Python 3.13 from winget |
| `winget: command not found` | Old Windows version or App Installer missing | Update Windows, or download installers manually |
| `brew: command not found` | Homebrew not installed | See [macos.md](macos.md) Step 2 |
| `rg is not recognized` | Recommended AI search tool is missing or PATH is stale | AI repo search will be slower, but coursework can continue. Install ripgrep from the Windows or macOS setup guide, then reopen the terminal |
| `permission denied` on macOS | The command is trying to change a protected system folder | Prefer repo-local setup commands; only use `sudo` when a trusted installer asks for it |
| Streamlit mentions Watchdog or Xcode Command Line Tools | Optional file-watching performance suggestion on macOS | This is not fatal; the app can still run. Install Command Line Tools later only if you want faster reloads |

## macOS Homebrew Python pyexpat/libexpat

On some Macs, `brew install python@3.13` can install Python successfully, but
pip fails before setup can create the course `.venv`.

Symptoms include:

- `ImportError` mentioning `pyexpat`
- `xml.parsers.expat`
- `libexpat`
- `XML_SetAllocTrackerActivationThreshold`

Fix:

1. Stop rerunning bootstrap.
2. Install Python 3.13 from <https://www.python.org/downloads/macos/>.
3. Close and reopen Terminal or PyCharm.
4. Verify:

```bash
python3.13 --version
python3.13 -m pip --version
```

Then rerun:

```bash
bash tools/bootstrap_macos.sh
```

## ripgrep Warning

`ripgrep` provides the `rg` command used by AI assistants for fast repo
search. It is not a Python package and it is not required by coursework
scripts, Streamlit apps, or Word reports.

If setup warns about `rg`, you can keep working. Install it later with:

```powershell
# Windows
winget install --id BurntSushi.ripgrep.MSVC -e
```

```bash
# macOS
brew install ripgrep
```

Then close and reopen PowerShell, Terminal, or PyCharm and verify:

```bash
rg --version
rg --files -g AGENTS.md
```

## Windows `.venv` In Use

On Windows, setup cannot replace compiled package files while another process
has loaded them from `.venv`. The most common cause is a PyCharm Python
Console, notebook, Streamlit app, running script, or terminal that is already
using the repo interpreter.

Symptoms include:

- `Access is denied` on a `.pyd` file
- `[BROKEN] pandas`, `[BROKEN] numpy`, or `DLL load failed`
- `partially initialized module`
- `no RECORD file was found`

Fix:

1. Close PyCharm Python Console tabs.
2. Stop notebooks, Streamlit apps, and running scripts.
3. Close terminals that have activated `.venv`.
4. Rerun:

```powershell
python tools/workflow.py onboard --rebuild
```

The setup scripts should report these lock holders before changing `.venv`.

## How to Get Help

1. Re-run `tools/setup_student.py` with the repo interpreter to see what's missing
2. Check this troubleshooting guide
3. If using an AI tool: describe the error and ask it to fix it
4. Post in the course discussion forum with:
   - Your operating system (Windows / macOS)
   - The exact error message
   - What command you ran
   - Whether the issue is general setup or an AI tool / PyCharm issue

## Resetting Everything

If things are really broken, you can start fresh:

```bash
# Delete the virtual environment
# Windows:
rmdir /s /q .venv

# macOS:
rm -rf .venv

# Recreate everything
# Windows:
py -3.13 -m venv .venv

# Windows fallback if `py` is unavailable and `python --version` already shows 3.13.x:
python -m venv .venv

# macOS:
python3.13 -m venv .venv

# Windows:
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt -r requirements-dev.txt

# macOS:
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/python -m pip install -r requirements.txt -r requirements-dev.txt

# Verify
.\.venv\Scripts\python.exe tools/setup_student.py   # Windows
./.venv/bin/python tools/setup_student.py           # macOS
```

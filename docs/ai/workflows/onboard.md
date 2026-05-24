# Onboard Workflow

## Use When

Use when a student needs first-time repo setup, environment verification, or
help getting Python 3.13, packages, or Word report tooling working.

This workflow has two phases:

1. install Python 3.13 if it is missing
2. create or repair the repo `.venv` and verify the environment

The workflow also checks `ripgrep` (`rg`) as a recommended AI search tool.
If `rg` is missing, warn and continue. Python coursework, packages, and Word
report tooling do not depend on it.

Default first-time commands:

```powershell
# Windows, from the repo root in PowerShell
powershell -ExecutionPolicy Bypass -File tools/bootstrap_windows.ps1
```

```bash
# macOS, from the repo root in Terminal or PyCharm's terminal
bash tools/bootstrap_macos.sh
```

Agent helper once a usable Python command exists:

```bash
python tools/workflow.py onboard
```

Verification-only and intentional rebuild modes:

```bash
python tools/workflow.py onboard --check
python tools/workflow.py onboard --rebuild
```

## Inputs

- optional error output from the student's machine
- the current OS

## Required Context

- `AGENTS.md`
- `docs/setup/troubleshooting.md`
- `docs/setup/windows.md`
- `docs/setup/macos.md`
- `docs/setup/pycharm.md`
- `tools/setup_student.py`

## Procedure

1. Detect Windows vs macOS vs Linux before suggesting commands.
2. Confirm the student is in the cloned `fins-agent` repo root. In PyCharm,
   the project root and terminal working directory should be the same folder.
3. Check whether Python 3.13 is available.
4. If Python 3.13 is missing:
   - show only the install command for the student's OS
   - explain that the repo helper cannot run until Python 3.13 exists
   - stop there until Python 3.13 is installed
5. On macOS, verify Python and pip before setup:
   - `python3.13 --version`
   - `python3.13 -m pip --version`
   If pip fails with `pyexpat`, `xml.parsers.expat`, `libexpat`, or
   `XML_SetAllocTrackerActivationThreshold`, treat Homebrew Python as the
   failing path. Tell the student to stop rerunning bootstrap, use the
   Python.org macOS installer, reopen Terminal or PyCharm, and verify pip
   again.
6. If the Mac repo is under an iCloud-synced Desktop or Documents folder,
   suggest moving it to a local folder such as `~/Developer/GitHub`.
7. Once Python 3.13 is available, use the OS bootstrap script for a true
   first-time setup or `python tools/workflow.py onboard` from an agent that
   has already found a Python command.
8. Check `rg --version` and `rg --files -g AGENTS.md`. If `rg` is missing,
   try the platform package manager when available:
   - Windows: `winget install --id BurntSushi.ripgrep.MSVC -e`
   - macOS: `brew install ripgrep`
   If install fails or PATH does not refresh, warn and continue.
9. Before changing an existing `.venv`, run the repo interpreter on
   `tools/setup_student.py`. If it passes, stop; do not rebuild or reinstall.
10. If repair is needed on Windows, first check whether PyCharm Python Console,
   notebooks, Streamlit apps, or terminals are using `.venv`. Ask the student
   to close them before changing the environment.
11. The setup endpoint is Python 3.13, required packages, `fintools`, and Word
   report support through `python-docx`. Microsoft Word itself is not checked.
12. If a required step fails, explain what failed and route the student to
   the relevant setup doc instead of changing repo dependencies or checked-in
   files.
13. End with a short status summary for Python, packages, Word report tooling,
    and the advisory `rg` search check.

## PyCharm Notes

- Prefer PyCharm's built-in terminal for setup commands so the IDE and
  terminal use the same repo root.
- On Windows, use PowerShell or cmd for repo commands. Git Bash uses
  different path syntax.
- Before repairing setup on Windows, close Python Console tabs, notebooks,
  running apps, and terminals that use `.venv`.
- Codex in PyCharm through JetBrains AI may not load Codex CLI skills or
  MCP state. If that happens, attach `AGENTS.md` and this workflow doc, or
  switch to Codex CLI in PyCharm's terminal.

## Output

- clear next steps
- student-friendly wording
- no jargon about repo internals

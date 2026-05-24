#!/usr/bin/env python3
r"""Post-setup verification for the fins-agent coursework toolkit.

Run this after creating `.venv` and installing the requirements to verify
that all packages and Word report tooling are available. This script is
called by the onboarding workflow and can also be run manually:

    Windows: .\.venv\Scripts\python.exe tools/setup_student.py
    macOS/Linux: ./.venv/bin/python tools/setup_student.py
"""

from __future__ import annotations

import platform
import shutil
import subprocess
import sys
from pathlib import Path

REQUIRED_PYTHON = (3, 13)
REPO_ROOT = Path(__file__).resolve().parents[1]


def check_mark(ok: bool) -> str:
    return "OK" if ok else "MISSING"


def python_install_hint() -> str:
    system = platform.system()
    if system == "Windows":
        return "winget install Python.Python.3.13"
    if system == "Darwin":
        return "brew install python@3.13"
    return "sudo apt install python3.13 python3.13-venv"


def bootstrap_command_hint() -> str:
    system = platform.system()
    if system == "Windows":
        return r"powershell -ExecutionPolicy Bypass -File tools/bootstrap_windows.ps1"
    if system == "Darwin":
        return "bash tools/bootstrap_macos.sh"
    return "python3.13 -m venv .venv"


def ripgrep_install_hint() -> str:
    system = platform.system()
    if system == "Windows":
        return "winget install --id BurntSushi.ripgrep.MSVC -e"
    if system == "Darwin":
        return "brew install ripgrep"
    return "install ripgrep with your OS package manager"


def repo_python_path() -> Path:
    if platform.system() == "Windows":
        return REPO_ROOT / ".venv" / "Scripts" / "python.exe"
    return REPO_ROOT / ".venv" / "bin" / "python"


def repo_python_command() -> str:
    if platform.system() == "Windows":
        return r".\.venv\Scripts\python.exe"
    return "./.venv/bin/python"


def create_venv_help_lines() -> list[str]:
    if platform.system() == "Windows":
        return [
            "py -3.13 -m venv .venv",
            "If `py` is unavailable but `python --version` is already 3.13.x:",
            "python -m venv .venv",
        ]
    return ["python3.13 -m venv .venv"]


def check_repo_interpreter() -> bool:
    expected = repo_python_path()
    actual = Path(sys.executable).resolve()
    actual_prefix = Path(sys.prefix).resolve()
    expected_prefix = (REPO_ROOT / ".venv").resolve()

    if expected.exists() and actual_prefix == expected_prefix:
        print(f"  [OK] repo interpreter ({actual})")
        return True

    print("  [MISSING] repo interpreter")
    if not expected.exists():
        print("         The repo .venv was not found yet.")
        print("         From the repo root, run:")
        print(f"         {bootstrap_command_hint()}")
        print("         Or create it manually with:")
        for line in create_venv_help_lines():
            print(f"         {line}")
        print(f"         {repo_python_command()} -m pip install --upgrade pip")
        print(
            "         "
            f"{repo_python_command()} -m pip install -r requirements.txt -r requirements-dev.txt"
        )
        return False

    print(f"         Current interpreter: {actual}")
    print(f"         Current prefix: {actual_prefix}")
    print(f"         Use the repo interpreter instead: {repo_python_command()}")
    return False


def check_python() -> bool:
    version = sys.version_info
    ok = (version.major, version.minor) == REQUIRED_PYTHON
    status = check_mark(ok)
    print(f"  [{status}] Python {version.major}.{version.minor}.{version.micro}")
    if not ok:
        print("         Python 3.13 is required.")
        print(f"         Install it first: {python_install_hint()}")
    return ok


def check_import(name: str, display: str | None = None) -> bool:
    display = display or name
    try:
        __import__(name)
        print(f"  [OK] {display}")
        return True
    except ImportError:
        print(f"  [MISSING] {display}")
        print(
            "         Run: "
            f"{repo_python_command()} -m pip install -r requirements.txt -r requirements-dev.txt"
        )
        return False
    except Exception as exc:
        print(f"  [BROKEN] {display}")
        print(f"         Import failed with {type(exc).__name__}: {exc}")
        print("         Close Python Console tabs, notebooks, running apps, and terminals")
        print("         that use .venv, then rerun:")
        print("         python tools/workflow.py onboard --rebuild")
        return False


def check_word_tooling() -> bool:
    try:
        from docx import Document
    except ImportError:
        print("  [MISSING] Word report tooling (python-docx)")
        print(
            "         Run: "
            f"{repo_python_command()} -m pip install -r requirements.txt -r requirements-dev.txt"
        )
        return False
    except Exception as exc:
        print("  [BROKEN] Word report tooling (python-docx)")
        print(f"         Import failed with {type(exc).__name__}: {exc}")
        print("         Close Python Console tabs, notebooks, running apps, and terminals")
        print("         that use .venv, then rerun:")
        print("         python tools/workflow.py onboard --rebuild")
        return False

    document = Document()
    document.add_paragraph("Word report tooling check")
    print("  [OK] Word report tooling (python-docx)")
    return True


def print_ripgrep_warning(detail: str) -> None:
    print("  [WARN] ripgrep")
    print(f"         {detail}")
    print("         AI assistants can still work, but repo search will be slower.")
    print(f"         Suggested install: {ripgrep_install_hint()}")
    print("         If the command was just installed, close and reopen your terminal")
    print("         or PyCharm, then rerun setup.")


def check_ripgrep() -> bool:
    path = shutil.which("rg")
    if not path:
        print_ripgrep_warning("ripgrep (`rg`) was not found on PATH.")
        return False

    try:
        version_proc = subprocess.run(
            ["rg", "--version"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=10,
            check=False,
        )
    except Exception as exc:
        print_ripgrep_warning(f"`rg --version` failed with {type(exc).__name__}: {exc}")
        return False

    if version_proc.returncode != 0:
        detail = version_proc.stderr.strip() or version_proc.stdout.strip()
        print_ripgrep_warning(f"`rg --version` failed. {detail}".strip())
        return False

    try:
        repo_proc = subprocess.run(
            ["rg", "--files", "-g", "AGENTS.md"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=10,
            check=False,
        )
    except Exception as exc:
        print_ripgrep_warning(
            f"`rg --files -g AGENTS.md` failed with {type(exc).__name__}: {exc}"
        )
        return False

    if repo_proc.returncode != 0 or "AGENTS.md" not in repo_proc.stdout:
        detail = repo_proc.stderr.strip() or repo_proc.stdout.strip()
        print_ripgrep_warning(
            "`rg --files -g AGENTS.md` did not find the repo context file."
            f" {detail}".strip()
        )
        return False

    first_line = version_proc.stdout.splitlines()[0] if version_proc.stdout else path
    print(f"  [OK] ripgrep ({first_line})")
    return True


def check_pip() -> bool:
    try:
        proc = subprocess.run(
            [sys.executable, "-m", "pip", "--version"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=10,
            check=False,
        )
    except Exception:
        proc = None

    if proc and proc.returncode == 0 and proc.stdout.strip():
        print(f"  [OK] pip ({proc.stdout.strip()})")
        return True

    print("  [MISSING] pip")
    print("         From the repo root, rerun:")
    print(f"         {bootstrap_command_hint()}")
    print("         Or recreate the environment manually with:")
    for line in create_venv_help_lines():
        print(f"         {line}")
    print(f"         {repo_python_command()} -m pip install --upgrade pip")
    return False


def main() -> int:
    print()
    print("=" * 50)
    print("  Fintech Toolkit - Setup Check")
    print("=" * 50)
    print(f"  Repo root: {REPO_ROOT}")
    if Path.cwd().resolve() != REPO_ROOT:
        print(f"  Current shell directory: {Path.cwd().resolve()}")
        print("  Tip: run setup commands from the repo root.")
    print()

    results: list[bool] = []

    print("Step 1: Repo Interpreter")
    results.append(check_repo_interpreter())
    print()

    print("Step 2: Python")
    results.append(check_python())
    print()

    print("Step 3: Package Manager")
    results.append(check_pip())
    print()

    print("Step 4: Python Packages")
    for name, display in [
        ("pandas", "pandas"),
        ("numpy", "numpy"),
        ("matplotlib", "matplotlib"),
        ("seaborn", "seaborn"),
        ("statsmodels", "statsmodels"),
        ("pyarrow", "pyarrow"),
        ("docx", "python-docx"),
        ("streamlit", "streamlit"),
        ("plotly", "plotly"),
    ]:
        results.append(check_import(name, display))
    print()

    print("Step 5: Shared Utilities")
    results.append(check_import("fintools", "fintools"))
    print()

    print("Step 6: Word Report Tooling")
    results.append(check_word_tooling())
    print()

    print("Step 7: AI Workflow Tools")
    check_ripgrep()
    print()

    print("=" * 50)
    all_required_ok = all(results)
    if all_required_ok:
        print("  All required checks passed. You're ready to go!")
    else:
        print("  Some checks failed. See above for fix instructions.")
        print(
            "  Then run this script again with: "
            f"{repo_python_command()} tools/setup_student.py"
        )
    print("=" * 50)

    system = platform.system()
    interp = r".venv\Scripts\python.exe" if system == "Windows" else ".venv/bin/python"
    print()
    print("  PyCharm users: set your interpreter to:")
    print(f"    {interp}")
    print(f"    {REPO_ROOT / interp}")
    print("  (Settings > Python Interpreter > Add > Existing > browse to above)")
    print()

    print("  Next steps:")
    if all_required_ok:
        print("    1. docs/setup/pycharm.md")
        print("    2. docs/ai/start-here.md")
        print("    3. fins2026/week0/")
    else:
        print("    1. docs/setup/troubleshooting.md")
        print("    2. docs/setup/ai-troubleshooting.md")
        print("    3. docs/setup/pycharm.md")
    print()

    return 0 if all_required_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

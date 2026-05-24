#!/usr/bin/env bash
set -euo pipefail

echo "Bootstrapping fins-agent with Python 3.13 and pip..."

if [[ ! -f "$PWD/pyproject.toml" || ! -f "$PWD/tools/setup_student.py" ]]; then
  echo "This script must be run from the fins-agent repo root."
  echo "Expected to find pyproject.toml and tools/setup_student.py in:"
  echo "  $PWD"
  echo "Fix: cd into the cloned fins-agent folder, then rerun."
  exit 1
fi

TEMP_ROOT="$PWD/.tmp-bootstrap/bootstrap-$$"
mkdir -p "$TEMP_ROOT"
export TMPDIR="$TEMP_ROOT"
export TMP="$TEMP_ROOT"
export TEMP="$TEMP_ROOT"

ripgrep_works() {
  if ! command -v rg >/dev/null 2>&1; then
    return 1
  fi
  if ! rg --version >/dev/null 2>&1; then
    return 1
  fi
  rg_files="$(rg --files -g AGENTS.md 2>/dev/null || true)"
  case "$rg_files" in
    *AGENTS.md*) ;;
    *) return 1 ;;
  esac
  return 0
}

ensure_ripgrep_recommended_tool() {
  echo "Checking optional AI search tool: ripgrep..."
  if ripgrep_works; then
    version="$(rg --version | head -n 1)"
    echo "ripgrep ready: $version"
    return
  fi

  echo "Warning: ripgrep (rg) is not available yet."
  echo "AI assistants can still work, but repo search will be slower."
  if ! command -v brew >/dev/null 2>&1; then
    echo "Suggested install after setup: brew install ripgrep"
    echo "If brew is missing, install Homebrew and follow its PATH instructions."
    return
  fi

  echo "Trying to install ripgrep for faster AI-assisted repo search..."
  if ! brew install ripgrep; then
    echo "Warning: could not install ripgrep automatically. Continuing setup."
    echo "Suggested install later: brew install ripgrep"
    return
  fi

  if ! ripgrep_works; then
    echo "Warning: ripgrep installed, but this shell cannot run rg yet."
    echo "Close and reopen Terminal or PyCharm, then run: rg --version"
  fi
}

looks_like_macos_pyexpat_failure() {
  case "$1" in
    *pyexpat*|*xml.parsers.expat*|*libexpat*|*XML_SetAllocTrackerActivationThreshold*)
      return 0
      ;;
    *)
      return 1
      ;;
  esac
}

check_python_pip_startup() {
  echo "Checking Python 3.13 pip startup..."
  if pip_output="$("$PYTHON_BIN" -m pip --version 2>&1)"; then
    echo "pip ready: $pip_output"
    return
  fi

  echo "Python 3.13 was found at: $PYTHON_BIN"
  echo "But pip could not start:"
  echo "$pip_output"
  if looks_like_macos_pyexpat_failure "$pip_output"; then
    echo
    echo "This looks like the macOS Homebrew Python pyexpat/libexpat issue."
    echo "Do not keep rerunning bootstrap; it will fail before the course .venv exists."
    echo "Install Python 3.13 from https://www.python.org/downloads/macos/ or ask for help."
    echo "Then close and reopen Terminal or PyCharm and verify:"
    echo "  python3.13 -m pip --version"
  else
    echo
    echo "Fix Python 3.13 pip first, then rerun bootstrap."
    echo "Try closing and reopening Terminal or PyCharm. If pip still fails, use the Python.org macOS installer or ask for help."
  fi
  exit 1
}

ensure_ripgrep_recommended_tool

if [[ -x "./.venv/bin/python" ]]; then
  echo "Checking existing .venv before rebuilding..."
  if ./.venv/bin/python tools/setup_student.py; then
    echo "Existing .venv passed setup checks; bootstrap complete."
    exit 0
  fi
  echo "Existing .venv did not pass setup checks; bootstrap will repair it."
fi

if command -v python3.13 >/dev/null 2>&1; then
  PYTHON_BIN="python3.13"
elif command -v python3 >/dev/null 2>&1 && python3 --version 2>&1 | grep -q '^Python 3\.13'; then
  PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1 && python --version 2>&1 | grep -q '^Python 3\.13'; then
  PYTHON_BIN="python"
else
  echo "Python 3.13 was not found."
  echo "Install it first with: brew install python@3.13"
  exit 1
fi

check_python_pip_startup

BUNDLED_PIP="$("$PYTHON_BIN" -c "import ensurepip, pathlib; d = pathlib.Path(ensurepip.__file__).resolve().parent / '_bundled'; print(sorted(d.glob('pip-*.whl'))[-1])")"
"$PYTHON_BIN" -m venv --clear --without-pip .venv
"$PYTHON_BIN" -m pip --python ./.venv/bin/python install "$BUNDLED_PIP"
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/python -m pip install -r requirements.txt -r requirements-dev.txt
./.venv/bin/python tools/setup_student.py

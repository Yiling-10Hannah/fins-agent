---
name: onboard
description: "Set up the Fintech coursework toolkit for a new student. Installs Python 3.13, packages, and checks Word report tooling."
argument-hint: ""
---

# Student Onboarding

Read `docs/ai/workflows/onboard.md` and follow it as the canonical
workflow.

Important bootstrap rule:

- if Python 3.13 is missing, help the student install Python 3.13 first
- warn but continue if `ripgrep` (`rg`) is missing; it only speeds up
  AI-assisted repo search
- for a true first-time setup, use the OS bootstrap script from the repo root
- only use `python tools/workflow.py onboard` after a usable Python command exists

Preferred deterministic commands:

- Windows: `powershell -ExecutionPolicy Bypass -File tools/bootstrap_windows.ps1`
- macOS: `bash tools/bootstrap_macos.sh`
- Agent helper: `python tools/workflow.py onboard`
- Verify only: `python tools/workflow.py onboard --check`
- Intentional rebuild: `python tools/workflow.py onboard --rebuild`

PyCharm note:

- on Windows, close Python Console tabs and running apps that use `.venv`
  before repair or rebuild

If this wrapper conflicts with the shared workflow doc, the shared workflow
doc wins.

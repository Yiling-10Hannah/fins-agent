---
name: onboard
description: Use when a student says set me up, onboard me, help me install Python 3.13, verify the repo environment, check Word report tooling, or fix first-time setup.
argument-hint: ""
---

# Onboard Skill

Read `docs/ai/workflows/onboard.md` and follow it as the canonical workflow.

Typical triggers:

- "set me up"
- "onboard me"
- "help me install Python 3.13"
- "check whether this repo is set up correctly"

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

- prefer PyCharm's built-in terminal for setup commands so the IDE and
  terminal use the same repo root
- on Windows, close Python Console tabs and running apps that use `.venv`
  before repair or rebuild

If the workflow doc conflicts with older tool-specific instructions, the
shared workflow doc wins.

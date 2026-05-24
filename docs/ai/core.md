# Shared AI Context

This repository is a fintech coursework toolkit for students built to work
closely with AI.

## Operating Model

- Shared AI guidance lives in `docs/ai/`.
- `docs/ai/start-here.md` is the first stop for students choosing an AI
  path.
- Shared workflow logic lives in `docs/ai/workflows/`.
- Claude Code uses `CLAUDE.md` plus `.claude/skills/`.
- Claude Code in PyCharm uses the same Claude repo surfaces and is
  documented separately in `docs/ai/claude-pycharm.md`.
- OpenAI-native Codex uses `AGENTS.md`, `.agents/skills/`, and
  `.codex/config.toml`.
- Codex in PyCharm via JetBrains AI is documented separately in
  `docs/ai/codex-pycharm.md`.
- OpenCode in PyCharm uses JetBrains ACP and can use the repo's
  `AGENTS.md`; it is documented separately in `docs/ai/opencode-pycharm.md`.
- Gemini CLI uses `GEMINI.md`, `.gemini/settings.json`, and
  `.gemini/commands/`.
- Gemini CLI in PyCharm uses the same Gemini repo surfaces and is
  documented separately in `docs/ai/gemini-pycharm.md`.
- Qwen Code uses `AGENTS.md`, `QWEN.md`, `.qwen/settings.json`, and
  `.qwen/skills/`.
- Qwen Code in PyCharm uses the same Qwen repo surfaces and is documented
  separately in `docs/ai/qwen-pycharm.md`.
- `docs/ai/rules/` is the shared source of truth for academic writing, Word
  reporting, citation, presentation, and legacy LaTeX rules.
- `docs/ai/code-review.md` is the shared assistant code-review rubric.
- `docs/ai/CONTEXT_AUDIT.md` is the checklist for auditing and hardening
  assistant context after repo or setup changes.
- `docs/setup/ai-support-matrix.md` and `docs/setup/ai-troubleshooting.md`
  are the shared setup and support references.

## Project Structure

- `fintools/` - shared Python utilities
- `docs/apps/streamlit/` - shared Streamlit app-building guidance
- `fins2026/` - weekly course folders, each with its own `data/` subfolder
- `projects/` - student project workspace
- `tools/` - setup and verification scripts
- `.claude/` - Claude wrappers plus writing rules
- `.agents/` - Codex skills
- `.codex/` - project-scoped Codex configuration
- `.gemini/` - Gemini project configuration and commands
- `.qwen/` - Qwen project configuration and skills

## Python Environment

- Python version: 3.13 (pinned in `.python-version`)
- Virtual environment: `.venv/` in the repo root
- Interpreter path:
  - Windows: `.venv\Scripts\python.exe`
  - macOS/Linux: `.venv/bin/python`
- Bootstrap helpers:
  - Windows: `powershell -ExecutionPolicy Bypass -File tools/bootstrap_windows.ps1`
  - macOS: `bash tools/bootstrap_macos.sh`
- Recommended AI search tool: `ripgrep` (`rg`)
  - Verify with `rg --version` and `rg --files -g AGENTS.md`
  - If missing, setup should warn but not fail; coursework can continue

## Package Management

This repo uses pip-managed requirements files:

- `requirements.txt` - runtime packages
- `requirements-dev.txt` - dev tools plus editable install of the repo
- terminal repo interpreter:
  - Windows: `.\.venv\Scripts\python.exe`
  - macOS/Linux: `./.venv/bin/python`
- repo interpreter + `-m pip install -r requirements.txt -r requirements-dev.txt`
  - install or refresh the environment
- repo interpreter + `tools/workflow.py ...`
  - run shared deterministic repo helpers

Students should use the requirements files and should not treat the PyCharm
package UI as the source of truth for repo dependencies.

## Dependency Changes

If a student asks to install a Python package:

- decide whether it belongs in `requirements.txt` or `requirements-dev.txt`
- update the correct requirements file before installing
- install or refresh packages with the repo interpreter plus
  `-m pip install -r requirements.txt -r requirements-dev.txt`
- in PyCharm, run the install step from the built-in terminal at the repo
  root so the shell, interpreter, and project stay aligned
- do not use the PyCharm package UI as the source of truth
- do not do ad hoc `pip install <package>` without updating requirements
  unless the student explicitly wants a temporary local experiment
- rerun the failing command, test, or `tools/setup_student.py` when relevant

## Conventions

- Each week has its own `data/` subfolder. Load datasets from there.
- Standard weekly scaffolds live under `fins2026/weekN/` with `data/`,
  `code/`, `scripts/`, `scratch/`, `results/`, `guidance/`, `prompts/`,
  `app/`, and `tests/`.
- Keep reusable code in `fintools/`.
- Weekly exercises go in `fins2026/weekN/`.
- Larger projects go in `projects/`.
- Use `python tools/workflow.py scaffold-week --target fins2026/weekN` to
  create or backfill the weekly scaffold.
- Use `python tools/workflow.py build-week-context --target fins2026/weekN`
  to refresh week, data, and output context files under `guidance/`.
- Use `fintools.figures` first for publication-quality figures, with
  matplotlib for time-series and final axis control and seaborn for
  statistical charts, distributions, and heatmaps.
- Mixed-frequency macro teaching weeks must declare both a common reference
  endpoint and a classroom information-set date before figures or merged
  panels are treated as canonical.
- Use `docs/apps/streamlit/` and the `build-app` workflow when turning
  analysis into a public Streamlit app.

# Project Guide

This repository is a fintech coursework toolkit for students. It supports
data analysis, portfolio construction, and academic writing with Word-first
reports.

## Repo Surfaces

Treat these as the repo-native entrypoints for each assistant:

- Claude Code: `CLAUDE.md` and `.claude/skills/`
- Codex: `AGENTS.md`, `.agents/skills/`, and `.codex/config.toml`
- Gemini CLI: `GEMINI.md`, `.gemini/settings.json`, and `.gemini/commands/`
- Qwen Code: `AGENTS.md`, `QWEN.md`, `.qwen/settings.json`, and
  `.qwen/skills/`

## Operating Model

- `docs/ai/workflows/*.md` is the shared source of truth for workflow
  behavior.
- `.claude/skills/*/SKILL.md`, `.agents/skills/*/SKILL.md`,
  `.gemini/commands/*`, and `.qwen/skills/*/SKILL.md` are assistant-specific
  adapters over those shared workflow docs.
- `docs/ai/rules/*` is the shared source of truth for academic writing,
  Word reporting, citation verification, presentation style, and legacy
  LaTeX rules.
- `docs/ai/code-review.md` is the shared review rubric for assistant code
  reviews.

If an assistant-specific adapter conflicts with a shared workflow doc, the
shared workflow doc wins.

## Common Commands

These are the quickest repo-level commands for assistants that need an
executable next step.

- Verify setup with the repo interpreter on `tools/setup_student.py`
- Run shared helpers with the repo interpreter on `tools/workflow.py list`
- Run tests with the repo interpreter on `-m pytest -q`
- Run lint with the repo interpreter on `-m ruff check .`
- Check the recommended AI search tool with `rg --version` and
  `rg --files -g AGENTS.md`
- For review tasks, read `docs/ai/code-review.md` before reporting findings

Repo interpreter paths:

- Windows: `.\.venv\Scripts\python.exe`
- macOS/Linux: `./.venv/bin/python`

## What This Repo Does

- Course weeks eventually span `fins2026/week0` through `fins2026/week10`.
- Public student releases may expose only the weeks published so far; the
  current release includes `fins2026/week0` through `fins2026/week5`.
- Shared Python utilities live in `fintools/`.
- Larger student projects live in `projects/`.
- Word report scaffolding is generated with `python-docx`; legacy LaTeX
  boilerplate lives in `boilerplate/`.
- Streamlit app-building guidance lives in `docs/apps/streamlit/`.

## First Actions for New Students

- If a student wants setup or says "set me up", use the `onboard` workflow.
- The practical verification command uses the repo interpreter on
  `tools/setup_student.py`.
- If the student is not using AI-driven setup, send them to `QUICKSTART.md`.
- Week 0 orientation lives in `fins2026/week0/`.
- Codex in PyCharm is a separate host path. Treat it through
  `docs/ai/codex-pycharm.md` instead of assuming full CLI parity.
- `ripgrep` (`rg`) is recommended for AI-assisted repo search. Setup should
  warn, not fail, if it is missing; Python coursework can continue.

## Task Routing

### Setup and Environment

- Use the `onboard` workflow for first-time setup.
- Onboarding is two-phase:
  - if Python 3.13 is missing, help the student install Python 3.13 first
  - for first-time setup, use the OS bootstrap script from the repo root
  - once a usable Python command exists, `python tools/workflow.py onboard`
    is the agent helper
  - use `python tools/workflow.py onboard --check` for verification only
  - use `python tools/workflow.py onboard --rebuild` only when intentionally
    recreating `.venv`
- Primary scripts after bootstrap:
  - Windows: `powershell -ExecutionPolicy Bypass -File tools/bootstrap_windows.ps1`
  - macOS: `bash tools/bootstrap_macos.sh`
  - agent helper: `python tools/workflow.py onboard`
  - repo interpreter + `tools/setup_student.py`
- Troubleshooting docs: `docs/setup/troubleshooting.md`,
  `docs/setup/windows.md`, `docs/setup/macos.md`, `docs/setup/pycharm.md`
- Package manager: always use `python -m pip`

### Weekly Analysis Work

- Load data from the current week's `data/` subfolder.
- Use `scaffold-week` to create or backfill the standard `fins2026/weekN/`
  structure when a week folder needs the full scaffold.
- Use `build-week-context` to refresh `guidance/week-context.md`,
  `guidance/data-context.md`, and `guidance/output-context.md` after week
  docs, scripts, data, or outputs change.
- Keep reusable code in `fintools/` instead of copying logic across weeks.
- Use pandas, numpy, matplotlib, seaborn, and statsmodels from the shared
  environment.
- Use `fintools.figures` for report-ready charts and Word/A4 exports before
  writing custom plotting boilerplate.
- Use `build-app` and `docs/apps/streamlit/` when students turn analysis into
  Streamlit apps. Public grading submissions should include the app URL,
  GitHub URL, branch, and entrypoint path.
- Use `audit-app` when students ask for a Streamlit app audit, review,
  benchmark, hardening pass, or best-practice gap analysis.

### Project Scaffolding

- `new-project` creates project scaffolds under `projects/<name>/`.
- `scaffold-week` creates or backfills a standard weekly scaffold under
  `fins2026/weekN/`.
- `new-project --with-app` includes a Streamlit app scaffold.
- `build-app` creates a Streamlit app scaffold in an existing week or project
  folder.
- `build-week-context` generates `guidance/week-context.md`,
  `guidance/data-context.md`, and `guidance/output-context.md` for a week.
- `setup-paper` creates `report/report.docx` by default. Legacy LaTeX is
  available only with `--format latex`.
- Keep reusable production code in `code/`, exploratory work in `scripts/`,
  Word reports in `report/`, Streamlit app code in `app/`, and outputs in
  `results/`.

### Writing and Reports

- Shared workflow docs: `docs/ai/workflows/`
- Shared writing guide: `docs/ai/writing.md`
- Shared review guide: `docs/ai/code-review.md`
- Context audit checklist: `docs/ai/CONTEXT_AUDIT.md`
- Codex guide: `docs/ai/codex.md`
- Gemini guide: `docs/ai/gemini.md`
- Qwen guide: `docs/ai/qwen.md`
- Academic style rules: `docs/ai/rules/academic-writing.md`
- Word reporting rules: `docs/ai/rules/word-reporting.md`
- Citation verification rules: `docs/ai/rules/citation-verification.md`
- Legacy LaTeX conventions: `docs/ai/rules/legacy-latex.md`
- Presentation rules: `docs/ai/rules/presentation.md`
- Legacy LaTeX boilerplate templates: `boilerplate/template_main.tex`,
  `boilerplate/template_references.bib`, `boilerplate/template_slides.tex`

Available workflows:

- `onboard`
- `new-project`
- `scaffold-week`
- `setup-paper`
- `word-report`
- `write-section`
- `edit-section`
- `proofread`
- `build-paper`
- `build-deck`
- `build-figure`
- `build-app`
- `audit-app`
- `build-context`
- `build-week-context`
- `outline`
- `latex-doctor`

## Package Management

This repo uses Python 3.13, a repo-local `.venv/`, and pip-managed
requirements files.

- In terminal commands after `.venv` exists, use the repo interpreter:
  - Windows: `.\.venv\Scripts\python.exe`
  - macOS/Linux: `./.venv/bin/python`
- Windows: `py -3.13 -m venv .venv` creates the environment when the Python Launcher is available
- Windows fallback: `python -m venv .venv` is acceptable only after `python --version` confirms 3.13.x
- macOS/Linux: `python3.13 -m venv .venv` creates the environment
- repo interpreter + `-m pip install -r requirements.txt -r requirements-dev.txt`
  installs packages
- repo interpreter + `tools/workflow.py ...` runs shared deterministic repo
  helpers
- `python path/to/script.py` is fine only after the environment is active or
  selected in PyCharm

Students should not edit the environment manually with random package
installs. If the repo should keep a package, update `requirements.txt` or
`requirements-dev.txt` and reinstall.

If a student asks to install a Python package:

- decide whether it belongs in `requirements.txt` or `requirements-dev.txt`
- update the correct requirements file first
- install with the repo interpreter plus `-m pip`
- in PyCharm, prefer the built-in terminal at the repo root for the install
  step so the active shell and `.venv` stay aligned
- avoid ad hoc installs that are not reflected in the requirements files

## Project Structure Rules

- Each week has its own `data/` subfolder. Load datasets from there.
- Keep weekly work in `fins2026/weekN/`.
- Keep larger projects in `projects/`.
- Use `fintools` for reusable code rather than duplicating across scripts.

# Weekly Coursework Guide

This directory contains weekly course workspaces. Root `AGENTS.md` still
applies; these rules add local guidance for `fins2026/weekN/` folders.

## Weekly Rules

- Keep week-specific work inside the matching `fins2026/weekN/` folder.
- Load datasets from that week's `data/` subfolder with paths relative to the
  repo root or the current week folder.
- Use `results/data/` for generated, cleaned, downloaded, or merged
  datasets, not `data/`.
- Keep disposable experiments in `scratch/`; promote anything real into
  `scripts/`, `code/`, or `fintools/`.
- Put reusable Python logic in `fintools/` instead of copying helper code
  between weeks.
- Use the repo interpreter for commands:
  - Windows: `..\.venv\Scripts\python.exe` from inside `fins2026/`, or
    `.\.venv\Scripts\python.exe` from the repo root
  - macOS/Linux: `../.venv/bin/python` from inside `fins2026/`, or
    `./.venv/bin/python` from the repo root
- Use `fintools.figures` for Word/A4-ready charts before writing custom
  plotting boilerplate.
- Keep generated outputs under the current week unless a workflow explicitly
  targets a project folder.
- Use `python tools/workflow.py scaffold-week --target fins2026/weekN` when a
  week folder needs the full standard scaffold.
- Use `python tools/workflow.py build-week-context --target fins2026/weekN`
  after the week docs, scripts, data, or outputs change.
- For mixed-frequency macro weeks, explicitly declare the common reference
  endpoint, the classroom information-set date, and whether panels are aligned
  on reference dates or observable dates before merging or plotting.

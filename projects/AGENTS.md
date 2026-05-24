# Student Projects Guide

This directory contains larger student projects. Root `AGENTS.md` still
applies; these rules add local guidance for `projects/<name>/` folders.

## Project Layout

- Keep production Python code in `code/`.
- Keep exploratory or one-off scripts in `scripts/`.
- Keep Word reports in `report/`, with `report/report.docx` as the default
  report source.
- Keep Streamlit app code in `app/`.
- Keep generated tables, figures, and exports in `results/`.
- Keep reusable cross-project helpers in `fintools/`, not copied between
  project folders.

## Workflow Rules

- Use `new-project` to scaffold new project folders.
- Use `setup-paper` without `--format latex` for Word report scaffolds.
- Use `build-app` when turning project analysis into a Streamlit app.
- Public app submissions should include the deployed app URL, GitHub URL,
  branch, and app entrypoint path.
- Run repo helpers with the repo interpreter from the repo root:
  - Windows: `.\.venv\Scripts\python.exe tools\workflow.py ...`
  - macOS/Linux: `./.venv/bin/python tools/workflow.py ...`


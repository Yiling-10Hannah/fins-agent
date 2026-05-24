# New Project Workflow

## Use When

Use when a student wants a clean project scaffold under `projects/`.

Deterministic helper:

```bash
python tools/workflow.py new-project <name> [--description "..."] [--datasets "..."] [--notes "..."]
```

Add `--with-app` when the project should include a Streamlit app scaffold.

## Inputs

- required project name
- optional description
- optional data sources or notes

## Required Context

- `AGENTS.md`
- `projects/`
- Word report workflow docs

## Procedure

1. Parse the first token as the project name and treat remaining text as an
   optional description.
2. Validate the name: lowercase, underscores only, starts with a letter,
   length 2-50, and not a Windows-reserved device name.
3. Refuse to overwrite `projects/<name>/` if it already exists.
4. If description or project context is missing, ask for a short
   description, expected datasets, and any initial notes.
5. Create this scaffold:
   - `projects/<name>/report/`
   - `projects/<name>/code/`
   - `projects/<name>/scripts/`
   - `projects/<name>/results/figures/`
   - `projects/<name>/results/tables/`
6. Create `README.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `QWEN.md`,
   `.gitignore`, and `scripts/make_figures.py` in the project root.
7. If `--with-app` is set, also create `app/streamlit_app.py`,
   `app/README.md`, root `.streamlit/config.toml`, `SUBMISSION_CHECKLIST.md`,
   `app/tests/`, and `results/app/`.
8. Offer the follow-on `setup-paper` workflow after the scaffold is created;
   it creates `report/report.docx` by default.

## Output

- collision-safe scaffold
- clear summary of files and next steps

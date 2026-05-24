# Setup Paper Workflow

## Use When

Use when a student wants a coursework report scaffold. Word is the default.
Legacy LaTeX is available only when explicitly requested.

Deterministic helper:

```bash
python tools/workflow.py setup-paper --title "..." [--authors "..."] [--topic "..."] [--target PATH] [--format word|latex] [--no-compile]
```

## Inputs

- title
- optional `--authors`
- optional `--topic`

## Required Context

- `AGENTS.md`
- `docs/ai/rules/academic-writing.md`
- `docs/ai/rules/word-reporting.md`
- `boilerplate/template_main.tex` and `boilerplate/template_references.bib`
  only for `--format latex`

## Procedure

1. Default to `--format word`.
2. Resolve the Word target:
   - inside `projects/<name>/` -> use `projects/<name>/report/report.docx`
   - inside a `report/` directory -> use `report.docx`
   - explicit `.docx` paths are allowed
3. Create the `.docx` scaffold with A4 layout, built-in Word styles, title
   block, abstract, table of contents field, standard report sections, and
   `[REMOVE]` placeholders.
4. Preserve Word built-in styles so Navigation Pane, table of contents, and
   accessibility checks work.
5. If `--format latex` is explicitly provided, use the legacy LaTeX boilerplate
   path and compile only when `--no-compile` is not set.

## Output

- `report/report.docx` by default
- legacy `main.tex` and `references.bib` only with `--format latex`
- target directory summary

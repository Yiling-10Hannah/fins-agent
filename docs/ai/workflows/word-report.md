# Word Report Workflow

## Use When

Use when a student wants to create, inspect, format, or troubleshoot a Word
report (`.docx`) for coursework.

Deterministic helpers:

```bash
python tools/workflow.py setup-paper --title "..." [--authors "..."] [--topic "..."] [--target PATH]
python tools/workflow.py word-report [path/to/report.docx]
python tools/workflow.py outline [path/to/report.docx]
python tools/workflow.py proofread [path/to/report.docx]
```

## Inputs

- optional `.docx` path
- optional title, authors, or topic for a new report scaffold
- optional section or revision goal

## Required Context

- `AGENTS.md`
- `docs/ai/rules/academic-writing.md`
- `docs/ai/rules/word-reporting.md`
- `guidance/paper-context.md` if present
- target `.docx` file if editing or checking an existing report

## Procedure

1. Prefer Word `.docx` as the report source for student writing.
2. Use `setup-paper` without `--format latex` to create `report/report.docx`.
3. Preserve Word built-in styles, especially Title, Heading 1, Heading 2,
   Heading 3, Normal, Caption, and bibliography-related fields.
4. Use Heading styles for structure so Navigation Pane, automatic table of
   contents, and outline checks work.
5. Use Word captions and cross-references for figures and tables. Use
   `fintools.figures` for Word/A4-ready exports before inserting images.
6. Use Word References for sources and bibliographies by default. Verify
   citation facts before adding or changing sources.
7. Before final hand-in, instruct the student to update fields, run
   Accessibility Checker, accept or reject tracked changes, remove comments,
   and export PDF from Word.

## Output

- Word report scaffold or check report
- concise notes on structure, placeholders, and next edits

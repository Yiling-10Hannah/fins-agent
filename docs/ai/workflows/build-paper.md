# Build Paper Workflow

## Use When

Use when a student explicitly wants to compile a legacy LaTeX paper to PDF.
For Word reports, use Word's PDF export instead.

Deterministic helper:

```bash
python tools/workflow.py build-paper [path/to/main.tex] [--quick]
```

## Inputs

- optional target `.tex` path
- optional `--quick`

## Required Context

- `AGENTS.md`
- target `.tex` file
- `pdflatex` and `bibtex` if installed

## Procedure

1. Resolve the target `.tex` file, defaulting to `main.tex`.
2. Change to the directory containing that file before compiling.
3. Default build cycle:
   - `pdflatex`
   - `bibtex`
   - `pdflatex`
   - `pdflatex`
4. If `--quick` is requested, run a single `pdflatex` pass.
5. Parse errors and warnings and report them clearly.
6. Point the user to `latex-doctor` when compilation fails.

## Output

- success or failure
- warning/error counts
- output PDF location

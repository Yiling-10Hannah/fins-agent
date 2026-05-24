# Proofread Workflow

## Use When

Use when a student wants a mechanical scan of Word/.docx report prose.
Legacy LaTeX is supported only when an explicit `.tex` target is supplied.

Deterministic helper:

```bash
python tools/workflow.py proofread [path/to/report.docx] [--section heading-slug] [--lines START-END]
```

## Inputs

- optional section key
- optional file path
- optional line range

## Required Context

- `AGENTS.md`
- target Word `.docx` report, or explicit legacy `.tex` source

## Procedure

1. Resolve the target text:
   - Word section by Heading 1 title or slug
   - legacy LaTeX section by `%% BEGIN/END` markers only for explicit `.tex`
     targets
   - explicit file path
   - otherwise prefer `report/report.docx` or `report.docx`
2. Scan for:
   - typos and doubled words
   - legacy LaTeX reference formatting issues when the target is `.tex`
   - spacing problems
   - equation punctuation issues
   - capitalization inconsistencies
3. Record concrete findings with line numbers.
4. Keep the report mechanical and specific; do not rewrite argumentation.

## Output

- line-numbered proofread report
- totals by category

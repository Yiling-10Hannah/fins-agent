# Build Context Workflow

## Use When

Use when a student wants a structured `guidance/paper-context.md` file built
from report sources.

Deterministic helper:

```bash
python tools/workflow.py build-context <source1> [source2 ...]
```

## Inputs

- one or more Word `.docx` files by default; explicit legacy `.tex`,
  Markdown, and PDF sources are also supported

## Required Context

- `AGENTS.md`
- source files supplied by the user

## Procedure

1. Read each supplied source file.
2. Extract:
   - paper identity
   - abstract
   - key results
   - terminology
   - sample description
   - citation context
3. If a `.docx` source is present, extract Word heading structure. If an
   explicit legacy `.tex` source is present, also extract:
   - `%% BEGIN/END` section keys
   - key `\label{}` values
   - section summaries
4. Write the result to `guidance/paper-context.md`.
5. If no path is supplied, scan the current project for likely report files
   and ask the user which one to use.

## Output

- `guidance/paper-context.md`
- source list and any missing-information notes

# Edit Section Workflow

## Use When

Use when a student wants an existing report section revised for style,
clarity, precision, or structure.

Recommended validation helpers:

```bash
python tools/workflow.py outline [path/to/report.docx]
python tools/workflow.py proofread [path/to/report.docx] [--section heading-slug]
```

## Inputs

- target section, file path, or section key
- optional revision goal

## Required Context

- `AGENTS.md`
- `docs/ai/rules/academic-writing.md`
- `docs/ai/rules/banned-words.md`
- `docs/ai/rules/word-reporting.md`
- `guidance/paper-context.md` if present
- current `.docx` report or legacy `.tex` source

## Procedure

1. Read the current text and note its structure and key claims.
2. Diagnose banned words, passive voice, vague claims, terminology drift,
   hedging, nominalizations, and structural AI tells.
3. Use `guidance/paper-context.md` when available to preserve the report's
   claims, numbers, and terminology.
4. Make targeted edits that preserve Word structure and minimize disruption.
   Use `tools/workflow.py outline` before editing if the section structure is
   unclear.
5. Preserve content that is already correct and strong.
6. Re-check citations before introducing or changing source references.
7. Present both the change categories and the revised report text.

## Output

- categorized edit summary
- revised report text
- human-review flags for unverifiable claims

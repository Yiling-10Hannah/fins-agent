# Outline Workflow

## Use When

Use when a student wants a structural review of a report.

Deterministic helper:

```bash
python tools/workflow.py outline [path/to/report.docx]
```

## Inputs

- optional mode such as balance-only or Cochrane-only

## Required Context

- `AGENTS.md`
- report Word `.docx` source, or explicit legacy `.tex` source
- `guidance/paper-context.md` if present

## Procedure

1. Extract Word Heading 1, Heading 2, and Heading 3 structure from `.docx`
   reports. For explicit legacy `.tex`, extract section commands.
2. Estimate body-section lengths using `%% BEGIN/END` markers when available
   for legacy `.tex`.
3. Verify Word heading presence or explicit legacy section markers.
4. Evaluate:
   - section presence
   - section balance
   - Cochrane-style organization
   - project-specific structure checks from `guidance/paper-context.md`
5. Report missing sections, badly imbalanced sections, and marker problems.

## Output

- structured outline report
- body/appendix length estimates
- marker integrity summary for legacy `.tex`; Word reports do not use markers

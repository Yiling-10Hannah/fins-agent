# LaTeX Doctor Workflow

## Use When

Use when a student explicitly wants a legacy `.tex` file cleaned up, compiled,
and checked for marker or reference problems. Do not use this for Word reports.

Deterministic helper:

```bash
python tools/workflow.py latex-doctor [path/to/main.tex] [--mode all|comments|markers|compile]
```

## Inputs

- optional mode: `comments`, `markers`, `compile`
- optional target `.tex` file

## Required Context

- `AGENTS.md`
- target `.tex` source
- `pdflatex` and `bibtex` if installed
- project `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, or `QWEN.md` if section
  keys or project terminology are registered there

## Procedure

1. Run the standard compile cycle and categorize the current errors and
   warnings.
2. Remove unnecessary LaTeX comments while preserving:
   - `%% BEGIN/END` markers
   - `% !TeX` directives
   - comments inside verbatim-style content
3. Verify section markers and registered section keys.
4. Fix safe, deterministic issues:
   - missing standard packages when usage is obvious
   - minor warning reductions
5. Do not silently auto-fix ambiguous labels or citations.
6. Recompile and report what changed.

## Output

- doctor report with comment cleanup, marker status, compile status, and
  remaining issues

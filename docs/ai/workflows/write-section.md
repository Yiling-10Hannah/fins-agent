# Write Section Workflow

## Use When

Use when a student wants a new report section or subsection drafted for a
Word-first coursework report. Legacy LaTeX reports remain supported when the
target is `.tex`.

Recommended validation helpers:

```bash
python tools/workflow.py outline [path/to/report.docx]
python tools/workflow.py proofread [path/to/report.docx]
```

## Inputs

- section name or description
- optional structural constraints or content notes

## Required Context

- `AGENTS.md`
- project `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, or `QWEN.md` if present
- `docs/ai/rules/academic-writing.md`
- `docs/ai/rules/word-reporting.md`
- `docs/ai/rules/citation-verification.md`
- `docs/ai/rules/legacy-latex.md` when working in explicit legacy LaTeX
- `.claude/exemplars/cochrane_writing_tips.md`
- current `.docx` report or legacy `.tex` source

## Procedure

1. Read the current report structure and identify what is missing.
2. Load project-specific terminology from any project instruction file or
   related project docs.
3. Follow the academic-writing rules:
   - concrete first sentence
   - active voice
   - specific numbers for quantitative claims
   - no banned words, throat-clearing, or self-praise
4. For Word reports, draft text that can be pasted under the matching Heading
   style. Preserve Word caption, cross-reference, and bibliography workflows.
5. Verify all citation claims before using them. In Word, add verified sources
   through the References tab; in legacy LaTeX, check citation keys against
   the `.bib` file.
6. Flag any uncertain claim with `[HUMAN EDIT REQUIRED: ...]`.
7. If requested, run `outline` and `proofread` after drafting. For legacy
   LaTeX only, `build-paper --quick` can be used as a syntax pass.

## Output

- report text ready to insert
- brief note on structural choices or human-review flags

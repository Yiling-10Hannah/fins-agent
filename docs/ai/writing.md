# Writing and Word Report Workflow

Writing guidance shared across Claude, Codex, Gemini CLI, and Qwen Code.

## Shared Rules

- Treat academic writing as a separate workflow from data or code changes.
- Use Word `.docx` under `report/` as the default report source.
- Shared workflow logic lives in `docs/ai/workflows/`.
- Deterministic helpers live in `tools/workflow.py`.
- Claude wrappers, Codex skills, Gemini commands, and Qwen skills should all
  route through the shared workflow docs before applying tool-specific
  behavior.

## Workflow Reference

| Workflow | Shared source | Primary rules |
|----------|---------------|---------------|
| Word report | `docs/ai/workflows/word-report.md` | `docs/ai/rules/word-reporting.md`, `docs/ai/rules/academic-writing.md` |
| Write section | `docs/ai/workflows/write-section.md` | `docs/ai/rules/academic-writing.md`, `docs/ai/rules/word-reporting.md` |
| Edit section | `docs/ai/workflows/edit-section.md` | `docs/ai/rules/academic-writing.md`, `docs/ai/rules/banned-words.md` |
| Proofread | `docs/ai/workflows/proofread.md` | Word `.docx` by default; explicit legacy `.tex` only |
| Build paper | `docs/ai/workflows/build-paper.md` | legacy `pdflatex`, `bibtex` |
| Build deck | `docs/ai/workflows/build-deck.md` | PowerPoint-first, `docs/ai/rules/presentation.md` |
| Build figure | `docs/ai/workflows/build-figure.md` | `fintools.figures`, `FigureContext`, Word/A4 exports |
| Build context | `docs/ai/workflows/build-context.md` | Word `.docx` by default; explicit legacy `.tex`, `.md`, or `.pdf` supported |
| Outline | `docs/ai/workflows/outline.md` | Word `.docx` by default; explicit legacy `.tex`, `guidance/paper-context.md` |
| LaTeX doctor | `docs/ai/workflows/latex-doctor.md` | legacy report `.tex`, compile logs |
| Setup paper | `docs/ai/workflows/setup-paper.md` | Word report scaffold by default |

## Validation Helpers

Use these deterministic helpers to support AI-authored writing changes:

- `python tools/workflow.py setup-paper --title "..." --target .`
- `python tools/workflow.py outline [path/to/report.docx]`
- `python tools/workflow.py proofread [path/to/report.docx] --section <heading-slug>`
- `python tools/workflow.py build-context [path/to/report.docx]`

## Deep References

When needed, read these shared files instead of duplicating them:

- `docs/ai/rules/word-reporting.md` - Word structure, citations, captions, and final checks
- `docs/ai/rules/academic-writing.md` - banned words and style rules
- `docs/ai/rules/legacy-latex.md` - explicit opt-in legacy LaTeX conventions
- `docs/ai/rules/citation-verification.md` - citation verification protocol, including legacy BibTeX
- `docs/ai/rules/banned-words.md` - quick-reference banned word list
- `docs/ai/rules/grammar-punctuation.md` - grammar and punctuation
- `docs/ai/rules/presentation.md` - slide design principles
- `.claude/exemplars/cochrane_writing_tips.md` - Cochrane writing guide

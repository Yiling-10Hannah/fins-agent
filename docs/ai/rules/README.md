# Tool-Neutral Writing Rules

These rules are the shared writing source of truth for Claude, Codex, Gemini,
and Qwen workflows.

Use Word `.docx` reports by default. Legacy LaTeX rules apply only when a
student explicitly works on `.tex`, BibTeX, or Beamer files.

## Rule Files

- `academic-writing.md` - report prose, argument structure, and style.
- `banned-words.md` - words and phrases to avoid in coursework writing.
- `grammar-punctuation.md` - Chicago-style grammar and punctuation baseline.
- `word-reporting.md` - Word document structure, captions, citations, fields,
  and final checks.
- `citation-verification.md` - source verification rules for Word citations
  and legacy BibTeX.
- `legacy-latex.md` - explicit opt-in LaTeX and Beamer conventions.
- `presentation.md` - slide design and presentation rules.

Assistant-specific adapters may link to these files, but should not override
them. If an adapter conflicts with these rules, these rules win.

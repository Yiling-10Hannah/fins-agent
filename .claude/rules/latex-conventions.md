# Legacy LaTeX Rules

LaTeX is explicit opt-in. Students do not need LaTeX for onboarding or normal
coursework reports.

Use these rules only when the user asks for legacy `.tex`, BibTeX, Beamer, or
PDF compilation work.

## Report Files

- Legacy report source lives in `latex/` only when requested.
- Use `setup-paper --format latex` to create a legacy LaTeX scaffold.
- Use `build-paper` to compile report `.tex` files.
- Use `latex-doctor` to diagnose legacy compile, marker, and citation issues.

## Source Conventions

- Keep section structure clear and stable.
- Use labels for sections, figures, tables, and equations that are referenced.
- Keep generated figures and tables under `results/`.
- Do not use LaTeX source comments as report prose.

## Citations

- Follow `citation-verification.md` before adding `\cite{}` commands or
  BibTeX entries.
- Do not add unverified BibTeX metadata.

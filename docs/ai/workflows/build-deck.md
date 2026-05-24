# Build Deck Workflow

## Use When

Use when a student wants to create, revise, or structure a PowerPoint-first
coursework presentation. Legacy LaTeX/Beamer slides are supported only when
the student explicitly asks for `.tex`, Beamer, or `pdflatex`.

Legacy deterministic helper, only for explicit Beamer targets:

```bash
python tools/workflow.py build-deck [path/to/deck.tex]
```

## Inputs

- optional target deck path
- optional `--working`

## Required Context

- `AGENTS.md`
- `docs/ai/rules/presentation.md`
- report context, results, figures, or assignment instructions
- `boilerplate/template_slides.tex` only for explicit legacy Beamer work

## Procedure

1. Before creating or heavily revising a deck, establish:
   - audience
   - visual tone
   - presentation length or slide budget
2. Read the presentation rules before drafting slides.
3. Default to a PowerPoint deck structure under a project `decks/` directory.
   Use `.pptx` as the expected deliverable unless the user says otherwise.
4. Draft assertion-style slide titles, concise body points, and speaker-note
   prompts. Slides should support the spoken argument rather than reproduce
   the report.
5. Use Word/A4-ready figures from `fintools.figures` where possible, then
   adapt labels and emphasis for slide readability.
6. Preserve PowerPoint accessibility expectations: readable contrast,
   descriptive titles, alt text for important figures, and no tiny tables.
7. If and only if the student explicitly requests legacy Beamer, use
   `boilerplate/template_slides.tex` as the starting point and compile with
   `pdflatex`.

## Output

- PowerPoint-first deck outline, slide text, or revised `.pptx` guidance
- legacy Beamer `.tex` file and compile result only when explicitly requested
- audience/tone assumptions used

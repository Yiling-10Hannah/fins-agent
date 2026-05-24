---
name: build-figure
description: "Create, improve, validate, or export publication-quality coursework figures, including Word/A4-ready plots."
argument-hint: "[--output results/figures] [--docx] [--style fins|ft] [--ft-background] [--suite CSV] [--narrative]"
---

# Build Figure Skill

Read `docs/ai/workflows/build-figure.md` and follow it as the canonical
workflow.

Typical triggers:

- "make a figure"
- "plot this time series"
- "export this for Word"
- "make FT-style figures for my dataframe"
- "make a publication-quality figure suite"

Preferred deterministic commands:

- `python tools/workflow.py build-figure --output results/figures`
- `python tools/workflow.py build-figure-suite data/my_data.csv --style ft --narrative --output results/figures`
- Use `build-figure-suite` without `--narrative` only when the user wants generic chart coverage rather than a story-first suite.

If this wrapper conflicts with the shared workflow doc, the shared workflow
doc wins.

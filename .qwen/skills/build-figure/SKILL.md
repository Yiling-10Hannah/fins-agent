---
name: build-figure
description: Use when a student asks to create, improve, validate, or export charts, figures, plots, time-series graphs, bar charts, scatter plots, heatmaps, or Word/A4-ready report figures.
argument-hint: "[--output results/figures] [--docx] [--style fins|ft] [--ft-background] [--suite CSV] [--narrative]"
---

# Build Figure Skill

Read `docs/ai/workflows/build-figure.md` and follow it as the canonical
workflow.

Typical triggers:

- "make a figure"
- "plot this time series"
- "export this for Word"
- "make the chart publication-quality"
- "make FT-style figures for my dataframe"
- "make a publication-quality figure suite"

Preferred deterministic command:

- `python tools/workflow.py build-figure --output results/figures`
- `python tools/workflow.py build-figure-suite data/my_data.csv --style ft --narrative --output results/figures`
- Use `build-figure-suite` without `--narrative` only when the user wants generic chart coverage rather than a story-first suite.

If the workflow doc conflicts with older tool-specific instructions, the
shared workflow doc wins.

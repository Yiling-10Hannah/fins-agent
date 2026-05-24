# Week 1: Structured Data Foundations

Week 1 introduces the core structured-data workflow used throughout the course:
load a table correctly, run Stage 1 checks, save typed data, query with
DuckDB, slice between panel and time-series views, and plot growth of $1.

This week uses two datasets:

1. The Tech 4 workshop panel: Apple, Microsoft, NVIDIA, and Oracle.
2. The Coke vs Pepsi practice panel: KO and PEP on the same 2000-2025 span.

Generated outputs belong under:

```text
fins2026/week1/results/
```

## What You Learn

- Why `dayfirst=True` matters when a CSV stores dates as `DD/MM/YYYY`
- Why a duplicate `(Date, Ticker)` pair breaks a `pivot`
- When Parquet is better than CSV for analytical reuse
- How DuckDB SQL and pandas `groupby` express the same summary
- How to move between panel, cross-section, time-series, and wide-return views
- Why log plots should use growth of $1, not `(1 + r).cumprod() - 1`

## Core Week 1 Files

- `WORKSHOP.md`: the in-class run sheet
- `DATA_GUIDE.md`: dataset definitions, schema, units, and traps
- `ASSIGNMENT.md`: the Practice 1 brief
- `PRACTICE_GUIDE.md`: transfer notes and expected results for KO vs PEP
- `guidance/*.md`: generated context summaries for students and AI tools

## Run Order

From the repo root:

```bash
python fins2026/week1/scripts/describe_data.py
python fins2026/week1/scripts/01_load_panel.py
python fins2026/week1/scripts/02_save_formats.py
python fins2026/week1/scripts/03_duckdb_query.py
python fins2026/week1/scripts/04_panel_slices.py
python fins2026/week1/scripts/05_end_to_end.py
python fins2026/week1/scripts/06_coke_pepsi_practice.py
python tools/workflow.py build-week-context --target fins2026/week1
```

## Week 1 Output Policy

- `data/` holds committed source inputs only.
- `results/data/` holds derived datasets such as cleaned or converted copies.
- `results/figures/` holds exported figures such as growth-of-$1 charts.
- `scripts/` holds canonical rerunnable code, not ad hoc experiments.

## Key Week 1 Numbers

- Raw Tech 4 CSV: 26,159 rows x 6 columns
- Duplicate Tech 4 `(Date, Ticker)` rows in raw CSV: 3
- Clean Tech 4 panel after dedup: 26,156 rows, 6,539 rows per ticker
- KO/PEP practice TSV: 13,078 rows x 10 columns before adding `Date`
- KO/PEP Stage 1 checks: 0 duplicates, 0 nulls, 6,539 rows per ticker

## Structure

- `data/` - committed Week 1 inputs
- `scripts/` - the official teaching ladder and practice runner
- `results/` - derived datasets, figures, tables, and local app outputs
- `guidance/` - generated summaries for student and AI context
- `prompts/` - reusable Week 1 assistant prompts
- `tests/` - local smoke coverage for the Week 1 surface


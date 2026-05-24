# Week Context

## Week Identity
- Week folder: `fins2026/week1`
- Title: Week 1: Structured Data Foundations
- README summary: Week 1 introduces the core structured-data workflow used throughout the course: load a table correctly, run Stage 1 checks, save typed data, query with DuckDB, slice between panel and time-series views, and plot growth of $1.

## Core Guides

- `fins2026/week1/README.md`: Week 1: Structured Data Foundations. Week 1 introduces the core structured-data workflow used throughout the course: load a table correctly, run Stage 1 checks, save typed data, query with DuckDB, slice between panel and time-series views, and plot growth of $1.
- `fins2026/week1/WORKSHOP.md`: Week 1 Workshop. Week 1 has one in-class ladder and one transfer practice.
- `fins2026/week1/DATA_GUIDE.md`: Week 1 Data Guide. Week 1 uses one workshop panel and one transfer-practice panel. Both are daily equity datasets, but they teach different lessons.
- `fins2026/week1/SUBMISSION_CHECKLIST.md`: Week 1 Submission Checklist. `README.md` explains the week purpose and canonical commands; `WORKSHOP.md` reflects the actual workshop flow; `DATA_GUIDE.md`, `data/README.md`, and `PRACTICE_GUIDE.md` describe the Week 1 datasets accurately

## Additional Week Docs

- `fins2026/week1/ASSIGNMENT.md`: Week 1 Practice: Coke vs Pepsi, 2000-2025. Practice for Quiz 1. Not graded, but it is the cleanest check that the Week 1 workflow has transferred from the Tech 4 workshop to a fresh dataset.
- `fins2026/week1/PRACTICE_GUIDE.md`: Week 1 Practice Guide. This guide explains how the Tech 4 workshop workflow transfers to Practice 1.

## Prompt Files

- `fins2026/week1/prompts/assistant_starter.md`: Week 1 Assistant Starter Prompt. Load Week 1 context in this order before answering:
- `fins2026/week1/prompts/practice1_coach.md`: Week 1 Practice 1 Coach Prompt. Use this prompt when the student needs focused help on the KO vs PEP transfer practice.
- `fins2026/week1/prompts/README.md`: Week 1 Prompts. This folder holds reusable Week 1 assistant prompts.
- `fins2026/week1/prompts/workshop_walkthrough.md`: Week 1 Workshop Walkthrough Prompt. Use this prompt when the student needs focused help on the Tech 4 workshop ladder.

## Current Scripts

- `fins2026/week1/scripts/01_load_panel.py`: Load the raw Week 1 Tech 4 CSV and verify the date parse.
- `fins2026/week1/scripts/02_save_formats.py`: Clean the Tech 4 workshop CSV and save typed copies under results/data.
- `fins2026/week1/scripts/03_duckdb_query.py`: Query the clean Tech 4 panel with DuckDB and pandas.
- `fins2026/week1/scripts/04_panel_slices.py`: Slice the clean Tech 4 panel into multiple Week 1 data shapes.
- `fins2026/week1/scripts/05_end_to_end.py`: Run the full Week 1 Tech 4 pipeline in one file.
- `fins2026/week1/scripts/06_coke_pepsi_practice.py`: Run the Week 1 KO vs PEP practice workflow end to end.
- `fins2026/week1/scripts/describe_data.py`: Describe the Week 1 workshop and practice datasets.
- `fins2026/week1/scripts/run_week.py`: Print the Week 1 run order and confirm output directories.

## Standard Working Rules

- `data/` is for committed source inputs.
- `results/data/` is for generated, downloaded, cleaned, or merged datasets.
- `scratch/` is for disposable experiments, not the final path.
- Promote reused week-local logic into `code/` and cross-week logic into `fintools/`.

## Current Paths

- Source data: `fins2026/week1/data`
- Generated outputs: `fins2026/week1/results`
- Current context files: `fins2026/week1/guidance`

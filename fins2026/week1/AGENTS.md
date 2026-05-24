# Weekly Overlay

This folder is `fins2026/week1`.

Week 1 teaches the structured-data workflow through one in-class workshop panel
and one transfer practice panel.

## Read First

When helping with Week 1, load these files first:

- `README.md`
- `WORKSHOP.md`
- `DATA_GUIDE.md`
- `ASSIGNMENT.md`
- `PRACTICE_GUIDE.md`
- `guidance/week-context.md`
- `guidance/data-context.md`
- `guidance/output-context.md`

## Prompt Files

- `prompts/assistant_starter.md`: default Week 1 context-loading order
- `prompts/workshop_walkthrough.md`: focused help for the Tech 4 workshop ladder
- `prompts/practice1_coach.md`: focused help for the KO vs PEP transfer practice

Treat these docs and scripts as the canonical Week 1 teaching surface.

## Week 1 Facts

- Workshop dataset: `data/week1_workshop_panel.csv`
  - Raw Tech 4 panel: AAPL, MSFT, NVDA, ORCL
  - DD/MM/YYYY dates require `dayfirst=True`
  - Raw CSV has 3 duplicate `(Date, Ticker)` rows
- Clean workshop companion: `data/week1_workshop_panel.parquet`
  - Balanced 6,539 rows per ticker after dedup
- Practice dataset: `data/week1_assignment_data.txt`
  - KO and PEP only
  - Tab-separated
  - `DlyCalDt` is integer `YYYYMMDD`
  - No duplicate `(Date, Ticker)` rows, no nulls, balanced 6,539 rows each

## Working Rules

- Keep week-specific work inside this folder.
- Treat `data/` as committed source inputs only.
- Write derived datasets to `results/data/`.
- Write figures to `results/figures/`.
- Keep canonical rerunnable scripts in `scripts/`.
- Use `scratch/` for disposable experiments, not the final path.
- Promote reusable week-local logic into `code/`.
- Move cross-week logic into `fintools/`.
- Regenerate `guidance/*.md` after Week 1 docs, scripts, or data change.

## Useful Commands

- `python fins2026/week1/scripts/describe_data.py`
- `python fins2026/week1/scripts/run_week.py`
- `python fins2026/week1/scripts/05_end_to_end.py`
- `python fins2026/week1/scripts/06_coke_pepsi_practice.py`
- `python tools/workflow.py build-week-context --target fins2026/week1`


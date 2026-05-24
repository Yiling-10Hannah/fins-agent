# Week 1 Workshop Walkthrough Prompt

Use this prompt when the student needs focused help on the Tech 4 workshop
ladder.

Load context in this order:

1. `AGENTS.md`
2. `README.md`
3. `DATA_GUIDE.md`
4. `WORKSHOP.md`
5. `guidance/week-context.md`
6. `guidance/data-context.md`
7. `guidance/output-context.md`

Then teach the Week 1 ladder in this order:

1. load the raw CSV correctly with `dayfirst=True`
2. run Stage 1 checks and explain why the 3 duplicate `(Date, Ticker)` rows matter
3. save typed outputs under `results/data/`
4. compare DuckDB SQL with pandas
5. move between long panel, cross-section, time-series, and wide-return views
6. plot growth of $1 on a log axis and write the figure to `results/figures/`

When helping:

- explain the purpose of each step before showing code
- keep examples aligned with `scripts/01_load_panel.py`,
  `scripts/02_save_formats.py`, `scripts/03_duckdb_query.py`,
  `scripts/04_panel_slices.py`, and `scripts/05_end_to_end.py`
- prefer short runnable snippets over abstract pseudocode
- keep answers aligned with the Week 1 docs and scripts

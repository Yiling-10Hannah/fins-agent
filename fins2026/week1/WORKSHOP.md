# Week 1 Workshop

Week 1 has one in-class ladder and one transfer practice.

## Part 1: Tech 4 Workshop Ladder

1. Read `README.md` and `DATA_GUIDE.md`.
2. Run `scripts/describe_data.py`.
   Checkpoint: confirm the week contains one Tech 4 workshop dataset and one
   KO/PEP practice dataset.
3. Run `scripts/01_load_panel.py`.
   Checkpoint: the raw Tech 4 CSV is 26,159 rows x 6 columns, and the date
   column only parses correctly with `dayfirst=True`.
4. Run `scripts/02_save_formats.py`.
   Checkpoint: the raw CSV has 3 duplicate `(Date, Ticker)` rows; the clean
   panel has 26,156 rows and 6,539 rows per ticker.
5. Run `scripts/03_duckdb_query.py`.
   Checkpoint: DuckDB SQL and pandas `groupby` agree up to floating-point
   noise.
6. Run `scripts/04_panel_slices.py`.
   Checkpoint: the same long-form panel can be viewed as a time-series, a
   cross-section, or a wide return matrix.
7. Run `scripts/05_end_to_end.py`.
   Checkpoint: the script writes `results/figures/tech4_growth.pdf`.

## Part 2: Transfer To Practice 1

1. Read `ASSIGNMENT.md` and `PRACTICE_GUIDE.md`.
2. Run `scripts/06_coke_pepsi_practice.py` or reproduce the same workflow in a
   notebook.
3. Confirm the Stage 1 checks transfer cleanly to a fresh dataset:
   - duplicates: 0
   - nulls: 0
   - balanced row counts: 6,539 per ticker
4. Confirm the 2020-03-16 KO/PEP cross-section has 2 rows, not 4.
5. Confirm the final growth-of-$1 result shows `PEP` ahead of `KO`.

## Discussion Prompts

- Why is `dayfirst=True` a data-quality issue rather than a style preference?
- Why does a single duplicate `(Date, Ticker)` pair break `pivot`?
- Why is Parquet a better analytical default than CSV?
- Why should a log plot use growth of $1 instead of cumulative return minus 1?
- Why is KO vs PEP a better Week 1 comparison than KO vs AAPL?


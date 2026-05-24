# Week 1 Data Guide

Week 1 uses one workshop panel and one transfer-practice panel. Both are
daily equity datasets, but they teach different lessons.

## Dataset 1: Tech 4 Workshop Panel

Files:

- `data/week1_workshop_panel.csv`
- `data/week1_workshop_panel.parquet`

Purpose:

- This is the in-class teaching panel for the full Week 1 ladder.
- It is the dataset used to demonstrate loading, Stage 1 checks, Parquet,
  DuckDB, panel slicing, and growth-of-$1 plotting.

Coverage:

- Tickers: `AAPL`, `MSFT`, `NVDA`, `ORCL`
- Span: `2000-01-03` to `2025-12-31`

Schema:

- `Date`
- `CompanyName`
- `Ticker`
- `Price`
- `TotalReturn`
- `PriceReturn`

Important Week 1 lessons:

- The raw CSV stores dates in `DD/MM/YYYY` form. Use
  `pd.read_csv(..., parse_dates=["Date"], dayfirst=True)`.
- The raw CSV contains 3 duplicate `(Date, Ticker)` rows.
- Those duplicates must be removed before any `pivot` to wide form.
- The committed Parquet companion is the clean typed version of the workshop
  panel and is safe to use in later steps.

Expected checks:

- Raw CSV shape: `26,159 x 6`
- Clean panel shape after dedup: `26,156 x 6`
- Clean panel counts: `6,539` rows per ticker

## Dataset 2: Practice 1 KO/PEP Panel

File:

- `data/week1_assignment_data.txt`

Purpose:

- This is the Week 1 transfer-practice dataset.
- It asks students to re-run the same workflow on a fresh CRSP panel with a
  different schema.

Coverage:

- Tickers: `KO`, `PEP`
- Span: `2000-01-03` to `2025-12-31`

Schema:

- `PERMNO`
- `HdrCUSIP`
- `SecurityNm`
- `Ticker`
- `PERMCO`
- `DlyCalDt`
- `DlyPrc`
- `DlyCap`
- `DlyRet`
- `DlyPrcVol`

Important Week 1 lessons:

- The file is tab-separated. Use `sep="\t"`.
- `DlyCalDt` is an integer `YYYYMMDD`, so `parse_dates` is not enough.
  Convert it explicitly with `pd.to_datetime(..., format="%Y%m%d")`.
- `DlyCap` is in thousands of USD.
- DuckDB `STDDEV_POP` matches pandas `std(ddof=0)`, not the pandas default.
- This panel ships clean: no duplicate `(Date, Ticker)` rows, no nulls, and
  balanced counts.

Expected checks:

- Raw TSV shape: `13,078 x 10`
- After adding `Date`: `13,078 x 11`
- Duplicate `(Date, Ticker)` rows: `0`
- Nulls: `0`
- Counts: `6,539` rows each for `KO` and `PEP`

## Derived Outputs

- Save derived Week 1 datasets to `results/data/`.
- Save exported charts to `results/figures/`.
- Do not commit practice outputs back into `data/`.


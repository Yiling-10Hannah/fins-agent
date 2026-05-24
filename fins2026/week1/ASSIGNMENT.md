# Week 1 Practice: Coke vs Pepsi, 2000-2025

> Practice for Quiz 1. Not graded, but it is the cleanest check that the Week 1
> workflow has transferred from the Tech 4 workshop to a fresh dataset.

This problem uses a CRSP daily panel for The Coca-Cola Company (`KO`) and
PepsiCo (`PEP`) over `2000-01-03` to `2025-12-31`.

The point is not just to answer the five tasks. The point is to show that you
can run the full Week 1 workflow again on a new schema:

- load correctly
- run Stage 1 checks
- save a typed copy
- compare DuckDB SQL with pandas
- slice the panel
- plot growth of $1

## Dataset

Source file:

```text
data/week1_assignment_data.txt
```

The file is tab-separated and has `13,078` rows x `10` columns.

| Column | Description |
| --- | --- |
| `PERMNO` | CRSP permanent security identifier |
| `HdrCUSIP` | Header CUSIP |
| `SecurityNm` | Full security name |
| `Ticker` | `KO` or `PEP` |
| `PERMCO` | CRSP permanent company identifier |
| `DlyCalDt` | Calendar date as integer `YYYYMMDD` |
| `DlyPrc` | Daily closing price in USD |
| `DlyCap` | Market capitalization in thousands of USD |
| `DlyRet` | Daily total return in decimal form |
| `DlyPrcVol` | Daily traded dollar volume in USD |

### Loading Rules

- Use `pd.read_csv(..., sep="\t")`.
- Convert `DlyCalDt` explicitly with
  `pd.to_datetime(df["DlyCalDt"], format="%Y%m%d")`.
- Do not expect `parse_dates` to handle an integer date column for you.
- Keep derived outputs under `results/`, not back inside `data/`.

## Tasks

### Task 1 - Load and inspect

Read the TSV into pandas and add a `Date` column from `DlyCalDt`.

Save the typed copy to:

```text
results/data/week1_assignment_data.parquet
```

Print:

- the shape
- the date range
- the unique tickers with their full `SecurityNm`
- the dtypes of every column

### Task 2 - Stage 1 sanity check

Run the same three checks used in the Tech 4 workshop:

1. duplicates: `panel.duplicated(["Date", "Ticker"]).sum()`
2. nulls: `panel.isna().sum()`
3. balance: `panel.groupby("Ticker").size()`

Then state clearly whether the panel needs cleaning or ships ready to use after
date conversion.

### Task 3 - Per-ticker summary, two ways

Build the same per-ticker summary in DuckDB and pandas.

Required columns:

| Column | Definition |
| --- | --- |
| `mean_price` | `AVG(DlyPrc)` |
| `sd_price` | `STDDEV_POP(DlyPrc)` |
| `mean_cap_million_usd` | `AVG(DlyCap) / 1000.0` |
| `n_days` | `COUNT(*)` |

Rules:

- sort by `mean_price` descending
- in pandas, use `lambda s: s.std(ddof=0)` so the standard deviation matches
  DuckDB's population standard deviation
- confirm that the two results agree up to floating-point noise

### Task 4 - Cross-section and time-series slices

1. Cross-section: filter to `2020-03-16`, the COVID-crash Monday.
   - print the resulting 2 rows
   - state which company held up better and by how many percentage points using
     `DlyRet`
2. Time-series: filter to `KO`, sort by `Date`, and print the first and last 2
   rows.
   - state the shape of the KO time-series

### Task 5 - KO vs PEP, growth of $1

Pivot the panel to wide form on `DlyRet`:

```python
wide = panel.pivot(index="Date", columns="Ticker", values="DlyRet").dropna()
```

Compute the value of $1 invested at the start of the sample:

```python
growth_of_one_dollar = (1 + wide).cumprod()
```

Do not plot `(1 + wide).cumprod() - 1` on a log axis. That quantity can go
negative during drawdowns, which makes a log plot misleading.

Print the final dollar value per ticker and save the plot to:

```text
results/figures/ko_vs_pep_growth.pdf
```

Then state:

- which company was the better long-run holding
- by what factor
- one finance-relevant reason KO vs PEP is a sensible comparison

## Suggested Starter

Use:

```text
scripts/06_coke_pepsi_practice.py
```

as the Week 1 canonical starter if you want a clean reference implementation of
the five-task flow.

## Self-Check

You are ready for Quiz 1 when you can:

- load the file correctly without guessing the separator or date parser
- explain what each Stage 1 check catches
- write the DuckDB and pandas summaries without mixing up the standard
  deviation convention
- move between cross-section, time-series, and wide-return views in one line
- plot growth of $1 on a log axis without the cumulative-return-minus-one trap

## Allowed Tools

Stay within the Week 1 toolkit:

- `pandas`
- `numpy`
- `matplotlib`
- `duckdb`
- `pyarrow`

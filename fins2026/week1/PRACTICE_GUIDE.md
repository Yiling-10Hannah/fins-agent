# Week 1 Practice Guide

This guide explains how the Tech 4 workshop workflow transfers to Practice 1.

## What Transfers Directly

The Coke vs Pepsi task is not a new workflow. It is the same Week 1 workflow on
a fresh dataset:

1. load the file correctly
2. run Stage 1 checks
3. save a typed copy
4. compare DuckDB SQL with pandas
5. slice the panel into cross-section and time-series views
6. pivot returns to wide form
7. plot growth of $1 on a log axis

If a student can do the Tech 4 ladder without notes, they should be able to do
Practice 1.

## What Changes Relative To Tech 4

- The file is tab-separated, not CSV.
- The date column is `DlyCalDt`, not `Date`.
- The date values are integers in `YYYYMMDD` form.
- The return column is `DlyRet`, not `TotalReturn`.
- The price column is `DlyPrc`, not `Price`.
- The market-cap column is `DlyCap`, and it is measured in thousands of USD.
- There are only 2 tickers, so the 2020-03-16 cross-section has 2 rows, not 4.

## Expected Stage 1 Results

These are the correct Week 1 practice checkpoints:

- raw file shape: `13,078 x 10`
- date range: `2000-01-03` to `2025-12-31`
- duplicate `(Date, Ticker)` rows: `0`
- null count: `0`
- per-ticker counts: `KO = 6,539`, `PEP = 6,539`

The correct interpretation is that this panel ships ready to use after date
conversion.

## Expected Task 4 Result

On `2020-03-16`, the KO/PEP cross-section has exactly 2 rows:

- `PEP` return: `-0.112672`
- `KO` return: `-0.066227`

`KO` held up better that day by about `4.64` percentage points.

## Expected Task 5 Result

For the full `2000-01-03` to `2025-12-31` sample:

- final KO growth of $1: about `4.93`
- final PEP growth of $1: about `7.90`
- long-run winner: `PEP`
- winner margin: about `1.60x`

## Common Mistakes

- Using `pd.read_csv(...)` without `sep="\t"`
- Trying to let `parse_dates` handle `DlyCalDt`
- Forgetting that `DlyCap` is in thousands of USD
- Comparing DuckDB `STDDEV_POP` with pandas `std()` without `ddof=0`
- Expecting a 4-row practice cross-section because the workshop panel had 4
  tickers
- Plotting `(1 + returns).cumprod() - 1` on a log axis
- Writing the derived Parquet file back into `data/` instead of `results/data/`

## Why KO vs PEP Is A Good Comparison

KO and PEP are a sensible Week 1 pair because they are both mature consumer
staples firms with broadly comparable products, long public histories, and
similar investor use cases. Comparing KO with AAPL would mix the Week 1 data
lesson with a much larger sector, growth, and business-model contrast.

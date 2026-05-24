# Week 1 Data

This folder holds the committed source inputs for Week 1.

## Files

### `week1_workshop_panel.csv`

- Raw Tech 4 workshop panel
- Tickers: `AAPL`, `MSFT`, `NVDA`, `ORCL`
- Span: `2000-01-03` to `2025-12-31`
- Shape: `26,159 x 6`
- Columns: `Date`, `CompanyName`, `Ticker`, `Price`, `TotalReturn`,
  `PriceReturn`
- Caveat: `Date` is stored in `DD/MM/YYYY` form, so pandas needs
  `dayfirst=True`
- Caveat: the raw file contains 3 duplicate `(Date, Ticker)` rows

### `week1_workshop_panel.parquet`

- Clean typed companion to the Tech 4 workshop CSV
- Shape: `26,156 x 6`
- Same columns as the CSV
- Balanced at `6,539` rows per ticker after dedup
- Used as the default clean input for DuckDB, slicing, and end-to-end scripts

### `week1_assignment_data.txt`

- Week 1 Practice 1 dataset for KO vs PEP
- Tickers: `KO`, `PEP`
- Span: `2000-01-03` to `2025-12-31`
- Shape: `13,078 x 10`
- Tab-separated, not comma-separated
- Key columns:
  - `DlyCalDt`: integer `YYYYMMDD`
  - `DlyPrc`: daily closing price in USD
  - `DlyCap`: market cap in thousands of USD
  - `DlyRet`: daily total return in decimal form
  - `DlyPrcVol`: traded dollar volume in USD
- Caveat: build the derived Parquet copy in `results/data/`, not here


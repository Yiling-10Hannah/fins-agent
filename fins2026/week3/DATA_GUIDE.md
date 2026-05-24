# Week 3 Data Guide

Week 3 keeps the public-data workflow introduced in Week 2, but now the
primary product is an Australia-first forecast lab rather than a U.S.
market-stress dashboard.

## Primary Australia Surface

Week 3 reuses the Week 2 Australia Stage 1 timing contract and treats the
observable panel as the forecasting source of truth.

- committed source: `fins2026/week3/data/australia_macro_stage1_long.csv`
- live rebuild path: the Week 3 loader reuses the Week 2 RBA parser when that
  module is available locally; standalone deploy bundles fall back to the
  committed Week 3 fixture if live rebuilds are unavailable
- monthly observable panel: used for cash rate, 10Y yield, unemployment, TWI,
  and commodity-price targets
- quarterly release surface: used for headline CPI inflation, Wage Price Index
  growth, and real GDP

Core Week 3 Australia forecast targets:

- monthly: cash rate target, 10Y government bond yield, unemployment rate,
  trade-weighted index, commodity price index (A$)
- quarterly: headline CPI inflation, Wage Price Index growth, real GDP

For the beginner forecasting lecture ladder, the main real-data teaching series
is the Australia unemployment rate. It is monthly, intuitive, and long enough
to show why we usually model the change in the series rather than the raw
level.

For the exogenous-variable step in the beginner ladder, use:

- first outside series: last month's cash-rate change
- second outside series: last month's commodity-price log change

These are kept simple on purpose so students can focus on the forecasting idea
rather than feature engineering.

For the regression and machine-learning step in the beginner ladder:

- OLS stays small and hand-picked: cash-rate change, commodity-price change,
  trade-weighted-index change, participation change, and vacancies-ratio
  change
- elastic net uses a wider bank: the OLS set plus employment-to-population
  change, Australia inflation indicators, and a small U.S. spillover block

For the horse-race and ensemble step in the beginner ladder:

- evaluate the target directly, not the reconstructed level path
- use target MAE, target RMSE, target MASE, and target out-of-sample
  R-squared versus the naive benchmark
- rank models by target RMSE

Context-only Australia series remain visible in the app, but are not forecast
targets in v1:

- participation rate
- employment-to-population ratio
- trimmed mean inflation
- vacancies to labour force ratio

## Secondary U.S. Surface

Week 3 keeps U.S. data as secondary context and exogenous input.

- fixture path: frozen validation datasets from `fintools.datasets`
- live path: no-key FRED graph CSV plus the Week 3 month-end panel helper
- U.S. data is not exposed as a Week 3 forecast target in v1

The main U.S. context columns are:

- Treasury yields and spreads
- federal funds rate
- VIX
- unemployment rate
- industrial production
- payroll employment
- S&P 500

For the U.S. mirror extension after the Australia core path:

- real teaching series: U.S. unemployment rate
- first outside series: last month's federal-funds change
- second outside series: last month's 10Y-2Y yield spread

That keeps the U.S. extension close to the main Week 3 lecture logic without
turning it into a second full product build.

## Forecasting Rules

- cash rate, 10Y yield, and unemployment are modeled as monthly changes
- TWI and commodity prices are modeled as monthly log changes
- headline CPI inflation and WPI growth are modeled on the published year-ended
  rate
- real GDP is modeled through annualized quarter-over-quarter growth and then
  mapped back into an implied GDP level path
- ARMA + exogenous and elastic-net models are one-step only in Week 3

## Generated Week 3 Inputs

`scripts/build_forecast_inputs.py` writes:

- `results/data/australia_monthly_forecast_panel.csv`
- `results/data/australia_quarterly_forecast_panel.csv`
- `results/data/us_monthly_context_panel.csv`
- `results/data/us_quarterly_context_panel.csv`
- `results/data/australia_stage1_observable_source.csv`

`scripts/run_forecast_benchmarks.py` writes:

- `results/forecasts/leaderboard.csv`
- per-series target forecast CSVs
- per-series displayed forecast CSVs
- per-series backtest CSVs

## Working Rules

- Keep committed source data in `data/`.
- Keep generated, merged, benchmarked, or downloaded datasets in `results/`.
- Treat live refresh time as different from each series' latest observable date.
- Use fixture mode first, then verify that live mode fails gracefully.

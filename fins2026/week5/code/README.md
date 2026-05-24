# Week 5 Week-Local Code

Use this folder for Week 5 reusable helpers. If the logic becomes useful
across multiple weeks, move it into `fintools/`.

Current Week 5 modules:

- `crypto_api_yahoo.py`: helpers for Yahoo crypto pulls, per-ticker cache and
  retry behavior, coverage summaries, and normalized long-panel outputs
- `risk_free_rate_french.py`: helpers for the Kenneth French daily risk-free
  download and final Parquet output
- `stage2_crypto_returns.py`: helpers for adjusted-price pivots, wide and long
  return construction, `rfr` merges, rolling six-month crypto features, and
  Stage 2 summary metrics
- `stage2_crypto_figures.py`: helpers for the FT-style Week 5 figure pack,
  including prices, cumulative returns, drawdowns, BTC-relative performance,
  upside/downside move panels, rolling-risk views,
  Sharpe/Sortino rankings, correlation matrices, and distribution diagnostics
- `stage3_oos_portfolios.py`: helpers for the Week 5 out-of-sample portfolio
  weight engine, including balanced-sample construction, crypto rebalance
  schedules, speed-oriented model estimation, daily holding-date weights,
  drifted daily out-of-sample portfolio returns, rebalance audit outputs, and
  the latest Stage 3 snapshot tables used by the factsheet figures
- `stage3_portfolio_figures.py`: helpers for the Week 5 FT-style Stage 3 OOS
  research pack for growth, drawdown, scorecard, target-holdings, and ex post
  frontier views, plus the long-only factsheet pack for holdings, concentration,
  trailing risk, turnover, and BTC/ETH exposure
- `stage4_app.py`: pure helpers for the Week 5 client-facing app, including
  live and fixture bundle loading, published-fund naming, cached scenario
  construction, display-window filtering, and illustrative allocation outputs


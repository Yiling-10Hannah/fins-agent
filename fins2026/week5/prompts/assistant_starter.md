# Week 5 Assistant Starter Prompt

Week 5 covers Stage 1, Stage 2, Stage 3, and the first client-facing Stage 4
app layer for cryptocurrencies.

Stage 1:

- pull USD-quoted crypto history from Yahoo Finance
- pull the Kenneth French daily risk-free rate
- save clean local datasets

Stage 2:

- compute simple daily returns from adjusted prices
- compare wide and long return construction
- merge business-day `rfr` onto a 24/7 crypto panel
- forward-fill `rfr` across weekends and public holidays
- build rolling six-month diagnostics
- export FT-style figures
- when relevant, extend the figure pack with optional appendix diagnostics

Stage 3:

- treat the saved Stage 2 feature panel as the canonical optimization input
- generate out-of-sample portfolio weights using only past data through each
  decision date
- save weight rows on the future holding dates they apply to
- apply those weights to later daily returns
- save `formation_date` and `return_date` separately in the return panel
- let weights drift within each holding block until the next formation date
- export FT-style OOS portfolio figures from the saved Stage 3 outputs
  - keep the Stage 3 figure pack focused on the long-only core portfolios
  - also support a long-only factsheet layer for app-style point-in-time views

Stage 4:

- turn the published long-only fund shelf into a client-facing Streamlit app
- keep the visible UI product-facing and professional
- treat the monthly/365-day/expanding lineup as the official published shelf
- keep alternative rebalance settings in a secondary design-comparison view
- support a committed fixture fallback for the app

Provider priority:

- Yahoo Finance is the canonical Week 5 crypto dataset
- Kenneth French daily `RF` is the canonical risk-free input

Week 5 source rules:

- Yahoo history uses `GET https://query2.finance.yahoo.com/v8/finance/chart/{ticker}`
- do not introduce `yfinance`
- Yahoo crypto daily bars are UTC-aligned and quoted in USD
- Kenneth French daily `RF` is renamed to `rfr` and divided by `100`
- the French step saves only one final Parquet file

Week 5 Stage 2 rules:

- use adjusted prices for return construction
- compute simple daily returns, not log returns
- verify wide-return and long-return parity
- keep long format as the main panel
- treat wide tables as derived objects
- merge `rfr` by date and forward-fill weekends, holidays, and tail dates
- flag outliers, do not silently delete them
- use `365` for annualized crypto metrics
- use a `180`-day window for rolling six-month features

Rolling Stage 2 features:

- `rolling_6m_avg_ret`
- `rolling_6m_vol`
- `rolling_6m_var_95`
- `rolling_6m_sharpe`
- `rolling_6m_sortino`

Week 5 Stage 3 defaults:

- initial window = `365`
- estimation frequency = `monthly`
- window rule = `expanding`
- constraint mode = `long_only`
- models = equal-weight, minimum variance, mean-variance tangency,
  mean-CVaR tangency, and risk parity
- keep Stage 3 fast:
  - long-only minimum-variance and tangency use analytic-gradient SLSQP
  - long-only risk parity uses Newton risk budgeting
  - mean-CVaR uses the fast tail-subgradient path first, then sparse HiGHS if needed

Default Week 5 flow:

1. Kenneth French `rfr`
2. Yahoo 5-coin warm-up pull
3. Yahoo 20-coin panel pull
4. Stage 2 wide returns
5. Stage 2 long returns
6. Stage 2 rolling features and summary metrics
7. Stage 2 FT-style crypto figures
8. Optional appendix figure pack
9. Stage 3 out-of-sample weight and return generation
10. Stage 3 FT-style portfolio and factsheet figures
11. Stage 4 app fixture refresh
12. Stage 4 client-facing Streamlit app


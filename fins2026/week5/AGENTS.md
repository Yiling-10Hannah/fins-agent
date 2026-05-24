# Weekly Overlay

This folder is `fins2026/week5`.

## Week Identity

- Week 5 covers Stage 1, Stage 2, Stage 3, and the client-facing Stage 4 app
  layer for crypto data.
- Stage 1: source connection and local dataset creation.
- Stage 2: return construction, business-day `rfr` merge logic, rolling
  diagnostics, and FT-style figures.
- Stage 3: out-of-sample portfolio-weight generation, daily portfolio returns,
  and FT-style OOS evaluation figures from the cleaned Stage 2 panel.
- Stage 4: the client-facing Streamlit app built on the published long-only
  crypto fund shelf.

Default mental model:

- Yahoo Finance is the canonical Week 5 crypto source
- Kenneth French supplies the business-day risk-free rate
- Stage 2 converts saved prices into usable crypto return panels
- Stage 3 turns those saved crypto returns into out-of-sample weight and return
  panels
- the key Week 5 lesson is the 24/7 crypto merge with business-day financial
  data
- the figure pack should tell a narrative about price paths, relative
  performance, co-movement, and tail risk
- the Stage 3 figure pack should tell a second narrative about realized OOS
  portfolio performance, portfolio concentration, and ex post opportunity sets
  for the long-only core portfolios
- the factsheet layer should translate the same Stage 3 engine into app-style
  point-in-time views of holdings, concentration, turnover, and
  BTC/ETH exposure
- the Stage 4 app should keep the main client surface fixed to the published
  monthly/365-day/expanding lineup and isolate alternative design controls in a
  secondary comparison view

## Working Rules

- Keep week-specific work inside this folder.
- Use `data/` for committed source inputs only.
- Use `results/data/` for generated datasets.
- Use `results/tables/` for Stage 2 and Stage 3 summary tables.
- Use `results/figures/` for exported Week 5 figures.
- Use `scratch/` for disposable experiments, not the final path.
- Keep reusable week-local logic in `code/`.
- Promote cross-week logic into `fintools/` only when it is genuinely reusable.
- Use Yahoo historical pulls through `https://query2.finance.yahoo.com/v8/finance/chart/{ticker}`.
- Do not introduce `yfinance` unless the user explicitly asks for it.
- Keep the canonical crypto output in long panel form with key `ticker, date`.
- Treat wide price and return tables as derived Stage 2 objects.
- Treat the Week 5 `rfr` merge as a teaching surface:
  - merge by `date`
  - forward-fill across weekends and public holidays
  - explain the assumption explicitly
- Use adjusted prices and simple daily returns.
- Use `365` for annualized crypto metrics.
- Use a `180`-day rolling window for the six-month features.
- Stage 2 should flag suspicious returns, not silently winsorize or drop them.
- Week 5 Stage 3 defaults:
  - initial window: `365`
  - estimation frequency: `monthly`
  - window rule: `expanding`
  - constraint mode: `long_only`
  - models: equal-weight, minimum variance, mean-variance tangency,
    mean-CVaR tangency, and risk parity
- Treat Stage 3 as out-of-sample:
  - estimate on the decision date using past data only
  - save weight rows on the later holding dates they apply to
  - save `formation_date` and `return_date` separately in the daily return panel
  - drift weights within each holding block until the next formation date
- Treat Stage 3 factsheet clocks explicitly:
  - use the latest formation date for target-weight and rebalance-change views
  - use the latest return date for live-holdings and realized-performance views
- Treat Stage 3 speed as part of the contract:
  - use analytic-gradient SLSQP for long-only minimum-variance and tangency
  - use Newton risk budgeting for long-only risk parity
  - use the fast mean-CVaR solver first and keep the sparse HiGHS fallback
- Treat the visible Stage 4 UI as a client product:
  - use published fund names
  - avoid raw internal keys outside methodology or download surfaces
  - keep the allocation view illustrative, not execution-focused
- Regenerate `guidance/*.md` after week docs, scripts, or data contracts change.

## Useful Commands

- `python fins2026/week5/scripts/describe_data.py`
- `python fins2026/week5/scripts/run_week.py`
- `python fins2026/week5/scripts/run_beginner_french_rfr.py`
- `python fins2026/week5/scripts/run_beginner_yahoo_crypto_intro_5.py`
- `python fins2026/week5/scripts/run_beginner_yahoo_crypto_20_since_2019.py`
- `python fins2026/week5/scripts/run_beginner_stage2_returns_wide.py`
- `python fins2026/week5/scripts/run_beginner_stage2_returns_long.py`
- `python fins2026/week5/scripts/run_beginner_stage2_features_long.py`
- `python fins2026/week5/scripts/make_stage2_crypto_figures.py`
- `python fins2026/week5/scripts/run_beginner_stage3_oos_weights.py`
- `python fins2026/week5/scripts/make_stage3_portfolio_figures.py`
- `python fins2026/week5/scripts/build_week5_app_fixture.py`
- `streamlit run fins2026/week5/app/streamlit_app.py`
- `python tools/workflow.py check-app-submission --target fins2026/week5 --entrypoint fins2026/week5/app/streamlit_app.py`
- `python tools/workflow.py prepare-app-repo --source fins2026/week5 --dest ../week5-digital-asset-fund-explorer --repo week5-digital-asset-fund-explorer --entrypoint fins2026/week5/app/streamlit_app.py --push`
- `python fins2026/week5/scripts/make_stage2_crypto_figures.py --include-appendix`
- `python tools/workflow.py build-week-context --target fins2026/week5`


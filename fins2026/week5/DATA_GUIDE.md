# Week 5 Data Guide

Week 5 has three data layers:

- Stage 1 source inputs
- Stage 1 downloaded outputs
- Stage 2 return, feature, and summary outputs
- Stage 3 out-of-sample portfolio, summary, and figure outputs
- Stage 4 app fixture and client-facing app outputs

Provider priority:

- Yahoo Finance is the canonical Week 5 crypto dataset
- Kenneth French daily `RF` is the canonical risk-free input

## Source Inputs in `data/`

- `yahoo_crypto_intro_5.txt`
  - tiny 5-coin warm-up universe
- `yahoo_crypto_20_since_2019.txt`
  - canonical balanced 20-coin universe for the full Week 5 panel

## Stage 1 Outputs in `results/data/`

### Kenneth French daily risk-free rate

- `results/data/french_daily_rfr/french_daily_rfr.parquet`

This file contains only:

- `date`
- `rfr`

The source `RF` column is in percent. Week 5 divides by `100`, so `rfr` is a
decimal daily rate.

### Yahoo 5-coin warm-up panel

- `results/data/yahoo_crypto_intro_5/yahoo_chart_panel_long.csv`
- `results/data/yahoo_crypto_intro_5/yahoo_chart_panel_long.parquet`
- `results/data/yahoo_crypto_intro_5/yahoo_chart_metadata.csv`
- `results/data/yahoo_crypto_intro_5/yahoo_chart_coverage_summary.csv`
- `results/data/yahoo_crypto_intro_5/yahoo_chart_failures.csv` only if some
  tickers fail

### Yahoo 20-coin panel

- `results/data/yahoo_crypto_20_since_2019/yahoo_chart_panel_long.csv`
- `results/data/yahoo_crypto_20_since_2019/yahoo_chart_panel_long.parquet`
- `results/data/yahoo_crypto_20_since_2019/yahoo_chart_metadata.csv`
- `results/data/yahoo_crypto_20_since_2019/yahoo_chart_coverage_summary.csv`
- `results/data/yahoo_crypto_20_since_2019/yahoo_chart_failures.csv` only if
  some tickers fail
- `results/data/yahoo_crypto_20_since_2019/_ticker_cache/`
  - per-ticker cache used for resume mode

Interpretation:

- this is the canonical Week 5 crypto dataset
- the panel is quoted in USD
- the long panel is the saved source of truth

## Yahoo Crypto Schema Notes

Key:

- `ticker`
- `date`

Fields:

- `open`
- `high`
- `low`
- `close`
- `adjClose`
- `volume`
- `dividend`
- `splitFactor`

Interpretation:

- Yahoo returns these as daily crypto bars
- `currency` should read `USD`
- `exchangeName` should read `CCC`
- `instrumentType` should read `CRYPTOCURRENCY`
- `exchangeTimezoneName` should read `UTC`
- `adjClose` is the canonical price field for return work
- for Yahoo `*-USD` crypto pairs, Week 5 treats `volume` as a USD or
  dollar-volume field rather than base-asset units
- do not multiply Yahoo crypto `volume` by `adjClose` when building a
  volume-based figure for USD pairs

## Stage 2 Outputs in `results/data/stage2/yahoo_crypto/`

Canonical Stage 2 Parquet files:

- `yahoo_crypto_adjclose_wide.parquet`
- `yahoo_crypto_returns_wide.parquet`
- `yahoo_crypto_returns_long.parquet`
- `yahoo_crypto_returns_features_long.parquet`

Interpretation:

- adjusted prices are the base input for return construction
- wide returns show the row-wise matrix calculation
- long returns show the `groupby` panel calculation
- the feature-rich long panel is the main Week 5 Stage 2 output

## Stage 2 Long-Panel Feature Columns

The feature-rich long panel adds:

- `ret`
- `abs_ret`
- `rfr`
- `excess_ret`
- `is_large_move_10pct`
- `is_large_move_20pct`
- `rolling_6m_avg_ret`
- `rolling_6m_vol`
- `rolling_6m_var_95`
- `rolling_6m_sharpe`
- `rolling_6m_sortino`

Definitions:

- six months = `180` daily observations
- `rolling_6m_avg_ret` stays in daily return units
- `rolling_6m_vol` is annualized with `sqrt(365)`
- `rolling_6m_var_95` is the trailing historical 5th percentile of daily
  returns
- `rolling_6m_sharpe` and `rolling_6m_sortino` use excess returns and are
  annualized with `sqrt(365)`

## Stage 2 Merge Rule

The Week 5 `rfr` merge is deliberately different from a plain equity example.

- crypto trades every day
- Kenneth French `rfr` only updates on business days
- Week 5 merges `rfr` by `date` and forward-fills it across weekends and public
  holidays

Interpretation:

- this is an explicit modelling assumption
- it is part of the Week 5 teaching objective, not a hidden implementation
  detail

## Stage 2 Summary Outputs

Week 5 saves the full-sample crypto summary metrics under:

- `results/tables/stage2/yahoo_crypto/yahoo_crypto_summary_metrics.csv`
- `results/tables/stage2/yahoo_crypto/yahoo_crypto_summary_metrics.parquet`

The summary includes:

- mean daily return
- annualized return
- annualized volatility
- full-sample Sharpe ratio
- full-sample Sortino ratio
- skewness
- excess kurtosis
- maximum absolute daily return
- tail shares above `|z| > 2`
- tail shares above `|z| > 3`

## Stage 2 Figure Outputs

Week 5 Stage 2 figures live under:

- `results/figures/stage2/yahoo_crypto/`

The canonical figure pack includes:

- BTC/ETH/DOGE/ADA price small multiples
- growth of `$1` for five well-known coins on log scale
- headline drawdowns
- altcoin wealth relative to BTC
- rolling correlations with BTC
- largest downside and upside one-day moves
- headline daily-return correlation matrix
- volatility ranking
- annualized return ranking
- Sharpe ratio ranking
- Sortino ratio ranking
- histogram-versus-normal small multiples
- tail-share dumbbell comparison against normal benchmarks

The optional appendix figure pack adds:

- cross-sectional dispersion over time
- rolling headline volatility
- rolling headline Sharpe ratios
- max drawdown ranking
- risk-return scatter
- headline dollar-volume small multiples
- daily dollar-volume concentration shares
- trailing 30-day dollar-volume ranking

## Stage 3 Outputs in `results/data/stage3/yahoo_crypto/`

Canonical Stage 3 files:

- `yahoo_crypto_oos_weights_daily.parquet`
- `yahoo_crypto_oos_portfolio_returns_daily.parquet`
- `yahoo_crypto_oos_ex_post_frontier.parquet`
- `yahoo_crypto_oos_rebalance_audit.parquet`
- `yahoo_crypto_oos_latest_target_weights.parquet`
- `yahoo_crypto_oos_latest_live_weights.parquet`
- `yahoo_crypto_oos_latest_risk_contributions.parquet`

Interpretation:

- Stage 3 starts from the saved balanced Stage 2 feature panel
- each rebalance uses only data available through the decision date
- `date` in the daily panel is the holding date the weight applies to
- `decision_date` records when the model was re-estimated
- the first holding date is always the next day after the decision date
- the daily return panel uses:
  - `formation_date` for the date the weights became known
  - `return_date` for the later daily date the portfolio return was earned
- daily portfolio returns drift within each holding block until the next
  formation date resets the target weights

Daily weight-panel columns:

- `date`
- `decision_date`
- `model`
- `constraint_mode`
- `ticker`
- `weight`

Rebalance-audit columns:

- `decision_date`
- `effective_start_date`
- `effective_end_date`
- `window_start_date`
- `window_end_date`
- `window_observations`
- `model`
- `constraint_mode`
- `ticker`
- `weight`
- `solver`
- `status`
- `elapsed_ms`

Daily return-panel columns:

- `return_date`
- `formation_date`
- `equal_weight`
- `minimum_variance_long_only`
- `mean_variance_tangency_long_only`
- `mean_cvar_tangency_long_only`
- `risk_parity_volatility_long_only`

Latest target-weight snapshot columns:

- `decision_date`
- `previous_decision_date`
- `portfolio_key`
- `portfolio`
- `ticker`
- `previous_weight`
- `latest_weight`
- `weight_change`

Latest live-weight snapshot columns:

- `return_date`
- `formation_date`
- `portfolio_key`
- `portfolio`
- `ticker`
- `weight`

Latest risk-contribution snapshot columns:

- `decision_date`
- `portfolio_key`
- `portfolio`
- `ticker`
- `weight`
- `variance_contribution`
- `variance_contribution_pct`

Current Stage 3 solver families:

- `SLSQP_jac` for the long-only minimum-variance and tangency solves
- `newton_risk_budgeting` for long-only risk parity
- `SLSQP_subgradient_or_sparse_HiGHS` for mean-CVaR

Stage 3 defaults:

- initial window = `365` daily observations
- estimation frequency = `monthly`
- window rule = `expanding`
- supported models = equal-weight, minimum variance, mean-variance tangency,
  mean-CVaR tangency, and risk parity
- supported constraint mode = `long_only`

## Stage 3 Summary Outputs

Week 5 saves the Stage 3 summary outputs under:

- `results/tables/stage3/yahoo_crypto/yahoo_crypto_oos_portfolio_metrics.csv`
- `results/tables/stage3/yahoo_crypto/yahoo_crypto_oos_portfolio_metrics.parquet`
- `results/tables/stage3/yahoo_crypto/yahoo_crypto_oos_solve_summary.csv`
- `results/tables/stage3/yahoo_crypto/yahoo_crypto_oos_solve_summary.parquet`
- `results/tables/stage3/yahoo_crypto/yahoo_crypto_oos_latest_concentration_metrics.csv`
- `results/tables/stage3/yahoo_crypto/yahoo_crypto_oos_latest_concentration_metrics.parquet`
- `results/tables/stage3/yahoo_crypto/yahoo_crypto_oos_trailing_return_snapshot.csv`
- `results/tables/stage3/yahoo_crypto/yahoo_crypto_oos_trailing_return_snapshot.parquet`
- `results/tables/stage3/yahoo_crypto/yahoo_crypto_oos_current_drawdown_snapshot.csv`
- `results/tables/stage3/yahoo_crypto/yahoo_crypto_oos_current_drawdown_snapshot.parquet`
- `results/tables/stage3/yahoo_crypto/yahoo_crypto_oos_trailing_risk_snapshot.csv`
- `results/tables/stage3/yahoo_crypto/yahoo_crypto_oos_trailing_risk_snapshot.parquet`
- `results/tables/stage3/yahoo_crypto/yahoo_crypto_oos_latest_turnover_snapshot.csv`
- `results/tables/stage3/yahoo_crypto/yahoo_crypto_oos_latest_turnover_snapshot.parquet`
- `results/tables/stage3/yahoo_crypto/yahoo_crypto_oos_latest_btc_eth_exposure.csv`
- `results/tables/stage3/yahoo_crypto/yahoo_crypto_oos_latest_btc_eth_exposure.parquet`

The portfolio-metrics files record:

- portfolio display label
- canonical portfolio key
- cumulative return
- annualized return
- annualized volatility
- Sharpe ratio
- Sortino ratio
- max drawdown

The solve summary records:

- model
- constraint mode
- rebalance count
- first and last decision dates
- average and maximum window size
- average and maximum solve time
- solver family
- status, including unsupported combinations

The factsheet snapshot tables record:

- latest concentration:
  - top 1, top 3, and top 5 weight share
  - effective number of holdings
- trailing returns:
  - 30-day, 90-day, 180-day, and since-inception realized OOS returns
- current drawdown:
  - latest realized drawdown from peak
- trailing risk:
  - 180-day annualized volatility
  - 180-day Sharpe ratio
  - 180-day Sortino ratio
  - 180-day historical CVaR
- latest turnover:
  - one-way turnover between the latest and previous formation dates
- latest BTC/ETH exposure:
  - combined BTC+ETH share
  - other-coin share

## Stage 3 Figure Outputs

Week 5 saves the Stage 3 figure packs under:

- `results/figures/stage3/long_only/`

Each folder contains:

- `yahoo_crypto_stage3_oos_growth_of_one.png`
- `yahoo_crypto_stage3_oos_drawdowns.png`
- `yahoo_crypto_stage3_oos_scorecard.png`
- `yahoo_crypto_stage3_oos_top_holdings_over_time.png`
- `yahoo_crypto_stage3_oos_efficient_frontier.png`
- `yahoo_crypto_stage3_factsheet_latest_holdings_dumbbell.png`
- `yahoo_crypto_stage3_factsheet_live_holdings_snapshot.png`
- `yahoo_crypto_stage3_factsheet_concentration_scorecard.png`
- `yahoo_crypto_stage3_factsheet_risk_contributions.png`
- `yahoo_crypto_stage3_factsheet_trailing_returns.png`
- `yahoo_crypto_stage3_factsheet_current_drawdown.png`
- `yahoo_crypto_stage3_factsheet_trailing_risk.png`
- `yahoo_crypto_stage3_factsheet_turnover_and_changes.png`
- `yahoo_crypto_stage3_factsheet_btc_eth_exposure.png`

Interpretation:

- the long-only pack uses the long-only core portfolios
- the same folder now contains both a research pack and a point-in-time
  factsheet pack
- the holdings figure uses formation-date target weights, not drifted daily
  weights
- the latest target-weight factsheet now shows the current target levels rather
  than a latest-versus-previous dumbbell comparison
- the holdings figure keeps the top 5 average target weights for each optimized
  long-only model
- target-weight factsheet figures use the latest formation date and the
  previous formation date when needed
- live-holding, realized-return, drawdown, and trailing-risk figures use the
  latest return date
- the BTC/ETH factsheet figure shows the combined current share in the two
  major coins, with the remainder implicitly invested in other coins
- the frontier figure is ex post and diagnostic:
  - it compares realized OOS portfolio outcomes with the realized OOS asset
    opportunity set
  - it is not an ex ante tradable frontier

## Stage 4 App Fixture And Surface

Week 5 now carries a real client-facing app under `app/`.

Committed app fixture:

- `app/fixtures/week5_app_features_long.parquet`

Interpretation:

- this is the committed fallback feature panel for the Stage 4 app
- it already contains prices, returns, `rfr`, and rolling six-month features
- the app first tries a live Yahoo/French refresh and then falls back to this
  file if the refresh fails

Stage 4 app modules:

- `app/app_config.py`
- `app/app_data.py`
- `app/app_insights.py`
- `app/app_views.py`
- `app/streamlit_app.py`

Stage 4 pure helper module:

- `code/stage4_app.py`

Stage 4 fixture refresh script:

- `scripts/build_week5_app_fixture.py`

## Rules

- keep committed source data in `data/`
- keep downloaded and derived outputs in `results/data/`
- keep summary tables in `results/tables/`
- use adjusted prices for Stage 2 returns
- use `365` for annualized crypto metrics
- do not silently delete outliers during Stage 2
- treat Stage 3 as out-of-sample and use only past data through each decision
  date
- keep Stage 3 daily weights indexed by the future holding dates they govern
- keep Stage 3 daily portfolio returns indexed by the earned `return_date`
  rather than a synthetic month-end label


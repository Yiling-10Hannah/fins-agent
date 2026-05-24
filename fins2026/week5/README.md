# Week 5: Crypto Data, Diagnostics, and OOS Portfolios

Week 5 adapts the Week 4 operating model to cryptocurrencies.

- Stage 1: pull crypto price history from Yahoo Finance and the daily risk-free
  rate from Kenneth French
- Stage 2: compute crypto returns, merge business-day `rfr` onto a 24/7 market,
  build rolling diagnostics, and export FT-style figures
- Stage 3: generate out-of-sample portfolio weights, daily portfolio returns,
  FT-style OOS portfolio figures, and point-in-time factsheet figures from the
  cleaned Stage 2 panel using only past data at each rebalance date
- Stage 4: turn the published long-only fund shelf into a client-facing
  Streamlit app with live/fixture data, portfolio factsheets, an allocation
  simulator, and an advanced design-comparison tab

Week 5 now covers the full data, diagnostics, portfolio-construction path, and
the first client-facing app layer.

## Week Aim

Students should leave Week 5 able to:

1. pull USD-quoted crypto prices from Yahoo Finance without `yfinance`
2. explain why a crypto panel uses calendar days instead of trading-day
   business calendars
3. download the Kenneth French daily `RF` series and save it as `rfr`
4. merge business-day `rfr` onto a 24/7 crypto panel with forward-fill across
   weekends and public holidays
5. compute simple daily returns from adjusted prices in both wide and long
   data
6. verify wide-return and long-return parity
7. build rolling six-month crypto features using a `180`-day daily window
8. annualize crypto risk metrics with `365` daily observations
9. produce FT-style figures for crypto prices, cumulative returns, Sharpe,
   Sortino, and non-normal return distributions
10. explain why crypto tails differ materially from a normal benchmark
11. define a rebalance calendar on a 24/7 crypto date index
12. estimate out-of-sample portfolio weights using only data available through
    each decision date
13. save daily holding-date weight panels and daily OOS portfolio-return
    panels
14. evaluate OOS portfolios with FT-style growth, drawdown, scorecard,
    holdings, and frontier figures
15. build point-in-time factsheet views of current holdings, concentration,
    trailing risk, turnover, and BTC/ETH exposure
16. translate the published fund lineup into a client-facing Streamlit product
    with a fixture-backed fallback path

## Stage 1: Source Connection

Week 5 Stage 1 uses two source pulls:

- Kenneth French daily `RF`
- Yahoo Finance crypto chart history

Stage 1 scripts:

```text
python fins2026/week5/scripts/run_beginner_french_rfr.py
python fins2026/week5/scripts/run_beginner_yahoo_crypto_intro_5.py
python fins2026/week5/scripts/run_beginner_yahoo_crypto_20_since_2019.py
```

Important Stage 1 rules:

- Yahoo crypto history is queried through the direct chart endpoint, not
  `yfinance`
- prices are quoted in USD
- save downloaded data under `results/data/`, not `data/`
- use the 5-coin warm-up pull first, then the 20-coin panel
- treat the long Yahoo panel as the canonical saved dataset
- drop all-null placeholder OHLCV rows before coverage checks

## Stage 2: Returns, Merge Logic, and Diagnostics

Stage 2 starts from the saved 20-coin Yahoo panel and the saved French
`rfr` file.

Stage 2 scripts:

```text
python fins2026/week5/scripts/run_beginner_stage2_returns_wide.py
python fins2026/week5/scripts/run_beginner_stage2_returns_long.py
python fins2026/week5/scripts/run_beginner_stage2_features_long.py
python fins2026/week5/scripts/make_stage2_crypto_figures.py
```

Stage 2 teaching contract:

- use adjusted prices
- compute simple daily returns, not log returns
- show the wide calculation and the long `groupby` calculation
- verify that the two return paths match
- merge `rfr` by `date`
- forward-fill `rfr` across weekends, public holidays, and tail dates after the
  latest French observation
- explain that this is a modelling assumption required when a 24/7 asset class
  is merged with business-day financial data

### Rolling Six-Month Features

Week 5 adds these long-panel columns:

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

### Stage 2 Figure Pack

The FT-style Week 5 figure pack includes:

1. 2x2 price small multiples for BTC, ETH, DOGE, and ADA
2. log-scale growth of `$1` for BTC, ETH, XRP, ADA, and DOGE
3. headline drawdowns
4. altcoin wealth relative to BTC
5. rolling headline correlations with BTC
6. largest downside and upside one-day moves
7. headline-coin daily-return correlation matrix
8. annualized volatility ranking
9. annualized return ranking
10. full-sample Sharpe ratio ranking
11. full-sample Sortino ratio ranking
12. histogram-versus-normal small multiples for headline coins
13. dumbbell comparison of observed tail shares against normal benchmarks

Optional appendix figures are available with:

```text
python fins2026/week5/scripts/make_stage2_crypto_figures.py --include-appendix
```

The appendix adds:

1. cross-sectional dispersion over time
2. rolling headline volatility
3. rolling headline Sharpe ratios
4. max drawdown ranking
5. risk-return scatter
6. 2x2 headline dollar-volume time-series for BTC, ETH, XRP, and DOGE
7. 100%-share daily dollar-volume concentration chart
8. trailing 30-day dollar-volume ranking

Volume note:

- for Yahoo `*-USD` crypto pairs, Week 5 treats `volume` as a USD or
  dollar-volume field
- the appendix ranking therefore uses Yahoo `volume` directly and does not
  multiply by price again

Important presentation rules:

- use FT-style exports through `fintools.figures`
- use the same NBER recession shading convention as Week 4 on long time-series
- keep titles short and move detail into the caption context
- use log scale for cumulative-return comparisons
- prefer FT-style ranking and benchmark-comparison charts over raw bar charts
- make the non-normality lesson visible, not implicit

## Stage 3: Out-of-Sample Weights, Returns, and Figures

Stage 3 starts from the saved Week 5 Stage 2 feature panel and builds
portfolio weights on a rebalance schedule using only data available through the
decision date. It then applies those weights to later daily returns to produce
the actual out-of-sample portfolio return panel.

Stage 3 scripts:

```text
python fins2026/week5/scripts/run_beginner_stage3_oos_weights.py
python fins2026/week5/scripts/make_stage3_portfolio_figures.py
```

Default Stage 3 contract:

- initial window: `365` daily observations
- estimation frequency: `monthly`
- window rule: `expanding`
- constraint mode: `long_only`
- models:
  - equal-weight
  - minimum variance
  - mean-variance tangency
  - mean-CVaR tangency
  - risk parity with volatility as the risk measure

Important Stage 3 rules:

- monthly re-estimation uses the last available crypto date in each calendar
  month
- weekly re-estimation uses Sunday-ended weeks on the crypto date index
- the training window ends on the decision date
- the saved weight rows are indexed by the holding dates they apply to, so the
  first holding date is always the day after the decision date
- `formation_date` is the date the weights became known
- `return_date` is the later daily date the portfolio return was earned
- within each holding block, the portfolio is buy-and-hold:
  - start from the target weights on the first holding day
  - let weights drift with realized returns until the next formation date
- the Stage 3 engine is speed-oriented:
  - long-only minimum-variance and tangency use analytic-gradient SLSQP
  - long-only risk parity uses a Newton risk-budgeting solver
  - mean-CVaR uses a fast tail-subgradient solve with a sparse HiGHS fallback
- the canonical Stage 3 figure script now builds the long-only core pack:
  - equal-weight
  - minimum variance
  - mean-variance
  - mean-CVaR
  - risk parity
- the same Stage 3 figure script also exports a long-only factsheet pack built
  around two clocks:
  - latest formation date for target-weight and rebalance-change views
  - latest return date for realized performance and live-holdings views
- the Stage 3 frontier figure is ex post:
  - it uses the realized OOS asset window as a diagnostic comparison surface
  - it is not an ex ante tradable frontier

### Stage 3 Figure Packs

The Stage 3 figure script exports two long-only surfaces under:

- `results/figures/stage3/long_only/`

Research pack:

1. OOS growth of `$1`
2. OOS drawdowns
3. OOS six-metric scorecard
4. top target holdings over time
5. ex post efficient frontier

Factsheet pack:

1. latest target-weight snapshot
2. live holdings snapshot
3. concentration scorecard
4. latest risk-contribution snapshot
5. trailing return bars
6. current drawdown snapshot
7. trailing risk snapshot
8. latest turnover and largest weight changes
9. combined BTC+ETH share snapshot

Supporting Stage 3 snapshot tables:

- latest target weights
- latest live weights
- latest risk contributions
- latest concentration metrics
- trailing return snapshot
- current drawdown snapshot
- trailing risk snapshot
- latest turnover snapshot
- latest BTC/ETH exposure snapshot

## Stage 4: Client-Facing App

Stage 4 turns the long-only published fund shelf into a client-facing Streamlit
product.

Stage 4 scripts and app entrypoints:

```text
python fins2026/week5/scripts/build_week5_app_fixture.py
streamlit run fins2026/week5/app/streamlit_app.py
python tools/workflow.py check-app-submission --target fins2026/week5 --entrypoint fins2026/week5/app/streamlit_app.py
```

Stage 4 product contract:

- the published lineup stays fixed to:
  - monthly rebalancing
  - 365-day initial window
  - expanding estimation window
- the visible fund shelf uses client-facing names:
  - Core Market
  - Low Volatility
  - Return Seeking
  - Downside Aware
  - Risk Balanced
- the app includes:
  - historical performance views
  - current live and target holdings
  - concentration, turnover, and risk snapshots
  - an illustrative allocation simulator
  - a secondary portfolio-design tab for monthly and weekly comparison scenarios
- the app first tries live Yahoo/French refreshes and then falls back to the
  committed fixture bundle in `app/fixtures/`

## Recommended Teaching Flow

1. review `README.md`, `DATA_GUIDE.md`, and `guidance/week-context.md`
2. run `python fins2026/week5/scripts/describe_data.py`
3. run the French `rfr` download
4. explain that `RF` is a business-day series and must be transformed to `rfr`
5. run the 5-coin Yahoo warm-up pull
6. run the 20-coin Yahoo panel pull
7. compute wide returns
8. compute long returns and verify parity
9. merge `rfr` and build rolling features
10. inspect Sharpe and Sortino rankings
11. export the FT-style figure pack
12. optionally export the appendix figure pack
13. build the Stage 3 out-of-sample weight and return panels
14. export the Stage 3 FT-style portfolio and factsheet figure pack
15. refresh the Week 5 app fixture
16. launch the client-facing app
17. refresh `guidance/`

## Run The Week

From the repo root:

```text
python fins2026/week5/scripts/describe_data.py
python fins2026/week5/scripts/run_week.py
python fins2026/week5/scripts/run_beginner_french_rfr.py
python fins2026/week5/scripts/run_beginner_yahoo_crypto_intro_5.py
python fins2026/week5/scripts/run_beginner_yahoo_crypto_20_since_2019.py
python fins2026/week5/scripts/run_beginner_stage2_returns_wide.py
python fins2026/week5/scripts/run_beginner_stage2_returns_long.py
python fins2026/week5/scripts/run_beginner_stage2_features_long.py
python fins2026/week5/scripts/make_stage2_crypto_figures.py
python fins2026/week5/scripts/make_stage2_crypto_figures.py --include-appendix
python fins2026/week5/scripts/run_beginner_stage3_oos_weights.py
python fins2026/week5/scripts/make_stage3_portfolio_figures.py
python fins2026/week5/scripts/build_week5_app_fixture.py
streamlit run fins2026/week5/app/streamlit_app.py
python tools/workflow.py check-app-submission --target fins2026/week5 --entrypoint fins2026/week5/app/streamlit_app.py
python tools/workflow.py build-week-context --target fins2026/week5
```

## Data and Output Contract

- `data/` holds only committed source inputs such as ticker lists
- `results/data/french_daily_rfr/french_daily_rfr.parquet` is the canonical
  daily risk-free file
- `results/data/yahoo_crypto_intro_5/` holds the 5-coin warm-up pull
- `results/data/yahoo_crypto_20_since_2019/` holds the canonical 20-coin long
  panel
- `results/data/stage2/yahoo_crypto/` holds the Stage 2 Parquet outputs
- `results/data/stage3/yahoo_crypto/` holds the Stage 3 weight and return outputs
- `results/tables/stage2/yahoo_crypto/` holds the Stage 2 summary tables
- `results/tables/stage3/yahoo_crypto/` holds the Stage 3 solve summary and OOS scorecards
- `results/figures/stage2/yahoo_crypto/` holds the FT-style Stage 2 figures
- `results/figures/stage3/long_only/` holds the FT-style Stage 3 long-only OOS portfolio figures
- `app/fixtures/week5_app_features_long.parquet` is the committed fallback
  bundle for the Stage 4 app
- long panel data is the canonical crypto shape
- wide price and return tables are derived Stage 2 objects

Canonical Stage 2 Parquet files:

- `yahoo_crypto_adjclose_wide.parquet`
- `yahoo_crypto_returns_wide.parquet`
- `yahoo_crypto_returns_long.parquet`
- `yahoo_crypto_returns_features_long.parquet`

Canonical Stage 2 summary files:

- `yahoo_crypto_summary_metrics.csv`
- `yahoo_crypto_summary_metrics.parquet`

Canonical Stage 3 files:

- `yahoo_crypto_oos_weights_daily.parquet`
- `yahoo_crypto_oos_portfolio_returns_daily.parquet`
- `yahoo_crypto_oos_ex_post_frontier.parquet`
- `yahoo_crypto_oos_rebalance_audit.parquet`
- `yahoo_crypto_oos_portfolio_metrics.csv`
- `yahoo_crypto_oos_portfolio_metrics.parquet`
- `yahoo_crypto_oos_solve_summary.csv`
- `yahoo_crypto_oos_solve_summary.parquet`

## Working Rules

- keep API logic in `code/` and student-run entrypoints in `scripts/`
- use adjusted prices for return construction
- use `365` for annualized crypto metrics
- use `180` daily observations for the rolling six-month window
- do not silently delete outliers during Stage 2
- treat Stage 3 as out-of-sample and use only past data through each decision
  date
- save Stage 3 weights on the holding dates they apply to
- save Stage 3 portfolio returns with `return_date` first and `formation_date`
  second
- keep the Stage 3 figure narrative focused on the long-only core portfolios
- keep the Stage 4 visible UI strictly client-facing and avoid raw internal
  model labels outside the Methodology tab
- keep Week 5 student-facing and rerunnable from the repo root
- refresh `guidance/` after week docs, scripts, or data contracts change


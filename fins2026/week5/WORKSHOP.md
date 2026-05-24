# Week 5 Workshop

Week 5 mirrors the Week 4 operating model and now extends into the first
out-of-sample Stage 3 weight, return, figure, and client-facing app layer.

- Stage 1: source connection and local dataset creation
- Stage 2: crypto returns, business-day `rfr` merge logic, and FT-style
  diagnostics
- Stage 3: out-of-sample portfolio weights, returns, and FT-style OOS figures
  on the crypto daily calendar
- Stage 4: a client-facing Streamlit app built on the published long-only fund
  lineup

## Core Path

1. Review `README.md`, `DATA_GUIDE.md`, and `guidance/week-context.md`.
2. Run `python fins2026/week5/scripts/describe_data.py`.
3. Run `python fins2026/week5/scripts/run_beginner_french_rfr.py`.
4. Explain the French `rfr` step:
   - it is still part of Stage 1
   - we keep only `RF`
   - we rename it to `rfr`
   - we divide by `100`
   - we save only one final Parquet file
5. Run `python fins2026/week5/scripts/run_beginner_yahoo_crypto_intro_5.py`.
6. Explain the Yahoo crypto role:
   - Yahoo is the canonical Week 5 crypto source
   - the endpoint is public but unofficial
   - the data are daily UTC crypto bars quoted in USD
   - for Yahoo `*-USD` pairs, treat `volume` as a dollar-volume field and do
     not multiply it by price again
7. Run `python fins2026/week5/scripts/run_beginner_yahoo_crypto_20_since_2019.py`.
8. Explain why the 20-coin panel matters:
   - it is balanced back to `2019-01-01`
   - it is the main downstream Week 5 dataset
9. Run `python fins2026/week5/scripts/run_beginner_stage2_returns_wide.py`.
10. Explain the wide return calculation from adjusted prices.
11. Run `python fins2026/week5/scripts/run_beginner_stage2_returns_long.py`.
12. Explain the long `groupby` return calculation and the parity check.
13. Run `python fins2026/week5/scripts/run_beginner_stage2_features_long.py`.
14. Explain the merge lesson:
   - crypto trades every day
   - `rfr` only exists on business days
   - forward-filling `rfr` across weekends and holidays is an explicit
     assumption
15. Explain the rolling six-month features:
   - average return
   - annualized volatility
   - VaR-95%
   - Sharpe
   - Sortino
16. Run `python fins2026/week5/scripts/make_stage2_crypto_figures.py`.
17. Explain the figure pack:
   - prices over time for BTC, ETH, DOGE, and ADA
   - log-scale growth of `$1` for five well-known coins
   - headline drawdowns
   - altcoin wealth relative to BTC
   - rolling correlations with BTC
   - biggest downside and upside one-day moves
   - Sharpe and Sortino rankings
   - histogram-versus-normal views
   - tail-share dumbbell comparisons versus normal benchmarks
   - headline-coin return correlations
18. If useful, run the appendix figure pack with:
   - `python fins2026/week5/scripts/make_stage2_crypto_figures.py --include-appendix`
19. The appendix can illustrate:
   - cross-sectional dispersion
   - rolling volatility and rolling Sharpe
   - max drawdown ranking
   - risk-return scatter
   - headline dollar-volume time-series
   - daily dollar-volume concentration shares
   - trailing dollar-volume ranking
20. Run `python fins2026/week5/scripts/run_beginner_stage3_oos_weights.py`.
21. Explain the Stage 3 logic:
   - the default training window is `365` daily observations
   - the default rebalance schedule is monthly on the crypto calendar
   - the default window rule is expanding
   - weights are estimated on the decision date and saved on the future holding
     dates
   - `formation_date` is when the weights became known
   - `return_date` is when the daily portfolio return was earned
   - weights drift within the holding block until the next formation date
   - Week 5 now uses the long-only portfolio family only
22. Explain the five model families:
   - equal-weight
   - minimum variance
   - mean-variance tangency
   - mean-CVaR tangency
   - risk parity with volatility as the risk measure
23. Explain the Stage 3 output contract:
   - one daily target-weight panel
   - one daily out-of-sample portfolio-return panel
   - the return panel keeps `return_date` first and `formation_date` second
   - the Stage 3 figure script also saves latest snapshot tables for target
     weights, live weights, concentration, risk, turnover, and
     BTC/ETH exposure
24. Run `python fins2026/week5/scripts/make_stage3_portfolio_figures.py`.
25. Explain the Stage 3 figure pack:
   - the script exports one long-only research pack
   - it includes OOS growth of `$1`, OOS drawdowns, a six-metric
     scorecard, top-holdings-over-time, and an ex post frontier
   - the same script also exports a long-only factsheet pack:
     - latest target weights
     - live holdings
     - concentration
     - risk contributions
     - trailing returns
     - current drawdown
     - trailing risk
     - turnover and largest changes
     - combined BTC+ETH share
   - target-weight factsheet views use the latest formation date
   - realized-performance factsheet views use the latest return date
26. Run `python fins2026/week5/scripts/build_week5_app_fixture.py`.
27. Explain the app fixture role:
   - the app first tries live Yahoo/French refreshes
   - if the live refresh fails, it falls back to the committed feature-panel
     fixture
28. Launch the app with `streamlit run fins2026/week5/app/streamlit_app.py`.
29. Explain the client-facing app contract:
   - the published lineup is fixed to monthly, 365-day, expanding
   - the visible funds use client-facing names
   - the main tabs show performance, holdings, and allocation views
   - the advanced design tab compares alternative monthly and weekly rebalance
     schedules without changing the official published lineup
30. Refresh `guidance/` with `python tools/workflow.py build-week-context --target fins2026/week5`.

## Teaching Message

- Stage 1 gets the crypto and `rfr` data in the door.
- Stage 2 checks whether the saved prices are usable for later work.
- The key Week 5 merge lesson is that 24/7 crypto data and business-day
  financial data do not line up automatically.
- Forward-filling `rfr` is a practical teaching assumption, not a hidden fact
  of the data.
- Crypto return distributions are not well described by a normal benchmark.
- Stage 3 now adds the first out-of-sample portfolio-engine lesson: estimate on
  one date, then carry those weights forward through later earned returns.
- Stage 3 also adds the first OOS portfolio-evaluation lesson: separate the
  realized portfolio paths, the scorecard, the holdings story, and the ex post
  comparison surface.
- The factsheet layer translates the same Stage 3 engine into app-style,
  point-in-time portfolio views that a potential user could scan quickly.
- Stage 4 completes the Week 5 ladder by turning the same published fund shelf
  into a front-end product.


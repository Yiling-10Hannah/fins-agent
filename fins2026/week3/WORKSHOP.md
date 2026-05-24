# Week 3 Workshop

Use this run sheet to move from the simple Week 2 app to the richer Week 3 app
package, with the Australia forecast monitor as the primary walkthrough.

The teaching flow is intentionally split into:

- a core in-class run path
- an extension path
- the finished app layer

## Core In-Class Path

1. Review `README.md`, `DATA_GUIDE.md`, `BEGINNER_FORECASTING.md`, `APP_LAB.md`, and `guidance/week-context.md`.
2. Run `python fins2026/week3/scripts/make_beginner_forecasting_series.py`.
3. Run `python fins2026/week3/scripts/run_beginner_unit_root_check.py`.
4. Run `python fins2026/week3/scripts/run_beginner_naive_forecast.py`.
5. Run `python fins2026/week3/scripts/run_beginner_ar_forecast.py`.
6. Run `python fins2026/week3/scripts/run_beginner_arma_forecast.py`.
7. Run `python fins2026/week3/scripts/run_beginner_arx_forecast.py`.
8. Run `python fins2026/week3/scripts/run_beginner_model_horse_race.py`.
9. Run `python fins2026/week3/scripts/make_beginner_forecast_story_figures.py`.
10. Launch `streamlit run fins2026/week3/app/streamlit_app.py`.
11. Walk through the views in order:
   - Overview
   - Australia Snapshot
   - Forecasts
   - Model Comparison
   - Backtests
   - U.S. Context
   - Data
   - Methodology
11. Keep the teaching message simple:
   - choose a target
   - benchmark against naive
   - add structure gradually
   - compare models on target out-of-sample performance, with training ending at `2019-12-31`

## Extension Path

1. Run `python fins2026/week3/scripts/run_beginner_armax_forecast.py`.
2. Run `python fins2026/week3/scripts/run_beginner_ols_forecast.py`.
3. Run `python fins2026/week3/scripts/run_beginner_enet_forecast.py`.
4. Run `python fins2026/week3/scripts/run_beginner_ensemble_forecast.py`.
5. Use `make_beginner_forecast_story_figures.py` when you want FT-style lecture figures rather than raw backtest plots.
6. If you want the mirror U.S. walkthrough, move to:
   - `make_us_beginner_forecasting_series.py`
   - `run_us_beginner_unit_root_check.py`
   - `run_us_beginner_naive_forecast.py`
   - `run_us_beginner_ar_forecast.py`
   - `run_us_beginner_arma_forecast.py`
   - `run_us_beginner_arx_forecast.py`
   - `run_us_beginner_model_horse_race.py`
   - `make_us_beginner_forecast_story_figures.py`
7. Use these as deeper comparisons rather than the default starting point.

## Finished Product Layer

1. Run `python fins2026/week3/scripts/describe_data.py`.
2. Run `python fins2026/week3/scripts/describe_forecast_data.py`.
3. Build the reusable fixture inputs with `python fins2026/week3/scripts/build_forecast_inputs.py --use-fixture`.
4. Build the fixture benchmark leaderboard with `python fins2026/week3/scripts/run_forecast_benchmarks.py --use-fixture`.
5. Inspect how the module split supports the UI:
   - `app_config.py`
   - `app_data.py`
   - `app_insights.py`
   - `app_views.py`
   - `streamlit_app.py`
6. Use `APP_AUDIT.md` to explain what changed from the Week 2 prototype into a
   richer forecasting product.

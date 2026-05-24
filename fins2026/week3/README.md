# Week 3: Dual Macro App Lab

Week 3 extends the Streamlit introduction into two companion products built
from the same repo. The primary app is an Australia macro forecast monitor with
benchmarking and release-lag-aware inputs. The companion app keeps the U.S.
macro stress and forecasting surface available as a separate entrypoint in the
same Week 3 package.

Week 3 also adds a separate beginner forecasting ladder. Students should use
that lecture code first, then move to the full app once the core forecasting
ideas make sense.

## Week Aim

The goal this week is not to memorize every forecasting model.

The goal is to learn one clean forecasting workflow:

1. choose a sensible target
2. build a naive benchmark
3. add structure step by step
4. compare models out of sample on the target
5. only then open the finished app

The lecture anchor is the Australia unemployment rate. Students start by
forecasting the monthly change in unemployment rather than the raw level.

The lecture scripts now use a fixed evaluation split by default:

- in sample through `2019-12-31`
- out of sample from `2020-01-31` onward

Generated files are written under:

```text
fins2026/week3/results/
```

They are intentionally ignored by git. Re-run the scripts whenever you want a
fresh local state.

## What You Will Build

1. `app/streamlit_app.py`: the Australia macro forecast monitor with benchmark,
   backtest, and U.S.-context views.
2. `us_app/streamlit_app.py`: the companion U.S. macro stress and forecast
   monitor.
3. `scripts/build_forecast_inputs.py`: writes the reusable Australia and U.S.
   input panels used by the Australia app and benchmark scripts.
4. `scripts/run_forecast_benchmarks.py`: runs the approved Australia model
   suite and saves a one-step benchmark leaderboard plus per-model outputs.
5. `BEGINNER_FORECASTING.md` plus the numbered beginner scripts:
   unit root, naive, AR, ARMA, ARX, ARMAX, OLS, elastic net, a horse race,
   and an equal-weight ensemble.
6. `US_BEGINNER_FORECASTING.md` plus the U.S. extension scripts:
   unit root, naive, AR, ARMA, ARX, and a horse race.
7. `app/tests/test_app_smoke.py` and `us_app/tests/test_app_smoke.py`:
   view-by-view smoke tests for both Streamlit entrypoints.

## Recommended Teaching Flow

Use Week 3 in three layers.

### Layer 1: Core In-Class Path

This is the default student run path:

1. `make_beginner_forecasting_series.py`
2. `run_beginner_unit_root_check.py`
3. `run_beginner_naive_forecast.py`
4. `run_beginner_ar_forecast.py`
5. `run_beginner_arma_forecast.py`
6. `run_beginner_arx_forecast.py`
7. `run_beginner_model_horse_race.py`
8. `make_beginner_forecast_story_figures.py`
9. open the Australia app

This gives students the main Week 3 story without forcing them through every
extension script in one sitting.

### Layer 2: Extension Path

Use these after the core path, or as instructor-led extras:

- `run_beginner_armax_forecast.py`
- `run_beginner_ols_forecast.py`
- `run_beginner_enet_forecast.py`
- `run_beginner_ensemble_forecast.py`
- `make_us_beginner_forecast_story_figures.py`
- `US_BEGINNER_FORECASTING.md` plus the `run_us_beginner_*` scripts

These scripts deepen the model comparison story, but they are not the minimum
path needed to understand the lecture.

### Layer 3: Finished Product

After the lecture ladder, move to:

- `build_forecast_inputs.py --use-fixture`
- `run_forecast_benchmarks.py --use-fixture`
- `app/streamlit_app.py`

That is the product layer, not the starting point.

Useful guides:

- `DATA_GUIDE.md`: explains the Australia observable panel, U.S. context
  inputs, and target-frequency mapping.
- `BEGINNER_FORECASTING.md`: the beginner Week 3 lecture ladder.
- `US_BEGINNER_FORECASTING.md`: the U.S. mirror extension after the Australia core path.
- `app/README.md`: local run instructions and module map for the Australia app.
- `us_app/README.md`: local run instructions and deployment note for the U.S.
  companion app.
- `APP_LAB.md`: the build brief for the Australia forecasting product.
- `APP_AUDIT.md`: the benchmark audit against current Streamlit practice.
- `docs/apps/streamlit/student-quickstart.md`: the Week 2 deployment workflow
  that this richer app still builds on.
- `data/australia_macro_stage1_long.csv`: the committed Australia Stage 1
  fixture that keeps the standalone Week 3 deploy bundle self-contained.

## Run The Week

From the repo root:

```bash
python fins2026/week3/scripts/make_beginner_forecasting_series.py
python fins2026/week3/scripts/run_beginner_unit_root_check.py
python fins2026/week3/scripts/run_beginner_naive_forecast.py
python fins2026/week3/scripts/run_beginner_ar_forecast.py
python fins2026/week3/scripts/run_beginner_arma_forecast.py
python fins2026/week3/scripts/run_beginner_arx_forecast.py
python fins2026/week3/scripts/run_beginner_model_horse_race.py
python fins2026/week3/scripts/make_beginner_forecast_story_figures.py
streamlit run fins2026/week3/app/streamlit_app.py
```

Extended ladder:

```bash
python fins2026/week3/scripts/run_beginner_armax_forecast.py
python fins2026/week3/scripts/run_beginner_ols_forecast.py
python fins2026/week3/scripts/run_beginner_enet_forecast.py
python fins2026/week3/scripts/run_beginner_ensemble_forecast.py
python fins2026/week3/scripts/make_us_beginner_forecasting_series.py
python fins2026/week3/scripts/run_us_beginner_unit_root_check.py
python fins2026/week3/scripts/run_us_beginner_naive_forecast.py
python fins2026/week3/scripts/run_us_beginner_ar_forecast.py
python fins2026/week3/scripts/run_us_beginner_arma_forecast.py
python fins2026/week3/scripts/run_us_beginner_arx_forecast.py
python fins2026/week3/scripts/run_us_beginner_model_horse_race.py
python fins2026/week3/scripts/make_us_beginner_forecast_story_figures.py
```

Finished product layer:

```bash
python fins2026/week3/scripts/describe_data.py
python fins2026/week3/scripts/describe_forecast_data.py
python fins2026/week3/scripts/build_forecast_inputs.py --use-fixture
python fins2026/week3/scripts/run_forecast_benchmarks.py --use-fixture
streamlit run fins2026/week3/app/streamlit_app.py
streamlit run fins2026/week3/us_app/streamlit_app.py
```

The Australia app starts in fixture mode so it can run offline. Switch to live
mode in the sidebar when internet access is available and you want fresh
RBA/FRED inputs. The companion U.S. app also starts in fixture mode and can be
run independently.

The beginner ladder also runs offline by default because it uses the committed
Week 3 Australia fixture rather than a live data pull.

If an AI assistant is helping with Week 3, the default assumption should be:

- start with the core in-class path
- keep the focus on the unemployment-change target
- compare models on target out-of-sample performance
- move to the app only after the lecture ladder makes sense
- use `US_BEGINNER_FORECASTING.md` only when the student explicitly asks for the U.S. mirror extension

Before deployment for the primary Australia target, run:

```bash
python tools/workflow.py check-app-submission --target fins2026/week3 --entrypoint fins2026/week3/app/streamlit_app.py
```

To rehearse a clean private deploy repo for the Australia app:

```bash
python tools/workflow.py prepare-app-repo --source fins2026/week3 --dest ../week3-aus-forecast --repo week3-aus-forecast --entrypoint fins2026/week3/app/streamlit_app.py
```

To prepare the companion U.S. app as its own rehearsal repo:

```bash
python tools/workflow.py prepare-app-repo --source fins2026/week3 --dest ../week3-us-macro --repo week3-us-macro --entrypoint fins2026/week3/us_app/streamlit_app.py
```

Then follow `docs/apps/streamlit/finish-deployment.md`.

## App Entry Points

- `fins2026/week3/app/streamlit_app.py`: primary Australia deployment target
- `fins2026/week3/us_app/streamlit_app.py`: companion U.S. macro app in the
  same repo
- The Australia app uses the richer benchmark pipeline. The U.S. app keeps the
  transparent baseline stress, curve, forecast, backtest, and GDP views.

## Module Map

- `app_config.py`: app labels, view options, model labels, and control defaults
- `app_data.py`: cached bundle loading, sample windows, source-status text, and
  cached benchmark/model outputs
- `app_insights.py`: snapshot tables, line charts, formatting helpers, and
  forecast/backtest interpretation text
- `app_views.py`: Streamlit rendering, controls, tabs, tables, and downloads
- `streamlit_app.py`: repo bootstrap and `main()` entrypoint
- `code/forecast_data.py`: Australia and U.S. input-panel builders
- `code/forecast_specs.py`: target metadata and week-specific series choices
- `code/forecast_pipeline.py`: exogenous feature engineering, model execution,
  and benchmark output writing
- `code/beginner_forecasting.py`: the beginner Week 3 lecture helpers for the
  Australia ladder plus the U.S. extension ladder
- `us_app/app_config.py`: U.S. app labels, specs, and options
- `us_app/app_data.py`: cached FRED and fixture loading for the U.S. app
- `us_app/app_insights.py`: U.S. stress, curve, GDP, and forecast helpers
- `us_app/app_views.py`: U.S. Streamlit rendering, controls, tabs, and downloads

## Working Rules

- Treat `data/` as committed source inputs only.
- Treat `results/data/` and `results/forecasts/` as derived outputs.
- Keep app-specific logic in `app/` unless it clearly belongs in `fintools/`.
- Use fixture mode first, then verify that live mode fails gracefully.
- Refresh `guidance/` with `python tools/workflow.py build-week-context --target fins2026/week3`
  after major Week 3 changes.

Week 2 still owns the first supported deployment walkthrough. Week 3 reuses the
same Streamlit deployment workflow while now carrying both the Australia
forecast monitor and the U.S. companion app in one package. For teaching,
students should usually start with `BEGINNER_FORECASTING.md` before opening the
full Week 3 app.

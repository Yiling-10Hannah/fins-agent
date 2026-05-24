# Week 3 U.S. Beginner Forecasting Extension

Use this only after the main Australia Week 3 ladder makes sense.

This guide mirrors the same forecasting workflow on a second market. The goal
is not to build a second main lecture. The goal is to show that the same logic
can be reused on a simple U.S. monthly macro target.

## Aim

The U.S. extension keeps the same teaching sequence:

1. choose a target
2. test whether the level should be transformed
3. build a naive benchmark
4. add AR structure
5. add ARMA structure
6. add one outside variable, then a second one
7. compare the models on target out-of-sample performance

The U.S. lecture target is:

- U.S. unemployment rate
- forecast target: monthly change in unemployment rate

By default, the U.S. extension uses the same split as Australia:

- in sample through `2019-12-31`
- out of sample from `2020-01-31` onward

The first outside variables are:

- last month's federal-funds change
- last month's 10Y-2Y yield spread

## Default Extension Path

Run these only after the Australia core path:

1. `make_us_beginner_forecasting_series.py`
2. `run_us_beginner_unit_root_check.py`
3. `run_us_beginner_naive_forecast.py`
4. `run_us_beginner_ar_forecast.py`
5. `run_us_beginner_arma_forecast.py`
6. `run_us_beginner_arx_forecast.py`
7. `run_us_beginner_model_horse_race.py`
8. `make_us_beginner_forecast_story_figures.py`
9. then optionally open the U.S. app

## Script Order

Windows:

```powershell
.\.venv\Scripts\python.exe fins2026\week3\scripts\make_us_beginner_forecasting_series.py
.\.venv\Scripts\python.exe fins2026\week3\scripts\run_us_beginner_unit_root_check.py
.\.venv\Scripts\python.exe fins2026\week3\scripts\run_us_beginner_naive_forecast.py
.\.venv\Scripts\python.exe fins2026\week3\scripts\run_us_beginner_ar_forecast.py
.\.venv\Scripts\python.exe fins2026\week3\scripts\run_us_beginner_arma_forecast.py
.\.venv\Scripts\python.exe fins2026\week3\scripts\run_us_beginner_arx_forecast.py
.\.venv\Scripts\python.exe fins2026\week3\scripts\run_us_beginner_model_horse_race.py
.\.venv\Scripts\python.exe fins2026\week3\scripts\make_us_beginner_forecast_story_figures.py
```

macOS/Linux:

```bash
./.venv/bin/python fins2026/week3/scripts/make_us_beginner_forecasting_series.py
./.venv/bin/python fins2026/week3/scripts/run_us_beginner_unit_root_check.py
./.venv/bin/python fins2026/week3/scripts/run_us_beginner_naive_forecast.py
./.venv/bin/python fins2026/week3/scripts/run_us_beginner_ar_forecast.py
./.venv/bin/python fins2026/week3/scripts/run_us_beginner_arma_forecast.py
./.venv/bin/python fins2026/week3/scripts/run_us_beginner_arx_forecast.py
./.venv/bin/python fins2026/week3/scripts/run_us_beginner_model_horse_race.py
./.venv/bin/python fins2026/week3/scripts/make_us_beginner_forecast_story_figures.py
```

## What Each Step Teaches

`make_us_beginner_forecasting_series.py`

- writes one clean U.S. unemployment-rate CSV
- writes one compact U.S. macro panel
- writes the deterministic simulated-series CSV used in the unit-root check

`run_us_beginner_unit_root_check.py`

- compares stationary and non-stationary simulated series
- runs a basic ADF test
- shows why the U.S. unemployment level becomes a monthly-change target

`run_us_beginner_naive_forecast.py`

- builds the simplest U.S. forecast benchmark
- keeps the one-step rolling evaluation visible
- evaluates the target directly

`run_us_beginner_ar_forecast.py`

- introduces AR(1) on the U.S. target
- shows a small lag ladder with BIC
- compares naive, AR(1), and the selected AR model

`run_us_beginner_arma_forecast.py`

- adds moving-average terms
- keeps the order search small and visible
- compares naive, AR, and ARMA on the same evaluation window

`run_us_beginner_arx_forecast.py`

- keeps the same unemployment-change target
- adds lagged federal-funds change first
- then adds the lagged yield spread

`run_us_beginner_model_horse_race.py`

- compares the U.S. extension models on the same target evaluation window
- ranks models by target RMSE
- reports target MAE, target RMSE, target MASE, and target out-of-sample R-squared

`make_us_beginner_forecast_story_figures.py`

- rebuilds the U.S. results as FT-style narrative figures
- shows the level-versus-change logic, the winner scorecard, and the latest forecast
- mirrors the Australia story pack on a second market

## Output Paths

Source CSVs:

```text
fins2026/week3/results/data/us_beginner_forecasting/
```

Teaching figures:

```text
fins2026/week3/results/figures/us_beginner_forecasting/
```

Teaching tables:

```text
fins2026/week3/results/tables/us_beginner_forecasting/
```

Story figures and tables:

```text
fins2026/week3/results/figures/us_beginner_forecast_story/
fins2026/week3/results/tables/us_beginner_forecast_story/
```

## Teaching Point

This is a mirror extension, not a separate main lecture.

The intended message is:

1. the workflow travels across countries
2. the target-first logic stays the same
3. the benchmark-first discipline stays the same
4. target-space out-of-sample evaluation still decides the winner

Only after that should students move to the U.S. companion app.

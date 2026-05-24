# Week 3 Beginner Forecasting

Start here if students are new to forecasting code.

The Week 3 app is the finished product. This guide is the beginner ladder that
explains where the forecast ideas come from before students open the full app.

## This Week's Aim

The aim is to teach one clean forecasting workflow, not to rush through every
possible model.

Students should finish Week 3 able to say:

1. what target they are forecasting
2. why they transformed that target
3. what the naive benchmark is
4. whether a richer model beats the benchmark out of sample
5. how the finished app fits on top of that logic

Keep the first pass narrow on purpose:

1. create the lecture source tables
2. check whether a level series looks stationary
3. build a naive benchmark
4. upgrade to an autoregression
5. upgrade again to a small ARMA ladder
6. add one outside variable with ARX
7. add shocks plus outside variables with ARMAX
8. expand into a small hand-picked OLS regression
9. expand again into a larger elastic-net feature bank
10. run a full horse race across the lecture models
11. compare the winner with a simple equal-weight ensemble

The real lecture anchor is the Australia unemployment rate. It is intuitive,
monthly, and long enough to show why we usually model the monthly change rather
than the raw level.

By default, the lecture scripts use a fixed split:

- in sample through `2019-12-31`
- out of sample from `2020-01-31` onward

## Default Run Path

Treat this as the default in-class sequence:

1. `make_beginner_forecasting_series.py`
2. `run_beginner_unit_root_check.py`
3. `run_beginner_naive_forecast.py`
4. `run_beginner_ar_forecast.py`
5. `run_beginner_arma_forecast.py`
6. `run_beginner_arx_forecast.py`
7. `run_beginner_model_horse_race.py`
8. `make_beginner_forecast_story_figures.py`
9. open the Australia app

The scripts below still matter, but they are extensions rather than the
minimum live lecture path:

- `run_beginner_armax_forecast.py`
- `run_beginner_ols_forecast.py`
- `run_beginner_enet_forecast.py`
- `run_beginner_ensemble_forecast.py`
- `make_beginner_forecast_story_figures.py`

## The Script Order

Windows:

```powershell
.\.venv\Scripts\python.exe fins2026\week3\scripts\make_beginner_forecasting_series.py
.\.venv\Scripts\python.exe fins2026\week3\scripts\run_beginner_unit_root_check.py
.\.venv\Scripts\python.exe fins2026\week3\scripts\run_beginner_naive_forecast.py
.\.venv\Scripts\python.exe fins2026\week3\scripts\run_beginner_ar_forecast.py
.\.venv\Scripts\python.exe fins2026\week3\scripts\run_beginner_arma_forecast.py
.\.venv\Scripts\python.exe fins2026\week3\scripts\run_beginner_arx_forecast.py
.\.venv\Scripts\python.exe fins2026\week3\scripts\run_beginner_armax_forecast.py
.\.venv\Scripts\python.exe fins2026\week3\scripts\run_beginner_ols_forecast.py
.\.venv\Scripts\python.exe fins2026\week3\scripts\run_beginner_enet_forecast.py
.\.venv\Scripts\python.exe fins2026\week3\scripts\run_beginner_model_horse_race.py
.\.venv\Scripts\python.exe fins2026\week3\scripts\run_beginner_ensemble_forecast.py
.\.venv\Scripts\python.exe fins2026\week3\scripts\make_beginner_forecast_story_figures.py
```

macOS/Linux:

```bash
./.venv/bin/python fins2026/week3/scripts/make_beginner_forecasting_series.py
./.venv/bin/python fins2026/week3/scripts/run_beginner_unit_root_check.py
./.venv/bin/python fins2026/week3/scripts/run_beginner_naive_forecast.py
./.venv/bin/python fins2026/week3/scripts/run_beginner_ar_forecast.py
./.venv/bin/python fins2026/week3/scripts/run_beginner_arma_forecast.py
./.venv/bin/python fins2026/week3/scripts/run_beginner_arx_forecast.py
./.venv/bin/python fins2026/week3/scripts/run_beginner_armax_forecast.py
./.venv/bin/python fins2026/week3/scripts/run_beginner_ols_forecast.py
./.venv/bin/python fins2026/week3/scripts/run_beginner_enet_forecast.py
./.venv/bin/python fins2026/week3/scripts/run_beginner_model_horse_race.py
./.venv/bin/python fins2026/week3/scripts/run_beginner_ensemble_forecast.py
./.venv/bin/python fins2026/week3/scripts/make_beginner_forecast_story_figures.py
```

## What Each Step Teaches

`make_beginner_forecasting_series.py`

- writes one clean unemployment-rate CSV
- writes one deterministic simulated-series CSV
- gives students a stable starting point before they fit any model

`run_beginner_unit_root_check.py`

- compares stationary and non-stationary simulated series
- runs a basic ADF test
- shows why the unemployment level becomes a monthly-change target

`run_beginner_naive_forecast.py`

- builds the simplest forecast benchmark
- shows one-step rolling evaluation
- converts forecasted changes back into an implied unemployment-rate path

`run_beginner_ar_forecast.py`

- introduces AR(1)
- shows a tiny lag ladder with BIC
- compares naive, AR(1), and the selected AR model

`run_beginner_arma_forecast.py`

- adds moving-average terms
- keeps the order search small and visible
- compares naive, AR, and ARMA on the same 2020-onward evaluation window

`run_beginner_arx_forecast.py`

- keeps the same unemployment-change target
- adds last month's cash-rate change first
- then adds last month's commodity-price log change as a second outside signal

`run_beginner_armax_forecast.py`

- keeps the selected ARMA backbone
- adds the same lagged outside variables
- shows the final step before the richer app benchmark surface

`run_beginner_ols_forecast.py`

- introduces a small hand-picked dynamic regression
- keeps the same unemployment-change target and target lags
- shows how lagged outside variables become ordinary regression predictors

`run_beginner_enet_forecast.py`

- keeps the regression setup but expands the predictor bank
- uses shrinkage to handle overlapping signals
- prepares students for the richer multi-predictor benchmark surface in the app

`run_beginner_model_horse_race.py`

- compares the full lecture ladder on the same target evaluation window
- ranks models by target RMSE
- reports target MAE, target RMSE, target MASE, and target out-of-sample R-squared

`run_beginner_ensemble_forecast.py`

- averages the successful non-naive forecasts
- compares the equal-weight ensemble with the naive benchmark and the horse-race winner
- keeps the evaluation in target space

`make_beginner_forecast_story_figures.py`

- turns the model outputs into FT-style narrative figures
- shows the level-versus-change logic, the scorecard, the out-of-sample fit, and the latest forecast
- is the bridge from model code to the finished Week 3 app story

## Output Paths

Source CSVs:

```text
fins2026/week3/results/data/beginner_forecasting/
```

Teaching figures:

```text
fins2026/week3/results/figures/beginner_forecasting/
```

Teaching tables:

```text
fins2026/week3/results/tables/beginner_forecasting/
```

Story figures and tables:

```text
fins2026/week3/results/figures/beginner_forecast_story/
fins2026/week3/results/tables/beginner_forecast_story/
```

## Teaching Point

Do not jump straight from a macro time series to a large forecast dashboard.

The Week 3 beginner ladder is:

1. look at the series
2. decide whether the level is appropriate
3. build a naive benchmark
4. add AR structure
5. add ARMA structure
6. ask whether outside information helps
7. turn the forecasting idea into a regression
8. use shrinkage when the predictor bank gets wider
9. compare the model families directly
10. test whether a simple ensemble helps
11. only then move toward richer benchmark products

Only after that should students move on to the full Week 3 app.

If an AI assistant helps with Week 3, it should default to the in-class path
first and only expand into ARMAX, OLS, ENet, or ensemble work when the student
asks for the extension layer.

If the student explicitly wants the same workflow on U.S. data, move to:

- `US_BEGINNER_FORECASTING.md`
- the `run_us_beginner_*` scripts

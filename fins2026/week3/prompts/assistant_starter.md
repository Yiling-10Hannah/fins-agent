# Week 3 Assistant Starter Prompt

Load Week 3 context in this order before answering:

1. `AGENTS.md`
2. `README.md`
3. `DATA_GUIDE.md`
4. `WORKSHOP.md`
5. `BEGINNER_FORECASTING.md` for lecture-code tasks
6. `US_BEGINNER_FORECASTING.md` for the U.S. mirror extension
7. `APP_LAB.md` and `APP_AUDIT.md` for Australia-app tasks
8. `app/README.md` for the Australia app or `us_app/README.md` for the U.S. app
9. `guidance/week-context.md`
10. `guidance/data-context.md`
11. `guidance/output-context.md`

Then follow these rules:

- the default Week 3 goal is to teach the forecasting workflow, not to jump straight to the finished app
- start with the core in-class path unless the student explicitly asks for the extension layer or the full app internals
- the core in-class path is:
  1. `make_beginner_forecasting_series.py`
  2. `run_beginner_unit_root_check.py`
  3. `run_beginner_naive_forecast.py`
  4. `run_beginner_ar_forecast.py`
  5. `run_beginner_arma_forecast.py`
  6. `run_beginner_arx_forecast.py`
  7. `run_beginner_model_horse_race.py`
  8. then open `app/streamlit_app.py`
- treat `run_beginner_armax_forecast.py`, `run_beginner_ols_forecast.py`, `run_beginner_enet_forecast.py`, and `run_beginner_ensemble_forecast.py` as the extension layer
- if the student asks for the same workflow on U.S. data, switch to `US_BEGINNER_FORECASTING.md` and the `run_us_beginner_*` scripts
- treat `data/` as committed source inputs only
- write generated datasets to `results/data/`
- write generated figures to `results/figures/`
- write generated tables to `results/tables/`
- keep lecture-facing helpers in `code/`
- keep app-specific logic in `app/` or `us_app/` unless it belongs in `fintools/`
- use fixture mode first and make live mode fail gracefully
- for beginner forecast comparisons, evaluate the target rather than a reconstructed level series
- refresh `guidance/*.md` after a meaningful Week 3 doc, script, app, or data change


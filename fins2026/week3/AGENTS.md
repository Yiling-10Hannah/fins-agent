# Weekly Overlay

This folder is `fins2026/week3`.

Week 3 now has three distinct surfaces:

- a beginner forecasting ladder for lecture code
- a primary Australia macro forecast app
- a companion U.S. macro app

Do not treat Week 3 as a single app-only folder.

## Read First

Load these files first for any Week 3 task:

- `README.md`
- `WORKSHOP.md`
- `DATA_GUIDE.md`
- `guidance/week-context.md`
- `guidance/data-context.md`
- `guidance/output-context.md`

Then branch by task:

- Beginner lecture code:
  - `BEGINNER_FORECASTING.md`
  - `code/beginner_forecasting.py`
- U.S. beginner extension:
  - `US_BEGINNER_FORECASTING.md`
  - `code/beginner_forecasting.py`
- Australia app:
  - `APP_LAB.md`
  - `APP_AUDIT.md`
  - `app/README.md`
- U.S. companion app:
  - `us_app/README.md`

## Working Rules

- Keep week-specific work inside this folder.
- Use `data/` for committed source inputs only.
- Use `results/data/`, `results/figures/`, and `results/tables/` for generated outputs.
- Keep canonical rerunnable scripts in `scripts/`.
- Keep lecture-facing helper logic in `code/` when students need to read it directly.
- Keep Australia app-specific logic in `app/` and U.S. app-specific logic in `us_app/` unless it clearly belongs in `fintools/`.
- Use `scratch/` for disposable experiments, not the final path.
- For beginner forecasting comparisons, evaluate the forecast target, not a reconstructed level path.
- Default to the core in-class path before suggesting the extension ladder or the full benchmark pipeline.
- Treat the U.S. beginner ladder as a mirror extension after the Australia core path, not as a second default lecture start.
- Regenerate `guidance/*.md` after the week docs, scripts, app, or data change.

## Useful Commands

- `python fins2026/week3/scripts/run_week.py`
- `python fins2026/week3/scripts/run_beginner_model_horse_race.py`
- `python fins2026/week3/scripts/run_beginner_ensemble_forecast.py`
- `python fins2026/week3/scripts/run_us_beginner_model_horse_race.py`
- `python fins2026/week3/scripts/describe_data.py`
- `python fins2026/week3/scripts/run_forecast_benchmarks.py --use-fixture`
- `streamlit run fins2026/week3/app/streamlit_app.py`
- `streamlit run fins2026/week3/us_app/streamlit_app.py`
- `python tools/workflow.py build-week-context --target fins2026/week3`


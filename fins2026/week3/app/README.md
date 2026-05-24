# Week 3 Australia Macro Forecast App

This is the primary Week 3 product surface. The app keeps Australian macro data
as the forecast target set and U.S. data as secondary context plus exogenous
input. A separate companion U.S. app now lives at `../us_app/README.md`.

Run locally from the repo root:

```bash
python fins2026/week3/scripts/run_forecast_benchmarks.py --use-fixture
streamlit run fins2026/week3/app/streamlit_app.py
```

Keep the terminal open while using the app locally. Closing it stops the local
server behind `localhost:8501`.

Default mode uses the frozen Week 3 fixture bundle. Live mode rebuilds the
Australia RBA and U.S. FRED inputs, then falls back to the fixture if that
refresh fails.

Use the `Sample period` segmented control to change the analysis window. The
selection controls the visible history, benchmark comparisons, backtests, and
downloads.

The app is split into small modules so the Streamlit entrypoint remains easy to
audit:

- `app_config.py`: labels, series specs, and option lists
- `app_data.py`: bundle loading, sample-window filtering, source-status text,
  and cached benchmark/model outputs
- `app_insights.py`: snapshot tables, figures, and forecast/backtest
  interpretation helpers
- `app_views.py`: Streamlit controls, tabs, tables, and downloads
- `streamlit_app.py`: repo bootstrap and `main()` entrypoint

This Week 3 version keeps its own committed Australia Stage 1 fixture so the
standalone deploy bundle can boot without importing another week's modules.

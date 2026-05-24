# Week 3 U.S. Macro App

This companion Week 3 app keeps the U.S. macro stress and forecasting product
available alongside the Australia forecast monitor. It focuses on Treasury
yields, credit spreads, volatility, and real GDP using public FRED data.

If the student wants a lecture-style U.S. forecasting walkthrough before
opening this app, use:

- `fins2026/week3/US_BEGINNER_FORECASTING.md`

Run locally from the repo root:

```bash
streamlit run fins2026/week3/us_app/streamlit_app.py
```

Keep the terminal open while using the app locally. Closing it stops the local
server behind `localhost:8501`.

Default mode uses frozen validation fixtures. Live mode pulls current FRED
graph CSV data and falls back to the fixture if that refresh fails.

Use the `Sample period` segmented control to change the analysis window. The
selection controls the metrics, charts, forecasts, backtests, and downloads.

The app is split into small modules so the Streamlit entrypoint remains easy to
audit:

- `app_config.py`: labels, series specs, and option lists
- `app_data.py`: FRED, fixture, sample-window, and source-status helpers
- `app_insights.py`: stress, yield-curve, GDP, forecasting, and plotting logic
- `app_views.py`: Streamlit controls, tabs, tables, and downloads
- `streamlit_app.py`: repo bootstrap and `main()` entrypoint

To prepare a standalone rehearsal bundle for this entrypoint, run from the repo
root:

```bash
python tools/workflow.py prepare-app-repo --source fins2026/week3 --dest ../week3-us-macro --repo week3-us-macro --entrypoint fins2026/week3/us_app/streamlit_app.py
```

The Australia app remains the primary Week 3 deployment target. This U.S. app
is the documented companion entrypoint in the same Week 3 package.

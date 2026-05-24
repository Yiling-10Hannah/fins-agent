# Week 3 App Lab: Australia-First Forecasting Extension

Week 3 now carries two app entrypoints in the same folder: the primary
Australia forecast product and a companion U.S. macro app. This lab remains
focused on the Australia forecasting build, which keeps the same modular app
pattern but asks a different product question: how should we structure an
Australia-first forecast lab that respects release timing, compares model
families transparently, and still keeps U.S. data in view?

This lab builds and inspects an app that:

- loads Australia observable panels plus U.S. month-end context through fixture
  or live mode
- keeps the product split across Overview, Australia Snapshot, Forecasts, Model
  Comparison, Backtests, U.S. Context, Data, and Methodology views
- benchmarks naive, drift, AR, ARMA, ARMA + exogenous, and elastic-net
  regression models
- plots history plus forecast paths with explicit target transforms
- reports one-step benchmark errors in a student-facing way
- explains why exogenous models stay one-step only in v1

Run from the repo root:

```bash
python fins2026/week3/scripts/build_forecast_inputs.py --use-fixture
python fins2026/week3/scripts/run_forecast_benchmarks.py --use-fixture
streamlit run fins2026/week3/app/streamlit_app.py
```

Use fixture mode first. Use live mode only when you have internet access and
want fresh RBA/FRED inputs.

## Extension Rules

- Keep the sidebar for global data-source selection only.
- Keep forecast-series, model, and horizon controls inside the views they
  affect.
- Do not blindly forecast levels. Forecast rates and unemployment as changes,
  external-sector indices as log changes, and GDP through annualized quarterly
  growth.
- Treat Australia as the primary product question and U.S. data as context plus
  selected exogenous input.
- Keep the selected sample window visible because it affects the benchmark
  comparisons and the displayed history.
- Use Streamlit math support for model equations in the Methodology view.

## What To Compare With Week 2

- Week 2: one simple month-end app and the first deployment path.
- Week 3: multiple views, richer interpretation, benchmarked model families,
  saved backtests, and explicit release-lag handling.
- Week 2 introduces deployment. Week 3 focuses on product depth and forecast
  discipline.

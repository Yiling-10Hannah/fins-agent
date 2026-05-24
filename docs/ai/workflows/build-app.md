# Build App Workflow

## Use When

Use when a student wants to create, improve, test, or deploy a Streamlit app
from coursework data or analysis.

Deterministic helper:

```bash
python tools/workflow.py build-app --target projects/my_project --title "My App"
```

For a new project with an app:

```bash
python tools/workflow.py new-project my_project --with-app --description "..."
```

Before hand-in, run:

```bash
python tools/workflow.py check-app-submission --target projects/my_project
```

To create and push a clean private deploy repo from a course workspace, run:

```bash
python tools/workflow.py prepare-app-repo --source projects/my_project --dest ../my_project_handin --repo my_project_handin --push
```

## Required Context

- `AGENTS.md`
- `docs/apps/streamlit/`
- current week folder or project folder
- data source or dataframe context
- deployment target, normally Streamlit Community Cloud

## Procedure

1. Identify the app's product question and audience.
2. Put reusable data/model logic in pure functions.
3. For forecast products, define series metadata before modeling. Use
   `SeriesSpec`, `forecast_series_spec`, and `rolling_backtest_spec` unless the
   app has a domain-specific model. Decide explicitly whether each series is a
   level, change, growth rate, or not forecastable.
4. Build `app/streamlit_app.py` with cached data loading, sidebar controls,
   metric cards, a data-health strip, URL-shareable state, lazy tabs, typed
   tables, downloads, and interactive figures.
5. Keep generated screenshots or app outputs in `results/app/`.
6. Add or update an app README with local run and deployment instructions.
7. Keep `SUBMISSION_CHECKLIST.md` as the human deployment signoff sheet. An
   optional `submission.json` is fine for metadata, but students should not
   need it to run, push, or deploy the app.
8. Run or recommend `check-app-submission` before hand-in so students get the
   exact Streamlit deploy fields and blocking issues.
9. When a student asks to deploy or prep an app from the course workspace, default
   to `prepare-app-repo --push` so a fresh private GitHub deploy repo is created
   and pushed unless the student explicitly asks for a local-only rehearsal.
10. For an existing or deployed app, run the `audit-app` workflow before broad
   refactors so product, state, testing, and deployment issues are captured in
   priority order.
11. Add a smoke test using `streamlit.testing.v1.AppTest` when Streamlit is
   installed.
12. Verify no local absolute paths or committed secrets are present.

## Standards

- Use Streamlit for the app shell and Plotly for interactive charts.
- Use the shared `fintools.apps` helpers before writing bespoke app boilerplate:
  query-param state, lazy tabs, data-health panels, metric strips, typed tables,
  downloads, and Plotly app figures.
- For URL-shareable tabs, initialize the tab from the URL only once per browser
  session, then let `st.session_state` own tab clicks. Re-reading a changing
  `?view=` value as `st.tabs(default=...)` on every rerun can cause first-click
  tab bounce.
- Use `st.cache_data(ttl=86400)` for API calls and loaded data.
- Keep global controls in the sidebar, but place model-specific or
  chart-specific controls beside the tab or view they affect.
- Run `streamlit run ...` from the repo root.
- Run `python tools/workflow.py check-app-submission --target ...` before
  deployment or final submission.
- Use `python tools/workflow.py prepare-app-repo --source ... --dest ... --push`
  by default for fresh private deploy repos. Drop `--push` only when the user
  explicitly wants a local-only rehearsal bundle.
- Default final-project workflow is a private student-owned GitHub repo during
  development, regular pushes, a public Streamlit app URL at hand-in, and
  GitHub repo access for the teaching team.
- Do not commit `.streamlit/secrets.toml`.
- Forecast apps must include target-transform language, uncertainty language,
  and a backtest or caveat.
- Do not render long method labels, target names, formulas, or caveats as large
  metric values. Use compact KPI cards, captions, or a Method tab.
- Render equations with Streamlit math support, such as `st.latex` or Markdown
  LaTeX delimiters. Do not show code-style formulas when the app is explaining
  finance or forecasting methods.
- Visible app copy must be client-facing. Avoid internal phrasing such as
  "This app...", "so the user can...", and implementation jargon.
- Visible metrics and table headers must include units or denominations where
  values are not self-explanatory.
- Composite indicators must include direction, unit, comparison window, and a
  current or recent reading. Interpret percentiles in words instead of showing
  a bare percentile label.
- If a composite indicator is standardized against a selected sample, include
  the comparison window in the visible metric label and explain that the value
  can change when the sample changes.
- If a current composite reading is a rolling average, compute its percentile
  against historical rolling averages that use the same window.
- Current market and macro metrics must state the actual latest observation
  date behind each reading, especially when mixed-frequency FRED series appear
  together.
- Sort time-series indexes before plotting. If a line chart has diagonal
  segments across the plotting area, diagnose date ordering before changing
  styling.
- Rates, yield spreads, and credit OAS should usually forecast changes, then
  show implied level paths. GDP-style fundamentals should usually forecast
  growth. VIX-style context series should not be forecast with simple
  baseline models by default.
- Domain tabs must answer the client question directly. Yield-curve views
  should interpret slope, inversion, flattening, or steepening; GDP views
  should interpret latest quarterly growth, year-over-year growth,
  forecast-implied level change, release lags, and revision risk.
- Time-series apps should use range controls, unified hover, and NBER recession
  shading when showing U.S. macro data. If a chart has a legend, use a range
  slider instead of range selector buttons so controls never overlap labels.
- Log-scale app charts must use human-readable tick labels and enough axis
  margin so labels are never clipped or visually ambiguous.
- Short presentation tables should use compact dynamic heights and should not
  show empty grid rows below the actual data.
- Method tabs for deterministic baseline models should include concrete model
  equations.
- App tests should exercise every tab or active view. Default-tab smoke tests
  are not enough because hidden tabs can still contain Streamlit runtime errors.

# Week 3 Streamlit App Audit

Audit date: 2026-04-20

Benchmarked against current Streamlit 1.56 documentation for stateful tabs,
session state, query parameters, caching, forms, fragments, dataframes,
AppTest, secrets, configuration, and Community Cloud deployment.

Primary app entrypoint: `fins2026/week3/app/streamlit_app.py`

## Summary

The current Week 3 Australia-first forecast app is above the baseline expected
for a coursework Streamlit app. It uses cached data loading, a committed
fixture benchmark leaderboard for the default sample, typed tables, stable
URL-backed lazy tabs, app-facing labels, client-facing interpretation, and
rendered equations. There are no obvious blocking defects in the current
source.

The first remediation pass now covers the top three audit actions: every app
view has a content-aware `AppTest` smoke path, the source-status line separates
fixture freshness from live FRED cache time, and the app is split into focused
configuration, data, insight, and view modules. The main remaining gaps are a
repeatable visual/layout regression check, forecast/backtest output caching,
and heavier use of forms or fragments for expensive model controls.

## Implemented Remediation

- UI smoke coverage now loops through Overview, Australia Snapshot, Forecasts,
  Model Comparison, Backtests, U.S. Context, Data, and Methodology with
  explicit query parameters and rendered-content assertions.
- The top-of-app data strip now reports either live RBA + FRED cache timing or
  the active fixture snapshot.
- `streamlit_app.py` remains a thin entrypoint. App configuration lives in
  `app_config.py`, loading and source status in `app_data.py`, Australia/U.S.
  insight logic in `app_insights.py`, and Streamlit rendering in `app_views.py`.

## What Already Meets Current Practice

- Page configuration is centralized through `configure_page`.
- FRED downloads and fixture loading use `st.cache_data(ttl=86400)`, matching
  Streamlit's guidance to cache API calls and data loading.
- Hidden expensive tab views use stateful tabs through the shared `lazy_tabs`
  helper. The helper now uses URL state only for first-load tab selection and
  `st.session_state` for later clicks.
- URL query params are validated before use.
- Current metrics state dates, units, comparison windows, and interpretation.
- Short tables use dynamic heights and Streamlit `column_config`.
- Figures use Plotly with unified hover, recession shading where useful, and
  range controls that avoid legend overlap.
- The Method tab uses `st.latex` instead of code-style equations.
- Live FRED failures degrade to fixture data rather than crashing.
- The app avoids committed secrets and uses repo-root `.streamlit/config.toml`
  for deployment-compatible configuration.

## Findings

### High - UI Runtime Coverage Is Too Thin

Surface: `fins2026/week3/app/tests/test_app_smoke.py`, `tests/test_apps.py`

Observed: The Streamlit `AppTest` smoke test now renders each active view with
validated `view` and `sample` query params and checks key rendered text plus
the source-status line. It is still skipped by default on native Windows
because Streamlit's test harness can leave locked temp files; Linux CI or the
`RUN_STREAMLIT_APPTEST_ON_WINDOWS=1` override can run it.

Impact: Hidden Streamlit runtime errors, tab state regressions, layout changes,
or widget identity problems can slip through local Windows development.

Fix: Wire the existing `AppTest` smoke test into a Linux CI path. Add a second
stateful case for one non-default forecast model when CI runtime is available.

Shared lesson: App tests should cover every tab or active view, with query
params and non-default widget states.

### High - No Automated Visual/Layout Regression Check

Surface: charts, tabs, metric strips, tables

Observed: Earlier defects included overlapping Plotly range controls and empty
table rows. Current unit tests check some Plotly layout properties, but there
is no screenshot or browser-level check for desktop/mobile visual regressions.

Impact: Streamlit apps can pass Python tests while still looking broken in the
browser.

Fix: Add a manual or automated visual audit step for final app reviews:
desktop width, narrow laptop width, and mobile-ish width. If automation is
available, use Playwright screenshots against a running local app; otherwise
record a checklist in the audit report.

Shared lesson: Layout regressions are product bugs, not cosmetic afterthoughts.

### Implemented - `streamlit_app.py` Module Boundary

Surface: `fins2026/week3/app/streamlit_app.py`

Observed: The previous single-file app mixed data loading, forecasting glue,
stress logic, yield-curve logic, GDP interpretation, plotting helpers,
controls, and tab rendering. This has been split into focused local modules.

Impact: Future student edits can now target smaller files and pure helper
logic can be tested without importing the whole Streamlit view layer.

Fix: Keep this as the standing pattern once a coursework app grows beyond a
short single-page prototype:

- `app_config.py`: labels, series specs, and option lists
- `app_data.py`: FRED, fixture, sample-window, and source-status helpers
- `app_insights.py`: stress, yield-curve, GDP, forecasting, and plotting logic
- `app_views.py`: Streamlit controls, tabs, tables, and downloads
- `streamlit_app.py`: repo bootstrap and `main()` entrypoint

Shared lesson: Keep `streamlit_app.py` as the orchestration layer once helpers
grow beyond one screen.

### Medium - Heavy Controls Still Trigger Full App Reruns

Surface: Forecasts, Backtests, GDP Outlook

Observed: Forecast series/model/horizon controls are normal widgets. With lazy
tabs, only the active tab renders, but every control change still reruns the
full script and rebuilds shared top-of-page state.

Impact: The app is fast enough now, but the pattern will become sluggish in
student apps with larger datasets or slower models.

Fix: Use `st.form` when users should choose several parameters before updating
a model. Use `st.fragment` for self-contained forecast or live-monitor panels
that can rerun independently. Keep shared results in `st.session_state` when a
fragment must communicate with the full app.

Shared lesson: Cache avoids repeated computation; forms batch user input;
fragments reduce rerun scope. Use the right tool for the bottleneck.

### Medium - Forecast And Backtest Results Are Not Cached

Surface: `forecast_and_backtest`, GDP forecast path

Observed: Data loading is cached, but forecast/backtest outputs are recomputed
when their tab renders. This is acceptable for current fixtures but not ideal
as a reusable pattern.

Impact: Larger apps or slower models will feel laggy, especially when users
change tabs or sample periods repeatedly.

Fix: Add a cacheable model-output layer keyed by series identifier, sample
window, model, horizon, and target specification. Keep cache invalidation
simple and avoid caching objects that include live Streamlit elements.

Shared lesson: Cache data and deterministic model outputs separately.

### Medium - Data Freshness Can Be Even More Explicit

Surface: Overview, Data tab, live/fixture source state

Observed: Current metrics show latest observation dates, and the data-health
strip shows the sample span. The app does not show the live data retrieval
time or fixture build date.

Impact: Users can understand the latest FRED observation, but not when the app
last attempted to refresh live data or how stale the fixture itself is.

Fix: Add a small source-status line:

- live mode: "Live FRED loaded at HH:MM local time; latest observation ..."
- fixture mode: "Fixture snapshot through YYYY-MM-DD"

Shared lesson: Latest observation date and app refresh date are different
concepts; show both when using cached live data.

### Low - KPI Cards Use Controlled HTML

Surface: `render_compact_metric_strip`

Observed: The shared compact metric helper uses `unsafe_allow_html=True` for
controlled card typography. The values are generated by the app, not entered
by users.

Impact: This is low risk in the current app, but it should not become a habit
for untrusted text.

Fix: Keep the invariant that metric values are app-generated. If student apps
display user-uploaded or API-provided strings in metric cards, escape them or
use native Streamlit text elements.

Shared lesson: Custom HTML is acceptable only when inputs are controlled and
there is a clear UI need.

### Low - Week 3 Deployment Position Should Stay Explicit

Surface: `fins2026/week3/app/README.md`, `APP_LAB.md`

Observed: Week 3 is an extension week, not the primary deployment rehearsal.
Readers still need an explicit statement that the first supported deployment
path lives in Week 2.

Impact: Students can confuse "richer app" with "main deployment path" and look
for a Week 3 submission manifest that does not exist.

Fix: Keep the Week 3 docs explicit that deployment belongs to Week 2 unless a
separate Week 3 submission manifest is intentionally added later.

Shared lesson: Keep the hand-in week and the extension week distinct in public
docs.

## Improvement Backlog

Immediate:

- Enable the existing view-by-view `AppTest` smoke test in Linux CI.
- Add a second `AppTest` case for a non-default forecast model and horizon.
- Add a repeatable desktop/narrow-screen visual audit step.

Next iteration:

- Cache deterministic forecast/backtest results.
- Use forms or fragments for heavy parameter panels.

Optional polish:

- Add per-series FRED links in the Data tab or latest-readings table.
- Add selectable table rows or drill-down only if it supports a real workflow.
- Add model-comparison cards if the assignment moves beyond baseline models.

## Streamlit Docs Used For Benchmarking

- `st.tabs`: <https://docs.streamlit.io/develop/api-reference/layout/st.tabs>
- Session state:
  <https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state>
- Query params:
  <https://docs.streamlit.io/develop/api-reference/caching-and-state/st.query_params>
- Caching: <https://docs.streamlit.io/develop/concepts/architecture/caching>
- Forms: <https://docs.streamlit.io/develop/concepts/architecture/forms>
- Fragments: <https://docs.streamlit.io/develop/concepts/architecture/fragments>
- App testing: <https://docs.streamlit.io/develop/concepts/app-testing>
- Dataframes:
  <https://docs.streamlit.io/develop/api-reference/data/st.dataframe>
- Secrets:
  <https://docs.streamlit.io/develop/concepts/connections/secrets-management>
- Community Cloud deployment:
  <https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy>

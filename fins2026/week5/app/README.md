# Week 5 Digital Asset Fund App

This is the client-facing Stage 4 surface for Week 5.

The app presents a published lineup of five long-only crypto funds built from
the Week 5 out-of-sample engine:

- Core Market
- Low Volatility
- Return Seeking
- Downside Aware
- Risk Balanced

The default published lineup uses:

- monthly rebalancing
- a 365-day initial training window
- an expanding estimation window

The app includes:

- historical published-fund performance
- current live and target holdings
- concentration, turnover, and risk snapshots
- an illustrative allocation simulator
- an advanced portfolio-design view for monthly and weekly rebalance comparisons

## Run locally

Run from the repo root:

```bash
streamlit run fins2026/week5/app/streamlit_app.py
```

The app first tries live Yahoo Finance crypto prices and live Kenneth French
daily cash-rate data. If a live refresh fails, it falls back to the committed
fixture bundle in `app/fixtures/`.

## App fixture

Refresh the committed fallback fixture with:

```bash
python fins2026/week5/scripts/build_week5_app_fixture.py
```

The current fallback fixture includes:

- `fixtures/week5_app_features_long.parquet`

## App structure

- `app_config.py`: labels, published-fund names, and visible defaults
- `app_data.py`: live/fallback data loading and cached scenario builds
- `app_insights.py`: Plotly figures, metric cards, and presentation tables
- `app_views.py`: Streamlit layout, tabs, controls, and downloads
- `streamlit_app.py`: repo bootstrap and `main()` entrypoint

## Deployment

Before deployment, run from the repo root:

```bash
python tools/workflow.py check-app-submission --target fins2026/week5 --entrypoint fins2026/week5/app/streamlit_app.py
```

To prepare a clean private deploy repo, run:

```bash
python tools/workflow.py prepare-app-repo --source fins2026/week5 --dest ../week5-digital-asset-fund-explorer --repo week5-digital-asset-fund-explorer --entrypoint fins2026/week5/app/streamlit_app.py --push
```

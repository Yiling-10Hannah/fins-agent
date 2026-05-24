# Week 5 App Fixtures

These files are the committed fallback bundle for the Week 5 Streamlit app.

The live app first tries:

- Yahoo Finance crypto prices
- Kenneth French daily cash-rate data

If a live refresh fails, the app falls back to the fixture below:

- `week5_app_features_long.parquet`

Refresh the fixture with:

```bash
python fins2026/week5/scripts/build_week5_app_fixture.py
```

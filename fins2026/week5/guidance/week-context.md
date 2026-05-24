# Week Context

## Week Identity
- Week folder: `fins2026/week5`
- Title: Week 5: Crypto Data, Diagnostics, and OOS Portfolios
- README summary: Week 5 adapts the Week 4 operating model to cryptocurrencies.

## Core Guides

- `fins2026/week5/README.md`: Week 5: Crypto Data, Diagnostics, and OOS Portfolios. Week 5 adapts the Week 4 operating model to cryptocurrencies.
- `fins2026/week5/WORKSHOP.md`: Week 5 Workshop. Week 5 mirrors the Week 4 operating model and now extends into the first out-of-sample Stage 3 weight, return, figure, and client-facing app layer.
- `fins2026/week5/DATA_GUIDE.md`: Week 5 Data Guide. Week 5 has three data layers:
- `fins2026/week5/SUBMISSION_CHECKLIST.md`: Week 5 Submission Checklist. `README.md` explains the week purpose and canonical commands; `WORKSHOP.md` reflects the actual workshop flow; `DATA_GUIDE.md` and `data/README.md` describe the inputs accurately; Canonical scripts live in `scripts/`, not `scratch/`

## Prompt Files

- `fins2026/week5/prompts/assistant_starter.md`: Week 5 Assistant Starter Prompt. Week 5 covers Stage 1, Stage 2, Stage 3, and the first client-facing Stage 4 app layer for cryptocurrencies.
- `fins2026/week5/prompts/README.md`: Week 5 Prompts. Keep reusable prompts here when the week benefits from repeated AI-assisted figure, app, report, or data-analysis tasks.

## Current Scripts

- `fins2026/week5/scripts/_bootstrap.py`: Small helper for Week 5 scripts that need repo-root imports.
- `fins2026/week5/scripts/build_week5_app_fixture.py`: Build the committed Week 5 app fallback fixture.
- `fins2026/week5/scripts/describe_data.py`: Summarize the current data files for this week.
- `fins2026/week5/scripts/make_stage2_crypto_figures.py`: Build FT-style Stage 2 crypto figures for Week 5.
- `fins2026/week5/scripts/make_stage3_portfolio_figures.py`: Export Week 5 Stage 3 FT-style out-of-sample portfolio figures.
- `fins2026/week5/scripts/run_beginner_french_rfr.py`: Download the Week 5 daily risk-free rate from Kenneth French.
- `fins2026/week5/scripts/run_beginner_stage2_features_long.py`: Add rolling Stage 2 features and summary metrics to the Week 5 long return panel.
- `fins2026/week5/scripts/run_beginner_stage2_returns_long.py`: Build long daily returns for Week 5 Stage 2 and verify parity with wide returns.
- `fins2026/week5/scripts/run_beginner_stage2_returns_wide.py`: Build wide adjusted-price and return tables for Week 5 Stage 2.
- `fins2026/week5/scripts/run_beginner_stage3_oos_weights.py`: Build Week 5 Stage 3 out-of-sample crypto portfolio weight and return panels.
- `fins2026/week5/scripts/run_beginner_yahoo_crypto_20_since_2019.py`: Run the Week 5 Yahoo Finance 20-coin panel pull.
- `fins2026/week5/scripts/run_beginner_yahoo_crypto_intro_5.py`: Run the Week 5 Yahoo Finance crypto warm-up pull on five headline coins.
- `fins2026/week5/scripts/run_week.py`: Print the canonical Week 5 workflow.

## Standard Working Rules

- `data/` is for committed source inputs.
- `results/data/` is for generated, downloaded, cleaned, or merged datasets.
- `scratch/` is for disposable experiments, not the final path.
- Promote reused week-local logic into `code/` and cross-week logic into `fintools/`.

## Timing And Alignment Notes

- Stage 3: generate out-of-sample portfolio weights, daily portfolio returns, FT-style OOS portfolio figures, and point-in-time factsheet figures from the cleaned Stage 2 panel using only past data at each rebalance date.
- the same folder now contains both a research pack and a point-in-time factsheet pack.
- keep Stage 3 daily portfolio returns indexed by the earned `return_date` rather than a synthetic month-end label.
- the factsheet layer should translate the same Stage 3 engine into app-style point-in-time views of holdings, concentration, turnover, and BTC/ETH exposure.

## Current Paths

- Source data: `fins2026/week5/data`
- Generated outputs: `fins2026/week5/results`
- Current context files: `fins2026/week5/guidance`

# Week Context

## Week Identity
- Week folder: `fins2026/week3`
- Title: Week 3: Dual Macro App Lab
- README summary: Week 3 extends the Streamlit introduction into two companion products built from the same repo. The primary app is an Australia macro forecast monitor with benchmarking and release-lag-aware inputs. The companion app keeps the U.S. macro stress and forecasting surface available as a separate entrypoint in the same Week

## Core Guides

- `fins2026/week3/README.md`: Week 3: Dual Macro App Lab. Week 3 extends the Streamlit introduction into two companion products built from the same repo. The primary app is an Australia macro forecast monitor with benchmarking and release-lag-aware inputs. The companion app keeps the U.S. macro stress and forecasting surface available as a separate entrypoint in the same Week
- `fins2026/week3/WORKSHOP.md`: Week 3 Workshop. Use this run sheet to move from the simple Week 2 app to the richer Week 3 app package, with the Australia forecast monitor as the primary walkthrough.
- `fins2026/week3/DATA_GUIDE.md`: Week 3 Data Guide. Week 3 keeps the public-data workflow introduced in Week 2, but now the primary product is an Australia-first forecast lab rather than a U.S. market-stress dashboard.
- `fins2026/week3/SUBMISSION_CHECKLIST.md`: Week 3 App Deployment Checklist. Use this checklist when you want to deploy the Week 3 Australia-first app as its own private GitHub deploy repository and public Streamlit app.

## Additional Week Docs

- `fins2026/week3/APP_AUDIT.md`: Week 3 Streamlit App Audit. Audit date: 2026-04-20
- `fins2026/week3/APP_LAB.md`: Week 3 App Lab: Australia-First Forecasting Extension. Week 3 now carries two app entrypoints in the same folder: the primary Australia forecast product and a companion U.S. macro app. This lab remains focused on the Australia forecasting build, which keeps the same modular app pattern but asks a different product question: how should we structure an Australia-first
- `fins2026/week3/BEGINNER_FORECASTING.md`: Week 3 Beginner Forecasting. Start here if students are new to forecasting code.
- `fins2026/week3/US_BEGINNER_FORECASTING.md`: Week 3 U.S. Beginner Forecasting Extension. Use this only after the main Australia Week 3 ladder makes sense.

## Prompt Files

- `fins2026/week3/prompts/assistant_starter.md`: Week 3 Assistant Starter Prompt. Load Week 3 context in this order before answering:
- `fins2026/week3/prompts/README.md`: Week 3 Prompts. This folder holds reusable Week 3 prompts.

## Current Scripts

- `fins2026/week3/scripts/build_forecast_inputs.py`: Build the Week 3 Australia/U.S. forecast input panels.
- `fins2026/week3/scripts/describe_data.py`: Summarize the data sources used in Week 3.
- `fins2026/week3/scripts/describe_forecast_data.py`: Print the Week 3 forecast target and model configuration.
- `fins2026/week3/scripts/make_beginner_forecast_story_figures.py`: Build the Week 3 Australia forecast story figure pack.
- `fins2026/week3/scripts/make_beginner_forecasting_series.py`: Create the Week 3 beginner forecasting source CSVs.
- `fins2026/week3/scripts/make_us_beginner_forecast_story_figures.py`: Build the Week 3 U.S. forecast story figure pack.
- `fins2026/week3/scripts/make_us_beginner_forecasting_series.py`: Create the Week 3 U.S. beginner forecasting source CSVs.
- `fins2026/week3/scripts/run_beginner_ar_forecast.py`: Run the Week 3 beginner AR-forecast walkthrough.
- `fins2026/week3/scripts/run_beginner_arma_forecast.py`: Run the Week 3 beginner ARMA-forecast walkthrough.
- `fins2026/week3/scripts/run_beginner_armax_forecast.py`: Run the Week 3 beginner ARMAX-forecast walkthrough.
- `fins2026/week3/scripts/run_beginner_arx_forecast.py`: Run the Week 3 beginner ARX-forecast walkthrough.
- `fins2026/week3/scripts/run_beginner_enet_forecast.py`: Run the Week 3 beginner elastic-net walkthrough.
- `fins2026/week3/scripts/run_beginner_ensemble_forecast.py`: Run the Week 3 beginner ensemble walkthrough.
- `fins2026/week3/scripts/run_beginner_model_horse_race.py`: Run the Week 3 beginner forecast horse race.
- `fins2026/week3/scripts/run_beginner_naive_forecast.py`: Run the Week 3 beginner naive-forecast walkthrough.
- `fins2026/week3/scripts/run_beginner_ols_forecast.py`: Run the Week 3 beginner OLS-forecast walkthrough.
- `fins2026/week3/scripts/run_beginner_unit_root_check.py`: Run the Week 3 beginner unit-root walkthrough.
- `fins2026/week3/scripts/run_forecast_benchmarks.py`: Run the Week 3 forecast benchmark suite.
- `fins2026/week3/scripts/run_us_beginner_ar_forecast.py`: Run the Week 3 U.S. beginner AR-forecast walkthrough.
- `fins2026/week3/scripts/run_us_beginner_arma_forecast.py`: Run the Week 3 U.S. beginner ARMA-forecast walkthrough.
- `fins2026/week3/scripts/run_us_beginner_arx_forecast.py`: Run the Week 3 U.S. beginner ARX-forecast walkthrough.
- `fins2026/week3/scripts/run_us_beginner_model_horse_race.py`: Run the Week 3 U.S. beginner forecast horse race.
- `fins2026/week3/scripts/run_us_beginner_naive_forecast.py`: Run the Week 3 U.S. beginner naive-forecast walkthrough.
- `fins2026/week3/scripts/run_us_beginner_unit_root_check.py`: Run the Week 3 U.S. beginner unit-root walkthrough.
- `fins2026/week3/scripts/run_week.py`: Print the canonical Week 3 workflow and create output folders.

## Standard Working Rules

- `data/` is for committed source inputs.
- `results/data/` is for generated, downloaded, cleaned, or merged datasets.
- `scratch/` is for disposable experiments, not the final path.
- Promote reused week-local logic into `code/` and cross-week logic into `fintools/`.

## Timing And Alignment Notes

- `DATA_GUIDE.md`: explains the Australia observable panel, U.S. context inputs, and target-frequency mapping.
- monthly observable panel: used for cash rate, 10Y yield, unemployment, TWI, and commodity-price targets.
- live path: no-key FRED graph CSV plus the Week 3 month-end panel helper.
- Treat live refresh time as different from each series' latest observable date.

## Current Paths

- Source data: `fins2026/week3/data`
- Generated outputs: `fins2026/week3/results`
- Current context files: `fins2026/week3/guidance`

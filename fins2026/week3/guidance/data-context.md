# Data Context

## Committed Inputs

- Folder: `fins2026/week3/data`
- Files: 3

### `fins2026/week3/data/australia_macro_stage1_long.csv`
- Size: 588.9 KB
- Shape: 2855 rows x 17 columns
- Columns: `series_id` (str), `display_name` (str), `source_name` (str), `source_table` (str), `native_frequency` (str), `reference_date_rule` (str), `raw_date` (str), `reference_date` (str), ... and 9 more

### `fins2026/week3/data/benchmark_leaderboard_fixture.csv`
- Size: 7.3 KB
- Shape: 48 rows x 12 columns
- Columns: `series` (str), `frequency` (str), `target` (str), `model` (str), `model_label` (str), `status` (str), `error` (float64), `target_mae` (float64), ... and 4 more

### `fins2026/week3/data/README.md`
- Size: 638 B
- Type: `.md`

## Generated Data

- Folder: `fins2026/week3/results/data`
- Status: generated locally and not committed by default


## Timing And Alignment Notes

- `DATA_GUIDE.md`: explains the Australia observable panel, U.S. context inputs, and target-frequency mapping.
- monthly observable panel: used for cash rate, 10Y yield, unemployment, TWI, and commodity-price targets.
- live path: no-key FRED graph CSV plus the Week 3 month-end panel helper.
- Treat live refresh time as different from each series' latest observable date.

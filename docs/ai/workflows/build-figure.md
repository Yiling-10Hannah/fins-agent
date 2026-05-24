# Build Figure Workflow

## Use When

Use when a student wants to create, improve, validate, or export a chart for
weekly coursework, a report, a slide deck, or a Word document.

Deterministic example helper:

```bash
python tools/workflow.py build-figure --output results/figures
```

Dataframe-driven FT/FINS figure suite from a CSV:

```bash
python tools/workflow.py build-figure-suite data/my_data.csv --style ft --narrative --output results/figures
```

Generic dataframe suite when the user explicitly wants broad chart coverage:

```bash
python tools/workflow.py build-figure-suite data/my_data.csv --style ft --output results/figures
```

FT-style validation gallery:

```bash
python tools/workflow.py build-figure --style ft --docx --output results/figures-ft
```

Week 2 student FT-style gallery:

```bash
python tools/workflow.py build-figure --style ft --docx --output fins2026/week2/results/figures/style_gallery
```

The matching teaching script is:

```bash
python fins2026/week2/scripts/make_ft_validation_figures.py
```

The full Week 2 lab, including the style gallery and the FRED 10-year
market-and-macro narrative pack, is:

```bash
python fins2026/week2/scripts/make_all_week2_figures.py --skip-live --use-fixture
```

## Inputs

- dataset or dataframe to plot
- figure purpose and intended document target
- optional output folder, defaulting to `results/figures`
- optional Word/A4 layout target such as `full_width`, `half_width`,
  `two_panel`, `portrait_tall`, `portrait_full`, or `landscape_wide`
- optional style, either `fins` or `ft`; the FT beige background is off unless
  `ft_background=True` or `--ft-background` is explicitly requested
- for dataframe-suite requests, optional `date`, `source`, `title_prefix`,
  `max_figures`, and `narrative` settings

## Required Context

- `AGENTS.md`
- `fintools/figures/`
- `fintools/datasets/`
- current week or project folder
- report or Word document constraints, if the figure will be inserted into a
  document

## Data And Validation

Use the frozen validation datasets in `fintools.datasets` when testing figure
code or checking assumptions:

- `ff3_monthly` - Fama/French 3 factors
- `ff_industry_10_monthly` - Fama/French 10 industry portfolios
- `ff25_size_value_monthly` - Fama/French 25 size-value portfolios
- `fred_macro_monthly` - long FRED macro series
- `fred_rates_daily` - long FRED Treasury rates and yield-curve spreads
- `fred_financial_stress_daily` - daily VIX and high-yield spread stress data
- `shiller_market_monthly` - Robert Shiller's long U.S. market and CAPE data
- `world_bank_country_panel_annual` - World Bank GDP, population, and GDP per
  capita panel data
- `world_bank_gdp_annual` - World Bank GDP data for ranking and slope-chart
  validation examples

If refreshing fixtures, use `tools/download_validation_data.py`. Raw downloads
must stay under ignored `_raw/` or `_refresh/` folders. Only compact curated
CSV/JSON fixtures belong in production.

## Plotting Standards

1. Start with `fintools.figures` helpers before writing custom plotting code.
2. Use Matplotlib for time-series, financial panels, and final axis control.
3. Use Seaborn for statistical plots, grouped categorical comparisons,
   distributions, and heatmaps.
4. Always supply a title, x label, y label, units, source, and sample period.
5. Use `FigureContext` for captions and source notes. Add a compact
   in-figure source note for standalone PNG/PDF proof packs when the chart may
   circulate outside the Word caption.
6. Check return units before plotting cumulative returns or drawdowns. Fama
   and French returns are percent returns, not decimal returns.
7. Use colorblind-safe palettes and avoid unreadable default legends.
8. For time-series figures, use the built-in NBER recession shading when the
   figure is a standard line-based macro or market time-series and the shading
   adds real interpretive value. It is clipped to the plotted date range so old
   recessions cannot create empty x-axis space.
   If custom Matplotlib code is necessary, call
   `add_nber_recession_shading` explicitly and keep the recession treatment
   consistent across related figures in the same pack.
   Do not add NBER recession shading by default to stacked-share, stacked-area,
   100%-composition, or other `fill_between`-style charts. Those figures are
   primarily part-to-whole views, the shading usually adds little value, and it
   can create rendering and readability problems in export.
   Use sparse horizontal date ticks for long samples; do not rely on rotated
   date labels to fit a crowded axis.
9. For bar charts that compare average returns, include standard-error bars
   unless there is a specific reason not to.
10. Close figures in scripts with `matplotlib.pyplot.close(fig)` after export.
11. Use `style="ft"` for FT-inspired colors, ticks, grids, and narrative
    examples. Use `ft_background=True` only when the FT beige/salmon
    background is desired.
12. Use `requirements-plotly.txt` only for optional Plotly demos. Plotly static
    export requires Kaleido and Chrome/Chromium, so Matplotlib remains the
    default Word/A4 backend.
13. Dense multi-line time-series should use slimmer lines and partial alpha;
    avoid letting one color dominate overlapping data.
14. Direct labels and slope-chart labels must use collision-avoidance with
    subtle leader lines. If labels cannot be made readable, fall back to a
    legend rather than accepting overlap.
15. Report cumulative return plots should use growth of `$1` on a log scale
    with dollar tick labels, not `x` suffixes.
16. Keep explanatory notes such as "error bars are standard errors" in the
    caption unless the plot itself needs a visual key.
17. Connected scatterplots are for short, interpretable episodes. Do not use
    them for long noisy macro paths that collapse into an unreadable squiggle.
18. Dense validation-gallery time-series should prefer legends over endpoint
    labels. Endpoint labels are acceptable only when rendered overlap checks
    pass cleanly.
19. Categorical comparison charts must have enough distinct colors for the
    plotted categories. Do not allow a color cycle to silently repeat on a
    slope chart or ranked comparison.
20. Choose chart types from the FT Visual Vocabulary idea first: deviation,
    correlation, ranking, distribution, change over time, part-to-whole,
    magnitude, and temporal patterns cover most student report needs.
    For FT-style rankings, prefer `lollipop_plot`; for observed-versus-
    benchmark comparisons, prefer `dumbbell_plot` or an equally explicit
    comparison form rather than default grouped bars.
21. Bubble charts, calendar heatmaps, and uncertainty bands should be used only
    when the extra encoding answers a clear question.
22. For Word/A4 figures, keep visible plot titles short. Put detailed claims,
    sample definitions, double-counting warnings, and source context in
    `FigureContext`, not in the image title. Rendered titles must stay inside
    the figure canvas.
23. In a 1x2 comparison layout, use equal-width subplots unless one panel is
    explicitly a legend, colorbar, table, or supporting annotation area.
24. Bubble charts should be snapshots or unconditional summaries unless a time
    path is essential. Avoid connected bubble paths for long noisy samples.
25. Never let raw dataframe field names leak into visible labels. Axis labels,
    colorbar labels, and legend titles must be display-ready, start uppercase
    when they start with a letter, and avoid underscores.
26. Generic legend titles are opt-in. Do not show titles such as `country`,
    `year`, `group`, or `Series` unless the title itself adds interpretation.
27. Bubble and scatter helpers must pad the axes enough that markers and labels
    are not clipped in Word/A4 exports.
28. Highlight colors must have caption context. Use muted comparison marks plus
    accent colors for highlighted observations, and explain the highlighted set
    in `FigureContext.note`.
29. For vague dataframe requests such as "make FT-style figures for my data",
    use `profile_dataframe`, `plan_figure_suite`, and `create_figure_suite`
    before writing one-off plotting code. Inspect the generated plan and the
    skipped validation notes before showing the student final output.
30. Long-panel charts should be planned only when each time period contains
    multiple category observations. A wide dataframe with one category label per
    date is not automatically a panel.
31. Use `narrative=True` when a dataframe contains recognizable domain
    structure and the user asks for a polished suite, not just generic chart
    coverage. Narrative mode should prefer story-first figures, semantic
    titles, display-ready labels, and highlighted comparisons over raw-column
    chart templates.
32. For broad prompts such as "make FT-style figures for my data", default to
    `narrative=True` or `--narrative`. Use generic mode only when the user asks
    for broad chart inventory or when no narrative detector recognizes the
    schema.
33. Heatmaps and correlation matrices need compact display labels before
    rendered validation. Prefer domain labels such as `10Y-3M`, `HY OAS`, and
    `VIX 21-day avg` over long raw FRED-style column names.
34. Mixed-frequency macro figures must document whether they are aligned on
    reference dates or observable dates. Do not silently mix those two clocks
    inside one canonical teaching figure.
35. For mixed-frequency macro figure packs, declare the frozen common endpoint
    up front and avoid vague titles or captions that imply a synchronized
    "latest" date when the releases are actually staggered.
36. Visible chart text must not use `pp` or `p.p.`. When plotting rates or
    changes in rates, use `%` in axes, legends, and annotations, then explain
    the transform in `FigureContext.note` if needed.
37. Legends must not overlap the main data. Move them to a low-signal corner,
    below the panel, or outside the plotting area if overlap checks fail.
38. Forecast-comparison figures must give each model a distinct, stable color.
    Do not let multiple model lines collapse onto the same accent color.
39. Prefer standard forecast diagnostics such as holdout actual-versus-forecast,
    RMSE scorecards, absolute-error views, and latest-forecast comparison. Do
    not introduce bespoke diagnostics by default when a more conventional plot
    tells the story more clearly.
40. If multiple forecast metrics matter, prefer a small-multiples scorecard
    over a single metric bar chart with dense inline annotations. Readers
    should be able to see RMSE, MAE, MASE, and OOS $R^2$ separately.
41. Avoid layouts where long y-axis labels force the whole figure off-centre.
    Shorten display labels, rotate x-axis labels, or switch the chart
    orientation before accepting large blank margins.
42. Do not stack several almost-identical endpoint markers at the end of a
    forecast line. If forecast endpoints overlap, simplify to one extension,
    a narrow band, or clear direct labels.
43. In multi-panel figures, leave explicit vertical and horizontal space
    between neighboring panels. Subplot titles must never collide with the
    tick labels or data region of the panel above or below.
    Do not swing too far the other way: tighten row gaps, suppress redundant
    upper-row or right-column axis labels, and avoid large blank bands between
    panels.
44. In stacked scorecards or small-multiples with x-axis ticks on the upper
    row, leave enough row gap and title padding that the lower-row titles sit
    visibly clear of the upper-row tick labels.
45. Source notes and figure notes need dedicated bottom margin. Do not place a
    note under the axes unless the layout explicitly reserves space below the
    lowest tick labels.
46. In multi-panel comparison charts where each panel contains a different
    group of series, use panel-specific legends or globally unique colors.
    Never reuse the same colors across panels and then combine the groups into
    one ambiguous shared legend.
47. Single-series charts should usually omit the legend when the title and
    y-axis already identify the series. If a legend is kept, the label must be
    display-ready English, never a raw dataframe or code column name.
48. Threshold and event-count legends should use compact mathematical labels
    such as `Return > |10%|` or `Spread < 0`, not vague prose like "large move"
    when the threshold itself is the point of the chart.
49. Dense multi-series drawdown charts should use thinner lines and modest
    alpha so all series remain visible. Do not let one portfolio or asset
    obscure the rest of the drawdown path.
50. Efficient-frontier figures need collision-checked point labels with clear
    offsets or leader lines. Do not allow labels for risk-free, equal-weight,
    minimum-variance, and tangency portfolios to overlap each other or the
    surrounding asset cloud.
51. When readers need the actual signed portfolio weights across many assets,
    prefer panel-per-portfolio diverging bar charts over a heatmap. Use a
    heatmap only when the comparison of patterns matters more than the exact
    weights.
52. In multi-panel portfolio scorecards with the same categories repeated, show
    the category labels only on the left panels unless the extra repetition adds
    real value. Suppress redundant right-panel category labels if they create
    clutter or collisions.
53. Bar-end value labels in scorecards must stay clear of category labels and
    panel boundaries. If space is tight, reduce repetition, move labels
    outside, or add padding before accepting overlap.
54. Dense category charts with many labels, such as full portfolio-weight
    panels, should proactively reduce category-label and panel-title font sizes
    before accepting collisions or unreadable crowding.
55. When a chart has dozens of category labels on one axis, bias toward
    visibly smaller label text rather than leaving overlap or stacked glyphs.
    Readability comes from clean separation first, not from preserving a
    standard font size.

## FT-Style References

- Financial Times Visual Vocabulary:
  <https://github.com/Financial-Times/chart-doctor/blob/main/visual-vocabulary/README.md>
- Roman Dogadin, "Style your visuals like the Financial Times using Plotly":
  <https://medium.com/@romandogadin/style-your-visuals-like-the-financial-times-using-plotly-3e7f1d6e293d>
- Arthur Turrell, "Narrative Data Visualisation":
  <https://aeturrell.github.io/coding-for-economists/vis-narrative.html>

## Word And A4 Export

Students will often paste figures into Word documents. Prefer:

```python
from fintools.figures import FigureContext, export_word_figure

context = FigureContext(
    title="Cumulative Market Excess Return",
    note="Cumulative return from monthly excess returns.",
    source="Kenneth French Data Library",
    sample="2020-2021",
    units="Cumulative return",
)
export_word_figure(fig, "results/figures", "market_cumulative", context=context)
```

Use `insert_figures_docx` when a quick Word proof pack is useful. Keep related
figures in one Word document so layout, captions, and source notes can be
reviewed together. Word proof packs are A4 portrait by default and clamp
figures to the usable page width, even if a wider export spec is requested.
Captions appear below each image as a contained `Figure X.` block with title,
note, sample-period sentence, units, and source. Use `export_figure_bundle`
when a figure also needs standalone PNG/PDF output for LaTeX or wide-screen
inspection.

## Dataframe Figure Suites

Use this path when a student provides a dataframe, a CSV, or asks
inside PyCharm for "some FT-style figures for my data."

```python
from fintools.figures import create_figure_suite

result = create_figure_suite(
    df,
    output="results/figures",
    style="ft",
    docx=True,
    source="",
    title_prefix="My Dataset",
    narrative=True,
)

print([figure.plan_item.title for figure in result.generated_figures])
print(result.skipped)
```

The suite generator:

- profiles date, numeric, categorical, return-like, and percent/share columns
- plans time-series, indexed time-series, cumulative-return, long-panel,
  part-to-whole, slope, ranking, bar/distribution, scatter, correlation, and
  distribution figures when the data supports them
- validates rendered figures for raw labels, overlap, marker clipping, blank
  images, and Word/A4 page fit
- skips charts that fail validation instead of exporting ugly figures
- in narrative mode, uses domain-aware planners when the schema is recognized;
  for example, electronic corporate-bond trading share data gets electronic
  versus voice small multiples, whole-market venue composition, electronic venue
  mix, segment adoption slope, and latest-period venue ranking figures
- portfolio/returns data gets growth of one dollar, drawdowns, risk-return
  scatter, return correlation, and return-distribution figures

For CSV-only usage:

```bash
python tools/workflow.py build-figure-suite path/to/data.csv --style ft --date date --source "" --narrative
```

## Procedure

1. Clarify the figure purpose and intended output medium.
2. Load the data from the current week, project folder, or validation fixture.
3. Validate units, date parsing, missing values, and sample period.
4. For broad suite requests, profile and plan first:
   - `profile_dataframe`
   - `plan_figure_suite`
   - `create_figure_suite`
   Default to `narrative=True`; fall back to generic planning when no narrative
   detector applies.
5. Choose a figure helper for custom or single-chart requests:
   - `time_series_plot`
   - `cumulative_returns_plot`
   - `indexed_time_series_plot`
   - `drawdown_plot`
   - `bar_plot`
   - `bubble_scatter_plot`
   - `calendar_heatmap`
   - `mean_return_bar_plot`
   - `stacked_area_plot`
   - `stacked_bar_plot`
   - `proportional_stacked_bar_plot`
   - `diverging_bar_plot`
   - `dumbbell_plot`
   - `grouped_bar_plot`
   - `scatter_plot`
   - `connected_scatter_plot`
   - `distribution_plot`
   - `distribution_comparison_plot`
   - `ecdf_plot`
   - `correlation_heatmap`
   - `value_heatmap`
   - `small_multiples`
   - `lollipop_plot`
   - `slope_chart`
   - `area_balance_plot`
   - `rolling_stat_plot`
   - `uncertainty_band_plot`
   - `add_source_note`
6. Export with `export_word_figure` for Word/A4 or `export_figure_bundle`
   for report-ready PNG/PDF plus caption sidecar.
7. Run validation helpers when relevant:
   - `validate_axes_labels`
   - `validate_category_label_count`
   - `validate_display_labels`
   - `validate_figure_context`
   - `validate_horizontal_grid`
   - `validate_legend_present`
   - `validate_markers_within_axes`
   - `validate_no_text_overlap`
   - `validate_image_not_blank`
   - `validate_no_tick_label_overlap`
   - `validate_series_identification`
   - `validate_unique_series_colors`
   - `validate_docx_images_fit_page`
   - `validate_word_readability`
   - `infer_return_scale`
8. Keep generated outputs in `results/figures/`; use `_checks/` for local
   throwaway validation images.

## Output

- publication-quality figure file
- caption/context sidecar when exported from `fintools.figures`
- clear note on source, sample period, and units
- optional Word document proof containing the figure

# Scaffold Week Workflow

## Use When

Use when a student wants to create, standardize, or backfill a weekly folder
under `fins2026/weekN/`.

Deterministic helper:

```bash
python tools/workflow.py scaffold-week --target fins2026/weekN [--title "..."]
```

## Inputs

- required week target under `fins2026/weekN/`
- optional title used for starter headings when the week files do not exist yet

## Required Context

- `AGENTS.md`
- `fins2026/AGENTS.md`
- target week folder under `fins2026/`

## Procedure

1. Resolve the target to `fins2026/weekN/`.
2. Create the standard weekly scaffold if folders or starter files are
   missing.
3. Never overwrite existing authored week files.
4. Always create or refresh:
   - `guidance/week-context.md`
   - `guidance/data-context.md`
   - `guidance/output-context.md`
5. Keep the standard weekly meaning stable:
   - `data/` for committed source inputs
   - `results/data/` for generated datasets
   - `scratch/` for disposable exploration
   - `scripts/` for canonical rerunnable week scripts
6. For mixed-frequency macro weeks, encode the Data Factory Floor split
   explicitly:
   - Station 1 outputs should preserve source authenticity, cadence, and
     observability metadata
   - Station 2 outputs should produce merged teaching panels and visual-ready
     transforms without jumping ahead to modelling
7. For mixed-frequency macro weeks, freeze and document:
   - the common reference endpoint
   - the classroom information-set date
   - any rules about forward-filling, quarter-end stamping, or point-in-time
     survey dates
8. Preserve existing week-specific materials such as extra lab docs, apps, or
   figures already present in the target week.

## Output

- full week scaffold under `fins2026/weekN/`
- generated week context files under `guidance/`
- summary of created directories and created starter files

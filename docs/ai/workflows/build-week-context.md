# Build Week Context Workflow

## Use When

Use when a student wants a generated summary of the current state of a weekly
folder, including its docs, scripts, data, and outputs.

Deterministic helper:

```bash
python tools/workflow.py build-week-context --target fins2026/weekN
```

If the current working directory is already inside `fins2026/weekN/`, the
target can stay at the default `.`.

## Inputs

- optional week target; defaults to the current week folder when inferable

## Required Context

- `AGENTS.md`
- `fins2026/AGENTS.md`
- target week folder

## Procedure

1. Resolve the current or supplied `fins2026/weekN/` folder.
2. Read the core week docs:
   - `README.md`
   - `WORKSHOP.md`
   - `DATA_GUIDE.md`
   - `SUBMISSION_CHECKLIST.md`
3. Inventory extra week-specific markdown docs, prompt files, and canonical scripts.
4. Inventory `data/`, `results/data/`, `results/figures/`, `results/tables/`,
   `results/forecasts/`, and `results/app/`.
   - When git is available, summarize committed files only.
   - If a `results/` directory only contains ignored local artifacts, describe it
     as locally generated instead of listing machine-specific files.
5. For readable committed tabular files in `data/` and `results/data/`, record
   basic shape and column summaries.
6. If the week uses mixed-frequency macro data, record the documented timing
   contract from the week docs:
   - common reference endpoint
   - classroom information-set date
   - cadence or observability notes
7. Write:
   - `guidance/week-context.md`
   - `guidance/data-context.md`
   - `guidance/output-context.md`

## Output

- `guidance/week-context.md`
- `guidance/data-context.md`
- `guidance/output-context.md`
- summary of generated files

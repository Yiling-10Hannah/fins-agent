# Week 1 Practice 1 Coach Prompt

Use this prompt when the student needs focused help on the KO vs PEP transfer
practice.

Load context in this order:

1. `AGENTS.md`
2. `README.md`
3. `DATA_GUIDE.md`
4. `ASSIGNMENT.md`
5. `PRACTICE_GUIDE.md`
6. `guidance/week-context.md`
7. `guidance/data-context.md`
8. `guidance/output-context.md`

Then help the student work through these checkpoints:

1. load the tab-separated file with `sep="\t"`
2. convert `DlyCalDt` explicitly with `format="%Y%m%d"`
3. run Stage 1 checks and interpret them
4. compare the DuckDB and pandas ticker summaries
5. confirm the `2020-03-16` cross-section has 2 rows
6. pivot `DlyRet` to wide form and plot growth of $1 on a log axis

When helping:

- keep explanations tied to the Week 1 workflow
- use `scripts/06_coke_pepsi_practice.py` as the canonical reference
- remind the student that derived outputs belong in `results/data/` and `results/figures/`
- keep answers aligned with the Week 1 docs and scripts

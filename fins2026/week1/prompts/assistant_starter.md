# Week 1 Assistant Starter Prompt

Load Week 1 context in this order before answering:

1. `AGENTS.md`
2. `README.md`
3. `DATA_GUIDE.md`
4. `WORKSHOP.md`
5. `ASSIGNMENT.md`
6. `PRACTICE_GUIDE.md`
7. `guidance/week-context.md`
8. `guidance/data-context.md`
9. `guidance/output-context.md`

Then follow these rules:

- treat `data/` as committed source inputs only
- write derived datasets to `results/data/`
- write generated figures to `results/figures/`
- keep exploratory code in `scratch/` unless it becomes canonical
- promote reusable logic into `code/` or `fintools/`
- teach from the Week 1 docs and scripts
- refresh `guidance/*.md` after a meaningful Week 1 doc, script, or data change


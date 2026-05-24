# Week 5 Submission Checklist

- `README.md` explains the week purpose and canonical commands.
- `WORKSHOP.md` reflects the actual workshop flow.
- `DATA_GUIDE.md` and `data/README.md` describe the inputs accurately.
- Canonical scripts live in `scripts/`, not `scratch/`.
- Generated outputs live under `results/` and are reproducible.
- `guidance/*.md` has been refreshed with `python tools/workflow.py build-week-context --target fins2026/week5`.
- Stage 2 summary tables and FT-style figures save to the documented paths.
- The Week 5 ladder is clear:
  - Yahoo and Kenneth French source pulls
  - Stage 2 return and feature construction
  - Stage 2 FT-style figure pack
  - Stage 3 OOS weights, returns, figures, and factsheets
  - Stage 4 app fixture refresh
  - Stage 4 client-facing Streamlit app
- Any app work is isolated under `app/`.
- The Week 5 app runs locally with `streamlit run fins2026/week5/app/streamlit_app.py`.
- The Week 5 app fallback fixture is refreshable with
  `python fins2026/week5/scripts/build_week5_app_fixture.py`.
- Before deployment, the Week 5 app passes
  `python tools/workflow.py check-app-submission --target fins2026/week5 --entrypoint fins2026/week5/app/streamlit_app.py`.


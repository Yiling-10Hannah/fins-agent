# Audit App Workflow

## Use When

Use when a student asks to audit, review, benchmark, harden, or improve a
Streamlit coursework app, including deployed Week apps and final-project apps.

## Required Context

- `AGENTS.md`
- `.agents/skills/audit-app/SKILL.md`
- `docs/apps/streamlit/audit-checklist.md`
- `docs/apps/streamlit/README.md`
- app entrypoint, usually `app/streamlit_app.py`
- app README, submission checklist, and deployment notes when present
- tests for the app and shared helpers
- current official Streamlit docs for any API that affects the audit

## Procedure

1. Identify the app entrypoint, deployment root, Streamlit version, and active
   repo branch.
2. Recheck official Streamlit docs for APIs used by the app when the behavior
   may have changed: tabs, session state, query params, caching, forms,
   fragments, AppTest, dataframes, config, secrets, and deployment.
3. Inspect the app against `docs/apps/streamlit/audit-checklist.md`.
4. Run focused verification where possible:
   - `python -m pytest -q`
   - `python -m ruff check .`
   - `python tools/workflow.py check-app-submission --target ...`
   - targeted import checks when a full app run is not appropriate
5. Produce an audit report with findings ordered by severity. Each finding must
   include the affected surface, observed pattern, impact, and concrete fix.
6. Separate immediate app fixes from durable context updates. If a recurring
   issue is found, update shared Streamlit docs and relevant assistant skills.
7. If implementation is requested, patch the app first, then update tests and
   context docs, then verify again.

## Audit Standards

- Findings first. Do not bury defects under praise.
- Use client-facing product standards, not only code-quality standards.
- Treat navigation/state bugs as product defects even when the Python code does
  not crash.
- Distinguish Streamlit runtime behavior from app bugs. Confirm whether the
  issue belongs to reruns, widget identity, query params, cache behavior, or
  application logic.
- Prefer shared `fintools.apps` helpers when fixing patterns that will recur
  across weeks.
- Do not recommend secrets, local absolute paths, or deployment settings that
  would only work on one machine.

## Output Shape

Use this structure:

```text
Summary
- one paragraph on current maturity and main risk

Findings
- [Severity] Surface: issue, impact, fix

Backlog
- immediate fixes
- next iteration
- optional polish

Reusable Context Updates
- docs or skill changes made or recommended

Verification
- commands run and results
```

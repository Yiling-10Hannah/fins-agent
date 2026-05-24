---
name: audit-app
description: Use when a student asks to audit, review, benchmark, harden, or improve a Streamlit coursework app or deployed app; covers Streamlit best practices, app UX, state/query params, caching, testing, deployment readiness, and reusable context updates.
---

# Audit App Skill

Read `docs/ai/workflows/audit-app.md` and
`docs/apps/streamlit/audit-checklist.md`. They are the canonical workflow and
rubric.

Use this skill for Streamlit audit requests before proposing or making fixes.
If the student asks for implementation after the audit, use this skill first,
then use `build-app` for the patch work.

## Workflow

1. Identify the app entrypoint, deployment root, Streamlit version, branch, and
   whether the app is local, deployed, or both.
2. Check current official Streamlit docs for APIs that matter to the audit:
   tabs, session state, query params, caching, fragments, forms, AppTest,
   dataframes, config, secrets, and deployment.
3. Inspect the app with the audit checklist.
4. Run focused verification when available:
   - repo interpreter plus `-m pytest -q`
   - repo interpreter plus `-m ruff check .`
   - `python tools/workflow.py check-app-submission --target ...`
   - targeted import checks for app helper functions
5. Report findings first, ordered by severity, with exact file or UI surface,
   impact, and concrete fix.
6. Update durable context when the audit reveals a reusable lesson.

## Standards

- Treat first-click tab bounce, stale query-param state, hidden tab exceptions,
  and chart/control overlap as product defects.
- Benchmark against current Streamlit behavior, not memory of older APIs.
- Separate immediate app fixes from shared helper or documentation changes.
- Keep visible app copy client-facing.
- Prefer shared `fintools.apps` helpers for recurring patterns.
- Do not push a main course repo unless explicitly asked.

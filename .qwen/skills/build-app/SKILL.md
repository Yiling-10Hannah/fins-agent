---
name: build-app
description: Use when a student asks to create, improve, test, or deploy a Streamlit coursework app from data or analysis.
argument-hint: "[--target projects/name] [--title \"...\"]"
---

# Build App Skill

Read `docs/ai/workflows/build-app.md` and `docs/apps/streamlit/README.md`.
Follow them as the canonical workflow.

Preferred commands:

- `python tools/workflow.py build-app --target projects/my_project --title "My App"`
- `python tools/workflow.py new-project my_project --with-app --description "..."`
- `python tools/workflow.py check-app-submission --target projects/my_project`
- `python tools/workflow.py prepare-app-repo --source projects/my_project --dest ../my_project_handin --repo my_project_handin`

If the workflow doc conflicts with older tool-specific instructions, the
shared workflow doc wins.

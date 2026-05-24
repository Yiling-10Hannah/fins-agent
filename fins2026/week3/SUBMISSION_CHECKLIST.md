# Week 3 App Deployment Checklist

Use this checklist when you want to deploy the Week 3 Australia-first app as
its own private GitHub deploy repository and public Streamlit app.

For the plain-English full workflow, see
`docs/apps/streamlit/student-quickstart.md`.

## Readiness Command

Run from the repo root:

```bash
python tools/workflow.py check-app-submission --target fins2026/week3 --entrypoint fins2026/week3/app/streamlit_app.py
```

Resolve every blocking issue before deployment or grading.

## Clean Deploy Repository

To prepare a minimal private-repo bundle, run from the course repo root:

```bash
python tools/workflow.py prepare-app-repo --source fins2026/week3 --dest ../week3-aus-forecast --repo week3-aus-forecast --entrypoint fins2026/week3/app/streamlit_app.py
```

To rehearse the companion U.S. app as a separate Streamlit deployment, use:

```bash
python tools/workflow.py prepare-app-repo --source fins2026/week3 --dest ../week3-us-macro --repo week3-us-macro --entrypoint fins2026/week3/us_app/streamlit_app.py
```

Add `--push` after GitHub CLI is authenticated if you want the workflow to
create the private GitHub repo and push it automatically.

After the private repo is pushed, use `docs/apps/streamlit/finish-deployment.md`
for the Streamlit browser steps.

## Required Deployment Fields

- Public Streamlit app URL: TODO
- GitHub repository URL accessible to the teaching team: TODO
- Branch: `main`
- App entrypoint: `fins2026/week3/app/streamlit_app.py`
- Final commit hash: TODO

## Before Hand-In

- [ ] The latest code is committed and pushed to GitHub.
- [ ] The app runs locally from the repo root with
  `streamlit run fins2026/week3/app/streamlit_app.py`.
- [ ] The Streamlit Community Cloud app loads in an incognito browser.
- [ ] The Streamlit app is public for grading: app list three-dot menu ->
  `Settings` -> `Sharing` -> `Who can view this app` ->
  `This app is public and searchable`.
- [ ] The teaching team can access the GitHub repository if it remains private.
- [ ] No secrets, `.streamlit/secrets.toml`, `.env`, `.venv/`, local absolute
  paths, or private raw data are committed.

A `localhost` URL is not a valid submission. It only works on the student's own
computer while the local Streamlit process is running.

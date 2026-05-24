# Week 0 - Getting Started

Welcome to FINS2026 Fintech. This folder is your starting point.

## What Is This Repo?

This is your coursework toolkit. Each week has a folder with exercises,
data, and starter code. You will use Python to analyze financial data,
build portfolios, and write up your findings with an AI coding assistant
helping you throughout.

## Setup (5 minutes)

**Option A - with an AI tool (recommended):**

1. Open the cloned `fins-agent` folder in PyCharm
2. Open PyCharm's built-in terminal at the repo root
3. Start with [../../docs/ai/start-here.md](../../docs/ai/start-here.md)
4. Follow the matching OpenCode, Claude, Codex, Gemini, or Qwen path
5. The AI helps install Python 3.13 if needed, then runs onboarding

**Option B - manual:**

Follow the steps in [QUICKSTART.md](../../QUICKSTART.md).

## What Success Looks Like

After setup, run:

```bash
.\.venv\Scripts\python.exe tools/setup_student.py   # Windows
./.venv/bin/python tools/setup_student.py           # macOS
```

You should see:

```text
  [OK] Python 3.13.x
  [OK] pip (...)
  [OK] pandas
  [OK] numpy
  [OK] matplotlib
  [OK] seaborn
  [OK] statsmodels
  [OK] pyarrow
  [OK] python-docx
  [OK] streamlit
  [OK] plotly
  [OK] fintools
```

Word report tooling is included in the Python setup through `python-docx`.
LaTeX is optional and only needed for legacy `.tex` reports or Beamer decks.

## Where Things Live

| Location | What's there |
|----------|-------------|
| `fins2026/week1/` through `week5/` | Weekly exercises currently released for the course, using the standard scaffold: docs, data, scripts, scratch, results, and guidance |
| `fins2026/weekN/data/` | Datasets for that week's exercises |
| `projects/` | Larger project work such as reports and presentations |
| `fintools/` | Shared Python utilities you can import |
| `fintools/figures/` | Figure helpers for plots and Word/A4 exports |
| `docs/apps/streamlit/` | Shared guidance for building public Streamlit apps |
| `boilerplate/` | Legacy LaTeX templates for reports and slides |

## Working with AI

This course is designed to work closely with AI. Read
[ai-workflow.md](ai-workflow.md) for:

- what the AI can help with
- example prompts you can try right now
- what you should verify yourself
- how to choose your AI path without guessing between multiple tools
- where the OpenCode in PyCharm guide lives
- where the PyCharm, support matrix, and troubleshooting docs live

## What's Next

After week 0, move into `week1/` and then continue through `week5/` as your
instructor directs. Later weeks `week6/` through `week10/` will be published
over time. When a new release is announced, update from the repo root with:

```bash
git pull --ff-only
```

In the meantime:

- complete the [setup checklist](checklist.md)
- read [ai-workflow.md](ai-workflow.md) and try some example prompts
- if you want to explore, ask your AI tool to scaffold a practice project
  such as `projects/test_project/`

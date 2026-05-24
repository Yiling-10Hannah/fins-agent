# Working with AI in This Course

AI is not an optional add-on. It is part of how this course works. Think
of the AI as a pair-programmer: it writes code with you, explains errors,
drafts sections of your reports, and helps you iterate faster.

## What the AI Can Help With

| Task | Example prompt |
|------|---------------|
| **Setup and errors** | "I'm getting this error when I run my script: [paste error]" |
| **OpenCode in PyCharm** | "Read `AGENTS.md`, then help me run onboarding from the repo root" |
| **Loading data** | "Help me load the CSV file in `data/` and show the first few rows" |
| **Analysis** | "Calculate daily returns and annualized volatility for each stock" |
| **Charts** | "Plot a line chart of cumulative returns for these three portfolios" |
| **Tables** | "Create a summary statistics table and format it for my Word report" |
| **Writing** | "Write the introduction section of my report" |
| **Editing** | "Revise this paragraph for clarity and active voice" |
| **Presentations** | "Build me a 12-slide PowerPoint deck for my project" |
| **Debugging** | "My Word report outline looks wrong. Here is the file path." |
| **Explaining** | "What does this regression output mean?" |

## Available Workflows

This repo has shared workflows, but you should not memorize every agent's
invocation surface from this page. Use the routing docs instead:

- Start here: `../../docs/ai/start-here.md`
- PyCharm setup: `../../docs/setup/pycharm.md`
- Support matrix: `../../docs/setup/ai-support-matrix.md`
- AI troubleshooting: `../../docs/setup/ai-troubleshooting.md`

The common first-step commands are:

| Tool path | First move |
|----------|------------|
| OpenCode in PyCharm | open AI Chat, add OpenCode, choose `MiniMax M2.5 Free`, then ask it to read `AGENTS.md` and help onboard |
| Claude Code | `/onboard` |
| Claude Code in PyCharm | run `claude` in PyCharm's terminal, then `/onboard` |
| OpenAI Codex | run `/status`, then `/skills`, then ask naturally for onboarding or use `$onboard` |
| Codex in PyCharm | start with a grounding prompt, then attach `AGENTS.md` if repo-specific context is missing |
| Gemini CLI | `/onboard` |
| Gemini CLI in PyCharm | use the Gemini agent in AI Chat, then `/onboard` |
| Qwen Code | ask naturally for onboarding or use `/skills onboard` |
| Qwen Code in PyCharm | ask naturally for onboarding or use `/skills onboard` |

Detailed guides:

- OpenCode in PyCharm: `../../docs/ai/opencode-pycharm.md`
- OpenAI Codex: `../../docs/ai/codex.md`
- Codex in PyCharm: `../../docs/ai/codex-pycharm.md`
- Claude Code: `../../docs/ai/claude.md`
- Claude Code in PyCharm: `../../docs/ai/claude-pycharm.md`
- Gemini guide: `../../docs/ai/gemini.md`
- Gemini in PyCharm guide: `../../docs/ai/gemini-pycharm.md`
- Qwen guide: `../../docs/ai/qwen.md`
- Qwen in PyCharm guide: `../../docs/ai/qwen-pycharm.md`

## What You Should Verify Yourself

The AI is a tool, not an oracle. Always check:

- **Numbers and results** - verify calculations make sense economically
- **Citations** - confirm papers exist and details are correct
- **Interpretation** - you are responsible for the economic argument
- **Data quality** - check for missing values, outliers, or errors before
  trusting analysis output

## How to Get the Best Results

1. **Be specific.** "Compute the Sharpe ratio for the equal-weight
   portfolio using monthly returns from 2015-2025" beats "analyze the
   data."

2. **Show your work.** Paste your code, error messages, Word report path, or
   report excerpt. The AI needs context to help effectively.

3. **Iterate.** If the first answer is not right, say what is wrong and
   ask for a revision.

4. **Ask for explanations.** "Why did you use a Newey-West correction
   here?" helps you learn, not just produce output.

5. **Use the workflows.** The writing and proofing workflows catch weak
   words, passive voice, and formatting issues that you would miss
   manually. If you forget how your tool invokes them, go back to
   `../../docs/ai/start-here.md` or `../../docs/setup/ai-support-matrix.md`
   instead of guessing.

## OpenCode Note

OpenCode in PyCharm is a useful extra path if you want current free models in
AI Chat. In this course:

- finish GitHub account setup before OpenCode auth
- use `MiniMax M2.5 Free` first for significant coding work
- treat the live PyCharm model picker as the source of truth because the free
  model list can change
- do not run `/init` in this repo because `AGENTS.md` already exists

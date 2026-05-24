# AI Context Audit Checklist

Use this checklist after changing assistant context files, adding a workflow,
or seeing a setup failure from a trial run.

## Source Of Truth

- `AGENTS.md` stays short, concrete, and repo-level.
- `docs/ai/workflows/*.md` owns workflow behavior.
- `docs/ai/rules/*.md` owns writing, Word reporting, citation,
  presentation, and legacy LaTeX rules.
- Assistant-specific wrappers point to shared docs instead of duplicating
  procedure.
- If a wrapper conflicts with a shared doc, update the wrapper or shared doc
  so the conflict disappears.
- Public AI surfaces must not expose internal-only workflows, local private
  workspaces, or solution-material references.

## Codex Checks

- `AGENTS.md` names repo layout, commands, conventions, and done criteria.
- `.agents/skills/*/SKILL.md` has clear `name` and `description`
  frontmatter with "Use when..." routing.
- `.agents/skills/*/agents/openai.yaml` exists for every Codex skill.
- Legacy LaTeX skills set `policy.allow_implicit_invocation: false`.
- `.codex/config.toml` parses, has the schema hint, and does not force
  model, sandbox, or approval settings.
- Project MCP servers are useful and scoped; OpenAI docs uses
  `openaiDeveloperDocs`.

## Student Defaults

- Onboarding does not require LaTeX.
- Word `.docx` is the default report path.
- Legacy LaTeX appears only as explicit opt-in.
- Setup commands use the repo interpreter and `python -m pip`.
- Windows guidance distinguishes environment restrictions from repo bugs.

## Cross-Agent Consistency

- Claude, Codex, Gemini, and Qwen surfaces reference the same shared
  workflows.
- `.claude/rules/*` mirrors `docs/ai/rules/*` for compatibility.
- Gemini commands and Qwen skills expose the same workflow set as Codex.
- PyCharm-specific docs call out host limitations without changing the repo
  contract.

## Verification

- Confirm `rg --version` and `rg --files -g AGENTS.md` when ripgrep is
  available. Missing `rg` is an advisory setup warning, not a Python setup
  failure.
- Run `.\.venv\Scripts\python.exe -m ruff check .` on Windows.
- Run `.\.venv\Scripts\python.exe -m pytest -q` on Windows.
- Confirm `rg -n "\.claude/rules" AGENTS.md README.md GEMINI.md QWEN.md docs/ai -g "!CONTEXT_AUDIT.md"`
  only returns Claude-specific compatibility notes.
- Commit context changes in a scoped commit after verification.

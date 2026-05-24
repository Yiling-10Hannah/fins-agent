# Shared Workflow Docs

These workflow docs are the tool-agnostic source of truth for repo
behavior. For deterministic tasks, the shared helper surface is:

```bash
python tools/workflow.py list
```

- Claude wrappers live in `.claude/skills/`
- Codex skills live in `.agents/skills/`
- Gemini commands live in `.gemini/commands/`
- Qwen skills live in `.qwen/skills/`
- Repo-wide instructions live in `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`,
  and `QWEN.md`

If an assistant-specific adapter and a shared workflow doc conflict, the
shared workflow doc wins.

## Workflow Index

- `onboard.md`
- `new-project.md`
- `scaffold-week.md`
- `setup-paper.md`
- `word-report.md`
- `write-section.md`
- `edit-section.md`
- `proofread.md`
- `build-paper.md`
- `build-deck.md`
- `build-figure.md`
- `build-app.md`
- `audit-app.md`
- `build-context.md`
- `build-week-context.md`
- `outline.md`
- `latex-doctor.md`

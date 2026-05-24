# Codex in PyCharm Guide

This guide is for students using Codex inside PyCharm through JetBrains AI.
This is different from OpenAI-native Codex in the CLI, Codex app, or
OpenAI IDE extension.

For the OpenAI-native Codex path, use `docs/ai/codex.md`.

## What This Path Is

- PyCharm 2025.3+ with the AI Assistant plugin
- Codex selected in the JetBrains AI chat agent picker
- Recommended authentication: ChatGPT account
- Alternatives: JetBrains AI subscription or an OpenAI API key
- `Agent` mode is the default working mode
- `Read-only` is for explanation and inspection
- `Agent (full access)` should only be used when a task genuinely needs
  broader machine access
- JetBrains AI agent mode does not work in WSL

## Path 1: Codex in PyCharm via JetBrains AI

1. Open this repo in PyCharm.
2. Install or enable the AI Assistant plugin.
3. Open AI Chat and select Codex in the agent picker.
4. Sign in with your ChatGPT account.
5. Start with a grounding prompt such as:

   ```text
   Read AGENTS.md, summarize how this repo is organized, then help me run onboarding.
   ```

6. If Codex seems to miss repo-specific workflow context, attach `AGENTS.md`
   and the relevant file from `docs/ai/workflows/` explicitly in the chat.
7. Run setup commands from PyCharm's built-in terminal at the repo root.
8. Treat this path as IDE-first convenience, not guaranteed CLI parity.

If you ask Codex in PyCharm to install a Python package, it should update
`requirements.txt` or `requirements-dev.txt` first and run the install from
PyCharm's built-in terminal with the repo interpreter. If the host chat path
cannot do that cleanly, switch to the Codex CLI path in the same PyCharm
terminal.

## Path 2: Codex CLI in PyCharm's Terminal

Use this path when you want the most repo-native Codex behavior.

1. Open PyCharm's built-in terminal at the repo root. On Windows, prefer
   PowerShell or cmd over Git Bash - see
   [terminal shell notes](../setup/pycharm.md#choosing-a-terminal-shell).
2. Launch the Codex CLI from that directory.
3. Use `/status`, `/skills`, and `/mcp` to inspect what Codex loaded.
4. Ask naturally for the task or explicitly invoke the matching skill with
   `$<skill-name>`.
5. If the CLI still looks wrong, use `/debug-config` and then
   `../setup/ai-troubleshooting.md`.

This is the path that should honor `AGENTS.md`, `.agents/skills/`, and
`.codex/config.toml` directly.

## What Context Is Safe To Assume

Safe to assume in PyCharm Codex:

- IDE project files and codebase context available through JetBrains AI
- attached files, folders, and selected code
- JetBrains approval, rollback, and chat history UI

Do not assume without checking in PyCharm:

- repo `.agents/skills/` appears in `/skills`
- repo `.codex/config.toml` is loaded automatically
- repo MCP servers appear in `/mcp`

If those repo-native surfaces do not show up, fall back to attaching
`AGENTS.md`, pointing Codex at the relevant workflow doc, and working from
the repo root in the IDE.

## Common Failure Modes

- Codex is missing from JetBrains AI Chat: verify the AI Assistant plugin,
  supported PyCharm version, and Codex availability in the agent picker
- PyCharm Codex does not reflect repo workflows: attach `AGENTS.md` and the
  relevant workflow doc explicitly
- `/skills` does not show repo skills: use natural-language prompting in
  PyCharm, or switch to the CLI path for clearer repo-native behavior
- `/mcp` does not show expected servers: treat that as a PyCharm-hosted
  limitation unless the CLI path also fails
- PyCharm and the terminal seem to see different files: confirm both are at
  the same repo root

Use `../setup/ai-troubleshooting.md` for the detailed fix steps.

## Which Path To Use

| Path | Best for |
|------|----------|
| Codex in PyCharm | quick IDE chat, attached files, and JetBrains approval UI |
| Codex CLI in PyCharm terminal | the clearest repo-native Codex behavior, including `/skills` and `/mcp` |

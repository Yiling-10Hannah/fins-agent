# AI Support Matrix

Use this page when you need the exact support status for a tool, host
surface, or PyCharm integration.

## Recommended Student Rule

- Default IDE: PyCharm
- Default AI policy: use the supported tool you already have access to
- Default setup shell: PyCharm's built-in terminal at the repo root
- If a PyCharm-hosted path is flaky, fall back to the agent's terminal path

## Supported Paths

| Path | Host surface | Minimum PyCharm | Install method | Auth path | JetBrains AI subscription required | WSL | Repo-native context guarantee | Recommended first action |
|---|---|---|---|---|---|---|---|---|
| Claude Code | Normal terminal | N/A | `npm install -g @anthropic-ai/claude-code` | Claude.ai or Anthropic Console | No | Vendor docs support WSL or Git Bash on Windows | Full Claude repo context | `/onboard`; install Python 3.13 first if missing |
| Claude Code in PyCharm | Claude Code JetBrains plugin | Repo baseline: PyCharm 2025.1+ | install Claude Code locally and install the plugin | Claude.ai or Anthropic Console | No | WSL needs extra setup; native Windows / Git Bash path is simpler | Full Claude repo context | run `claude` in PyCharm terminal, then `/onboard` |
| OpenCode in PyCharm | JetBrains ACP agent | PyCharm 2025.3.2+ | Add ACP Agent in AI Chat; if unavailable, add a custom ACP agent with `opencode acp` | OpenCode Zen API key after GitHub setup for the course path | No for ACP agents | JetBrains ACP agents do not support WSL | `AGENTS.md` project rules through OpenCode ACP; if context looks wrong, attach `AGENTS.md` explicitly | finish GitHub setup, add OpenCode in AI Chat, choose `MiniMax M2.5 Free`, then ask it to read `AGENTS.md` and help onboard |
| OpenAI Codex | CLI, app, or OpenAI IDE extension | N/A | `npm install -g @openai/codex` or use the app | ChatGPT account or OpenAI API key | No | Vendor docs apply | Full Codex repo context when launched from repo root | run `/status`, then `/skills`, then `$onboard` or say "set me up" |
| Codex in PyCharm | JetBrains AI Chat | PyCharm 2025.3+ | install AI Assistant, then install Codex from the agent picker | ChatGPT account, OpenAI API key, or JetBrains AI | No if using ChatGPT or API key | JetBrains agent mode does not support WSL | Partial until `/skills` and `/mcp` confirm repo state | start with a grounding prompt, then fall back to attached `AGENTS.md` and workflow docs if repo-native surfaces are not visible |
| Gemini CLI | Normal terminal | N/A | `npm install -g @google/gemini-cli` | Google login, Gemini API key, or Vertex AI | No | Vendor docs apply | Full Gemini repo context | `/onboard`; install Python 3.13 first if missing |
| Gemini CLI in PyCharm | JetBrains ACP agent | PyCharm 2025.3.2+ | ACP registry install if available, otherwise custom ACP agent | authenticate through Gemini CLI | No for ACP agents | JetBrains ACP agents do not support WSL | Intended Gemini repo context; if the ACP path drifts, use the terminal path as the reference behavior | `/onboard`; if the ACP path drifts, switch to the terminal path |
| Qwen Code | Normal terminal | N/A | `npm install -g @qwen-code/qwen-code@latest` | Qwen OAuth / account login | No | Vendor docs apply | Full Qwen repo context | ask naturally for onboarding or use `/skills onboard`; install Python 3.13 first if missing |
| Qwen Code in PyCharm | JetBrains ACP agent | PyCharm 2025.3.2+ | ACP registry install if available, otherwise custom ACP agent with `--acp` | authenticate through Qwen Code | No for ACP agents | JetBrains ACP agents do not support WSL | Intended Qwen repo context; if the ACP path drifts, use the terminal path as the reference behavior | ask naturally for onboarding or use `/skills onboard`; if the ACP path drifts, switch to the terminal path |

## Context Guarantee Levels

- Full Claude repo context:
  `CLAUDE.md`, `.claude/skills/`, `.claude/rules/`, shared workflow docs
- Full Codex repo context:
  `AGENTS.md`, `.agents/skills/`, `.codex/config.toml`, shared workflow docs
- OpenCode ACP repo context:
  `AGENTS.md` project rules through OpenCode ACP; this repo does not yet ship
  OpenCode-specific wrapper files
- Full Gemini repo context:
  `GEMINI.md`, `.gemini/settings.json`, `.gemini/commands/`, shared workflow docs
- Full Qwen repo context:
  `AGENTS.md`, `QWEN.md`, `.qwen/settings.json`, `.qwen/skills/`, shared workflow docs
- Host-dependent PyCharm Codex context:
  the JetBrains-hosted Codex path may differ from the CLI unless `/skills`
  and `/mcp` confirm repo state

Note on naming: Claude, Gemini, and Qwen each have a root `*.md` file
(`CLAUDE.md`, `GEMINI.md`, `QWEN.md`). Codex intentionally does not - by
OpenAI convention, Codex reads `AGENTS.md` at the repo root, so the absence
of a `CODEX.md` is expected and does not indicate weaker support.

## Reference Pages

- `../ai/start-here.md`
- `../ai/opencode-pycharm.md`
- `pycharm.md`
- `ai-troubleshooting.md`

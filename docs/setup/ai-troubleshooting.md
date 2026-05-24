# AI Troubleshooting

This page covers AI-agent installation, shell, auth, and PyCharm-hosted
integration failures. For Python, pip, Word report tooling, and interpreter issues, use
`troubleshooting.md`.

## Install Prerequisites

| Agent | Common install path | Key prerequisite |
|---|---|---|
| Claude Code | `npm install -g @anthropic-ai/claude-code` | Node.js 18+ |
| OpenCode | `npm install -g opencode-ai` | Node.js if using npm install |
| OpenAI Codex CLI | `npm install -g @openai/codex` | Node.js if using npm install |
| Gemini CLI | `npm install -g @google/gemini-cli` | Node.js |
| Qwen Code | `npm install -g @qwen-code/qwen-code@latest` | Node.js 20+ |

If the install command itself is missing or blocked, keep reading.

## Windows Shell And PATH Issues

### `npm` is not recognized

**Error**

```text
npm : The term 'npm' is not recognized...
```

**Cause**

Node.js is missing, so npm is missing too.

**Fix**

Install Node.js LTS, then restart PowerShell or the PyCharm terminal:

```powershell
winget install OpenJS.NodeJS.LTS
```

This is the most likely install blocker for Claude Code, Gemini CLI, and
Qwen Code. It can also affect OpenCode and OpenAI Codex if you install them
through npm.

### PowerShell blocks `npm.ps1`

**Error**

```text
File ...\npm.ps1 cannot be loaded because running scripts is disabled...
```

**Cause**

PowerShell execution policy blocks npm's PowerShell shim.

**Fix**

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Confirm with `Y`, then reopen the terminal and re-run the install.

This failure was observed directly during Claude Code installation on
Windows and is likely to recur for any npm-installed coding agent.

### `<agent>` is not recognized

**Error examples**

```text
claude : The term 'claude' is not recognized...
opencode : The term 'opencode' is not recognized...
codex : The term 'codex' is not recognized...
gemini : The term 'gemini' is not recognized...
qwen : The term 'qwen' is not recognized...
```

**Cause**

- the agent CLI is not installed
- PATH has not refreshed after install
- PyCharm is still using an older shell environment

**Fix**

1. Install the correct CLI.
2. Close and reopen the terminal.
3. If the command works in a normal terminal but not in PyCharm, restart
   PyCharm completely.

### Codex or Claude fails before reading the repo

**Symptoms**

- the agent errors before `/status`, `/skills`, `/mcp`, or `/onboard` works
- the error mentions auth, model access, or an unsupported/default model
- the agent never reaches `AGENTS.md` or `CLAUDE.md`

**Fix**

Check the CLI itself before diagnosing the repo:

```bash
codex --version
claude --version
```

Update the CLI if it is old, complete the login/auth flow in a normal
terminal, and choose a model your account and CLI version support. After the
agent starts cleanly, relaunch it from the repo root and rerun the repo
context checks.

### `rg` is not recognized

**Cause**

`ripgrep` is missing or the terminal has not refreshed PATH after install.
AI assistants use `rg` for fast repo search. They can still work without it,
but file search will be slower.

**Fix**

Windows:

```powershell
winget install --id BurntSushi.ripgrep.MSVC -e
```

macOS:

```bash
brew install ripgrep
```

Then close and reopen PowerShell, Terminal, or PyCharm and verify:

```bash
rg --version
rg --files -g AGENTS.md
```

### `python` is missing or the wrong version

**Symptoms**

- `python` is not recognized
- `python --version` prints something other than 3.13
- onboarding says Python 3.13 is required

**Fix**

- install Python 3.13
- restart the terminal
- on Windows, try `py -3.13 --version`
- then rerun the repo bootstrap or onboarding helper

### `winget` is not recognized

**Cause**

App Installer is missing or Windows is outdated.

**Fix**

- update Windows / install App Installer
- or install Node.js, Python, or Git manually from vendor download pages

## PyCharm And JetBrains AI Issues

### AI Chat or AI Assistant is missing

**Cause**

The AI Assistant plugin is not installed or enabled.

**Fix**

- install or enable AI Assistant in PyCharm
- restart the IDE fully

### ACP agent missing from AI Chat

**Cause**

- ACP registry not available in your IDE build
- the agent is not installed locally
- the agent needs to be added manually as a custom ACP agent

**Fix**

- try the ACP registry first
- if unavailable, add the agent manually through the Agents settings
- if that fails, use the terminal path instead

This applies most directly to OpenCode, Gemini CLI, and Qwen Code in
PyCharm.

### PyCharm terminal cannot find the agent, but a normal terminal can

**Cause**

PyCharm inherited an older PATH before the install completed.

**Fix**

- close all PyCharm terminals
- restart PyCharm
- verify the command again

### JetBrains-hosted agent path fails under WSL

**Cause**

JetBrains AI Agent mode and ACP agents currently do not support WSL.

**Fix**

- use native Windows PyCharm + native Windows terminal path
- or use the agent directly in a normal terminal outside the PyCharm-hosted
  path

## Auth And Account Issues

### Claude Code login confusion

Use one of these:

- Claude.ai account
- Anthropic Console account with active billing

If login fails, start `claude` in a normal terminal first and complete the
auth flow there.

### Codex login confusion in PyCharm

Codex in JetBrains can use:

- ChatGPT account
- OpenAI API key
- JetBrains AI

If the wrong auth path keeps winning, check the provider settings in
JetBrains AI Assistant and log out of the conflicting provider.

### OpenCode Zen login issues

In this course, complete GitHub account setup before this step.

OpenCode Zen currently supports sign-in through the OpenCode auth page. If
PyCharm AI Chat is not prompting cleanly, do the auth step in a normal
terminal first:

- if the auth page shows multiple sign-in options, use the GitHub-backed
  course path
- run `opencode auth login`
- or run `opencode`, then use `/connect`
- choose OpenCode Zen
- sign in, copy the API key, and finish the auth flow

After that, return to PyCharm AI Chat and start a new OpenCode chat.

### Gemini CLI login issues

Gemini CLI supports:

- Google login
- Gemini API key
- Vertex AI

If PyCharm ACP is not prompting cleanly, run `gemini` in a normal terminal
first, authenticate there, then return to PyCharm.

### Qwen Code login issues

Qwen Code typically authenticates on first interactive launch. If login is
not complete in PyCharm, run `qwen` in a normal terminal first and complete
the auth flow there.

## Repo Context And Working Directory Issues

### The agent is in the wrong folder

**Symptoms**

- onboarding cannot find repo files
- skills or commands look unrelated
- edits target the wrong project

**Fix**

Start the agent from the repo root:

```text
.../fins-agent
```

The PyCharm project root and the terminal working directory should match.

### Repo-specific skills or commands are missing

**Claude**

- start from the repo root
- confirm `CLAUDE.md` and `.claude/skills/` exist

**Codex**

- start from the repo root
- use `/status`, `/skills`, and `/mcp`
- if the PyCharm-hosted path does not show expected repo state, attach
  `AGENTS.md` and the relevant workflow doc or switch to the CLI path

**OpenCode**

- start from the repo root
- OpenCode ACP can use project-specific rules from `AGENTS.md`
- do not run `/init` in this repo because `AGENTS.md` already exists
- if context looks wrong in PyCharm, attach `AGENTS.md` explicitly or finish
  auth in the terminal path first

**Gemini**

- start from the repo root
- confirm `GEMINI.md` and `.gemini/commands/` exist

**Qwen**

- start from the repo root
- ask naturally or use `/skills <workflow>`
- confirm `AGENTS.md`, `QWEN.md`, and `.qwen/skills/` exist

### Project-scoped config is ignored

For Codex, `.codex/config.toml` only applies when the project is trusted.
If it seems ignored, confirm the project is trusted or use the CLI from the
repo root.

## Agent-Specific Notes

### Claude Code

- Windows install can fail because Node.js is missing or PowerShell blocks
  `npm.ps1`
- JetBrains plugin may need a full IDE restart
- if the plugin cannot find `claude`, set the Claude command path manually

### OpenAI Codex

- if installed with npm, the same Windows npm and execution-policy issues
  can apply
- in PyCharm, install Codex from the agent picker if it is not already
  available
- use `/status`, `/skills`, and `/mcp` to inspect what loaded
- if the CLI still looks wrong, use `/debug-config` before assuming the
  repo config is broken

### OpenCode

- the easiest PyCharm path is Add ACP Agent in AI Chat
- if OpenCode is missing from the agent list, add a custom ACP agent with
  `opencode acp`
- OpenCode Zen is not a blanket free plan; it currently exposes a changing
  subset of free models alongside paid models
- if auth works in a normal terminal but not in AI Chat, complete
  `opencode auth login` or `/connect` in the terminal first
- if OpenCode suggests creating a new `AGENTS.md`, do not overwrite the
  repo file

### Gemini CLI

- install commonly uses npm, so Node.js and PowerShell policy issues can
  apply
- if ACP registry install is unavailable, use a custom ACP agent or the
  terminal path
- if Gemini in PyCharm behaves differently from Gemini in a normal
  terminal, trust the terminal path first and treat the ACP host as the
  variable

### Qwen Code

- requires Node.js 20+ for the npm install path
- if the PyCharm agent path is unavailable, use a custom ACP agent with
  `--acp` or use the terminal path
- if explicit workflow invocation is needed, use `/skills <workflow>`
- if Qwen in PyCharm behaves differently from Qwen in a normal terminal,
  trust the terminal path first and treat the ACP host as the variable

## Still Stuck

1. Re-run `tools/setup_student.py` with the repo interpreter
2. Re-check `pycharm.md`
3. Re-check `ai-support-matrix.md`
4. Post the exact error, OS, shell, and command you ran

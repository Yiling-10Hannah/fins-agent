# OpenCode In PyCharm Guide

This guide is for students using OpenCode inside PyCharm through JetBrains ACP.

This is not OpenAI Codex. OpenCode is a separate coding agent that can still
use this repo's `AGENTS.md`.

## Before You Start

- complete GitHub account setup first
- open this repo in PyCharm as one project root
- install or enable the AI Assistant plugin
- use native Windows PyCharm if you are on Windows; JetBrains ACP agents do
  not support WSL

In this course, treat GitHub as required before the OpenCode setup step.

## Recommended Path: OpenCode In AI Chat

1. Open AI Chat in PyCharm.
2. Click **Add ACP Agent**.
3. Search for **OpenCode** and install it.
4. Start a new OpenCode chat.
5. Authenticate OpenCode Zen.
6. Pick a model from the AI Chat model dropdown.
7. Start with this prompt:

   ```text
   Read AGENTS.md, summarize how this repo is organized, then help me run onboarding.
   ```

If repo-specific context looks weak, attach `AGENTS.md` explicitly in the
chat.

## OpenCode Zen Auth

OpenCode Zen is the course-recommended provider for this path.

The reliable auth sequence is:

1. make sure your GitHub account is already ready
2. sign in to OpenCode Zen
3. copy the API key
4. finish the auth flow in PyCharm or the OpenCode terminal flow

At the time of writing, the OpenCode auth page offers more than one sign-in
option. For this course path, use your GitHub-backed setup.

If PyCharm AI Chat does not prompt cleanly, authenticate in a terminal first:

```bash
opencode auth login
```

Or launch OpenCode and use:

```text
/connect
```

Then return to PyCharm and start a new OpenCode chat.

## Model Guidance

As of **May 1, 2026**, the course recommendation is:

- use `MiniMax M2.5 Free` first for significant coding work
- use `Big Pickle` next if `MiniMax M2.5 Free` is unavailable
- treat the other free models as fallbacks rather than your default path

The current live OpenCode Zen free-model list can change. At the time of this
guide, the live OpenCode model list shows these free options:

- `MiniMax M2.5 Free`
- `Big Pickle`
- `Ling 2.6 Flash Free`
- `Hy3 Preview Free`
- `Trinity Large Preview Free`
- `Nemotron 3 Super Free`

Two important notes:

- OpenCode Zen is not a blanket free plan. It mixes free models and paid
  models.
- The model picker in PyCharm is the source of truth if the live list changes.
- `GPT 5 Nano` is available in OpenCode Zen, but it is not part of the
  current free-model list.

## Repo Context In This Course

OpenCode ACP supports project-specific rules from `AGENTS.md`.

That matters here because this repo already ships its own `AGENTS.md`.

Use these rules:

- let OpenCode read `AGENTS.md`
- do not run `/init` in this repo to create a new `AGENTS.md`
- if OpenCode suggests replacing `AGENTS.md`, keep the repo file and point the
  agent back to it

## Manual ACP Fallback

If OpenCode is missing from **Add ACP Agent**, use the custom ACP path.

Install OpenCode locally if needed:

```bash
npm install -g opencode-ai
```

Then add a custom ACP agent that runs:

```text
command: opencode
args: acp
```

If auth still behaves better in the terminal than in AI Chat, trust the
terminal path first and return to PyCharm after auth succeeds.

## Common Failure Modes

- OpenCode is missing from AI Chat: use the custom ACP agent path
- auth works in the terminal but not in AI Chat: complete `opencode auth login`
  or `/connect` in the terminal first
- the wrong files appear in chat: confirm PyCharm opened the real
  `fins-agent` folder
- OpenCode suggests `/init`: do not overwrite the repo `AGENTS.md`
- the model list looks different from this page: trust the live model picker

## Related Docs

- `../setup/pycharm.md`
- `../setup/ai-support-matrix.md`
- `../setup/ai-troubleshooting.md`
- `start-here.md`

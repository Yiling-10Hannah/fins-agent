# Codex Review Checklist

Use this checklist for `/review`, review-style prompts, and final checks after
Codex changes code, docs, or workflow files.

## Review Priorities

1. Identify bugs, regressions, unsafe setup behavior, and missing tests first.
2. Check whether the change follows repo conventions in `AGENTS.md`.
3. Confirm student-facing instructions are Word-first unless the task is
   explicitly legacy LaTeX.
4. Preserve user changes and avoid unrelated rewrites.
5. Keep machine-specific workarounds out of shared code when a local override
   is enough.

## Verification Expectations

- For Python behavior changes, run focused tests and then `-m pytest -q` when
  practical.
- For shared helpers, run `-m ruff check .`.
- For setup changes, verify the relevant bootstrap or `tools/workflow.py`
  command path.
- For docs-only changes, check links, paths, and whether student commands still
  match the repo interpreter model.

## Done Criteria

- The requested behavior is implemented or the remaining blocker is explicit.
- Tests or checks relevant to the risk have run.
- The final diff avoids unrelated churn.
- Any skipped verification is named with the reason.

"""Tests for assistant-specific workflow surfaces."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARED_FIGURE_WORKFLOW = "docs/ai/workflows/build-figure.md"
DATAFRAME_EXAMPLE = "docs/ai/examples/figure_suite_from_dataframe.py"


def read_repo_text(*parts: str) -> str:
    return (ROOT.joinpath(*parts)).read_text(encoding="utf-8")


def test_claude_build_figure_skill_exposes_dataframe_suite_path() -> None:
    skill_text = read_repo_text(".claude", "skills", "build-figure", "SKILL.md")

    assert SHARED_FIGURE_WORKFLOW in skill_text
    assert "build-figure-suite" in skill_text
    assert "--narrative" in skill_text


def test_claude_docs_point_dataframe_requests_to_narrative_suite() -> None:
    claude_doc = read_repo_text("docs", "ai", "claude.md")
    pycharm_doc = read_repo_text("docs", "ai", "claude-pycharm.md")

    assert "build-figure-suite" in claude_doc
    assert DATAFRAME_EXAMPLE in claude_doc
    assert 'create_figure_suite(df, style="ft", docx=True, narrative=True)' in claude_doc
    assert "create_figure_suite" in pycharm_doc
    assert "narrative=True" in pycharm_doc


def test_gemini_build_figure_command_exposes_dataframe_suite_path() -> None:
    command_text = read_repo_text(".gemini", "commands", "build-figure.toml")

    assert SHARED_FIGURE_WORKFLOW in command_text
    assert "build-figure-suite" in command_text
    assert "--narrative" in command_text


def test_gemini_docs_point_dataframe_requests_to_narrative_suite() -> None:
    gemini_doc = read_repo_text("docs", "ai", "gemini.md")
    pycharm_doc = read_repo_text("docs", "ai", "gemini-pycharm.md")

    assert "build-figure-suite" in gemini_doc
    assert DATAFRAME_EXAMPLE in gemini_doc
    assert 'create_figure_suite(df, style="ft", docx=True, narrative=True)' in gemini_doc
    assert "create_figure_suite" in pycharm_doc
    assert "narrative=True" in pycharm_doc


def test_qwen_build_figure_skill_exposes_dataframe_suite_path() -> None:
    skill_text = read_repo_text(".qwen", "skills", "build-figure", "SKILL.md")

    assert SHARED_FIGURE_WORKFLOW in skill_text
    assert "build-figure-suite" in skill_text
    assert "--narrative" in skill_text


def test_qwen_docs_point_dataframe_requests_to_narrative_suite() -> None:
    qwen_doc = read_repo_text("docs", "ai", "qwen.md")
    pycharm_doc = read_repo_text("docs", "ai", "qwen-pycharm.md")

    assert "build-figure-suite" in qwen_doc
    assert DATAFRAME_EXAMPLE in qwen_doc
    assert 'create_figure_suite(df, style="ft", docx=True, narrative=True)' in qwen_doc
    assert "create_figure_suite" in pycharm_doc
    assert "narrative=True" in pycharm_doc


def test_shared_figure_suite_references_exist() -> None:
    assert (ROOT / SHARED_FIGURE_WORKFLOW).is_file()
    assert (ROOT / DATAFRAME_EXAMPLE).is_file()

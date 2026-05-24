"""Smoke tests for assistant-specific repo surfaces."""

from __future__ import annotations

import json
import re
import tomllib
from pathlib import Path

from tools import workflow_lib

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = {
    "audit-app",
    "build-context",
    "build-week-context",
    "build-deck",
    "build-figure",
    "build-app",
    "build-paper",
    "edit-section",
    "latex-doctor",
    "new-project",
    "onboard",
    "outline",
    "proofread",
    "scaffold-week",
    "setup-paper",
    "word-report",
    "write-section",
}
LEGACY_CODEX_SKILLS = {"build-paper", "latex-doctor"}
WORD_FIRST_CODEX_SKILLS = {
    "build-context",
    "edit-section",
    "proofread",
    "setup-paper",
    "word-report",
    "write-section",
}
SHARED_AI_DOCS_WITHOUT_CLAUDE_RULE_REFERENCES = [
    ROOT / "AGENTS.md",
    ROOT / "GEMINI.md",
    ROOT / "README.md",
    ROOT / "QWEN.md",
    ROOT / "docs" / "ai" / "codex.md",
    ROOT / "docs" / "ai" / "core.md",
    ROOT / "docs" / "ai" / "gemini.md",
    ROOT / "docs" / "ai" / "qwen.md",
    ROOT / "docs" / "ai" / "writing.md",
]
CLAUDE_RULE_MIRRORS = {
    "README.md": "README.md",
    "academic-writing.md": "academic-writing.md",
    "banned-words.md": "banned-words.md",
    "citation-verification.md": "latex-citations.md",
    "grammar-punctuation.md": "grammar-punctuation.md",
    "legacy-latex.md": "latex-conventions.md",
    "presentation.md": "presentation-rules.md",
    "word-reporting.md": "word-reporting.md",
}


def workflow_docs() -> list[Path]:
    return sorted((ROOT / "docs" / "ai" / "workflows").glob("*.md"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = read_text(path)
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.DOTALL)
    assert match, f"missing YAML frontmatter in {path}"
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields


def test_shared_workflow_docs_cover_expected_workflows() -> None:
    workflow_dir = ROOT / "docs" / "ai" / "workflows"
    found = {path.stem for path in workflow_dir.glob("*.md") if path.stem != "README"}
    assert found == WORKFLOWS


def test_python_packaging_surfaces_use_python_313_and_requirements_files() -> None:
    pyproject = tomllib.loads(read_text(ROOT / "pyproject.toml"))
    assert pyproject["project"]["requires-python"] == ">=3.13,<3.14"
    assert pyproject["tool"]["ruff"]["target-version"] == "py313"
    assert read_text(ROOT / ".python-version").strip() == "3.13"

    requirements = read_text(ROOT / "requirements.txt")
    for expected in [
        "pandas>=2.0",
        "numpy>=1.24",
        "matplotlib>=3.7",
        "seaborn>=0.13",
        "statsmodels>=0.14",
        "pyarrow>=14.0",
        "python-docx>=1.2",
        "Pillow>=10",
        "streamlit>=1.50,<2",
        "plotly>=6.1.1",
    ]:
        assert expected in requirements

    dev_requirements = read_text(ROOT / "requirements-dev.txt")
    for expected in ["pytest", "ruff", "-e ."]:
        assert expected in dev_requirements


def test_assistant_surfaces_cover_expected_workflows() -> None:
    for relative in [Path(".agents") / "skills", Path(".claude") / "skills"]:
        skill_dir = ROOT / relative
        found = {path.name for path in skill_dir.iterdir() if (path / "SKILL.md").is_file()}
        assert found == WORKFLOWS
        for workflow in WORKFLOWS:
            fields = parse_frontmatter(skill_dir / workflow / "SKILL.md")
            assert fields["name"] == workflow
            assert fields["description"]

    qwen_dir = ROOT / ".qwen" / "skills"
    found = {path.name for path in qwen_dir.iterdir() if (path / "SKILL.md").is_file()}
    assert found == WORKFLOWS
    for workflow in WORKFLOWS:
        fields = parse_frontmatter(qwen_dir / workflow / "SKILL.md")
        assert fields["name"] == workflow
        assert fields["description"]

    gemini_dir = ROOT / ".gemini" / "commands"
    found = {path.stem for path in gemini_dir.glob("*.toml")}
    assert found == WORKFLOWS
    for workflow in WORKFLOWS:
        command = tomllib.loads(read_text(gemini_dir / f"{workflow}.toml"))
        assert command["description"]
        assert command["prompt"]


def test_codex_project_config_is_minimal_and_parseable() -> None:
    config_path = ROOT / ".codex" / "config.toml"
    config_text = read_text(config_path)
    config = tomllib.loads(config_text)

    assert config_text.startswith(
        "#:schema https://developers.openai.com/codex/config-schema.json"
    )
    assert config["project_root_markers"] == [".git"]
    assert (
        config["mcp_servers"]["openaiDeveloperDocs"]["url"]
        == "https://developers.openai.com/mcp"
    )
    for user_owned_setting in ["model", "sandbox_mode", "approval_policy"]:
        assert user_owned_setting not in config


def test_codex_skill_openai_metadata_exists_for_each_skill() -> None:
    for workflow in WORKFLOWS:
        metadata_path = (
            ROOT / ".agents" / "skills" / workflow / "agents" / "openai.yaml"
        )
        assert metadata_path.is_file(), f"missing Codex metadata for {workflow}"
        metadata = read_text(metadata_path)
        assert "interface:" in metadata
        assert "display_name:" in metadata
        assert "short_description:" in metadata
        assert "default_prompt:" in metadata
        if workflow in LEGACY_CODEX_SKILLS:
            assert "allow_implicit_invocation: false" in metadata


def test_codex_word_first_skill_descriptions_keep_latex_explicit() -> None:
    for workflow in WORD_FIRST_CODEX_SKILLS:
        fields = parse_frontmatter(ROOT / ".agents" / "skills" / workflow / "SKILL.md")
        description = fields["description"]
        assert "Word" in description or ".docx" in description
        if "LaTeX" in description or ".tex" in description:
            lowered = description.lower()
            assert "legacy" in lowered
            assert "explicit" in lowered


def test_cross_agent_report_wrappers_keep_word_first_descriptions() -> None:
    qwen_word_first_skills = [
        "build-context",
        "edit-section",
        "proofread",
        "setup-paper",
        "write-section",
    ]
    claude_word_first_skills = ["build-context", "proofread"]

    descriptions: list[str] = []
    descriptions.extend(
        parse_frontmatter(ROOT / ".qwen" / "skills" / skill / "SKILL.md")[
            "description"
        ]
        for skill in qwen_word_first_skills
    )
    descriptions.extend(
        parse_frontmatter(ROOT / ".claude" / "skills" / skill / "SKILL.md")[
            "description"
        ]
        for skill in claude_word_first_skills
    )
    descriptions.extend(
        tomllib.loads(read_text(ROOT / ".gemini" / "commands" / f"{command}.toml"))[
            "description"
        ]
        for command in ["build-context", "proofread"]
    )

    for description in descriptions:
        assert "Word" in description or ".docx" in description
        assert "Word, LaTeX" not in description
        assert "Word or legacy LaTeX" not in description
        if "LaTeX" in description or ".tex" in description:
            lowered = description.lower()
            assert "legacy" in lowered
            assert "explicit" in lowered


def test_shared_writing_workflows_keep_latex_explicit() -> None:
    for path in [
        ROOT / "docs" / "ai" / "workflows" / "build-context.md",
        ROOT / "docs" / "ai" / "workflows" / "outline.md",
        ROOT / "docs" / "ai" / "workflows" / "proofread.md",
        ROOT / "docs" / "ai" / "writing.md",
    ]:
        text = read_text(path)
        assert "Word or legacy LaTeX" not in text
        assert "Word, LaTeX" not in text
        assert "otherwise the main `.tex` file" not in text
        if "legacy `.tex`" in text:
            assert "explicit" in text


def test_codex_build_deck_is_powerpoint_first() -> None:
    skill_text = read_text(ROOT / ".agents" / "skills" / "build-deck" / "SKILL.md")
    metadata = read_text(
        ROOT / ".agents" / "skills" / "build-deck" / "agents" / "openai.yaml"
    )
    workflow = read_text(ROOT / "docs" / "ai" / "workflows" / "build-deck.md")

    assert "PowerPoint-first" in skill_text
    assert "PowerPoint-first" in metadata
    assert "PowerPoint-first" in workflow
    assert "allow_implicit_invocation: false" not in metadata
    assert "only when explicitly requested" in workflow


def test_student_presentation_prompts_are_powerpoint_first() -> None:
    week0_ai_workflow = read_text(ROOT / "fins2026" / "week0" / "ai-workflow.md")
    assert "PowerPoint deck" in week0_ai_workflow
    assert "Beamer deck" not in week0_ai_workflow

    for path in [
        ROOT / "docs" / "ai" / "claude-pycharm.md",
        ROOT / "docs" / "ai" / "gemini-pycharm.md",
    ]:
        assert "`/build-deck` for PowerPoint decks" in read_text(path)

    assert "Legacy LaTeX boilerplate templates" in read_text(ROOT / "AGENTS.md")


def test_shared_ai_rules_are_tool_neutral_and_referenced() -> None:
    expected_rules = {
        "README.md",
        "academic-writing.md",
        "banned-words.md",
        "citation-verification.md",
        "grammar-punctuation.md",
        "legacy-latex.md",
        "presentation.md",
        "word-reporting.md",
    }
    rule_dir = ROOT / "docs" / "ai" / "rules"
    found_rules = {path.name for path in rule_dir.glob("*.md")}
    assert expected_rules <= found_rules

    for path in [
        *SHARED_AI_DOCS_WITHOUT_CLAUDE_RULE_REFERENCES,
        *workflow_docs(),
    ]:
        assert ".claude/rules" not in read_text(path), path


def test_claude_rule_files_mirror_tool_neutral_rules() -> None:
    source_dir = ROOT / "docs" / "ai" / "rules"
    mirror_dir = ROOT / ".claude" / "rules"

    for source_name, mirror_name in CLAUDE_RULE_MIRRORS.items():
        assert read_text(mirror_dir / mirror_name) == read_text(source_dir / source_name)


def test_code_review_guide_is_referenced_from_agents() -> None:
    review_path = ROOT / "docs" / "ai" / "code-review.md"
    assert review_path.is_file()
    assert "docs/ai/code-review.md" in read_text(ROOT / "AGENTS.md")


def test_context_audit_checklist_is_referenced_from_shared_context() -> None:
    audit_path = ROOT / "docs" / "ai" / "CONTEXT_AUDIT.md"
    assert audit_path.is_file()
    assert "docs/ai/CONTEXT_AUDIT.md" in read_text(ROOT / "AGENTS.md")
    assert "docs/ai/CONTEXT_AUDIT.md" in read_text(ROOT / "docs" / "ai" / "core.md")
    assert "Legacy LaTeX appears only as explicit opt-in" in read_text(audit_path)


def test_private_maintainer_workspace_stays_ignored() -> None:
    assert ".maintainers/" in read_text(ROOT / ".gitignore")


def test_public_repo_surfaces_exclude_internal_maintainer_material() -> None:
    status, lines = workflow_lib.audit_public_repo_privacy(ROOT)
    assert status == 0, "\n".join(lines)


def test_nested_codex_project_docs_cover_high_traffic_folders() -> None:
    projects_agents = ROOT / "projects" / "AGENTS.md"
    weekly_agents = ROOT / "fins2026" / "AGENTS.md"

    assert projects_agents.is_file()
    assert weekly_agents.is_file()
    assert "report/report.docx" in read_text(projects_agents)
    assert "fintools" in read_text(weekly_agents)


def test_context_files_point_to_expected_assistant_surfaces() -> None:
    gemini_settings = json.loads(read_text(ROOT / ".gemini" / "settings.json"))
    qwen_settings = json.loads(read_text(ROOT / ".qwen" / "settings.json"))

    assert gemini_settings["context"]["fileName"] == "GEMINI.md"
    assert qwen_settings["context"]["fileName"] == ["AGENTS.md", "QWEN.md"]
    assert "AGENTS.md" in read_text(ROOT / "GEMINI.md")
    assert "AGENTS.md" in read_text(ROOT / "QWEN.md")


def test_onboarding_surfaces_document_bootstrap_before_agent_helper() -> None:
    surfaces = [
        ROOT / "AGENTS.md",
        ROOT / ".agents" / "skills" / "onboard" / "SKILL.md",
        ROOT / ".claude" / "skills" / "onboard" / "SKILL.md",
        ROOT / ".gemini" / "commands" / "onboard.toml",
        ROOT / ".qwen" / "skills" / "onboard" / "SKILL.md",
        ROOT / "docs" / "ai" / "workflows" / "onboard.md",
        ROOT / "docs" / "setup" / "pycharm.md",
    ]
    for path in surfaces:
        text = read_text(path)
        assert "bootstrap_windows.ps1" in text
        assert "bootstrap_macos.sh" in text
        assert "python tools/workflow.py onboard" in text
        if "onboard" in str(path) or path.name == "pycharm.md":
            assert "LaTeX" not in text
            assert "pdflatex" not in text


def test_bootstrap_scripts_verify_existing_venv_before_rebuild() -> None:
    windows_bootstrap = read_text(ROOT / "tools" / "bootstrap_windows.ps1")
    assert "Checking existing .venv before rebuilding" in windows_bootstrap
    assert "Assert-VenvUnlocked" in windows_bootstrap
    assert "BurntSushi.ripgrep.MSVC" in windows_bootstrap
    assert windows_bootstrap.index("Assert-VenvUnlocked") < windows_bootstrap.index(
        "-m venv --clear"
    )

    macos_bootstrap = read_text(ROOT / "tools" / "bootstrap_macos.sh")
    assert "Checking existing .venv before rebuilding" in macos_bootstrap
    assert "brew install ripgrep" in macos_bootstrap
    assert '"$PYTHON_BIN" -m pip --version' in macos_bootstrap
    assert macos_bootstrap.index("Checking existing .venv") < macos_bootstrap.index(
        "-m venv --clear"
    )
    assert macos_bootstrap.index('"$PYTHON_BIN" -m pip --version') < macos_bootstrap.index(
        "-m venv --clear"
    )


def test_setup_docs_document_advisory_ripgrep_search_tool() -> None:
    windows_setup = read_text(ROOT / "docs" / "setup" / "windows.md")
    assert "winget install --id BurntSushi.ripgrep.MSVC -e" in windows_setup
    assert "rg --version" in windows_setup
    assert "rg --files -g AGENTS.md" in windows_setup

    macos_setup = read_text(ROOT / "docs" / "setup" / "macos.md")
    assert "brew install ripgrep" in macos_setup
    assert "rg --version" in macos_setup
    assert "rg --files -g AGENTS.md" in macos_setup
    assert "python3.13 -m pip --version" in macos_setup
    assert "brew install --cask pycharm" in macos_setup
    assert "pycharm-ce" not in macos_setup
    assert "https://www.python.org/downloads/macos/" in macos_setup
    assert "~/Developer/GitHub" in macos_setup

    troubleshooting = read_text(ROOT / "docs" / "setup" / "troubleshooting.md")
    assert "rg is not recognized" in troubleshooting
    assert "coursework can continue" in troubleshooting
    assert "XML_SetAllocTrackerActivationThreshold" in troubleshooting


def test_student_docs_keep_setup_pycharm_first_and_repo_root_explicit() -> None:
    for path in [
        ROOT / "README.md",
        ROOT / "QUICKSTART.md",
        ROOT / "docs" / "ai" / "start-here.md",
        ROOT / "docs" / "setup" / "pycharm.md",
        ROOT / "fins2026" / "week0" / "README.md",
    ]:
        text = read_text(path)
        assert "PyCharm" in text
        assert "repo root" in text


def test_public_setup_docs_avoid_uv_and_old_python_guidance() -> None:
    for path in [
        ROOT / "README.md",
        ROOT / "QUICKSTART.md",
        ROOT / "AGENTS.md",
        ROOT / "docs" / "ai" / "core.md",
        ROOT / "docs" / "ai" / "start-here.md",
        ROOT / "docs" / "ai" / "workflows" / "onboard.md",
        ROOT / "docs" / "setup" / "windows.md",
        ROOT / "docs" / "setup" / "macos.md",
        ROOT / "docs" / "setup" / "pycharm.md",
        ROOT / "docs" / "setup" / "troubleshooting.md",
    ]:
        text = read_text(path)
        assert text.isascii(), f"non-ASCII text found in {path}"
        assert "uv run" not in text
        assert "uv sync" not in text
        assert "uv add" not in text
        assert "Python 3.11" not in text


def test_ai_troubleshooting_front_runs_codex_claude_startup_failures() -> None:
    troubleshooting = read_text(ROOT / "docs" / "setup" / "ai-troubleshooting.md")
    assert "Codex or Claude fails before reading the repo" in troubleshooting
    assert "codex --version" in troubleshooting
    assert "claude --version" in troubleshooting
    assert "model" in troubleshooting
    assert "auth" in troubleshooting


def test_streamlit_docs_treat_watchdog_xcode_as_nonfatal() -> None:
    docs = [
        read_text(ROOT / "docs" / "apps" / "streamlit" / "README.md"),
        read_text(ROOT / "docs" / "apps" / "streamlit" / "student-quickstart.md"),
        read_text(ROOT / "docs" / "setup" / "troubleshooting.md"),
    ]
    for text in docs:
        assert "Watchdog" in text
        assert "Xcode" in text
        assert "fatal" in text

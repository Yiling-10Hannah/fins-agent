"""Tests for the Week 2 student-facing figure scaffold."""

from __future__ import annotations

import importlib.util
from io import StringIO
from pathlib import Path
from types import ModuleType

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
WEEK2 = ROOT / "fins2026" / "week2"


def import_module_from_path(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_week2_figure_scaffold_files_exist() -> None:
    assert (WEEK2 / "README.md").is_file()
    assert (WEEK2 / "DATA_GUIDE.md").is_file()
    assert (WEEK2 / "FIGURE_GALLERY.md").is_file()
    assert (WEEK2 / "data" / "README.md").is_file()
    assert (WEEK2 / "data" / "australia_macro_stage1_long.csv").is_file()
    assert (WEEK2 / "prompts" / "australia_macro_prompt.md").is_file()
    assert (WEEK2 / "prompts" / "figure_correction_prompt.md").is_file()
    assert (WEEK2 / "prompts" / "ft_figure_prompt.md").is_file()
    assert (WEEK2 / "scripts" / "describe_week2_data.py").is_file()
    assert (WEEK2 / "scripts" / "make_all_week2_figures.py").is_file()
    assert (WEEK2 / "scripts" / "make_australia_macro_figures.py").is_file()
    assert (WEEK2 / "scripts" / "make_fred_market_figures.py").is_file()
    assert (WEEK2 / "scripts" / "make_ft_validation_figures.py").is_file()
    assert (WEEK2 / "scripts" / "make_single_word_figure.py").is_file()
    assert (WEEK2 / "scripts" / "pull_australia_macro_data.py").is_file()
    assert (WEEK2 / "scripts" / "pull_fred_market_data.py").is_file()
    assert (WEEK2 / "code" / "australia_macro_panel.py").is_file()
    assert (WEEK2 / "code" / "australia_macro_specs.py").is_file()
    assert (WEEK2 / "code" / "market_panel.py").is_file()
    assert (WEEK2 / "code" / "market_window.py").is_file()
    assert (WEEK2 / "results" / "data" / ".gitkeep").is_file()
    assert (WEEK2 / "results" / "figures" / ".gitkeep").is_file()
    assert not (WEEK2 / ".gitkeep").exists()


def test_week2_readme_has_run_guidance_and_output_path() -> None:
    text = (WEEK2 / "README.md").read_text(encoding="utf-8")

    assert "validation_figures_ft.docx" in text
    assert "week2_market_macro_story_ft.docx" in text
    assert "week2_australia_macro_story_ft.docx" in text
    windows_command = (
        r".\.venv\Scripts\python.exe "
        r"fins2026\week2\scripts\make_ft_validation_figures.py"
    )
    assert windows_command in text
    assert "./.venv/bin/python fins2026/week2/scripts/make_ft_validation_figures.py" in text
    assert "python tools/workflow.py build-figure --style ft --docx" in text
    assert "pull_fred_market_data.py" in text
    assert "make_fred_market_figures.py" in text
    assert "pull_australia_macro_data.py" in text
    assert "make_australia_macro_figures.py" in text
    assert "results/figures/market_macro_story/" in text
    assert "results/figures/australia_macro_story/" in text
    assert "results/figures/style_gallery" in text
    assert "2025-12-31" in text
    assert "2026-03-31" in text
    assert "figure_correction_prompt.md" in text
    assert "australia_macro_prompt.md" in text
    assert "prompts/ft_figure_prompt.md" in text
    assert "PyCharm" in text
    assert "repo root" in text
    assert "bond-trading" not in text
    assert "electronic_trading" not in text


def test_week2_data_readme_points_students_to_generated_fred_paths() -> None:
    text = (WEEK2 / "data" / "README.md").read_text(encoding="utf-8")

    assert "fred_market_macro.csv" in text
    assert "australia_macro_stage1_long.csv" in text
    assert "australia_macro_reference_panel.csv" in text
    assert "australia_macro_feature_panel.csv" in text
    assert "results/figures/market_macro_story/" in text
    assert "results/figures/australia_macro_story/" in text
    assert "results/figures/style_gallery/" in text
    assert "electronic_trading_percentages.csv" not in text


def test_week2_gallery_script_calls_canonical_ft_generator(monkeypatch) -> None:
    module = import_module_from_path(
        "week2_ft_gallery",
        WEEK2 / "scripts" / "make_ft_validation_figures.py",
    )
    captured: dict[str, object] = {}

    def fake_build_figure_examples(root, cwd, **kwargs):
        captured["root"] = root
        captured["cwd"] = cwd
        captured.update(kwargs)
        return 0, ["generated fake gallery"]

    monkeypatch.setattr(
        module.workflow_lib,
        "build_figure_examples",
        fake_build_figure_examples,
    )

    docx_path = module.build_validation_gallery()

    assert captured["root"] == module.REPO_ROOT
    assert captured["cwd"] == module.REPO_ROOT
    assert captured["output"] == "fins2026/week2/results/figures/style_gallery"
    assert captured["docx"] is True
    assert captured["style"] == "ft"
    assert docx_path == (
        module.REPO_ROOT
        / "fins2026"
        / "week2"
        / "results"
        / "figures"
        / "style_gallery"
        / "validation_figures_ft.docx"
    )


def test_week2_single_figure_script_shows_direct_word_export_pattern() -> None:
    text = (WEEK2 / "scripts" / "make_single_word_figure.py").read_text(
        encoding="utf-8"
    )

    assert "load_validation_dataset" in text
    assert "FigureContext" in text
    assert "cumulative_returns_plot" in text
    assert "export_word_figure" in text
    assert "insert_figures_docx" in text
    assert 'style="ft"' in text


def test_week2_new_scripts_are_student_facing_and_repo_local() -> None:
    for script in [
        "describe_week2_data.py",
        "make_all_week2_figures.py",
        "make_australia_macro_figures.py",
        "make_fred_market_figures.py",
        "pull_australia_macro_data.py",
        "pull_fred_market_data.py",
    ]:
        text = (WEEK2 / "scripts" / script).read_text(encoding="utf-8")
        assert ".maintainers" not in text
        assert "Downloads" not in text


def test_week2_fred_pull_url_and_cleaning_are_deterministic() -> None:
    module = import_module_from_path(
        "week2_pull_fred",
        WEEK2 / "scripts" / "pull_fred_market_data.py",
    )
    url = module.fred_csv_url()

    assert url == (
        "https://fred.stlouisfed.org/graph/fredgraph.csv?"
        "id=DGS10,DGS2,DTB3,T10Y2Y,VIXCLS,UNRATE,INDPRO,PAYEMS,FEDFUNDS,SP500"
    )

    raw = pd.read_csv(
        StringIO(
            "observation_date,DGS10,DGS2,DTB3,T10Y2Y,VIXCLS,UNRATE,INDPRO,PAYEMS,FEDFUNDS,SP500\n"
            "2024-01-01,4.0,3.0,2.0,1.0,15.0,3.7,102.0,156000,5.3,4800\n"
            "2024-01-02,4.2,3.1,2.2,1.1,16.0,3.7,102.0,156000,5.3,4810\n"
            "2024-01-03,.,3.2,2.3,1.2,17.0,3.7,102.0,156000,5.3,4820\n"
            "2024-01-04,4.4,3.3,2.4,1.3,18.0,3.7,102.0,156000,5.3,4830\n"
            "2024-01-05,4.5,3.4,2.5,1.4,19.0,3.7,102.0,156000,5.3,4840\n"
            "2024-01-06,4.6,3.5,2.6,1.5,20.0,3.7,102.0,156000,5.3,4850\n"
            "2024-01-07,4.7,3.6,2.7,1.6,21.0,3.7,102.0,156000,5.3,4860\n"
            "2024-01-08,4.8,3.7,2.8,1.7,22.0,3.7,102.0,156000,5.3,4870\n"
            "2024-01-09,4.9,3.8,2.9,1.8,23.0,3.7,102.0,156000,5.3,4880\n"
            "2024-01-10,5.0,3.9,3.0,1.9,24.0,3.7,102.0,156000,5.3,4890\n"
        )
    )
    clean = module.clean_fred_market_data(raw)

    assert "ten_year_minus_two_year" in clean
    assert "ten_year_minus_three_month" in clean
    assert "vix_rolling_21d" in clean
    assert "SP500_RETURN_PCT" in clean
    assert "SP500_LOG_RETURN_PCT" in clean
    assert "SP500_CUMULATIVE_RETURN_PCT" in clean
    assert clean.loc[0, "ten_year_minus_two_year"] == 1.0
    assert clean.loc[0, "ten_year_minus_three_month"] == 2.0


def test_week2_prompt_teaches_dataframe_figure_suite() -> None:
    text = (WEEK2 / "prompts" / "ft_figure_prompt.md").read_text(encoding="utf-8")

    assert "create_figure_suite" in text
    assert 'style="ft"' in text
    assert "docx=True" in text
    assert "narrative=True" in text
    assert "FigureContext" in text or "caption" in text
    assert "style_gallery" in text
    assert "levels" in text.lower()
    assert "log changes" in text.lower()
    assert "electronic-trading" not in text


def test_week2_australia_prompt_teaches_dff_timing_contract() -> None:
    text = (WEEK2 / "prompts" / "australia_macro_prompt.md").read_text(
        encoding="utf-8"
    )

    assert "Station 1" in text
    assert "Station 2" in text
    assert "reference_date" in text
    assert "observable_month_end" in text
    assert "2025-12-31" in text
    assert "2026-03-31" in text
    assert "results/figures/australia_macro_story/" in text


def test_week2_australia_pipeline_uses_frozen_fixture_and_timing_contract() -> None:
    module = import_module_from_path(
        "week2_pull_australia",
        WEEK2 / "scripts" / "pull_australia_macro_data.py",
    )
    stage1 = module.load_fixture_long_table(WEEK2 / "data" / "australia_macro_stage1_long.csv")
    bundle = module.build_output_bundle(stage1)

    assert stage1.shape == (2855, 17)
    assert str(stage1["reference_date"].min().date()) == "2000-01-31"
    assert str(stage1["reference_date"].max().date()) == "2025-12-31"
    assert str(stage1["observable_month_end"].max().date()) == "2026-03-31"
    assert bundle["reference_panel"].shape == (312, 16)
    assert str(bundle["reference_panel"].index.max().date()) == "2025-12-31"
    assert str(bundle["observable_panel"].index.max().date()) == "2026-03-31"
    assert "Real GDP quarterly log growth (%)" in bundle["feature_panel"].columns
    assert "Trade-weighted index log change (%)" in bundle["feature_panel"].columns


def test_week2_all_figures_script_includes_australia_pack() -> None:
    text = (WEEK2 / "scripts" / "make_all_week2_figures.py").read_text(
        encoding="utf-8"
    )

    assert "build_australia_macro_figures" in text
    assert "pull_australia_macro_data" in text
    assert "--skip-australia" in text
    assert "australia_docx" in text


def test_week2_market_macro_script_uses_log_wealth_and_clear_scatter_layout() -> None:
    text = (WEEK2 / "scripts" / "make_fred_market_figures.py").read_text(encoding="utf-8")
    lower = text.lower()

    assert 'stats_location="upper right"' in text
    assert "Cumulative wealth, log scale ($1 investment)" in text
    assert "S&P 500 Growth Of One Dollar" in text
    assert "Month-End Transformations By Series" in text
    assert "set_label_position(\"right\")" in text
    assert "Treasury Yields" in text
    assert "basis points" in lower
    assert "percentage points" in lower
    assert "Yield curve slope (10Y minus 3M)" in text


def test_week2_figure_correction_prompt_teaches_screenshot_workflow() -> None:
    text = (WEEK2 / "prompts" / "figure_correction_prompt.md").read_text(encoding="utf-8")

    assert "Win+Shift+S" in text
    assert "Alt+V" in text
    assert "Command+Control+Shift+4" in text
    assert "fix the generating Python code" in text
    assert "not the exported PNG/PDF directly" in text
    assert "results/figures/market_macro_story" in text

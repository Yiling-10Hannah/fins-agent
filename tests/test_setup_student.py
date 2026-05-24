"""Tests for the student setup verifier diagnostics."""

from __future__ import annotations

import builtins
import subprocess

from tools import setup_student


def test_check_import_reports_missing_imports(capsys) -> None:
    assert not setup_student.check_import("definitely_missing_fins_package", "missingpkg")
    output = capsys.readouterr().out
    assert "[MISSING] missingpkg" in output
    assert "-m pip install -r requirements.txt -r requirements-dev.txt" in output


def test_check_import_reports_broken_imports_without_traceback(monkeypatch, capsys) -> None:
    real_import = builtins.__import__

    def fake_import(name, *args, **kwargs):
        if name == "brokenpkg":
            raise AttributeError("partially initialized module 'brokenpkg'")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", fake_import)

    assert not setup_student.check_import("brokenpkg", "broken package")
    output = capsys.readouterr().out
    assert "[BROKEN] broken package" in output
    assert "partially initialized module" in output
    assert "python tools/workflow.py onboard --rebuild" in output


def test_check_word_tooling_reports_broken_docx_without_traceback(monkeypatch, capsys) -> None:
    real_import = builtins.__import__

    def fake_import(name, *args, **kwargs):
        if name == "docx":
            raise OSError("DLL load failed")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", fake_import)

    assert not setup_student.check_word_tooling()
    output = capsys.readouterr().out
    assert "[BROKEN] Word report tooling" in output
    assert "DLL load failed" in output
    assert "python tools/workflow.py onboard --rebuild" in output


def test_check_ripgrep_missing_is_advisory(monkeypatch, capsys) -> None:
    monkeypatch.setattr(setup_student.shutil, "which", lambda name: None)
    monkeypatch.setattr(setup_student.platform, "system", lambda: "Windows")

    assert not setup_student.check_ripgrep()

    output = capsys.readouterr().out
    assert "[WARN] ripgrep" in output
    assert "AI assistants can still work" in output
    assert "winget install --id BurntSushi.ripgrep.MSVC -e" in output


def test_check_ripgrep_reports_ok_when_repo_search_works(monkeypatch, capsys) -> None:
    monkeypatch.setattr(setup_student.shutil, "which", lambda name: "rg")

    def fake_run(command, **kwargs):
        del kwargs
        if command == ["rg", "--version"]:
            return subprocess.CompletedProcess(command, 0, stdout="ripgrep 15.1.0\n", stderr="")
        if command == ["rg", "--files", "-g", "AGENTS.md"]:
            return subprocess.CompletedProcess(command, 0, stdout="AGENTS.md\n", stderr="")
        raise AssertionError(f"unexpected command: {command}")

    monkeypatch.setattr(setup_student.subprocess, "run", fake_run)

    assert setup_student.check_ripgrep()

    output = capsys.readouterr().out
    assert "[OK] ripgrep (ripgrep 15.1.0)" in output


def test_main_does_not_fail_when_only_ripgrep_is_missing(monkeypatch, capsys) -> None:
    monkeypatch.setattr(setup_student, "check_repo_interpreter", lambda: True)
    monkeypatch.setattr(setup_student, "check_python", lambda: True)
    monkeypatch.setattr(setup_student, "check_pip", lambda: True)
    monkeypatch.setattr(setup_student, "check_import", lambda name, display=None: True)
    monkeypatch.setattr(setup_student, "check_word_tooling", lambda: True)
    monkeypatch.setattr(setup_student, "check_ripgrep", lambda: False)

    assert setup_student.main() == 0

    output = capsys.readouterr().out
    assert "Step 7: AI Workflow Tools" in output
    assert "All required checks passed" in output

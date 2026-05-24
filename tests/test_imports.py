"""Smoke tests verifying all required packages import correctly.

Run with: python -m pytest tests/
"""

import importlib

import pytest

REQUIRED_PACKAGES = [
    ("pandas", "pandas"),
    ("numpy", "numpy"),
    ("matplotlib", "matplotlib"),
    ("matplotlib.pyplot", "matplotlib.pyplot"),
    ("seaborn", "seaborn"),
    ("statsmodels", "statsmodels"),
    ("statsmodels.api", "statsmodels.api"),
    ("pyarrow", "pyarrow"),
    ("docx", "python-docx"),
    ("fintools", "fintools"),
    ("fintools.datasets", "fintools.datasets"),
    ("fintools.documents", "fintools.documents"),
    ("fintools.figures", "fintools.figures"),
]


@pytest.mark.parametrize("module,name", REQUIRED_PACKAGES, ids=[p[1] for p in REQUIRED_PACKAGES])
def test_import(module, name):
    """Verify that each required package can be imported."""
    importlib.import_module(module)

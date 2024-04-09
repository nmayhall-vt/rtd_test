"""
Unit and regression test for the rtd_test package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import rtd_test


def test_rtd_test_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "rtd_test" in sys.modules

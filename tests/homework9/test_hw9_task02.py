import pytest

from homework9.hw9_task02 import ContextManSupressor, supressing


def test_supresses_passed_exception():
    with supressing(IndexError):
        assert [][2]

    with ContextManSupressor(IndexError):
        assert [][2]


def test_does_not_supress_not_passed_exception():
    with supressing(ValueError):
        with pytest.raises(IndexError):
            [][2]

    with ContextManSupressor(ValueError):
        with pytest.raises(IndexError):
            [][2]

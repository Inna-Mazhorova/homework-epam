import pytest

from homework9.hw9_task02 import ContextMan_Supressor, supressing


def test_supresses_passed_exception():
    with supressing(IndexError):
        assert [][2]

    with ContextMan_Supressor(IndexError):
        assert [][2]


def test_does_not_supress_not_passed_exception():
    with supressing(ValueError):
        with pytest.raises(IndexError):
            [][2]

    with ContextMan_Supressor(ValueError):
        with pytest.raises(IndexError):
            [][2]

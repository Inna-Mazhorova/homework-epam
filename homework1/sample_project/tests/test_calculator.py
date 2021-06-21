import pytest

from homework1.sample_project.calculator.calc import check_power_of_2


def test_positive_case():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(65536)


def test_negative_case():
    """Testing that non-powers of 2 give False"""
    assert not check_power_of_2(12)


def test_zero_case():
    """Testing that a = zero gives False"""
    assert not check_power_of_2(0)


test_positive_case()
test_negative_case()
test_zero_case()

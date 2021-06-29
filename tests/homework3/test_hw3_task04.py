from homework3.hw3_task04 import is_armstrong


def test_positive_armstrong_case():
    assert is_armstrong(153) == 'Is Armstrong number'


def test_negative_armstrong_case():
    assert is_armstrong(10) == 'Is not Armstrong number'

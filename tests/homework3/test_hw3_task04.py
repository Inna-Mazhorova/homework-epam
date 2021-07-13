from homework3.hw3_task04 import is_armstrong


def test_if_number_is_armstrong_true_case():
    assert is_armstrong(153) is True, "Is Armstrong number"


def test_if_number_is_armstrong_false_case():
    assert is_armstrong(10) is False, "Is not Armstrong number"

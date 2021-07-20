from homework7.hw7_task02 import backspace_compare


def test_true_case_1():
    assert backspace_compare("a##c", "#a#c")


def test_true_case_2():
    assert backspace_compare("ab#c", "ad#c")


def test_false_case():
    assert not backspace_compare("a#c", "b")

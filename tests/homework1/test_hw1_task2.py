from homework1.task02.fibonacci import check_fibonacci

data_for_check1 = [
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
    144,
    233,
    377,
    610,
    987,
    1597,
    2584,
    4181,
    6765,
]


def test_fibonacci_case():
    """Testing if Sequence is fibonacci"""
    assert check_fibonacci(data_for_check1)


data_for_check2 = [
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    22,
    34,
    55,
    89,
    144,
    233,
    377,
    610,
    987,
    1597,
    2584,
    4181,
    6765,
]


def test_non_fibonacci_case():
    """Testing if Sequence is fibonacci"""
    assert not check_fibonacci(data_for_check2)


data_for_check3 = [0, 1]


def test_short_case():
    """Testing short sequence case"""
    assert not check_fibonacci(data_for_check3)

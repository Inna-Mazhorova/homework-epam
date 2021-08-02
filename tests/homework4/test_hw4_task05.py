from homework4.hw4_task05 import array

data_for_test_fizzbuzz = [
    1,
    2,
    "fizz",
    4,
    "buzz",
    "fizz",
    7,
    8,
    "fizz",
    "buzz",
    11,
    "fizz",
    13,
    14,
    "fizzbuzz",
    16,
    17,
    "fizz",
    19,
    "buzz",
]

data_for_test_non_fizzbuzz = [
    1,
    2,
    "fizz",
    4,
    5,
    "fizz",
    7,
    8,
    "fizz",
    "buzz",
    11,
    "fizz",
    13,
    14,
    "fizzbuzz",
    16,
    17,
    "fizz",
    19,
    "buzz",
]


def test_list_is_fizzbuzz():
    assert array == data_for_test_fizzbuzz


def test_list_is_fizzbuzz():
    assert array != data_for_test_non_fizzbuzz

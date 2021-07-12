from homework2.hw2_task01_part3 import count_punctuation_chars


def test_count_punctuation_chars():
    assert count_punctuation_chars("tests/homework2/data.txt") == 5305

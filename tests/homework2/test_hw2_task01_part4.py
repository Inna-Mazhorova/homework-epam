from homework2.hw2_task01_part4 import count_non_ascii_chars


def test_count_non_ascii_chars():
    assert count_non_ascii_chars("tests/homework2/data.txt") == 2972

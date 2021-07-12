from homework2.hw2_task01_part5 import get_most_common_non_ascii_char


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char("tests/homework2/data.txt") == "ä"

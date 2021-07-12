from homework2.hw2_task01_part2 import get_rarest_char


def test_get_rarest_char():
    assert get_rarest_char("tests/homework2/data.txt") == [
        "›",
        "‹",
        "Y",
        "î",
        "’",
        "X",
        "(",
        ")",
    ]

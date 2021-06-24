from homework1.task03.hw1_task03 import find_maximum_and_minimum


def test_max_min_tuple():
    assert find_maximum_and_minimum("tests/homework1/some_file.txt") == (1, 5)

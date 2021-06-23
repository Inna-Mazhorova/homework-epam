from homework1.task03.hw1_task03 import find_maximum_and_minimum


def test_max_min_tuple():
    assert find_maximum_and_minimum("some_file.txt") == (1, 5)


test_max_min_tuple()

from homework1.task03.hw1_task03 import find_maximum_and_minimum


def test_max_min_tuple():
    assert find_maximum_and_minimum(
        "C:/Users/Lantana/PycharmProjects/homework-epam/homework1/task03/some_file.txt"
    ) == (1, 5)


test_max_min_tuple()

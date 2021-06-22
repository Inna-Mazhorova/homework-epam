from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(
        "C:/Users/Lantana/PycharmProjects/homework-epam/homework1/task03/some_file.txt"
    ) as fi:
        my_lines = fi.read().splitlines()

    minimum = int(min(my_lines))
    maximum = int(max(my_lines))
    result = (minimum, maximum)
    return result

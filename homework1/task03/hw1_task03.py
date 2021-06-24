from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as fi:
        my_lines = [int(line.rstrip("\n")) for line in fi]
    result = (min(my_lines), max(my_lines))
    return result

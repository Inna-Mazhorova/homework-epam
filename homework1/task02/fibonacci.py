from typing import Sequence


def _check_window(x: int, y: int, z: int) -> bool:
    return (x + y) == z


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) < 3:
        return False
    counter = 0
    while counter < len(data) - 2:
        if not _check_window(data[counter], data[counter + 1], data[counter + 2]):
            return False
        counter += 1
    return True

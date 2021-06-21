from typing import Sequence


def _check_window(x: int, y: int, z: int) -> bool:
    return (x + y) == z


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) < 3:
        return False

    a, b, c = data[0], data[1], data[2]

    data.append(0)
    while len(data) > 3:
        if not _check_window(a, b, c):
            return False
        a, b, c = b, c, data[3]
        data = data[1:]

    return True

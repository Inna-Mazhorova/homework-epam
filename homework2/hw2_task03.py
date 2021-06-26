import itertools
from typing import List, Any


"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""


def combinations_list(*args: List[Any]) -> List[List]:
    combin = list(itertools.product(*args))
    result = list(map(lambda x: list(x), combin))
    return result

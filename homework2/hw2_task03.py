import itertools
from typing import Any, List


def combinations_list(*args: List[Any]) -> List[List]:
    combin = list(itertools.product(*args))
    result = list(map(lambda x: list(x), combin))
    return result

from typing import Dict, List, Tuple


def find_maximum(d: Dict[int, int]) -> int:
    for elem, freq in d.items():
        if freq == max(d.values()):
            return elem


def find_minimum(d: Dict[int, int]) -> int:
    for elem, freq in d.items():
        if freq == min(d.values()):
            return elem


def major_and_minor_elem(a: List[int]) -> Tuple[int, int]:
    elements = {}
    for i in a:
        if i not in elements:
            elements[i] = 1
        else:
            elements[i] += 1
    result = (find_maximum(elements), find_minimum(elements))
    return result

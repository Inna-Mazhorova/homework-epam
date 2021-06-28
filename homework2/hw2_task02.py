from typing import Dict, List, Tuple

# Given an array of size n, find the most common and the least common elements.
# The most common element is the element that appears more than n // 2 times.
# The least common element is the element that appears fewer than other.
# You may assume that the array is non-empty and the most common element
# always exist in the array.


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

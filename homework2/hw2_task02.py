from collections import defaultdict
from typing import List, Tuple

# Given an array of size n, find the most common and the least common elements.
# The most common element is the element that appears more than n // 2 times.
# The least common element is the element that appears fewer than other.
# You may assume that the array is non-empty and the most common element
# always exist in the array.


def major_and_minor_elem(elements_list: List[int]) -> Tuple[int, int]:
    elements_dict = defaultdict(int)
    for i in elements_list:
        elements_dict[i] += 1
    result = (max(elements_dict, key=elements_dict.get)), (
        min(elements_dict, key=elements_dict.get)
    )
    return result

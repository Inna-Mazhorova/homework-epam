from typing import Any

"""
Given a dictionary (tree), that contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contain basic structures like:
    str, list, tuple, dict, set, int, bool
"""


def find_occurrences(tree: dict, element: Any) -> int:

    all_tree_items = list(tree.items())
    occurrences = 0
    while all_tree_items:
        next_element = all_tree_items.pop()
        if next_element == element:
            occurrences += 1
        elif isinstance(next_element, dict):
            all_tree_items.extend(next_element.items())
        elif isinstance(next_element, (list, tuple, set)):
            all_tree_items.extend(next_element)
    return occurrences

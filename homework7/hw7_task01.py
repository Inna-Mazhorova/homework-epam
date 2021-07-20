from collections import Counter
from itertools import chain
from typing import Any

"""
Given a dictionary (tree), that contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contain basic structures like:
    str, list, tuple, dict, set, int, bool
"""


example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}


#def find_occurrences(tree: dict, element: Any) -> int:
def find_occurrences(tree: dict) -> int:

    #tree_keys = Counter(tree)

    #tree_values = list(tree.values())
   # nested_tree_values = tree_values.values()


    #tree_values = list(chain(tree.values()))
    #nested_tree_values = list(chain(tree_values.values()))
    tree_values = [**tree]

    return tree_values



#print(find_occurrences(example_tree, "RED"))
print(find_occurrences(example_tree))
from homework7.hw7_task01 import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "RED": {
        "abc": ["RED", "BLUE"],
        "jhl": "RED",
        "RED": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def test_word_count():
    assert find_occurrences(example_tree, "RED") == 9


def test_dict_count():
    assert find_occurrences(example_tree, {"nested_key": "RED"}) == 1


def test_list_count():
    assert find_occurrences(example_tree, ["RED", "BLUE"]) == 2


empty_tree = {}


def test_empty_count():
    assert find_occurrences(empty_tree, "RED") == 0


def test_inexistent_word_count():
    assert find_occurrences(example_tree, "green") == 0

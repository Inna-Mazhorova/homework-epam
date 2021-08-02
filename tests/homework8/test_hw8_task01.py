import pytest

from homework8.hw8_task01 import KeyValueStorage


def test_positive_test():
    storage = KeyValueStorage("tests/homework8/task1_positive.txt")
    assert storage["name"] == "kek"
    assert storage.power == 9001


def test_repeat_test():
    with pytest.raises(ValueError, match="Key power is already in dict"):
        storage = KeyValueStorage("tests/homework8/task1_repeat.txt")
        storage.power


def test_keyword_test():
    with pytest.raises(
        ValueError, match="Value cannot be assigned to an attribute continue."
    ):
        storage = KeyValueStorage("tests/homework8/task01_keyword.txt")
        storage.power


def test_many_equals_test():
    with pytest.raises(ValueError, match="Line must contain one '=' symbol"):
        storage = KeyValueStorage("tests/homework8/task01_equals.txt")
        storage.name

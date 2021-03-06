import pytest

from homework9.hw9_task01 import merge_sorted_files


def test_correct_sorted_merge():
    assert list(
        merge_sorted_files(["tests/homework9/file1.txt", "tests/homework9/file2.txt"])
    ) == [
        1,
        2,
        3,
        4,
        5,
        6,
    ]


def test_error_in_file():
    with pytest.raises(ValueError):
        list(
            merge_sorted_files(
                ["tests/homework9/file3.txt", "tests/homework9/file2.txt"]
            )
        )

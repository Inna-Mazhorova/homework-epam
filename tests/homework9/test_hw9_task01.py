import pytest

from homework9.hw9_task01 import merge_sorted_files


def test_correct_sorted_merge():
    assert list(merge_sorted_files(["file1.txt", "file2.txt"])) == [1, 2, 3, 4, 5, 6]


def test_error_in_file():
    with pytest.raises(ValueError, match="file can only contain numbers"):
        list(merge_sorted_files(["file3.txt", "file2.txt"]))

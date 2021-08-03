import os

from homework9.hw9_task03 import universal_file_counter

file_dir = os.path.dirname(__file__) + "/files"


def test_count_without_tokenizer():
    assert universal_file_counter("files/", ".txt") == 13


def test_count_without_tokenizer():
    assert universal_file_counter("files/", ".txt", 4) == 16

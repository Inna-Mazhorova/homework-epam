from homework9.hw9_task03 import universal_file_counter


def test_count_without_tokenizer():
    assert universal_file_counter(r"tests/homework9/files", ".txt") == 13


def test_count_without_tokenizer():
    assert universal_file_counter(r"tests/homework9/files", ".txt", 4) == 16

from homework9.hw9_task03 import universal_file_counter


def test_count_without_tokenizer():
    assert universal_file_counter("tests/homework9/files", "txt") == 14


def test_count_with_tokenizer():
    assert universal_file_counter("tests/homework9/files", "txt", str.split) == 17

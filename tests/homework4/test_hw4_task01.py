import tempfile

import pytest

from homework4.hw4_task01 import number_returning_function


@pytest.fixture()
def test_file_creation(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "test.txt"
    p.write_text("3")
    # first_line_int = int(p.read_text())
    return p


def test_number_returning_function_returns_number(test_file_creation):
    assert number_returning_function("mydir/test.txt") == False

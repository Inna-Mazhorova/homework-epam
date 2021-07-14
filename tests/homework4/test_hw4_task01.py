import tempfile

import pytest

from homework4.hw4_task01 import number_returning_function


@pytest.fixture()
def file_creation():
    with tempfile.NamedTemporaryFile(dir="homework4/") as temp:
        temp.write(b"3")
    return temp


def test_number_returning_function_returns_number(file_creation):
    assert number_returning_function(tmp.name) == False

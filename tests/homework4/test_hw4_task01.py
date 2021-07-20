import os
import tempfile

import pytest

from homework4.hw4_task01 import number_returning_function


def with_temp_file(content):
    def create_temp_file(func):
        def replacement_function(*args, **kwargs):
            with tempfile.NamedTemporaryFile(mode="w+t") as data_file:
                data_file.write(content)
                data_file.flush()
                return func(data_file.name, *args, **kwargs)

        return replacement_function

    return create_temp_file


@with_temp_file(content="2\n")
def test_number_returning_function_returns_True(file_path):
    assert number_returning_function(file_path) is True

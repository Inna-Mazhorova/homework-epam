import pathlib
from functools import partial
from glob import glob
from pathlib import Path
from typing import Callable, List, Optional

"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6
"""


def file_list_creator(dir_path: Path, file_extension: str) -> List:
    file_list = list(pathlib.Path("r" + dir_path).glob("*." + file_extension))
    return file_list


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    counter = 0
    for file in file_list_creator(dir_path, file_extension):
        with open(file, "r") as f:

            for block in iter(partial(f.read, tokenizer), "") if tokenizer else f:
                counter += 1
    return counter

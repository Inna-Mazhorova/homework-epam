"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
import heapq
from pathlib import Path
from typing import Generator, Iterator, List, Union


def number_generation(file_name: Union[Path, str]) -> Iterator:
    with open(file_name) as text:
        try:
            result = map(lambda x: int(x.rstrip("\n")), text.readlines())
            return iter(result)
        except ValueError:
            raise ValueError("file can only contain numbers")


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Generator:
    gen = (number_generation(file_name) for file_name in file_list)
    yield from heapq.merge(*gen)

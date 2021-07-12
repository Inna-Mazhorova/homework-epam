from collections import defaultdict
from typing import List


def get_rarest_char(file_path: str, encoding="unicode_escape") -> List[str]:
    with open(file_path, "r", encoding=encoding) as infile:
        text = infile.read()
    symbols_dict = defaultdict(int)
    for i in text:
        symbols_dict[i] += 1
    minimum_list = []
    for i in symbols_dict:
        if symbols_dict[i] == min(symbols_dict.values()):
            minimum_list.append(i)
    return minimum_list

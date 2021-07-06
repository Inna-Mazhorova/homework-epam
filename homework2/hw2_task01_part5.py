from collections import defaultdict


def get_most_common_non_ascii_char(file_path: str, encoding="unicode_escape") -> str:
    with open(file_path, "r", encoding=encoding) as infile:
        text = infile.read()
    non_ascii_text = "".join(filter(lambda x: ord(x) > 127, text))
    non_ascii_symbols_dict = defaultdict(int)
    for i in non_ascii_text:
        non_ascii_symbols_dict[i] += 1
    maximum = max(non_ascii_symbols_dict, key=lambda x: non_ascii_symbols_dict[x])
    return maximum


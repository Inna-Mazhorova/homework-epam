def count_non_ascii_chars(file_path: str, encoding="unicode_escape") -> int:
    with open(file_path, "r", encoding=encoding) as infile:
        text = infile.read()
    non_ascii_count = len("".join(filter(lambda x: ord(x) > 127, text)))
    return non_ascii_count

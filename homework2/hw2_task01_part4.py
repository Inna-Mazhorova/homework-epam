def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, "r") as infile:
        words = infile.read().split()
        words_clean = list(
            map(lambda x: x.encode("ascii").decode("unicode_escape"), words)
        )
        text_clean = " ".join(words_clean)
    non_ascii_count = len("".join(filter(lambda x: ord(x) > 127, text_clean)))
    return non_ascii_count

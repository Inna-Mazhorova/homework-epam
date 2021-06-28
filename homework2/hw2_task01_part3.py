def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, "r") as infile:
        words = infile.read().split()
        words_clean = list(
            map(lambda x: x.encode("ascii").decode("unicode_escape"), words)
        )
        text_clean = " ".join(words_clean)
    count = 0
    for i in range(0, len(text_clean)):
        if text_clean[i] in (
            "!",
            ",",
            "'",
            ";",
            '"',
            ".",
            "-",
            "?",
            "«",
            "»",
            "’",
            "—",
            ":",
        ):
            count = count + 1
    return count

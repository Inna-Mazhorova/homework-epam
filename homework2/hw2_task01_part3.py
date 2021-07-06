import string


def count_punctuation_chars(file_path: str, encoding="unicode_escape") -> int:
    with open(file_path, "r", encoding=encoding) as infile:
        text = infile.read()
    count = 0
    for i in range(0, len(text)):
        if text[i] in string.punctuation:
            count = count + 1
    return count

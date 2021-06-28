from typing import List

# Given a file containing text. Complete using only default collections:
#   1) Find 10 longest words consisting from largest amount of unique symbols
#  2) Find rarest symbol for document
# 3) Count every punctuation char
# 4) Count every non ascii char
# 5) Find most common non ascii char for document


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, "r") as infile:
        words = infile.read().split()
        words_clean = list(
            map(lambda x: x.encode("ascii").decode("unicode_escape"), words)
        )
        text_clean = " ".join(words_clean)
    punctuation = ["!", ",", "'", ";", '"', ".", "-", "?", "«", "»", "’", "—", ":"]
    text_clean_punc = "".join(ch for ch in text_clean if ch not in punctuation)
    words_new = text_clean_punc.split()
    words_clean_diverse = {i: "".join(set(i)) for i in words_new}
    list_words_clean_diverse = list(words_clean_diverse.items())
    list_words_clean_diverse.sort(key=lambda i: len(i[1]), reverse=True)
    return [i[0] for i in list_words_clean_diverse[:10]]


def get_rarest_char(file_path: str) -> List[str]:
    with open(file_path, "r") as infile:
        words = infile.read().split()
        words_clean = list(
            map(lambda x: x.encode("ascii").decode("unicode_escape"), words)
        )
        text_clean = " ".join(words_clean)
    elements = {}
    for i in text_clean:
        if i not in elements:
            elements[i] = 1
        else:
            elements[i] += 1
    minimum_list = []
    for i in elements:
        if elements[i] == 1:
            minimum_list.append(i)
    return minimum_list


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


def count_non_ascii_chars(file_path: str) -> int:

    with open(file_path, "r") as infile:
        words = infile.read().split()
        words_clean = list(
            map(lambda x: x.encode("ascii").decode("unicode_escape"), words)
        )
        text_clean = " ".join(words_clean)
    non_ascii_count = len("".join(filter(lambda x: ord(x) > 127, text_clean)))
    return non_ascii_count


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, "r") as infile:
        words = infile.read().split()
        words_clean = list(
            map(lambda x: x.encode("ascii").decode("unicode_escape"), words)
        )
        text_clean = " ".join(words_clean)
    non_ascii_text = "".join(filter(lambda x: ord(x) > 127, text_clean))
    non_ascii_elements = {}
    for i in non_ascii_text:
        if i not in non_ascii_elements:
            non_ascii_elements[i] = 1
        else:
            non_ascii_elements[i] += 1
    maximum = max(non_ascii_elements, key=lambda x: non_ascii_elements[x])
    return maximum

import string
from typing import List


def get_longest_diverse_words(file_path: str, encoding="unicode_escape") -> List[str]:
    with open(file_path, "r", encoding=encoding) as infile:
        text = infile.read()
    text_clean_punc = "".join(ch for ch in text if ch not in string.punctuation)
    words_new = text_clean_punc.split()
    words_clean_diverse = {i: "".join(set(i)) for i in words_new}
    list_words_clean_diverse = list(words_clean_diverse.items())
    list_words_clean_diverse.sort(key=lambda i: len(i[1]), reverse=True)
    return [i[0] for i in list_words_clean_diverse[:10]]


print(get_longest_diverse_words("data1.txt"))

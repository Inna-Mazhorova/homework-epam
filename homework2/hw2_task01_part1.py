from typing import List


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
